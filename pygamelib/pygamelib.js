var PygameLib = {};

PygameLib.eventSource = typeof window !== 'undefined' ? window : global;

function keydownEventListener(event) {
    var e = [PygameLib.constants.KEYDOWN, { key: event.key }];
    if (event.key == "Escape")  {
        e[0] = PygameLib.constants.QUIT;
    }
    PygameLib.eventQueue.unshift(e);
}

PygameLib.init = function (baseURL, canvasElement) {
    Sk.externalLibraries = Sk.externalLibraries || {};
    var pygame_modules = {
        'pygame.display': {
            path: baseURL + '/display.js'
        },
        'pygame.event': {
            path: baseURL + '/event.js'
        },
        'pygame.draw': {
            path: baseURL + '/draw.js'
        },
        'pygame': {
            path: baseURL + '/pygame.js',
        }
    };
    for (var k in pygame_modules) {
        Sk.externalLibraries[k] = pygame_modules[k];
    }
    PygameLib.CanvasElement = canvasElement;
    PygameLib.eventSource.addEventListener("keydown", keydownEventListener);
}

// pygame module
function pygame_init() {
    // ovo je mi ne izgleda najelegantnije, ali još nisam našao lepši način 
    var display_m = Sk.importModule("pygame.display", false, false);
    var event_m   = Sk.importModule("pygame.event", false, false);
    var draw_m    = Sk.importModule("pygame.draw", false, false);
    var pygame_m  = Sk.importModule("pygame", false, false);
    pygame_m.$d['display'] = display_m.$d['display'];
    pygame_m.$d['event'] = display_m.$d['event'];
    pygame_m.$d['draw'] = display_m.$d['draw'];
    // testiranja radi stavili smo nešto u queue na početku
    PygameLib.eventQueue = [
        [PygameLib.constants.KEYDOWN, {'key':PygameLib.constants.K_SPACE}]
    ];
}

PygameLib.pygame_module = function (name) {
    var mod = {};
    for (k in PygameLib.constants) {
        mod[k] = Sk.ffi.remapToPy(PygameLib.constants[k]);
    }
    mod.init = new Sk.builtin.func(pygame_init);
    mod.Surface = Sk.misceval.buildClass(mod, surface$1, 'Surface', []);
    PygameLib.SurfaceType = mod.Surface;
    mod.Color = Sk.misceval.buildClass(mod, color_type_f, 'Color', []);
    PygameLib.ColorType = mod.Color;
    mod.Rect = Sk.misceval.buildClass(mod, rect_type_f, 'Rect', []);
    PygameLib.RectType = mod.Rect;
    return mod;
}


// Surface([width, height])
var init$1 = function $__init__123$(self, size) {
    Sk.builtin.pyCheckArgs('__init__', arguments, 2, 5, false, false);
    self.canvasElement = PygameLib.CanvasElement;
    self.context2d = self.canvasElement.getContext("2d");
    var tuple_js = Sk.ffi.remapToJs(size);
    self.width = tuple_js[0];
    self.height = tuple_js[1];
    self.canvasElement.setAttribute('width', self.width);
    self.canvasElement.setAttribute('height', self.height);
    if (self.width < 0 || self.height < 0) {
      throw new PygameError('Invalid resolution for Surface');
    }
    return Sk.builtin.none.none$;
};
init$1.co_name = new Sk.builtins['str']('__init__');
init$1.co_varnames = ['self', 'size', 'flags', 'depth', 'masks'];
init$1.$defaults = [new Sk.builtin.int_(0), new Sk.builtin.int_(0), Sk.builtin.none.none$];
  
var repr$1 = function $__repr__123$(self) {
    var width = Sk.ffi.remapToJs(self.width);
    var height = Sk.ffi.remapToJs(self.height);

    return Sk.ffi.remapToPy('<Surface(' + width + 'x' + height + 'x32 SW)>');
};
repr$1.co_name = new Sk.builtins['str']('__repr__');
repr$1.co_varnames = ['self'];
  
function get_height(self) {
    Sk.builtin.pyCheckArgs('get_height', arguments, 1, 1, false, false);
    return self.height;
}
get_height.co_name = new Sk.builtins['str']('get_height');
get_height.co_varnames = ['self'];
  
function get_width(self) {
    Sk.builtin.pyCheckArgs('get_width', arguments, 1, 1, false, false);
    return self.width;
}
get_width.co_name = new Sk.builtins['str']('get_width');
get_width.co_varnames = ['self'];
  
