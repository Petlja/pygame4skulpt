var $builtinmodule = function (name) {
    mod = {};
    mod.wait = new Sk.builtin.func(function (amount) {
        var t_m = Sk.importModule("time", false, true);
        var sec = Sk.ffi.remapToJs(amount) / 1000;
        return Sk.misceval.callsimOrSuspend(t_m.$d['sleep'], Sk.ffi.remapToPy(sec));
    });

    mod.get_ticks = new Sk.builtin.func(function () {
        return Sk.ffi.remapToPy(new Date() - PygameLib.initial_time);
    });
    mod.delay = new Sk.builtin.func(function (amount) {
        var t_m = Sk.importModule("time", false, false);
        var sec = Sk.ffi.remapToJs(amount) / 1000;
        return Sk.misceval.callsimOrSuspend(t_m.$d['sleep'], Sk.ffi.remapToPy(sec));
    });
    mod.set_timer = new Sk.builtin.func(function (eventid, milliseconds) {
        var event = Sk.ffi.remapToJs(eventid);
        var ms = Sk.ffi.remapToJs(milliseconds);
        if (PygameLib.eventTimer[event]) {
            clearInterval(PygameLib.eventTimer[event].timer);
        }
        else {
            PygameLib.eventTimer[event] = {};
            PygameLib.eventTimer[event].f = function () {
                var e = [event, {}];
                PygameLib.eventQueue.unshift(e);
            }
        }
        if (ms) {
            PygameLib.eventTimer[event].timer = setInterval(PygameLib.eventTimer[event].f, ms);
        }
        return mod;
    });

    mod.Clock = Sk.misceval.buildClass(mod, time_Clock, 'Clock', []);
    PygameLib.ClockType = mod.Clock;
    return mod;
};

function time_Clock($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function (self) {
        Sk.abstr.sattr(self, 'prevTime', Sk.builtin.none.none$, false);
        Sk.abstr.sattr(self, 'getTime', Sk.builtin.none.none$, false);
        Sk.abstr.sattr(self, 'rawTime', Sk.ffi.remapToPy(0), false);
        Sk.abstr.sattr(self, 'fpsArray', Sk.ffi.remapToPy([]), false);
        Sk.abstr.sattr(self, 'fpsIdx', Sk.ffi.remapToPy(0));
        return Sk.builtin.none.none$;
    }, $gbl);
    $loc.__init__.co_name = new Sk.builtins['str']('__init__');

    $loc.tick = new Sk.builtin.func(function (self, framerate) {

        var currTime = Date.now();
        var mills = 0;
        if (Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'prevTime', false)) !== null) {
            var prevTime = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'prevTime', false));
            mills = (currTime - prevTime);
        }
        Sk.abstr.sattr(self, 'prevTime', Sk.ffi.remapToPy(currTime), false);
        Sk.abstr.sattr(self, 'getTime', Sk.ffi.remapToPy(mills), false);
        var arr = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'fpsArray', false));
        var idx = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'fpsIdx', false));
        if (arr.length < 10) {
            arr.push(mills);
        } else {
            arr[idx] = mills;
        }
        idx = (idx + 1) % 10;
        Sk.abstr.sattr(self, 'fpsArray', Sk.ffi.remapToPy(arr), false);
        Sk.abstr.sattr(self, 'fpsIdx', Sk.ffi.remapToPy(idx), false);
        if (framerate !== undefined) {
            var timeout = 1000 / Sk.ffi.remapToJs(framerate);
            return new Sk.misceval.promiseToSuspension(
                new Promise(function (resolve) {
                    var f = function () {
                        Sk.abstr.sattr(self, 'rawTime', Sk.ffi.remapToPy(Date.now() - currTime), false);
                        resolve(mills);
                    };

                    if (PygameLib.running) {
                        Sk.setTimeout(f, timeout);
                    }
                }));
        }
        Sk.abstr.sattr(self, 'rawTime', Sk.ffi.remapToPy(Date.now() - currTime), false);
        return Sk.ffi.remapToPy(mills);
    }, $gbl);
    $loc.tick.co_name = new Sk.builtins['str']('tick');
    $loc.tick.co_varnames = ['framerate'];
    $loc.tick.$defaults = [Sk.ffi.remapToPy(0)];

    $loc.tick_busy_loop = new Sk.builtin.func(function (self, framerate) {
        var currTime = Date.now();
        var mills = 0;
        if (Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'prevTime', false)) !== null) {
            var prevTime = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'prevTime', false));
            mills = (currTime - prevTime);
        }
        Sk.abstr.sattr(self, 'prevTime', Sk.ffi.remapToPy(currTime), false);
        Sk.abstr.sattr(self, 'getTime', Sk.ffi.remapToPy(mills), false);

        if (framerate !== undefined) {
            var timeout = 1000 / Sk.ffi.remapToJs(framerate);
            return new Sk.misceval.promiseToSuspension(
                new Promise(function (resolve) {
                    var f = function () {
                        Sk.abstr.sattr(self, 'rawTime', Sk.ffi.remapToPy(Date.now() - currTime), false);
                        resolve(mills);
                    };
                    if (PygameLib.running) {
                        Sk.setTimeout(f, timeout);
                    }
                }));
        }
        Sk.abstr.sattr(self, 'rawTime', Sk.ffi.remapToPy(Date.now() - currTime), false);
        return Sk.ffi.remapToPy(mills);
    }, $gbl);
    $loc.tick_busy_loop.co_name = new Sk.builtins['str']('tick_busy_loop');
    $loc.tick_busy_loop.co_varnames = ['framerate'];
    $loc.tick_busy_loop.$defaults = [Sk.ffi.remapToPy(0)];

    $loc.get_time = new Sk.builtin.func(function (self) {
        return Sk.abstr.gattr(self, 'getTime', false);
    });
    $loc.get_time.co_name = new Sk.builtins['str']('get_time');

    $loc.get_rawtime = new Sk.builtin.func(function (self) {
        return Sk.abstr.gattr(self, 'rawTime', false);
    });
    $loc.get_rawtime.co_name = new Sk.builtins['str']('get_rawtime');

    $loc.get_fps = new Sk.builtin.func(function (self) {
        var arr = Sk.ffi.remapToJs(Sk.abstr.gattr(self, 'fpsArray', false));
        if (arr.length < 10 || arr[0] === 0) {
            return Sk.ffi.remapToPy(0);
        }
        var sum = 0;
        for (var i = 0; i < 10; i++) {
            sum += arr[i];
        }
        return Sk.ffi.remapToPy(sum / 10);
    });
}

time_Clock.co_name = new Sk.builtins['str']('Clock');
