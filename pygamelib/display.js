var $builtinmodule =  function (name) {
        var mod = {};
        mod.set_mode = new Sk.builtin.func(function (size) {
            mod.surface = Sk.misceval.callsim(PygameLib.SurfaceType, size, true);
            PygameLib.surface = mod.surface;
            return mod.surface;
        });
        mod.update = new Sk.builtin.func(function() {
            Sk.misceval.callsim(mod.surface.update, mod.surface);
        });
        mod.flip = new Sk.builtin.func(function() {
            Sk.misceval.callsim(mod.surface.update, mod.surface);
        });
        mod.set_caption = new Sk.builtin.func(function(caption) {
            if ($('.modal-title')) $('.modal-title').html(Sk.ffi.remapToJs(caption));
            PygameLib.caption = Sk.ffi.remapToJs(caption);
        });
        return mod;
    };