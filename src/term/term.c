#include "flanterm/flanterm.h"
#include "flanterm/backends/fb.h"
#include "../boot.h"
#include "../utils/string.h"
#include "./term.h"

static struct flanterm_context *context;

void init_term(struct limine_framebuffer *framebuffer) {
    context = flanterm_fb_init(
        NULL, NULL,
        framebuffer->address, framebuffer->width, framebuffer->height, framebuffer->pitch,
        framebuffer->red_mask_size, framebuffer->red_mask_shift,
        framebuffer->green_mask_size, framebuffer->green_mask_shift,
        framebuffer->blue_mask_size, framebuffer->blue_mask_shift,
        NULL,
        NULL, NULL,
        NULL, NULL,
        NULL, NULL,
        NULL, 0, 0, 1,
        0, 0,
        0
    );
}

void term_write(const char *c) {
    flanterm_write(context, c, strlen(c));
}