#!/bin/sh

make distclean

rm build_log.txt

make V=1 CROSS_COMPILE=aarch64-none-elf- PLAT=qemu > build_log.txt

cp build/qemu/debug/bl1.bin build/qemu/debug/bl2.bin build/qemu/debug/bl31.bin virt_image

python3 gen_compile_command.py