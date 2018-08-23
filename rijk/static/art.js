function loadTileInfo(objectNumber) {
    return $.getJSON("https://www.rijksmuseum.nl/api/nl/collection/OBJECT_NUMBER/tiles?format=jsonp&key=9UogSlO5"
        .replace("OBJECT_NUMBER", objectNumber.toUpperCase()));
}
// load them tiles
loadTileInfo("sk-c-5")
    .done(function(data) {
        // select a zoom level 
        var level = data.levels[0];

        // select a tile frome the zoom level
        var tile = level.tiles[4];

        // set the src of the image to the url of the tile        
        $("art-frame").attr("src", tile.url);
    });