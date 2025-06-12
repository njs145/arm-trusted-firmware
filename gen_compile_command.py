import argparse
import json
import logging
import os
import re

_DEFAULT_OUTPUT = 'compile_commands.json'
_DEFAULT_LOG_LEVEL = 'WARNING'

_FILENAME_PATTERN = r'(?:\s|^)(\S+\.c)(?=\s|$)'
_VALID_LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

def parse_arguments():
    usage = 'Creates a compile_commands.json database for rtos'
    parser = argparse.ArgumentParser(description=usage)

    directory_help = ('Path to the kernel source directory to search(defaults to the working directory)')
    parser.add_argument('-d', '--directory', type=str, help=directory_help)

    output_help = ('The location to write compile_commands.json (defaults to compile_commands.json in the search directory)')
    parser.add_argument('-o', '--output', type=str, help=output_help)

    log_level_help = ('The level of log messages to produce (one of ' + ', '.join(_VALID_LOG_LEVELS) + '; defaults to ' + _DEFAULT_LOG_LEVEL + ')')
    parser.add_argument('--log_level', type=str, default=_DEFAULT_LOG_LEVEL, help=log_level_help)

    args = parser.parse_args()

    log_level = args.log_level
    if log_level not in _VALID_LOG_LEVELS:
        raise ValueError('%s is not a valid log level' % log_level)
    
    directory = args.directory or os.getcwd()
    output = args.output or os.path.join(directory, _DEFAULT_OUTPUT)
    directory = os.path.abspath(directory)

    return log_level, directory, output

def main():
    log_level, directory, output = parse_arguments()

    level = getattr(logging, log_level)
    logging.basicConfig(format='%(levelname)s: %(message)s', level=level)

    source_matcher = re.compile(_FILENAME_PATTERN)

    build_log_file = directory + '/build_log.txt'
    with open (build_log_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    compile_commands = []
    for line in lines:
        command_line = line.strip()
        matches = source_matcher.search(command_line)
        if matches:
            compile_command = {
                'directory': directory,
                'command': command_line,
                'file': matches.group(1)
            }
            compile_commands.append(compile_command)

    with open(output, 'wt') as f:
        json.dump(compile_commands, f, indent=4, sort_keys=False)

if __name__ == '__main__':
    main()