function get_size(self) {
    Sk.builtin.pyCheckArgs('get_size', arguments, 1, 1, false, false);
    return Sk.builtin.tuple([self.width, self.height]);
}
get_size.co_name = new Sk.builtins['str']('get_size');
get_size.co_varnames = ['self'];
  
function get_flags() {
    Sk.builtin.pyCheckArgs('get_flags', arguments, 1, 1, false, false);
    return new Sk.builtin.int_(0);
}
get_flags.co_name = new Sk.builtins['str']('get_flags');
get_flags.co_varnames = ['self'];
  
var surface$1 = function $Surface$class_outer(gbl, loc) {
    loc.__init__ = new Sk.builtins.function(init$1, gbl);
    loc.__repr__ = new Sk.builtins.function(repr$1, gbl);

    loc.get_width = new Sk.builtins.function(get_width, gbl);
    loc.get_height = new Sk.builtins.function(get_height, gbl);
    loc.get_size = new Sk.builtins.function(get_size, gbl);
    loc.get_flags = new Sk.builtins.function(get_flags, gbl);

    return;
};
  
surface$1.co_name = new Sk.builtins['str']('Surface');

// pygame.display module
PygameLib.display_module = function (name) {
    var mod = {};
    mod.set_mode = new Sk.builtin.func(function (size) {
        //Create Surface object and return it
        return Sk.misceval.callsim(PygameLib.SurfaceType, size);
    });
    return mod;
}

// pygame.event module
function event_get() {
    var list = [];
    var t,d;
    while((event = PygameLib.eventQueue.pop())!== undefined) {
        var type = Sk.ffi.remapToPy(event[0]);
        var dictjs =event[1];
        kvs = [];
        for (k in dictjs) {
            kvs.push(Sk.ffi.remapToPy(k));
            kvs.push(Sk.ffi.remapToPy(dictjs[k]));
        }
        var dict = new Sk.builtin.dict(kvs);
        var e = Sk.misceval.callsim(PygameLib.EventType, type, dict);
        list.push(e);
    }
    return new Sk.builtin.list(list);
}

function event_EventType_f($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self,type,dict) {
        Sk.builtin.pyCheckArgs('__init__', arguments, 2, 3, false, false);
        dict = dict || new Sk.builtin.dict();
        Sk.abstr.sattr(self, 'dict', dict, false);
        Sk.abstr.sattr(self, 'type', type, false);
        dictjs = Sk.ffi.remapToJs(dict); 
        for(k in dictjs) {
            Sk.abstr.sattr(self, k, Sk.ffi.remapToPy(dictjs[k]), false);
        }
        return Sk.builtin.none.none$;
    });
    $loc.__init__.co_name = new Sk.builtins['str']('__init__');
    $loc.__init__.co_varnames = ['self', 'type', 'dict'];

    $loc.__repr__ = new Sk.builtin.func(function(self) {
        var dict = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'dict', false)['$r']());
        var type = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'type', false)['$r']());
        return Sk.ffi.remapToPy('<Event(' + type + ' ' + dict + ')>');
    });
    $loc.__repr__.co_name = new Sk.builtins['str']('__repr__');
    $loc.__repr__.co_varnames = ['self'];

}

PygameLib.event_module = function (name) {
    var mod = {};
    mod.get = new Sk.builtin.func(event_get);
    mod.EventType = Sk.misceval.buildClass(mod, event_EventType_f, "EventType",[]);
    PygameLib.EventType = mod.EventType;
    mod.Event = new Sk.builtin.func(function(type,dict) {
        return Sk.misceval.callsim(mod.EventType, type, dict)
    });
    return mod;
}

