var $builtinmodule = function (name) {
    mod = {};
    mod.ver = Sk.ffi.remapToPy("1.9.3");
    mod.vernum = Sk.builtin.tuple([1, 9, 3]);
    mod.rev = Sk.builtin.none.none$;
    return mod;
};
