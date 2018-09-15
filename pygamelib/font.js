var $builtinmodule = function (name) {
    mod = {};
    mod.__is_initialized = false;
    mod.SysFont = Sk.misceval.buildClass(mod, font_SysFont, "SysFontType", []);
    PygameLib.SysFontType = mod.SysFontType;
    // TODO: Font class
    mod.init = new Sk.builtin.func(function () {
        mod.__is_initialized = true;
    });
    mod.quit = new Sk.builtin.func(function () {
        mod.__is_initialized = false;
    });
    mod.get_init = new Sk.builtin.func(function () {
        if (mod.__is_initialized) {
            return Sk.ffi.remapToPy(true);
        }
        return Sk.ffi.remapToPy(false);
    });
    mod.get_default_font = new Sk.builtin.func(function () {
        return Sk.ffi.remapToPy('arial');
    });
    mod.get_fonts = new Sk.builtin.func(function () {
        return Sk.ffi.remapToPy(['arial', 'helvetica', 'times', 'courier']);
        // TODO: maybe we should extend this list
    });
    mod.match_font = new Sk.builtin.func(function () {
        return Sk.builtin.none.none$;
        // TODO: how do we browse the filesystem from JS?
    });
    return mod;
};

function font_SysFont($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function (self, name, size, bold, italic) {
        Sk.abstr.sattr(self, 'name', name, false);
        Sk.abstr.sattr(self, 'sz', size, false);
        if (bold === undefined) {
            Sk.abstr.sattr(self, 'bold', Sk.ffi.remapToPy(false), false);
        } else {
            Sk.abstr.sattr(self, 'bold', bold, false);
        }
        if (italic === undefined) {
            Sk.abstr.sattr(self, 'italic', Sk.ffi.remapToPy(false), false);
        } else {
            Sk.abstr.sattr(self, 'italic', italic, false);
        }
        Sk.abstr.sattr(self, 'underline', Sk.ffi.remapToPy(false), false);
        return Sk.builtin.none.none$;
    }, $gbl);
    $loc.__init__.co_name = new Sk.builtins['str']('__init__');
    $loc.__init__.co_varnames = ['bold', 'italic'];
    $loc.__init__.$defaults = [false, false];

    $loc.__repr__ = new Sk.builtin.func(function (self) {
        var name = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'name', false));
        var size = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'sz', false));
        return Sk.ffi.remapToPy('<SysFont(' + name + ' ' + size + ')>');
    });
    $loc.__repr__.co_name = new Sk.builtins['str']('__repr__');
    $loc.__repr__.co_varnames = ['self'];

    $loc.render = new Sk.builtin.func(renderFont, $gbl);
    $loc.render.co_name = new Sk.builtins['str']('render');
    $loc.render.co_varnames = ['self', 'text', 'antialias', 'color', 'background'];
    $loc.render.$defaults = [Sk.builtin.none.none$];

    $loc.size = new Sk.builtin.func(fontSize, $gbl);
    $loc.size.co_name = new Sk.builtins['str']('size');

    $loc.set_underline = new Sk.builtin.func(function (self, bool) {
        Sk.abstr.sattr(self, 'underline', bool, false);
    }, $gbl);
    $loc.get_underline = new Sk.builtin.func(function (self) {
        return Sk.abstr.gattr(self, 'underline', false);
    }, $gbl);

    $loc.set_italic = new Sk.builtin.func(function (self, bool) {
        Sk.abstr.sattr(self, 'italic', bool, false);
    }, $gbl);
    $loc.get_italic = new Sk.builtin.func(function (self) {
        return Sk.abstr.gattr(self, 'italic', false);
    }, $gbl);

    $loc.set_bold = new Sk.builtin.func(function (self, bool) {
        Sk.abstr.sattr(self, 'bold', bool, false);
    }, $gbl);
    $loc.get_bold = new Sk.builtin.func(function (self) {
        return Sk.abstr.gattr(self, 'bold', false);
    }, $gbl);
}

