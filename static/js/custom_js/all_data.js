// $(document).ready(function() {
//     // Periksa apakah elemen dengan ID 'example-table' ada di halaman
//     if ($("#table_settings").length > 0) {
//         // Jika elemen ada, inisialisasi Tabulator
//         $(document).ready(function() {
//             // Inisialisasi Tabulator dengan data dari endpoint Django
//             var table = new Tabulator("#table_settings", {
//                 ajaxURL: "{% url 'setting_data' %}",  // Endpoint Django untuk mengambil data
//                 autoColumns: true,  // Membuat kolom otomatis berdasarkan field data
//             });
//         });
       
//     } else {
//         // Jika elemen tidak ada, lakukan sesuatu yang lain, atau biarkan kosong
//         console.log("Table element not found on this page.");
//     }
// });



$(document).ready(function() {
    // Inisialisasi Tabulator dengan data dari endpoint Django
    var table = new Tabulator("#table_settings", {
        ajaxURL: "/scanner/setting-data/",  // Endpoint Django untuk mengambil data
        autoColumns: true,  // Membuat kolom otomatis berdasarkan field data
    });
});