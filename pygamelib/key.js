var $builtinmodule = function(name) {
        mod = {};

        mod.set_repeat = new Sk.builtin.func(function (delay, interval) {
            // TODO: consider a more realistic implementation where the interval is taken into account
            if (delay !== undefined) {
                PygameLib.repeatKeys = true;
            } else {
                PygameLib.repeatKeys = false;
            }
        });
        mod.get_repeat = new Sk.builtin.func(function() {
            if (PygameLib.repeatKeys) {
                return Sk.builtin.tuple([1, 1]);
            } else {
                return Sk.builtin.tuple([0, 0]);
            }
        });
        mod.get_focused = new Sk.builtin.func(function () {
            return Sk.ffi.remapToPy(document.hasFocus());
        });
        mod.get_pressed = new Sk.builtin.func(function () {
            var pressed = new Array(323).fill(false);
            for (var i = 0; i < PygameLib.eventQueue.length; i++) {
                pressed[PygameLib.eventQueue[i][1].key] = true;
            }
            return Sk.ffi.remapToPy(pressed);
        });
        mod.get_mods = new Sk.builtin.func(function () {
            var mask = 0;
            for (var i = 0; i < PygameLib.eventQueue.length; i++) {
                for (var j = 0; j < keyboardModifierKeys.length; j++) {
                    if (PygameLib.eventQueue[i][1].key === keyboardModifierKeys[j]) {
                        mask &= 1 << j;
                    }
                }
            }
            return Sk.ffi.remapToPy(mask);
        });
        mod.set_mods = new Sk.builtin.func(function(m) {
            var mask = Sk.ffi.remapToJs(m);
            for (var i = 0; i < keyboardModifierKeys.length; i++) {
                if (mask & (1 << i)) {
                    PygameLib.eventQueue.unshift([PygameLib.constants.KEYDOWN, { key: keyboardModifierKeys[i]}]);
                }
            }

        });
        mod.name = new Sk.builtin.func(function (idx) {
            var i = Sk.ffi.remapToJs(idx);
            if (i < 0 || i >= 323) {
                return Sk.ffi.remapToPy("unknown key");
            }
            return Sk.ffi.remapToPy(keyToName[i]);
        });
        return mod;
    };