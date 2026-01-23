his project is Arm trusted firmwware study.

사용법

1. virt_image 폴더로 이동
cd virt_image

2. qemu 실행
qemu-system-aarch64 -nographic -machine virt,secure=on -cpu cortex-a53  \
    -kernel Image                           \
    -append "console=ttyAMA0,38400 keep_bootcon"   \
    -smp 2 -m 1024 -bios bl1.bin   \
    -d unimp -semihosting-config enable=on,target=native   \
    --machine virt,gic-version=2\
    -dtb virt-custom.dtb \
    -netdev user,id=net0,hostfwd=tcp::10022-:22 \
    -device virtio-net-device,netdev=net0 \
    -virtfs local,path=/home/song/9p_share,security_model=none,mount_tag=host0 \
    -s
