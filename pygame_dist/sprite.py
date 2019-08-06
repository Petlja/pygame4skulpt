                                  
                                                  
                                      
                                                                   
                                                                 
                                                                  
                                                                      
  
                                                                     
                                                                    
                                                                       
                                                      
  
                                                                       
                                                                
                                                                               
  
                   
                       

"""pygame module with basic game object classes

This module contains several simple classes to be used within games. There
are the main Sprite class and several Group classes that contain Sprites.
The use of these classes is entirely optional when using Pygame. The classes
are fairly lightweight and only provide a starting place for the code
that is common to most games.

The Sprite class is intended to be used as a base class for the different
types of objects in the game. There is also a base Group class that simply
stores sprites. A game could create new types of Group classes that operate
on specially customized Sprite instances they contain.

The basic Sprite class can draw the Sprites it contains to a Surface. The
Group.draw() method requires that each Sprite have a Surface.image attribute
and a Surface.rect. The Group.clear() method requires these same attributes
and can be used to erase all the Sprites with background. There are also
more advanced Groups: pygame.sprite.RenderUpdates() and
pygame.sprite.OrderedUpdates().

Lastly, this module contains several collision functions. These help find
sprites inside multiple groups that have intersecting bounding rectangles.
To find the collisions, the Sprites are required to have a Surface.rect
attribute assigned.

The groups are designed for high efficiency in removing and adding Sprites
to them. They also allow cheap testing to see if a Sprite already exists in
a Group. A given Sprite can exist in any number of groups. A game could use
some groups to control object rendering, and a completely separate set of
groups to control interaction or player movement. Instead of adding type
attributes or bools to a derived Sprite class, consider keeping the
Sprites inside organized Groups. This will allow for easier lookup later
in the game.

Sprites and Groups manage their relationships with the add() and remove()
methods. These methods can accept a single or multiple group arguments for
membership.  The default initializers for these classes also take a
single group or list of groups as argments for initial membership. It is safe
to repeatedly add and remove the same Sprite from a Group.

While it is possible to design sprite and group classes that don't derive
from the Sprite and AbstractGroup classes below, it is strongly recommended
that you extend those when you create a new Sprite or Group class.

Sprites are not thread safe, so lock them yourself if using threads.

"""

      
                                                        
                                                       
                  
  
                                                         
                                                              
                                                            
                                                            
                                         
  
                                                              
                                                               
                                                                 
  
                                                             
                                                                  
                                                                 
                     

import pygame
from pygame import Rect
from pygame.time import get_ticks
from operator import truth

                                                  
try:
    from pygame.mask import from_surface
except:
    pass


def get_id(data):
    return data.return_id()


class Sprite(object):
           

    def __init__(self, *groups):
        self.__g = {}                                 
        if groups:
            self.add(*groups)

    def add(self, *groups):
                   
        has = self.__g.__contains__
        for group in groups:
            if hasattr(group, '_spritegroup'):
                if not has(group):
                    group.add_internal(self)
                    self.add_internal(group)
            else:
                self.add(*group)

    def remove(self, *groups):
                   
        has = self.__g.__contains__
        for group in groups:
            if hasattr(group, '_spritegroup'):
                if has(group):
                    group.remove_internal(self)
                    self.remove_internal(group)
            else:
                self.remove(*group)

    def add_internal(self, group):
        self.__g[group] = 0

    def remove_internal(self, group):
        del self.__g[group]

    def update(self, *args):
                   
        pass

    def kill(self):
                   
        for c in self.__g:
            c.remove_internal(self)
        self.__g.clear()

    def groups(self):
                   
        return list(self.__g)

    def alive(self):
                   
        return truth(self.__g)

    def __repr__(self):
        return "<%s sprite(in %d groups)>" % (self.__class__.__name__, len(self.__g))


class DirtySprite(Sprite):
           

    def __init__(self, *groups):
        self.dirty = 1
        self.blendmode = 0                                                 
                                                   
        self._visible = 1
        self._layer = 0                                                 
        self.source_rect = None
        Sprite.__init__(self, *groups)

    def _set_visible(self, val):
                                                                       
        self._visible = val
        if self.dirty < 2:
            self.dirty = 1

    def _get_visible(self):
                                                     
        return self._visible

    visible = property(lambda self: self._get_visible(),
                       lambda self, value: self._set_visible(value),
                       doc="you can make this sprite disappear without "
                           "removing it from the group,\n"
                           "assign 0 for invisible and 1 for visible")

    def __repr__(self):
        return "<%s DirtySprite(in %d groups)>" %               (self.__class__.__name__, len(self.groups()))


