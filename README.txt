This project is Arm trusted firmwware study.

사용법

1. virt_image 폴더로 이동
cd virt_image

2. qemu 실행
qemu-system-aarch64 -nographic -machine virt,secure=on -cpu cortex-a57  \
    -kernel Image                           \
    -append "console=ttyAMA0,38400 keep_bootcon"   \
    -smp 2 -m 1024 -bios bl1.bin   \
    -d unimp -semihosting-config enable,target=native   \
    --machine virt,gic-version=2\
    -dtb virt-custom.dtb \
    -device loader,addr=0x82000000,file=rootfs.cpio.gz \
    -s -S