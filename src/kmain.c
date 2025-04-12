#include <stdbool.h>
#include <stddef.h>
#include "limine.h"
#include "boot.h"
#include "term/term.h"

static void hcf() {
    for (;;) {
        asm ("hlt");
    }
}

void kmain() {
    if (framebuffer_request.response == NULL || framebuffer_request.response->framebuffer_count < 1) {
        // framebuffer not available — handle error
        while (1) { __asm__("hlt"); }
    }
    
    struct limine_framebuffer *fb = framebuffer_request.response->framebuffers[0];
    init_term(fb);
    
    term_write("Hello World");

    hcf();
}