class AbstractGroup(object):
           

                                                                           
    _spritegroup = True

    def __init__(self):
        self.spritedict = {}
        self.lostsprites = []

    def sprites(self):
                   
        return list(self.spritedict)

    def add_internal(self, sprite):
        self.spritedict[sprite] = 0

    def remove_internal(self, sprite):
        r = self.spritedict[sprite]
        if r:
            self.lostsprites.append(r)
        del self.spritedict[sprite]

    def has_internal(self, sprite):
        return sprite in self.spritedict

    def copy(self):
                   
        return self.__class__(self.sprites())

    def __iter__(self):
        return iter(self.sprites())

    def __contains__(self, sprite):
        return self.has(sprite)

    def add(self, *sprites):
                   
        for sprite in sprites:
                                                                             
                                                                               
                                                      
            if isinstance(sprite, Sprite):
                if not self.has_internal(sprite):
                    self.add_internal(sprite)
                    sprite.add_internal(self)
            else:
                try:
                                                                                             
                                                
                    self.add(*sprite)
                except (TypeError, AttributeError):
                                                                                                
                                                                                                 
                                                                                                   
                                                                 
                    if hasattr(sprite, '_spritegroup'):
                        for spr in sprite.sprites():
                            if not self.has_internal(spr):
                                self.add_internal(spr)
                                spr.add_internal(self)
                    elif not self.has_internal(sprite):
                        self.add_internal(sprite)
                        sprite.add_internal(self)

    def remove(self, *sprites):
                   
                                                                                   
                                                                                      
                                                                                  
                                                                                    
                                                                                    
                                                       
        for sprite in sprites:
            if isinstance(sprite, Sprite):
                if self.has_internal(sprite):
                    self.remove_internal(sprite)
                    sprite.remove_internal(self)
            else:
                try:
                    self.remove(*sprite)
                except (TypeError, AttributeError):
                    if hasattr(sprite, '_spritegroup'):
                        for spr in sprite.sprites():
                            if self.has_internal(spr):
                                self.remove_internal(spr)
                                spr.remove_internal(self)
                    elif self.has_internal(sprite):
                        self.remove_internal(sprite)
                        sprite.remove_internal(self)

    def has(self, *sprites):
                   
        return_value = False

        for sprite in sprites:
            if isinstance(sprite, Sprite):
                                                                                      
                if self.has_internal(sprite):
                    return_value = True
                else:
                    return False
            else:
                try:
                    if self.has(*sprite):
                        return_value = True
                    else:
                        return False
                except (TypeError, AttributeError):
                    if hasattr(sprite, '_spritegroup'):
                        for spr in sprite.sprites():
                            if self.has_internal(spr):
                                return_value = True
                            else:
                                return False
                    else:
                        if self.has_internal(sprite):
                            return_value = True
                        else:
                            return False

        return return_value

    def update(self, *args):
                   
        for s in self.sprites():
            s.update(*args)

    def draw(self, surface):
                   
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []

    def clear(self, surface, bgd):
                   
        if callable(bgd):
            for r in self.lostsprites:
                bgd(surface, r)
            for r in self.spritedict.values():
                if r:
                    bgd(surface, r)
        else:
            surface_blit = surface.blit
            for r in self.lostsprites:
                surface_blit(bgd, r, r)
            for r in self.spritedict.values():
                if r:
                    surface_blit(bgd, r, r)

    def empty(self):
                   
        for s in self.sprites():
            self.remove_internal(s)
            s.remove_internal(self)

    def __nonzero__(self):
        return truth(self.sprites())

    def __len__(self):
                   
        return len(self.sprites())

    def __repr__(self):
        return "<%s(%d sprites)>" % (self.__class__.__name__, len(self))


class Group(AbstractGroup):
           

    def __init__(self, *sprites):
        AbstractGroup.__init__(self)
        self.add(*sprites)


