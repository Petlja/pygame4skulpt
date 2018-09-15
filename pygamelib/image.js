var $builtinmodule = function (name) {
    mod = {};
    mod.load = new Sk.builtin.func(load_image);
    mod.get_extended = new Sk.builtin.func(function () {
        return Sk.ffi.remapToPy(false);
    });
    mod.save = new Sk.builtin.func(function (surf, filename) {

    });
    return mod;
}

var load_image = function (filename) {
    return new Sk.misceval.promiseToSuspension(new Promise(function (resolve) {
        var img = new Image();
        img.src = PygameLib.imgPath + Sk.ffi.remapToJs(filename);
        img.onload = function () {
            var w = PygameLib.surface.width;
            var h = PygameLib.surface.height;
            var t = Sk.builtin.tuple([img.width, img.height]);
            var s = Sk.misceval.callsim(PygameLib.SurfaceType, t, false);
            var ctx = s.offscreen_canvas.getContext("2d");
            ctx.drawImage(img, 0, 0);
            resolve(s);
        }
    }));
}