$(document).ready(function() {
    var table = new Tabulator("#table_settings", {
        ajaxURL: '/scanner/setting_data/',
        autoColumns: true,
        ajaxError: function(err) {
            console.error("Error fetching data: ", err);
        }
    });
});


