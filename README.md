# Pygame module for Skulpt
An example of the module can be found on [http://petlja.github.io/pygame4skulpt](http://petlja.github.io/pygame4skulpt).
## How to use
In order to use the module, you will probably want to have files served by a http server as in [run-example.sh](https://github.com/Petlja/pygame4skulpt/blob/master/run-example.sh) and [run-example.bat](https://github.com/Petlja/pygame4skulpt/blob/master/run-example.bat).  
else:
use `python compress_js.py` to compress js files.  
this command needs environment:   
`npm`  
`python3.5+`  
You need install:  
```npm i install babel uglifyjs -g```  
Our Pygame module can be imported as follows:
~~~
    var basePath = 'pygame/';
    Sk.externalLibraries = {
        'pygame': {
            path: basePath + '__init__.js',
        },
        'pygame.display': {
            path: basePath + 'display.js',
        },
        'pygame.draw': {
            path: basePath + 'draw.js',
        },
        'pygame.event': {
            path: basePath + 'event.js',
        },
        'pygame.font': {
            path: basePath + 'font.js',
        },
        'pygame.image': {
            path: basePath + 'image.js',
        },
        'pygame.key': {
            path: basePath + 'key.js',
        },
        'pygame.mouse': {
            path: basePath + 'mouse.js',
        },
        'pygame.time': {
            path: basePath + 'time.js',
        },
        'pygame.transform': {
            path: basePath + 'transform.js',
        },
        'pygame.version': {
            path: basePath + 'version.js',
        },
    };
~~~
Base path should correspond to the location where you put the Pygame module. A CDN version can be found at
[https://cdn.rawgit.com/Petlja/pygame4skulpt/3435847b/pygame/__init__.js](https://cdn.rawgit.com/Petlja/pygame4skulpt/3435847b/pygame/__init__.js).

### API
#### Sk.main_canvas
Since the Pygame module relies heavily on the graphics and event handling, we provide several functionalities for
communicating with the module. First and the most important one is registering your canvas. Basically, Pygame module
needs to have a reference to the canvas to be used for rendering graphics. In order to register your canvas, use the following:
~~~
Sk.main_canvas = document.createElement("canvas");
~~~
or
~~~
Sk.main_canvas = document.getElementById("myCanvas");
~~~

#### Sk.insertEvent
Pygame module has mouse and keyboard event listeners added to canvas and window. If you want to have an additional way of
inserting the events (eg. you want to add the arrows that create keydown events) you can use Sk.insertEvent function as follows:
~~~
Sk.insertEvent("left");
~~~
Currently, the only supported events are:
- "up" corresponding to ```KEYDOWN``` event with ```K_UP``` key.
- "down" corresponding to ```KEYDOWN``` event with ```K_DOWN``` key.
- "right" corresponding to ```KEYDOWN``` event with ```K_RIGHT``` key.
- "left" corresponding to ```KEYDOWN``` event with ```K_LEFT``` key.
- "quit" corresponding to ```QUIT``` event with ```K_ESCAPE``` key.

#### Sk.title_container
If you want to have an element where the title is going to be shown, make use of the following:
~~~
Sk.title_container = ...
~~~

#### Sk.quitHandler
After running the Pygame code, you want to make sure that everything got cleaned up. For that reason, there exists
```Sk.quitHandler``` which gets called by pygame.quit() method. An possible example is:
~~~
Sk.quitHandler = function () {
    $('.modal').modal('hide');
};
~~~
## Implemented parts
###### Most useful stuff:
- [x] Color
    - [x] pygame.Color.r	—	Gets or sets the red value of the Color.
    - [x] pygame.Color.g	—	Gets or sets the green value of the Color.
    - [x] pygame.Color.b	—	Gets or sets the blue value of the Color.
    - [x] pygame.Color.a	—	Gets or sets the alpha value of the Color.
    - [x] pygame.Color.cmy	—	Gets or sets the CMY representation of the Color.
    - [x] pygame.Color.hsva	—	Gets or sets the HSVA representation of the Color.
    - [x] pygame.Color.hsla	—	Gets or sets the HSLA representation of the Color.
    - [x] pygame.Color.i1i2i3	—	Gets or sets the I1I2I3 representation of the Color.
    - [x] pygame.Color.normalize	—	Returns the normalized RGBA values of the Color.
    - [x] pygame.Color.correct_gamma	—	Applies a certain gamma value to the Color.
    - [x] pygame.Color.set_length	—	Set the number of elements in the Color to 1,2,3, or 4.
- [x] display
    - [x] pygame.display.init	—	Initialize the display module
    - [x] pygame.display.quit	—	Uninitialize the display module
    - [x] pygame.display.get_init	—	Returns True if the display module has been initialized
    - [x] pygame.display.set_mode	—	Initialize a window or screen for display
    - [x] pygame.display.get_surface	—	Get a reference to the currently set display surface
    - [x] pygame.display.flip	—	Update the full display Surface to the screen
    - [x] pygame.display.update	—	Update portions of the screen for software displays
    - [ ] pygame.display.get_driver	—	Get the name of the pygame display backend
    - [ ] pygame.display.Info	—	Create a video display information object
    - [ ] pygame.display.get_wm_info	—	Get information about the current windowing system
    - [ ] pygame.display.list_modes	—	Get list of available fullscreen modes
    - [ ] pygame.display.mode_ok	—	Pick the best color depth for a display mode
    - [ ] pygame.display.gl_get_attribute	—	Get the value for an OpenGL flag for the current display
    - [ ] pygame.display.gl_set_attribute	—	Request an OpenGL display attribute for the display mode
    - [x] pygame.display.get_active	—	Returns True when the display is active on the display
    - [ ] pygame.display.iconify	—	Iconify the display surface
    - [ ] pygame.display.toggle_fullscreen	—	Switch between fullscreen and windowed displays
    - [ ] pygame.display.set_gamma	—	Change the hardware gamma ramps
    - [ ] pygame.display.set_gamma_ramp	—	Change the hardware gamma ramps with a custom lookup
    - [ ] pygame.display.set_icon	—	Change the system image for the display window
    - [x] pygame.display.set_caption	—	Set the current window caption
    - [x] pygame.display.get_caption	—	Get the current window caption
    - [ ] pygame.display.set_palette	—	Set the display color palette for indexed displays
- [x] draw
    - [x] pygame.draw.rect	—	draw a rectangle shape
    - [x] pygame.draw.polygon	—	draw a shape with any number of sides
    - [x] pygame.draw.circle	—	draw a circle around a point
    - [x] pygame.draw.ellipse	—	draw a round shape inside a rectangle
    - [x] pygame.draw.arc	—	draw a partial section of an ellipse
    - [x] pygame.draw.line	—	draw a straight line segment
    - [x] pygame.draw.lines	—	draw multiple contiguous line segments
    - [x] pygame.draw.aaline	—	draw fine antialiased lines
    - [x] pygame.draw.aalines	—	draw a connected sequence of antialiased lines
- [x] event
    - [ ] pygame.event.pump	—	internally process pygame event handlers
    - [x] pygame.event.get	—	get events from the queue
    - [ ] pygame.event.poll	—	get a single event from the queue
    - [x] pygame.event.wait	—	wait for a single event from the queue
    - [ ] pygame.event.peek	—	test if event types are waiting on the queue
    - [ ] pygame.event.clear	—	remove all events from the queue
    - [ ] pygame.event.event_name	—	get the string name from and event id
    - [ ] pygame.event.set_blocked	—	control which events are allowed on the queue
    - [ ] pygame.event.set_allowed	—	control which events are allowed on the queue
    - [ ] pygame.event.get_blocked	—	test if a type of event is blocked from the queue
    - [ ] pygame.event.set_grab	—	control the sharing of input devices with other applications
    - [ ] pygame.event.get_grab	—	test if the program is sharing input devices
    - [ ] pygame.event.post	—	place a new event on the queue
    - [x] pygame.event.Event	—	create a new event object
    - [x] pygame.event.EventType	—	pygame object for representing SDL events
- [x] font
    - [x] pygame.font.init	—	initialize the font module
    - [x] pygame.font.quit	—	uninitialize the font module
    - [x] pygame.font.get_init	—	true if the font module is initialized
    - [x] pygame.font.get_default_font	—	get the filename of the default font
    - [x] pygame.font.get_fonts	—	get all available fonts
    - [x] pygame.font.match_font	—	find a specific font on the system
    - [x] pygame.font.SysFont	—	create a Font object from the system fonts
    - [x] pygame.font.Font	—	create a new Font object from a file
- [x] image
    - [x] pygame.image.load	—	load new image from a file
    - [x] pygame.image.save	—	save an image to disk
    - [x] pygame.image.get_extended	—	test if extended image formats can be loaded
    - [ ] pygame.image.tostring	—	transfer image to string buffer
    - [ ] pygame.image.fromstring	—	create new Surface from a string buffer
    - [ ] pygame.image.frombuffer	—	create a new Surface that shares data inside a string buffer
- [x] key
    - [x] pygame.key.get_focused	—	true if the display is receiving keyboard input from the system
    - [x] pygame.key.get_pressed	—	get the state of all keyboard buttons
    - [x] pygame.key.get_mods	—	determine which modifier keys are being held
    - [x] pygame.key.set_mods	—	temporarily set which modifier keys are pressed
    - [x] pygame.key.set_repeat	—	control how held keys are repeated
    - [x] pygame.key.get_repeat	—	see how held keys are repeated
    - [x] pygame.key.name	—	get the name of a key identifier
- [ ] locals
- [ ] mixer
- [x] mouse
    - [x] pygame.mouse.get_pressed	—	get the state of the mouse buttons
    - [x] pygame.mouse.get_pos	—	get the mouse cursor position
    - [x] pygame.mouse.get_rel	—	get the amount of mouse movement
    - [x] pygame.mouse.set_pos	—	set the mouse cursor position
    - [x] pygame.mouse.set_visible	—	hide or show the mouse cursor
    - [x] pygame.mouse.get_focused	—	check if the display is receiving mouse input
    - [x] pygame.mouse.set_cursor	—	set the image for the system mouse cursor
    - [x] pygame.mouse.get_cursor	—	get the image for the system mouse cursor
- [x] Rect
    - [x] pygame.Rect.copy	—	copy the rectangle
    - [x] pygame.Rect.move	—	moves the rectangle
    - [x] pygame.Rect.move_ip	—	moves the rectangle, in place
    - [x] pygame.Rect.inflate	—	grow or shrink the rectangle size
    - [x] pygame.Rect.inflate_ip	—	grow or shrink the rectangle size, in place
    - [x] pygame.Rect.clamp	—	moves the rectangle inside another
    - [x] pygame.Rect.clamp_ip	—	moves the rectangle inside another, in place
    - [x] pygame.Rect.clip	—	crops a rectangle inside another
    - [x] pygame.Rect.union	—	joins two rectangles into one
    - [x] pygame.Rect.union_ip	—	joins two rectangles into one, in place
    - [x] pygame.Rect.unionall	—	the union of many rectangles
    - [x] pygame.Rect.unionall_ip	—	the union of many rectangles, in place
    - [x] pygame.Rect.fit	—	resize and move a rectangle with aspect ratio
    - [x] pygame.Rect.normalize	—	correct negative sizes
    - [x] pygame.Rect.contains	—	test if one rectangle is inside another
    - [x] pygame.Rect.collidepoint	—	test if a point is inside a rectangle
    - [x] pygame.Rect.colliderect	—	test if two rectangles overlap
    - [x] pygame.Rect.collidelist	—	test if one rectangle in a list intersects
    - [x] pygame.Rect.collidelistall	—	test if all rectangles in a list intersect
    - [ ] pygame.Rect.collidedict	—	test if one rectangle in a dictionary intersects
    - [ ] pygame.Rect.collidedictall	—	test if all rectangles in a dictionary intersect
- [x] Surface
    - [x] pygame.Surface.blit	—	draw one image onto another
    - [ ] pygame.Surface.blits	—	draw many images onto another
    - [x] pygame.Surface.convert	—	change the pixel format of an image
    - [x] pygame.Surface.convert_alpha	—	change the pixel format of an image including per pixel alphas
    - [x] pygame.Surface.copy	—	create a new copy of a Surface
    - [ ] pygame.Surface.fill	—	fill Surface with a solid color
    - [x] pygame.Surface.scroll	—	Shift the surface image in place
    - [ ] pygame.Surface.set_colorkey	—	Set the transparent colorkey
    - [ ] pygame.Surface.get_colorkey	—	Get the current transparent colorkey
    - [ ] pygame.Surface.set_alpha	—	set the alpha value for the full Surface image
    - [ ] pygame.Surface.get_alpha	—	get the current Surface transparency value
    - [ ] pygame.Surface.lock	—	lock the Surface memory for pixel access
    - [ ] pygame.Surface.unlock	—	unlock the Surface memory from pixel access
    - [ ] pygame.Surface.mustlock	—	test if the Surface requires locking
    - [ ] pygame.Surface.get_locked	—	test if the Surface is current locked
    - [ ] pygame.Surface.get_locks	—	Gets the locks for the Surface
    - [x] pygame.Surface.get_at	—	get the color value at a single pixel
    - [x] pygame.Surface.set_at	—	set the color value for a single pixel
    - [ ] pygame.Surface.get_at_mapped	—	get the mapped color value at a single pixel
    - [ ] pygame.Surface.get_palette	—	get the color index palette for an 8-bit Surface
    - [ ] pygame.Surface.get_palette_at	—	get the color for a single entry in a palette
    - [ ] pygame.Surface.set_palette	—	set the color palette for an 8-bit Surface
    - [ ] pygame.Surface.set_palette_at	—	set the color for a single index in an 8-bit Surface palette
    - [ ] pygame.Surface.map_rgb	—	convert a color into a mapped color value
    - [ ] pygame.Surface.unmap_rgb	—	convert a mapped integer color value into a Color
    - [ ] pygame.Surface.set_clip	—	set the current clipping area of the Surface
    - [ ] pygame.Surface.get_clip	—	get the current clipping area of the Surface
    - [ ] pygame.Surface.subsurface	—	create a new surface that references its parent
    - [ ] pygame.Surface.get_parent	—	find the parent of a subsurface
    - [ ] pygame.Surface.get_abs_parent	—	find the top level parent of a subsurface
    - [ ] pygame.Surface.get_offset	—	find the position of a child subsurface inside a parent
    - [ ] pygame.Surface.get_abs_offset	—	find the absolute position of a child subsurface inside its top level parent
    - [x] pygame.Surface.get_size	—	get the dimensions of the Surface
    - [x] pygame.Surface.get_width	—	get the width of the Surface
    - [x] pygame.Surface.get_height	—	get the height of the Surface
    - [x] pygame.Surface.get_rect	—	get the rectangular area of the Surface
    - [ ] pygame.Surface.get_bitsize	—	get the bit depth of the Surface pixel format
    - [ ] pygame.Surface.get_bytesize	—	get the bytes used per Surface pixel
    - [x] pygame.Surface.get_flags	—	get the additional flags used for the Surface
    - [ ] pygame.Surface.get_pitch	—	get the number of bytes used per Surface row
    - [ ] pygame.Surface.get_masks	—	the bitmasks needed to convert between a color and a mapped integer
    - [ ] pygame.Surface.set_masks	—	set the bitmasks needed to convert between a color and a mapped integer
    - [ ] pygame.Surface.get_shifts	—	the bit shifts needed to convert between a color and a mapped integer
    - [ ] pygame.Surface.set_shifts	—	sets the bit shifts needed to convert between a color and a mapped integer
    - [ ] pygame.Surface.get_losses	—	the significant bits used to convert between a color and a mapped integer
    - [x] pygame.Surface.get_bounding_rect	—	find the smallest rect containing data
    - [ ] pygame.Surface.get_view	—	return a buffer view of the Surface's pixels.
    - [ ] pygame.Surface.get_buffer	—	acquires a buffer object for the pixels of the Surface.
    - [ ] pygame.Surface._pixels_address	—	pixel buffer address
- [x] time
    - [x] pygame.time.get_ticks	—	get the time in milliseconds
    - [x] pygame.time.wait	—	pause the program for an amount of time
    - [x] pygame.time.delay	—	pause the program for an amount of time
    - [x] pygame.time.set_timer	—	repeatedly create an event on the event queue
    - [x] pygame.time.Clock	—	create an object to help track time
- [ ] music
- [x] pygame
    - [x] pygame.init	—	initialize all imported pygame modules
    - [x] pygame.quit	—	uninitialize all pygame modules
    - [x] pygame.error	—	standard pygame exception
    - [ ] pygame.get_error	—	get the current error message
    - [ ] pygame.set_error	—	set the current error message
    - [x] pygame.get_sdl_version	—	get the version number of SDL
    - [x] pygame.get_sdl_byteorder	—	get the byte order of SDL
    - [ ] pygame.register_quit	—	register a function to be called when pygame quits
    - [ ] pygame.encode_string	—	Encode a Unicode or bytes object
    - [ ] pygame.encode_file_path	—	Encode a Unicode or bytes object as a file system path

###### Advanced stuff:
- [ ] cursors
- [ ] joystick
- [ ] mask
- [ ] sprite
- [x] transform
    - [x] pygame.transform.flip	—	flip vertically and horizontally
    - [x] pygame.transform.scale	—	resize to new resolution
    - [x] pygame.transform.rotate	—	rotate an image
    - [x] pygame.transform.rotozoom	—	filtered scale and rotation
    - [x] pygame.transform.scale2x	—	specialized image doubler
    - [x] pygame.transform.smoothscale	—	scale a surface to an arbitrary size smoothly
    - [ ] pygame.transform.get_smoothscale_backend	—	return smoothscale filter version in use: 'GENERIC', 'MMX', or 'SSE'
    - [ ] pygame.transform.set_smoothscale_backend	—	set smoothscale filter version to one of: 'GENERIC', 'MMX', or 'SSE'
    - [x] pygame.transform.chop	—	gets a copy of an image with an interior area removed
    - [ ] pygame.transform.laplacian	—	find edges in a surface
    - [ ] pygame.transform.average_surfaces	—	find the average surface from many surfaces.
    - [ ] pygame.transform.average_color	—	finds the average color of a surface
    - [ ] pygame.transform.threshold	—	finds which, and how many pixels in a surface are within a threshold of a 'search_color' or a 'search_surf'.
- [ ] BufferProxy
- [ ] freetype
- [ ] gfxdraw
- [ ] midi
- [ ] Overlay
- [ ] PixelArray
- [ ] pixelcopy
- [ ] sndarray
- [ ] surfarray
- [ ] math

###### Other:
- [ ] camera
- [ ] cdrom
- [ ] examples
- [ ] scrap
- [ ] tests
- [x] version
    - [x] pygame.version.ver	—	version number as a string
    - [x] pygame.version.vernum	—	tupled integers of the version
    - [x] pygame.version.rev	—	repository revision of the build
