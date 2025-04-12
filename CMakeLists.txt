cmake_minimum_required(VERSION 3.10)

project(kernel C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ffreestanding -Wall -Wextra -O2 -mcmodel=kernel -mgeneral-regs-only")

set(SOURCES 
    src/kmain.c
    src/term/term.c
    src/boot.c
    src/term/flanterm/flanterm.c
    src/term/flanterm/backends/fb.c
    src/utils/string.c)

include_directories()

add_executable(kernel ${SOURCES})

set(CMAKE_C_COMPILER "x86_64-elf-gcc")
set(CMAKE_ASM_COMPILER "x86_64-elf-gcc")
set(CMAKE_ASM_COMPILER "x86_64-elf-ld")


set(CMAKE_EXE_LINKER_FLAGS "-T linker.ld -nostdlib -mcmodel=kernel")