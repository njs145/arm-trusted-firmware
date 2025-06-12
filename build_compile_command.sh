#!/bin/sh

make distclean

rm build_log.txt

make V=1 CROSS_COMPILE=aarch64-none-elf- PLAT=qemu > build_log.txt

python3 gen_compile_command.py