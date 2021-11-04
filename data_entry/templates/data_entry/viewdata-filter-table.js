function filter() {
	var input, filter, table, tr, td, i, txtValue, index;
	input = document.getElementById("sandman");
	index = document.getElementById("searchselect").value
	filter = input.value.toUpperCase();
	table = document.getElementById("spiderman");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[index];
		if (td) {
			txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}       
	}
}