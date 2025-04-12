import sys
import os

def main():
    args = sys.argv
    if args[1] == "kernel":
        build_kernel()
    elif args[1] == "image":
        build_image()
    elif args[1] == "clean":
        clean()
    else:
        print("Usage: python build.py [kernel|image|clean]")
        sys.exit(1)

def build_kernel():
    print("Building kernel...")
    os.system("cmake . --toolchain x86_64.cmake")
    os.system("make -j" + str(os.cpu_count()))

def build_image():
    print("Building image...")
    os.system("cmake .")
    os.system("make -j" + str(os.cpu_count()))
    if not os.path.exists("limine"):
        os.system("git clone https://github.com/limine-bootloader/limine --branch=v9.x-binary --depth=1")
    os.system("make -C limine -j" + str(os.cpu_count()))
    os.system("rm -rf iso_root")
    os.system("mkdir -p iso_root/boot")
    os.system("cp -v kernel iso_root/boot/")
    os.system("mkdir -p iso_root/boot/limine")
    os.system("cp -v limine.conf iso_root/boot/limine/")
    os.system("mkdir -p iso_root/EFI/BOOT")
    os.system("cp -v limine/limine-bios.sys limine/limine-bios-cd.bin limine/limine-uefi-cd.bin iso_root/boot/limine/")
    os.system("cp -v limine/BOOTX64.EFI iso_root/EFI/BOOT/")
    os.system("cp -v limine/BOOTIA32.EFI iso_root/EFI/BOOT/")
    os.system("xorriso -as mkisofs -R -r -J -b boot/limine/limine-bios-cd.bin \
        -no-emul-boot -boot-load-size 4 -boot-info-table -hfsplus \
        -apm-block-size 2048 --efi-boot boot/limine/limine-uefi-cd.bin \
        -efi-boot-part --efi-boot-image --protective-msdos-label \
        iso_root -o kernel.iso")
    os.system("./limine/limine bios-install kernel.iso")

def clean():
    os.system("make clean")
    os.system("rm -rf kernel CmakeCache.txt cmake_install.cmake *.iso Makefile CMakeFiles iso_root limine build")

if __name__ == "__main__":
    main()