$(document).ready(function() {
    if ($("#table_settings").length) {
        // var counter = 1; // Inisialisasi counter dari 1
        var table = new Tabulator("#table_settings", {
            ajaxURL: "/scanner/setting_data/",
            ajaxParams: {
                page: 1,
                size: 15,  // Jumlah data per halaman
            },
            autoColumns: false,
            layout:"fitColumns",
            pagination:"local",
            paginationSize:15,
            paginationSizeSelector:[10, 15, 30, 50],
            columns: [
                {
                    title: "No",
                    field: "no",
                    // formatter: function(cell) {
                    //     return counter++; // Kembalikan nilai counter dan increment
                    // },
                    formatter: "rownum", 
                    hozAlign: "center", // Menyelaraskan teks ke kanan
                    width: 100 ,// Lebar kolom,
                    headerHozAlign: "center", // Menyelaraskan teks judul kolom ke tengah
                },        
                {title: "CODE", field: "code" ,  headerHozAlign: "center",  width: 100 ,  hozAlign: "center",  },
                {title: "COMPANY NAME", field: "company_name" ,  headerHozAlign: "center",  },
                {title: "LISTING BOARD", field: "listing_board",  headerHozAlign: "center", },
            ],
            paginationDataReceived: {
                last_page: "total_pages", // Nama field untuk total halaman
                data: "data",  // Nama field untuk data
                page: "current_page",    // Nama field untuk halaman saat ini
            },
            ajaxResponse: function(url, params, response){
                // Optional: Manipulasi data jika diperlukan
                return response;
            },
        });
        $("#search").on("keyup", function() {
            const searchTerm = $(this).val();
            table.setFilter("code", "like", searchTerm); // Filter berdasarkan kolom 'name'
        });
        
    }
});

