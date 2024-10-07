$(document).ready(function() {
    if ($("#table_settings").length) {
        var counter = 1; // Inisialisasi counter dari 1
        var table = new Tabulator("#table_settings", {
            ajaxURL: "/scanner/setting_data/",
            autoColumns: false,
            layout:"fitColumns",
            pagination:"local",
            paginationSize:15,
            paginationSizeSelector:[10, 15, 30, 50],
            columns: [
                {
                    title: "No",
                    field: "no",
                    formatter: function(cell) {
                        return counter++; // Kembalikan nilai counter dan increment
                    },
                    hozAlign: "center", // Menyelaraskan teks ke kanan
                    width: 150 ,// Lebar kolom,
                    headerHozAlign: "center", // Menyelaraskan teks judul kolom ke tengah
                },        
                {title: "COMPANY NAME", field: "company_name" ,  headerHozAlign: "center",  },
                {title: "LISTING BOARD", field: "listing_board",  headerHozAlign: "center", },
            ],
            ajaxError: function(err) {
                console.error("Error fetching data: ", err);
            }
        });
        $("#search").on("keyup", function() {
            const searchTerm = $(this).val();
            table.setFilter("company_name", "like", searchTerm); // Filter berdasarkan kolom 'name'
        });
        
    }
});

