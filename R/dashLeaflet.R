# AUTO GENERATED FILE - DO NOT EDIT

dashLeaflet <- function(id=NULL, style=NULL, mapOptions=NULL, baselayer=NULL, lines=NULL, markers=NULL, circleMarkers=NULL) {
    
    props <- list(id=id, style=style, mapOptions=mapOptions, baselayer=baselayer, lines=lines, markers=markers, circleMarkers=circleMarkers)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashLeaflet',
        namespace = 'dash_leaflet',
        propNames = c('id', 'style', 'mapOptions', 'baselayer', 'lines', 'markers', 'circleMarkers'),
        package = 'dashLeaflet'
        )

    structure(component, class = c('dash_component', 'list'))
}
