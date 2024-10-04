// $(document).ready(function() {
//     if ($("#table_settings").length > 0) {
        
//         var table = new Tabulator("#table_settings", {
//             ajaxURL: '/scanner/setting_data/',
//             autoColumns: true,
//             ajaxError: function(err) {
//                 console.error("Error fetching data: ", err);
//             }
//         });

//     } else {
//         console.log("Table element not found on this page.");
//     }

// });

$(document).ready(function() {
    if ($("#table_settings").length) {
        var table = new Tabulator("#table_settings", {
            ajaxURL: "/scanner/setting_data/",
            autoColumns: true,
            ajaxError: function(err) {
                console.error("Error fetching data: ", err);
            }
        });
    }
});