//pygame.Color
function color_type_f($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, r, g, b, a) {
        Sk.builtin.pyCheckArgs('__init__', arguments, 5, 5, false, false);
        Sk.abstr.sattr(self, 'r', r, false);
        Sk.abstr.sattr(self, 'g', g, false);
        Sk.abstr.sattr(self, 'b', b, false);
        Sk.abstr.sattr(self, 'a', a, false);
        return Sk.builtin.none.none$;
    });
    $loc.__init__.co_name = new Sk.builtins['str']('__init__');
    $loc.__init__.co_varnames = ['self', 'r', 'g', 'b', 'a'];

    $loc.__repr__ = new Sk.builtin.func(function(self) {
        var r = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'r', false)['$r']());
        var g = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'g', false)['$r']());
        var b = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'b', false)['$r']());
        var a = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'a', false)['$r']());
        return Sk.ffi.remapToPy('<Color(' + r + ', ' + g + ', ' + b + ', ' + a + ')>');
    });
    $loc.__repr__.co_name = new Sk.builtins['str']('__repr__');
    $loc.__repr__.co_varnames = ['self'];

    $loc.set_r = new Sk.builtin.func(function(self, r) {
        Sk.abstr.sattr(self, 'r', r, false);
    });
    $loc.set_r.co_name = new Sk.builtins['str']('set_r');
    $loc.set_r.co_varnames = ['self', 'r'];

    $loc.set_g = new Sk.builtin.func(function(self, g) {
        Sk.abstr.sattr(self, 'g', g, false);
    });
    $loc.set_g.co_name = new Sk.builtins['str']('set_g');
    $loc.set_g.co_varnames = ['self', 'g'];

    $loc.set_b = new Sk.builtin.func(function(self, b) {
        Sk.abstr.sattr(self, 'b', b, false);
    });
    $loc.set_b.co_name = new Sk.builtins['str']('set_b');
    $loc.set_b.co_varnames = ['self', 'b'];

    $loc.set_a = new Sk.builtin.func(function(self, a) {
        Sk.abstr.sattr(self, 'a', a, false);
    });
    $loc.set_a.co_name = new Sk.builtins['str']('set_a');
    $loc.set_a.co_varnames = ['self', 'a'];
}

//pygame.Rect
function rect_type_f($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, left, top, width, height) {
        Sk.builtin.pyCheckArgs('__init__', arguments, 5, 5, false, false);
        Sk.abstr.sattr(self, 'top', top, false);
        Sk.abstr.sattr(self, 'left', left, false);
        Sk.abstr.sattr(self, 'width', width, false);
        Sk.abstr.sattr(self, 'height', height, false);
        return Sk.builtin.none.none$;
    });
    $loc.__init__.co_name = new Sk.builtins['str']('__init__');
    $loc.__init__.co_varnames = ['self', 'left', 'top', 'width', 'heght'];

    $loc.__repr__ = new Sk.builtin.func(function(self) {
        var left = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'left', false)['$r']());
        var top = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'top', false)['$r']());
        var width = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'width', false)['$r']());
        var height = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'height', false)['$r']());
        return Sk.ffi.remapToPy('<Rect(' + left + ', ' + top + ', ' + width + ', ' + height + ')>');
    });
    $loc.__repr__.co_name = new Sk.builtins['str']('__repr__');
    $loc.__repr__.co_varnames = ['self'];
}

//pygame.draw
PygameLib.draw_module = function(name) {
    mod = {};
    mod.rect = new Sk.builtin.func(draw_rect);
    mod.line = new Sk.builtin.func(draw_line);
    return mod;
}

var draw_rect = function(surface, color, rect, width = 0) {
    var ctx = surface.context2d;
}

var draw_line = function(surface, color, start_pos, end_pos, width = 1) {
    var width_js = Sk.ffi.remapToJs(width);
    var start_pos_js = Sk.ffi.remapToJs(start_pos);
    var end_pos_js = Sk.ffi.remapToJs(end_pos);
    var ctx = surface.context2d;
    ctx.beginPath();
    ctx.lineWidth = width_js;
    ctx.moveTo(start_pos_js[0], start_pos_js[1]);
    ctx.lineTo(end_pos_js[0], end_pos_js[1]);
    ctx.stroke();
}