font_SysFont.co_name = new Sk.builtins['str']('SysFont');

function fontSize(self, text) {
    var msg = Sk.ffi.remapToJs(text);
    var h = 1.01 * Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'sz', false));
    var fontName = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'name', false));
    fontName = "" + h + "px " + fontName;
    var bold = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'bold', false));
    if (bold) {
        fontName = 'bold ' + fontName;
    }
    var italic = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'italic', false));
    if (italic) {
        fontName = 'italic ' + fontName;
    }
    var w = 300;

    // Create a dummy canvas in order to exploit its measureText() method
    var t = Sk.builtin.tuple([w, h]);
    var s = Sk.misceval.callsim(PygameLib.SurfaceType, t, false);
    var ctx = s.offscreen_canvas.getContext("2d");
    ctx.font = fontName;
    return new Sk.builtin.tuple([ctx.measureText(msg).width, h]);
}

function renderFont(self, text, antialias, color, background) {
    // TODO: antialias is ignored
    var msg = Sk.ffi.remapToJs(text);
    var STRETCH_CONST = 1.1;
    var h = STRETCH_CONST * Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'sz', false));
    var fontName = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'name', false));
    fontName = "" + h + "px " + fontName;
    var bold = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'bold', false));
    if (bold) {
        fontName = 'bold ' + fontName;
    }
    var italic = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'italic', false));
    if (italic) {
        fontName = 'italic ' + fontName;
    }
    var underline = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'underline', false));

    var w = 300;

    // Create a dummy canvas in order to exploit its measureText() method
    var t = Sk.builtin.tuple([w, h]);
    var s = Sk.misceval.callsim(PygameLib.SurfaceType, t, false);
    var ctx = s.offscreen_canvas.getContext("2d");
    ctx.font = fontName;
    w = ctx.measureText(msg).width;

    t = Sk.builtin.tuple([w, h]);
    s = Sk.misceval.callsim(PygameLib.SurfaceType, t, false);
    ctx = s.offscreen_canvas.getContext("2d");
    if (background !== undefined) {
        var background_js = extract_color(background);
        ctx.fillStyle = 'rgba(' + background_js[0] + ', ' + background_js[1] + ', ' + background_js[2] + ', '
            + background_js[3] + ')';
        ctx.fillRect(0, 0, s.offscreen_canvas.width, s.offscreen_canvas.height);
    }
    ctx.font = fontName;
    var color_js = extract_color(color);
    ctx.fillStyle = 'rgba(' + color_js[0] + ', ' + color_js[1] + ', ' + color_js[2] + ', ' + color_js[3] + ')';
    ctx.fillText(msg, 0, 1 / STRETCH_CONST * h);
    if (underline) {
        ctx.strokeStyle = 'rgba(' + color_js[0] + ', ' + color_js[1] + ', ' + color_js[2] + ', ' + color_js[3] + ')';
        ctx.lineWidth = 1;
        ctx.moveTo(0, h - 1);
        ctx.lineTo(w, h - 1);
        ctx.stroke();
    }
    return s;
}

//converts color argument to js type
var extract_color = function (color) {
    var color_js = [0, 0, 0, 0];
    if (Sk.abstr.typeName(color) == "Color") {
        color_js[0] = Sk.ffi.remapToJs(Sk.abstr.gattr(color, 'r', false));
        color_js[1] = Sk.ffi.remapToJs(Sk.abstr.gattr(color, 'g', false));
        color_js[2] = Sk.ffi.remapToJs(Sk.abstr.gattr(color, 'b', false));
        color_js[3] = Sk.ffi.remapToJs(Sk.abstr.gattr(color, 'a', false));
    }
    else {
        color_js = Sk.ffi.remapToJs(color);
        if (color_js.length == 3) color_js.push(1);
    }
    return color_js;
}