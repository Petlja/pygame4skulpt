var $builtinmodule=function e(n){mod={};mod.load=new Sk.builtin.func(function(e){function n(e){var n=new XMLHttpRequest;n.open("HEAD",e,true);n.send();return n.status===200}if(n(Sk.imgPath+Sk.ffi.remapToJs(e))){return Sk.misceval.promiseToSuspension(new Promise(function(i){var a=new Image;a.crossOrigin="";a.src=Sk.imgPath+Sk.ffi.remapToJs(e);a.onload=function(){var e=Sk.builtin.tuple([a.width,a.height]);var n=Sk.misceval.callsim(PygameLib.SurfaceType,e);var t=n.offscreen_canvas.getContext("2d");t.drawImage(a,0,0);i(n)}}))}else throw new Sk.builtin.RuntimeError("Image does not exist.")});mod.get_extended=new Sk.builtin.func(function(){return Sk.ffi.remapToPy(false)});mod.save=new Sk.builtin.func(function(e,n){var t="surface";if(n!==undefined){t=Sk.ffi.remapToJs(n)}i(e.offscreen_canvas,t);function i(e,n){var t,i,a;function o(e){function n(e,n){var t=document.createElement("canvas");t.width=e;t.height=n;return t}var t=canvas(img.width,img.height);t.ctx=t.getContext("2d");t.ctx.drawImage(e,0,0);return t}if(e.toDataURL===undefined){e=o(e)}if(e.msToBlob!==undefined&&navigator.msSaveBlob!==undefined){a=e.msToBlob();navigator.msSaveBlob(a,n+".png");return}t=document.createElement("a");t.href=e.toDataURL();if(t.download!==undefined){t.download=n+".png";if(typeof MouseEvent==="function"){i=new MouseEvent("click",{view:window,bubbles:true,cancelable:true,ctrlKey:false,altKey:false,shiftKey:false,metaKey:false,button:0,buttons:1});t.dispatchEvent(i)}else if(t.fireEvent){t.fireEvent("onclick")}}}});return mod};