RenderPlain = Group
RenderClear = Group


class RenderUpdates(Group):
           

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        for s in self.sprites():
            r = spritedict[s]
            newrect = surface_blit(s.image, s.rect)
            if r:
                if newrect.colliderect(r):
                    dirty_append(newrect.union(r))
                else:
                    dirty_append(newrect)
                    dirty_append(r)
            else:
                dirty_append(newrect)
            spritedict[s] = newrect
        return dirty


class OrderedUpdates(RenderUpdates):
           

    def __init__(self, *sprites):
        self._spritelist = []
        RenderUpdates.__init__(self, *sprites)

    def sprites(self):
        return list(self._spritelist)

    def add_internal(self, sprite):
        RenderUpdates.add_internal(self, sprite)
        self._spritelist.append(sprite)

    def remove_internal(self, sprite):
        RenderUpdates.remove_internal(self, sprite)
        self._spritelist.remove(sprite)


class LayeredUpdates(AbstractGroup):
           

    _init_rect = Rect(0, 0, 0, 0)

    def __init__(self, *sprites, **kwargs):
                   
        self._spritelayers = {}
        self._spritelist = []
        AbstractGroup.__init__(self)
        self._default_layer = kwargs.get('default_layer', 0)

        self.add(*sprites, **kwargs)

    def add_internal(self, sprite, layer=None):
                   
        self.spritedict[sprite] = self._init_rect

        if layer is None:
            try:
                layer = sprite._layer
            except AttributeError:
                layer = sprite._layer = self._default_layer
        elif hasattr(sprite, '_layer'):
            sprite._layer = layer

        sprites = self._spritelist             
        sprites_layers = self._spritelayers
        sprites_layers[sprite] = layer

                                                      
                                    
        leng = len(sprites)
        low = mid = 0
        high = leng - 1
        while low <= high:
            mid = low + (high - low) // 2
            if sprites_layers[sprites[mid]] <= layer:
                low = mid + 1
            else:
                high = mid - 1
                                                      
        while mid < leng and sprites_layers[sprites[mid]] <= layer:
            mid += 1
        sprites.insert(mid, sprite)

    def add(self, *sprites, **kwargs):
                   

        if not sprites:
            return
        if 'layer' in kwargs:
            layer = kwargs['layer']
        else:
            layer = None
        for sprite in sprites:
                                                                             
                                                                               
                                                      
            if isinstance(sprite, Sprite):
                if not self.has_internal(sprite):
                    self.add_internal(sprite, layer)
                    sprite.add_internal(self)
            else:
                try:
                                                                                             
                                                
                    self.add(*sprite, **kwargs)
                except (TypeError, AttributeError):
                                                                                                
                                                                                                 
                                                                                                   
                                                                 
                    if hasattr(sprite, '_spritegroup'):
                        for spr in sprite.sprites():
                            if not self.has_internal(spr):
                                self.add_internal(spr, layer)
                                spr.add_internal(self)
                    elif not self.has_internal(sprite):
                        self.add_internal(sprite, layer)
                        sprite.add_internal(self)

    def remove_internal(self, sprite):
                   
        self._spritelist.remove(sprite)
                                                                
        r = self.spritedict[sprite]
        if r is not self._init_rect:
            self.lostsprites.append(r)                
        if hasattr(sprite, 'rect'):
            self.lostsprites.append(sprite.rect)                

        del self.spritedict[sprite]
        del self._spritelayers[sprite]

    def sprites(self):
                   
        return list(self._spritelist)

    def draw(self, surface):
                   
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect)
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty

    def get_sprites_at(self, pos):
                   
        _sprites = self._spritelist
        rect = Rect(pos, (0, 0))
        colliding_idx = rect.collidelistall(_sprites)
        colliding = [_sprites[i] for i in colliding_idx]
        return colliding

    def get_sprite(self, idx):
                   
        return self._spritelist[idx]

    def remove_sprites_of_layer(self, layer_nr):
                   
        sprites = self.get_sprites_from_layer(layer_nr)
        self.remove(*sprites)
        return sprites

                            
    def layers(self):
                   
        return sorted(set(self._spritelayers.values()))

    def change_layer(self, sprite, new_layer):
                   
        sprites = self._spritelist             
        sprites_layers = self._spritelayers             

        sprites.remove(sprite)
        sprites_layers.pop(sprite)

                                                      
                                    
        leng = len(sprites)
        low = mid = 0
        high = leng - 1
        while low <= high:
            mid = low + (high - low) // 2
            if sprites_layers[sprites[mid]] <= new_layer:
                low = mid + 1
            else:
                high = mid - 1
                                                      
        while mid < leng and sprites_layers[sprites[mid]] <= new_layer:
            mid += 1
        sprites.insert(mid, sprite)
        if hasattr(sprite, 'layer'):
            sprite.layer = new_layer

                                
        sprites_layers[sprite] = new_layer

    def get_layer_of_sprite(self, sprite):
                   
        return self._spritelayers.get(sprite, self._default_layer)

    def get_top_layer(self):
                   
        return self._spritelayers[self._spritelist[-1]]

    def get_bottom_layer(self):
                   
        return self._spritelayers[self._spritelist[0]]

    def move_to_front(self, sprite):
                   
        self.change_layer(sprite, self.get_top_layer())

    def move_to_back(self, sprite):
                   
        self.change_layer(sprite, self.get_bottom_layer() - 1)

    def get_top_sprite(self):
                   
        return self._spritelist[-1]

    def get_sprites_from_layer(self, layer):
                   
        sprites = []
        sprites_append = sprites.append
        sprite_layers = self._spritelayers
        for spr in self._spritelist:
            if sprite_layers[spr] == layer:
                sprites_append(spr)
            elif sprite_layers[spr] > layer:                                       
                                                        
                break
        return sprites

    def switch_layer(self, layer1_nr, layer2_nr):
                   
        sprites1 = self.remove_sprites_of_layer(layer1_nr)
        for spr in self.get_sprites_from_layer(layer2_nr):
            self.change_layer(spr, layer1_nr)
        self.add(layer=layer2_nr, *sprites1)


