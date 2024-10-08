$(document).ready(function() {
    if ($("#table_settings").length) {
        var counter = 1; // Inisialisasi counter dari 1
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
                {title: "CODE", field: "code" ,  headerHozAlign: "center",  width: 100 ,  hozAlign: "center",  },
                {title: "COMPANY NAME", field: "company_name" ,  headerHozAlign: "center",  },
                {title: "LISTING BOARD", field: "listing_board",  headerHozAlign: "center", },
            ],
            paginationDataReceived: {
                last_page: "total_pages",
                data: "data",
            },
            ajaxResponse: function(url, params, response){
                // Optional: Manipulasi data jika diperlukan
                return response;
            },
        });
        // $("#search").on("keyup", function() {
        //     const searchTerm = $(this).val();
        //     table.setFilter("code", "like", searchTerm); // Filter berdasarkan kolom 'name'
        // });

        $("#search").on("keyup", function() {
            const searchTerm = $(this).val().toLowerCase(); // Convert to lowercase for case-insensitive search
            table.setFilter(function(data, filterParams) {
                // Iterate over each field in the data object
                for (let key in data) {
                    if (data[key] && data[key].toString().toLowerCase().includes(searchTerm)) {
                        return true; // If any field contains the search term, include this row
                    }
                }
                return false; // Otherwise, exclude this row
            });
        });
        

    }
});

