const today = new Date();
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, '0'); // January is 0
const day = String(today.getDate()).padStart(2, '0');
var formattedDate = year + '-' + month + '-' + day;

function show(id) {

    if (document.getElementById(id).style.display == 'none') {
        document.getElementById(id).style.display = '';
    }
    else {
        document.getElementById(id).style.display = 'none';
    }

}
function slugify(str) {
    return String(str)
        .normalize('NFKD')
        .replace(/[\u0300-\u036f]/g, '')
        .trim() 
        .toLowerCase()
        .replace(/[^a-z0-9 -]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-');
}

function splitPascalCase(word) {
    const camelCase = word.replace(/([a-z])([A-Z])/g, '$1 $2').split(" ");

    let flat = "";

    camelCase.forEach(word => {
        flat = flat + word.charAt(0).toUpperCase() + word.slice(1) + " "
    });
    return flat;
}

function capitalizeFirstLetter(str) {
    return str.replace(/\w\S*/g, function (txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

function stripHTML(s) {
    s = s.replace(/<[^>]*>?/gm, '');
    return s;
}    