class LayeredDirty(LayeredUpdates):
           

    def __init__(self, *sprites, **kwargs):
                   
        LayeredUpdates.__init__(self, *sprites, **kwargs)
        self._clip = None

        self._use_update = False

        self._time_threshold = 1000.0 / 80.0                  

        self._bgd = None
        for key, val in kwargs.items():
            if key in ['_use_update', '_time_threshold', '_default_layer']:
                if hasattr(self, key):
                    setattr(self, key, val)

    def add_internal(self, sprite, layer=None):
                   
                                                        
        if not hasattr(sprite, 'dirty'):
            raise AttributeError()
        if not hasattr(sprite, 'visible'):
            raise AttributeError()
        if not hasattr(sprite, 'blendmode'):
            raise AttributeError()

        if not isinstance(sprite, DirtySprite):
            raise TypeError()

        if sprite.dirty == 0:                               
            sprite.dirty = 1

        LayeredUpdates.add_internal(self, sprite, layer)

    def draw(self, surface, bgd=None):
                   
                          
        _orig_clip = surface.get_clip()
        _clip = self._clip
        if _clip is None:
            _clip = _orig_clip

        _surf = surface
        _sprites = self._spritelist
        _old_rect = self.spritedict
        _update = self.lostsprites
        _update_append = _update.append
        _ret = None
        _surf_blit = _surf.blit
        _rect = Rect
        if bgd is not None:
            self._bgd = bgd
        _bgd = self._bgd
        init_rect = self._init_rect

        _surf.set_clip(_clip)
                         
                                                                 
        start_time = get_ticks()
        if self._use_update:                      
                                                                                     
                                                        
            for spr in _sprites:
                if 0 < spr.dirty:
                                                              
                    if spr.source_rect:
                        _union_rect = _rect(spr.rect.topleft,
                                            spr.source_rect.size)
                    else:
                        _union_rect = _rect(spr.rect)

                    _union_rect_collidelist = _union_rect.collidelist
                    _union_rect_union_ip = _union_rect.union_ip
                    i = _union_rect_collidelist(_update)
                    while -1 < i:
                        _union_rect_union_ip(_update[i])
                        del _update[i]
                        i = _union_rect_collidelist(_update)
                    _update_append(_union_rect.clip(_clip))

                    if _old_rect[spr] is not init_rect:
                        _union_rect = _rect(_old_rect[spr])
                        _union_rect_collidelist = _union_rect.collidelist
                        _union_rect_union_ip = _union_rect.union_ip
                        i = _union_rect_collidelist(_update)
                        while -1 < i:
                            _union_rect_union_ip(_update[i])
                            del _update[i]
                            i = _union_rect_collidelist(_update)
                        _update_append(_union_rect.clip(_clip))
                                                                                        
                                    

                                                
            if _bgd is not None:
                for rec in _update:
                    _surf_blit(_bgd, rec, rec)

                                 
            for spr in _sprites:
                if 1 > spr.dirty:
                    if spr._visible:
                                                                                                   
                        _spr_rect = spr.rect
                        if spr.source_rect is not None:
                            _spr_rect = Rect(spr.rect.topleft,
                                             spr.source_rect.size)
                        _spr_rect_clip = _spr_rect.clip
                        for idx in _spr_rect.collidelistall(_update):
                                                              
                            clip = _spr_rect_clip(_update[idx])
                            _surf_blit(spr.image,
                                       clip,
                                       (clip[0] - _spr_rect[0],
                                        clip[1] - _spr_rect[1],
                                        clip[2],
                                        clip[3]),
                                       spr.blendmode)
                else:                  
                    if spr._visible:
                        _old_rect[spr] = _surf_blit(spr.image,
                                                    spr.rect,
                                                    spr.source_rect,
                                                    spr.blendmode)
                    if spr.dirty == 1:
                        spr.dirty = 0
            _ret = list(_update)
        else:                            
            if _bgd is not None:
                _surf_blit(_bgd, (0, 0))
            for spr in _sprites:
                if spr._visible:
                    _old_rect[spr] = _surf_blit(spr.image,
                                                spr.rect,
                                                spr.source_rect,
                                                spr.blendmode)
            _ret = [_rect(_clip)]                                                

                                            
                                                                                
        end_time = get_ticks()
        if end_time - start_time > self._time_threshold:
            self._use_update = False
        else:
            self._use_update = True

                                 
                                                                                            

                                        
        _update[:] = []

                         
                                       
        _surf.set_clip(_orig_clip)
        return _ret

    def clear(self, surface, bgd):
                   
        self._bgd = bgd

    def repaint_rect(self, screen_rect):
                   
        if self._clip:
            self.lostsprites.append(screen_rect.clip(self._clip))
        else:
            self.lostsprites.append(Rect(screen_rect))

    def set_clip(self, screen_rect=None):
                   
        if screen_rect is None:
            self._clip = pygame.display.get_surface().get_rect()
        else:
            self._clip = screen_rect
        self._use_update = False

    def get_clip(self):
                   
        return self._clip

    def change_layer(self, sprite, new_layer):
                   
        LayeredUpdates.change_layer(self, sprite, new_layer)
        if sprite.dirty == 0:
            sprite.dirty = 1

    def set_timing_treshold(self, time_ms):
                   
        self._time_threshold = time_ms


