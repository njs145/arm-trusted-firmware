#!/bin/sh

make distclean

rm build_log.txt

make V=1 CROSS_COMPILE=aarch64-none-elf- PLAT=qemu > build_log.txt

llvm-objdump -d -C -S build/qemu/debug/bl31/bl31.elf > virt_image/build/bl31.s
llvm-objdump -d -C -S build/qemu/debug/bl2/bl2.elf > virt_image/build/bl2.s
llvm-objdump -d -C -S build/qemu/debug/bl1/bl1.elf > virt_image/build/bl1.s

cp build/qemu/debug/bl1.bin build/qemu/debug/bl2.bin build/qemu/debug/bl31.bin virt_image

python3 gen_compile_command.py