// constants
PygameLib.constants = {
    'ACTIVEEVENT': 1,
    'ANYFORMAT': 268435456,
    'ASYNCBLIT': 4,
    'AUDIO_S16': 32784,
    'AUDIO_S16LSB': 32784,
    'AUDIO_S16MSB': 36880,
    'AUDIO_S16SYS': 32784,
    'AUDIO_S8': 32776,
    'AUDIO_U16': 16,
    'AUDIO_U16LSB': 16,
    'AUDIO_U16MSB': 4112,
    'AUDIO_U16SYS': 16,
    'AUDIO_U8': 8,
    'BIG_ENDIAN': 4321,
    'BLEND_ADD': 1,
    'BLEND_MAX': 5,
    'BLEND_MIN': 4,
    'BLEND_MULT': 3,
    'BLEND_PREMULTIPLIED': 17,
    'BLEND_RGBA_ADD': 6,
    'BLEND_RGBA_MAX': 16,
    'BLEND_RGBA_MIN': 9,
    'BLEND_RGBA_MULT': 8,
    'BLEND_RGBA_SUB': 7,
    'BLEND_RGB_ADD': 1,
    'BLEND_RGB_MAX': 5,
    'BLEND_RGB_MIN': 4,
    'BLEND_RGB_MULT': 3,
    'BLEND_RGB_SUB': 2,
    'BLEND_SUB': 2,
    'BUTTON_X1': 6,
    'BUTTON_X2': 7,
    'DOUBLEBUF': 1073741824,
    'FULLSCREEN': -2147483648,
    'GL_ACCELERATED_VISUAL': 15,
    'GL_ACCUM_ALPHA_SIZE': 11,
    'GL_ACCUM_BLUE_SIZE': 10,
    'GL_ACCUM_GREEN_SIZE': 9,
    'GL_ACCUM_RED_SIZE': 8,
    'GL_ALPHA_SIZE': 3,
    'GL_BLUE_SIZE': 2,
    'GL_BUFFER_SIZE': 4,
    'GL_DEPTH_SIZE': 6,
    'GL_DOUBLEBUFFER': 5,
    'GL_GREEN_SIZE': 1,
    'GL_MULTISAMPLEBUFFERS': 13,
    'GL_MULTISAMPLESAMPLES': 14,
    'GL_RED_SIZE': 0,
    'GL_STENCIL_SIZE': 7,
    'GL_STEREO': 12,
    'GL_SWAP_CONTROL': 16,
    'HAT_CENTERED': 0,
    'HAT_DOWN': 4,
    'HAT_LEFT': 8,
    'HAT_LEFTDOWN': 12,
    'HAT_LEFTUP': 9,
    'HAT_RIGHT': 2,
    'HAT_RIGHTDOWN': 6,
    'HAT_RIGHTUP': 3,
    'HAT_UP': 1,
    'HAVE_NEWBUF': 1,
    'HWACCEL': 256,
    'HWPALETTE': 536870912,
    'HWSURFACE': 1,
    'IYUV_OVERLAY': 1448433993,
    'JOYAXISMOTION': 7,
    'JOYBALLMOTION': 8,
    'JOYBUTTONDOWN': 10,
    'JOYBUTTONUP': 11,
    'JOYHATMOTION': 9,
    'KEYDOWN': 2,
    'KEYUP': 3,
    'KMOD_ALT': 768,
    'KMOD_CAPS': 8192,
    'KMOD_CTRL': 192,
    'KMOD_LALT': 256,
    'KMOD_LCTRL': 64,
    'KMOD_LMETA': 1024,
    'KMOD_LSHIFT': 1,
    'KMOD_META': 3072,
    'KMOD_MODE': 16384,
    'KMOD_NONE': 0,
    'KMOD_NUM': 4096,
    'KMOD_RALT': 512,
    'KMOD_RCTRL': 128,
    'KMOD_RMETA': 2048,
    'KMOD_RSHIFT': 2,
    'KMOD_SHIFT': 3,
    'K_0': 48,
    'K_1': 49,
    'K_2': 50,
    'K_3': 51,
    'K_4': 52,
    'K_5': 53,
    'K_6': 54,
    'K_7': 55,
    'K_8': 56,
    'K_9': 57,
    'K_AMPERSAND': 38,
    'K_ASTERISK': 42,
    'K_AT': 64,
    'K_BACKQUOTE': 96,
    'K_BACKSLASH': 92,
    'K_BACKSPACE': 8,
    'K_BREAK': 318,
    'K_CAPSLOCK': 301,
    'K_CARET': 94,
    'K_CLEAR': 12,
    'K_COLON': 58,
    'K_COMMA': 44,
    'K_DELETE': 127,
    'K_DOLLAR': 36,
    'K_DOWN': 274,
    'K_END': 279,
    'K_EQUALS': 61,
    'K_ESCAPE': 27,
    'K_EURO': 321,
    'K_EXCLAIM': 33,
    'K_F1': 282,
    'K_F10': 291,
    'K_F11': 292,
    'K_F12': 293,
    'K_F13': 294,
    'K_F14': 295,
    'K_F15': 296,
    'K_F2': 283,
    'K_F3': 284,
    'K_F4': 285,
    'K_F5': 286,
    'K_F6': 287,
    'K_F7': 288,
    'K_F8': 289,
    'K_F9': 290,
    'K_FIRST': 0,
    'K_GREATER': 62,
    'K_HASH': 35,
    'K_HELP': 315,
    'K_HOME': 278,
    'K_INSERT': 277,
    'K_KP0': 256,
    'K_KP1': 257,
    'K_KP2': 258,
    'K_KP3': 259,
    'K_KP4': 260,
    'K_KP5': 261,
    'K_KP6': 262,
    'K_KP7': 263,
    'K_KP8': 264,
    'K_KP9': 265,
    'K_KP_DIVIDE': 267,
    'K_KP_ENTER': 271,
    'K_KP_EQUALS': 272,
    'K_KP_MINUS': 269,
    'K_KP_MULTIPLY': 268,
    'K_KP_PERIOD': 266,
    'K_KP_PLUS': 270,
    'K_LALT': 308,
    'K_LAST': 323,
    'K_LCTRL': 306,
    'K_LEFT': 276,
    'K_LEFTBRACKET': 91,
    'K_LEFTPAREN': 40,
    'K_LESS': 60,
    'K_LMETA': 310,
    'K_LSHIFT': 304,
    'K_LSUPER': 311,
    'K_MENU': 319,
    'K_MINUS': 45,
    'K_MODE': 313,
    'K_NUMLOCK': 300,
    'K_PAGEDOWN': 281,
    'K_PAGEUP': 280,
    'K_PAUSE': 19,
    'K_PERIOD': 46,
    'K_PLUS': 43,
    'K_POWER': 320,
    'K_PRINT': 316,
    'K_QUESTION': 63,
    'K_QUOTE': 39,
    'K_QUOTEDBL': 34,
    'K_RALT': 307,
    'K_RCTRL': 305,
    'K_RETURN': 13,
    'K_RIGHT': 275,
    'K_RIGHTBRACKET': 93,
    'K_RIGHTPAREN': 41,
    'K_RMETA': 309,
    'K_RSHIFT': 303,
    'K_RSUPER': 312,
    'K_SCROLLOCK': 302,
    'K_SEMICOLON': 59,
    'K_SLASH': 47,
    'K_SPACE': 32,
    'K_SYSREQ': 317,
    'K_TAB': 9,
    'K_UNDERSCORE': 95,
    'K_UNKNOWN': 0,
    'K_UP': 273,
    'K_a': 97,
    'K_b': 98,
    'K_c': 99,
    'K_d': 100,
    'K_e': 101,
    'K_f': 102,
    'K_g': 103,
    'K_h': 104,
    'K_i': 105,
    'K_j': 106,
    'K_k': 107,
    'K_l': 108,
    'K_m': 109,
    'K_n': 110,
    'K_o': 111,
    'K_p': 112,
    'K_q': 113,
    'K_r': 114,
    'K_s': 115,
    'K_t': 116,
    'K_u': 117,
    'K_v': 118,
    'K_w': 119,
    'K_x': 120,
    'K_y': 121,
    'K_z': 122,
    'LIL_ENDIAN': 1234,
    'MOUSEBUTTONDOWN': 5,
    'MOUSEBUTTONUP': 6,
    'MOUSEMOTION': 4,
    'NOEVENT': 0,
    'NOFRAME': 32,
    'NUMEVENTS': 32,
    'OPENGL': 2,
    'OPENGLBLIT': 10,
    'PREALLOC': 16777216,
    'QUIT': 12,
    'RESIZABLE': 16,
    'RLEACCEL': 16384,
    'RLEACCELOK': 8192,
    'SCRAP_BMP': 'image/bmp',
    'SCRAP_CLIPBOARD': 0,
    'SCRAP_PBM': 'image/pbm',
    'SCRAP_PPM': 'image/ppm',
    'SCRAP_SELECTION': 1,
    'SCRAP_TEXT': 'text/plain',
    'SRCALPHA': 65536,
    'SRCCOLORKEY': 4096,
    'SWSURFACE': 0,
    'SYSWMEVENT': 13,
    'TIMER_RESOLUTION': 10,
    'USEREVENT': 24,
    'USEREVENT_DROPFILE': 4096,
    'UYVY_OVERLAY': 1498831189,
    'VIDEOEXPOSE': 17,
    'VIDEORESIZE': 16,
    'YUY2_OVERLAY': 844715353,
    'YV12_OVERLAY': 842094169,
    'YVYU_OVERLAY': 1431918169
}