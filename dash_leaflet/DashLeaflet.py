# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashLeaflet(Component):
    """A DashLeaflet component.
DashLeaflet is allows to display a map in dash. Several point and line layers can be added to the map.

Keyword arguments:
- id (string; optional): The id of the main element
- style (dict; default { height: '600px' }): The style of the main element. style has the following type: dict containing keys 'height'.
Those keys have the following types:
  - height (string; optional)
- mapOptions (dict; default {
    center: [0, 0],
    zoom: 4,
    minZoom: 0,
    maxZoom: 20
}): The style of the main element. mapOptions has the following type: dict containing keys 'bounds', 'center', 'minBounds', 'maxBounds', 'minZoom', 'maxZoom', 'zoom'.
Those keys have the following types:
  - bounds (list of list of numberss; optional)
  - center (list of numbers; optional)
  - minBounds (list of list of numberss; optional)
  - maxBounds (list of list of numberss; optional)
  - minZoom (number; optional)
  - maxZoom (number; optional)
  - zoom (number; optional)
- baselayer (dict; default {
    url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}): The baselayer(s) of the map. Can either be a single one or an array of multiple baselayers including their name.
     If no baselayer is provided, the OSM will serve as default. baselayer has the following type: dict containing keys 'url', 'attribution'.
Those keys have the following types:
  - url (string; optional)
  - attribution (string; optional) | list of dicts containing keys 'name', 'url', 'attribution'.
Those keys have the following types:
  - name (string; optional)
  - url (string; optional)
  - attribution (string; optional)
- lines (dict; optional): Array containing one or many shapes of:
     - title: Title of line layer that is to be rendered on the map.
     - geom: Array of arrays containing lines that are to be rendered on the map. These can either be lines or polylines.
     - popup: String containing popup-text for this layer group or list of strings containing popup-texts,
     - options: Shape containing element options:
     - color: Stroke color
     - weight: Stroke width in pixels
     - opacity: Stroke opacity. lines has the following type: list of dicts containing keys 'title', 'geom', 'popup', 'options'.
Those keys have the following types:
  - title (string; optional)
  - geom (list of list of list of numberss | list of list of list of numberssss; required)
  - popup (list of strings | string; optional)
  - options (dict; optional): options has the following type: dict containing keys 'color', 'weight', 'opacity'.
Those keys have the following types:
  - color (string; optional)
  - weight (number; optional)
  - opacity (number; optional)
- markers (dict; optional): Array containing one or many shapes of:
     - title: Title of marker layer that is to be rendered on the map.
     - geom: Array of arrays containing coordinates ([lat, lng]) of markers that are to be rendered on the map.
     - popup: String containing popup-text for this layer group or list of strings containing popup-texts
     - icon: Shape for the icon that is to be rendered for the markers. Attention, the iconUrl must be an
     external link and cannot be a relative link. markers has the following type: list of dicts containing keys 'title', 'geom', 'popup', 'icon'.
Those keys have the following types:
  - title (string; optional)
  - geom (list of list of numberss; required)
  - popup (list of strings | string; optional)
  - icon (dict; optional): icon has the following type: dict containing keys 'iconUrl', 'iconRetinaUrl', 'shadowUrl', 'iconSize', 'iconSizeMultiplier', 'iconAnchor', 'popupAnchor', 'tooltipAnchor', 'shadowSize'.
Those keys have the following types:
  - iconUrl (string; optional)
  - iconRetinaUrl (string; optional)
  - shadowUrl (string; optional)
  - iconSize (list of numbers; optional)
  - iconSizeMultiplier (list of numbers; optional)
  - iconAnchor (list of numbers; optional)
  - popupAnchor (list of numbers; optional)
  - tooltipAnchor (list of numbers; optional)
  - shadowSize (list of numbers; optional)
- circleMarkers (dict; optional): Array containing one or many shapes of:
     - title: Title of marker layer that is to be rendered on the map.
     - geom: Array of arrays containing coordinates ([lat, lng]) of markers that are to be rendered on the map.
     - popup: String containing popup-text for this layer group or list of strings containing popup-texts
     - options: Shape containing element options:
     - radius: Single number or array of numbers indicating the radius of the circle markers
     - stroke: Whether to draw stroke along the circle. Set it to false to disable borders.
     - color: Stroke color
     - weight: Stroke width in pixels
     - opacity: Stroke opacity
     - fill: Whether to fill the path with color. Set it to false to disable filling.
     - fillColor: Fill color. Defaults to color of stroke
     - fillOpacity: Fill opacity. circleMarkers has the following type: list of dicts containing keys 'title', 'geom', 'popup', 'options'.
Those keys have the following types:
  - title (string; optional)
  - geom (list of list of numberss; required)
  - popup (list of strings | string; optional)
  - options (dict; optional): options has the following type: dict containing keys 'radius', 'stroke', 'color', 'weight', 'opacity', 'fill', 'fillColor', 'fillOpacity'.
Those keys have the following types:
  - radius (list of numbers | number; optional)
  - stroke (boolean; optional)
  - color (string; optional)
  - weight (number; optional)
  - opacity (number; optional)
  - fill (boolean; optional)
  - fillColor (string; optional)
  - fillOpacity (number; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, mapOptions=Component.UNDEFINED, baselayer=Component.UNDEFINED, lines=Component.UNDEFINED, markers=Component.UNDEFINED, circleMarkers=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'mapOptions', 'baselayer', 'lines', 'markers', 'circleMarkers']
        self._type = 'DashLeaflet'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style', 'mapOptions', 'baselayer', 'lines', 'markers', 'circleMarkers']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashLeaflet, self).__init__(**args)
