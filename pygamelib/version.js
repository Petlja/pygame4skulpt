var $builtinmodule = function(name) {
        mod = {};
        mod.ver = new Sk.builtin.func(function () {
            return Sk.ffi.remapToPy("1.9.3");
        });
        mod.vernum = new Sk.builtin.func(function () {
            return Sk.builtin.tuple([1, 9, 3]);
        });
        mod.rev = new Sk.builtin.func(function () {
            return Sk.builtin.none.none$;
        });
        return mod;
    };