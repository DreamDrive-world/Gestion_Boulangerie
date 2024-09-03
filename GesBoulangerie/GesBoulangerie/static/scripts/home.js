document.addEventListener('DOMContentLoaded', function() {
    // const table = new DataTable('#approvisionnement_table');
    const table = $('#approvisionnement_table').DataTable({
        language: {
            search: "Rechercher :",
            lengthMenu: "Afficher _MENU_ enregistrements par page",
            zeroRecords: "Aucun résultat",
            info: "Page _PAGE_ sur _PAGES_",
            infoEmpty: "Aucun enregistrement disponible",
            infoFiltered: "(filtrés à partir de _MAX_ enregistrements au total)"
        },
        lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "Tous"]],
        pageLength: 10
    });
    const trieSelect = document.getElementById('trie');
    const searchInput = document.getElementById('search');

    searchInput.addEventListener('keyup', function() {
        table.column(1).search(this.value).draw();
    });

    trieSelect.addEventListener('change', function() {
        table.column(1).search(this.value).draw();
    });
});