class GroupSingle(AbstractGroup):
           

    def __init__(self, sprite=None):
        AbstractGroup.__init__(self)
        self.__sprite = None
        if sprite is not None:
            self.add(sprite)

    def copy(self):
        return GroupSingle(self.__sprite)

    def sprites(self):
        if self.__sprite is not None:
            return [self.__sprite]
        else:
            return []

    def add_internal(self, sprite):
        if self.__sprite is not None:
            self.__sprite.remove_internal(self)
            self.remove_internal(self.__sprite)
        self.__sprite = sprite

    def __nonzero__(self):
        return self.__sprite is not None

    def _get_sprite(self):
        return self.__sprite

    def _set_sprite(self, sprite):
        self.add_internal(sprite)
        sprite.add_internal(self)
        return sprite

    sprite = property(_get_sprite,
                      _set_sprite,
                      None,
                      "The sprite contained in this group")

    def remove_internal(self, sprite):
        if sprite is self.__sprite:
            self.__sprite = None
        if sprite in self.spritedict:
            AbstractGroup.remove_internal(self, sprite)

    def has_internal(self, sprite):
        return self.__sprite is sprite

                          
    def __contains__(self, sprite):
        return self.__sprite is sprite


                                                                  
def collide_rect(left, right):
           
    return left.rect.colliderect(right.rect)


