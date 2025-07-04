ymaps.ready(function () {
    var map = new ymaps.Map("map", {
        center: [55.751244, 37.618423], // координаты центра (Москва)
        zoom: 14
    });
    var placemark = new ymaps.Placemark([55.751244, 37.618423], {
        balloonContent: 'MerchShop<br>ул. Примерная, д. 10'
    });
    map.geoObjects.add(placemark);
});