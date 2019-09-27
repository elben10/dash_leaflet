% Auto-generated: do not edit by hand
\name{dashLeaflet}

\alias{dashLeaflet}

\title{DashLeaflet component}

\description{
DashLeaflet is allows to display a map in dash. Several point and line layers can be added to the map.
}

\usage{
dashLeaflet(id=NULL, style=NULL, mapOptions=NULL, baselayer=NULL, lines=NULL, markers=NULL,
circleMarkers=NULL)
}

\arguments{
\item{id}{Character. The id of the main element}

\item{style}{Lists containing elements 'height'.
those elements have the following types:
  - height (character; optional). The style of the main element}

\item{mapOptions}{Lists containing elements 'bounds', 'center', 'minbounds', 'maxbounds', 'minzoom', 'maxzoom', 'zoom'.
those elements have the following types:
  - bounds (list of list of numericss; optional)
  - center (list of numerics; optional)
  - minbounds (list of list of numericss; optional)
  - maxbounds (list of list of numericss; optional)
  - minzoom (numeric; optional)
  - maxzoom (numeric; optional)
  - zoom (numeric; optional). The style of the main element}

\item{baselayer}{Lists containing elements 'url', 'attribution'.
those elements have the following types:
  - url (character; optional)
  - attribution (character; optional) | list of lists containing elements 'name', 'url', 'attribution'.
those elements have the following types:
  - name (character; optional)
  - url (character; optional)
  - attribution (character; optional)s. The baselayer(s) of the map. Can either be a single one or an array of multiple baselayers including their name.
     If no baselayer is provided, the OSM will serve as default.}

\item{lines}{List of lists containing elements 'title', 'geom', 'popup', 'options'.
those elements have the following types:
  - title (character; optional)
  - geom (list of list of list of numericss | list of list of list of numericssss; required)
  - popup (list of characters | character; optional)
  - options (optional): . options has the following type: lists containing elements 'color', 'weight', 'opacity'.
those elements have the following types:
  - color (character; optional)
  - weight (numeric; optional)
  - opacity (numeric; optional)s. Array containing one or many shapes of:
     - title: Title of line layer that is to be rendered on the map.
     - geom: Array of arrays containing lines that are to be rendered on the map. These can either be lines or polylines.
     - popup: String containing popup-text for this layer group or list of strings containing popup-texts,
     - options: Shape containing element options:
     - color: Stroke color
     - weight: Stroke width in pixels
     - opacity: Stroke opacity}

\item{markers}{List of lists containing elements 'title', 'geom', 'popup', 'icon'.
those elements have the following types:
  - title (character; optional)
  - geom (list of list of numericss; required)
  - popup (list of characters | character; optional)
  - icon (optional): . icon has the following type: lists containing elements 'iconurl', 'iconretinaurl', 'shadowurl', 'iconsize', 'iconsizemultiplier', 'iconanchor', 'popupanchor', 'tooltipanchor', 'shadowsize'.
those elements have the following types:
  - iconurl (character; optional)
  - iconretinaurl (character; optional)
  - shadowurl (character; optional)
  - iconsize (list of numerics; optional)
  - iconsizemultiplier (list of numerics; optional)
  - iconanchor (list of numerics; optional)
  - popupanchor (list of numerics; optional)
  - tooltipanchor (list of numerics; optional)
  - shadowsize (list of numerics; optional)s. Array containing one or many shapes of:
     - title: Title of marker layer that is to be rendered on the map.
     - geom: Array of arrays containing coordinates ([lat, lng]) of markers that are to be rendered on the map.
     - popup: String containing popup-text for this layer group or list of strings containing popup-texts
     - icon: Shape for the icon that is to be rendered for the markers. Attention, the iconUrl must be an
     external link and cannot be a relative link.}

\item{circleMarkers}{List of lists containing elements 'title', 'geom', 'popup', 'options'.
those elements have the following types:
  - title (character; optional)
  - geom (list of list of numericss; required)
  - popup (list of characters | character; optional)
  - options (optional): . options has the following type: lists containing elements 'radius', 'stroke', 'color', 'weight', 'opacity', 'fill', 'fillcolor', 'fillopacity'.
those elements have the following types:
  - radius (list of numerics | numeric; optional)
  - stroke (logical; optional)
  - color (character; optional)
  - weight (numeric; optional)
  - opacity (numeric; optional)
  - fill (logical; optional)
  - fillcolor (character; optional)
  - fillopacity (numeric; optional)s. Array containing one or many shapes of:
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
     - fillOpacity: Fill opacity}
}