class collide_rect_ratio:
           

    def __init__(self, ratio):
                   
        self.ratio = ratio

    def __call__(self, left, right):
                   

        ratio = self.ratio

        leftrect = left.rect
        width = leftrect.width
        height = leftrect.height
        leftrect = leftrect.inflate(width * ratio - width,
                                    height * ratio - height)

        rightrect = right.rect
        width = rightrect.width
        height = rightrect.height
        rightrect = rightrect.inflate(width * ratio - width,
                                      height * ratio - height)

        return leftrect.colliderect(rightrect)


def collide_circle(left, right):
           

    xdistance = left.rect.centerx - right.rect.centerx
    ydistance = left.rect.centery - right.rect.centery
    distancesquared = xdistance ** 2 + ydistance ** 2

    if hasattr(left, 'radius'):
        leftradius = left.radius
    else:
        leftrect = left.rect
                                                                                     
                                                                                  
        leftradius = 0.5 * ((leftrect.width ** 2 + leftrect.height ** 2) ** 0.5)
                                                              
        setattr(left, 'radius', leftradius)

    if hasattr(right, 'radius'):
        rightradius = right.radius
    else:
        rightrect = right.rect
                                                                                    
                                                                                  
        rightradius = 0.5 * ((rightrect.width ** 2 + rightrect.height ** 2) ** 0.5)
                                                              
        setattr(right, 'radius', rightradius)
    return distancesquared <= (leftradius + rightradius) ** 2


class collide_circle_ratio(object):
           

    def __init__(self, ratio):
                   
        self.ratio = ratio

    def __call__(self, left, right):
                   

        ratio = self.ratio
        xdistance = left.rect.centerx - right.rect.centerx
        ydistance = left.rect.centery - right.rect.centery
        distancesquared = xdistance ** 2 + ydistance ** 2

        if hasattr(left, "radius"):
            leftradius = left.radius * ratio
        else:
            leftrect = left.rect
            leftradius = ratio * 0.5 * ((leftrect.width ** 2 + leftrect.height ** 2) ** 0.5)
                                                                      
            setattr(left, 'radius', leftradius)

        if hasattr(right, "radius"):
            rightradius = right.radius * ratio
        else:
            rightrect = right.rect
            rightradius = ratio * 0.5 * ((rightrect.width ** 2 + rightrect.height ** 2) ** 0.5)
                                                                      
            setattr(right, 'radius', rightradius)

        return distancesquared <= (leftradius + rightradius) ** 2


def collide_mask(left, right):
           
    xoffset = right.rect[0] - left.rect[0]
    yoffset = right.rect[1] - left.rect[1]
    try:
        leftmask = left.mask
    except AttributeError:
        leftmask = from_surface(left.image)
    try:
        rightmask = right.mask
    except AttributeError:
        rightmask = from_surface(right.image)
    return leftmask.overlap(rightmask, (xoffset, yoffset))


def spritecollide(sprite, group, dokill, collided=None):
           
    if dokill:

        crashed = []
        append = crashed.append

        if collided:
            for s in group.sprites():
                if collided(sprite, s):
                    s.kill()
                    append(s)
        else:
            spritecollide = sprite.rect.colliderect
            for s in group.sprites():
                if spritecollide(s.rect):
                    s.kill()
                    append(s)

        return crashed

    elif collided:
        return [s for s in group if collided(sprite, s)]
    else:
        spritecollide = sprite.rect.colliderect
        return [s for s in group if spritecollide(s.rect)]


def groupcollide(groupa, groupb, dokilla, dokillb, collided=None):
           
    crashed = {}
    SC = spritecollide
    if dokilla:
        for s in groupa.sprites():
            c = SC(s, groupb, dokillb, collided)
            if c:
                crashed[s] = c
                s.kill()
    else:
        for s in groupa:
            c = SC(s, groupb, dokillb, collided)
            if c:
                crashed[s] = c
    return crashed


def spritecollideany(sprite, group, collided=None):
           
    if collided:
        for s in group:
            if collided(sprite, s):
                return s
    else:
                                                       
        spritecollide = sprite.rect.colliderect
        for s in group:
            if spritecollide(s.rect):
                return s
    return None
