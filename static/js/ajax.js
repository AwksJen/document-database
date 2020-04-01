"use strict";


// PART 1: SHOW A FORTUNE

// function showFortune(evt) {

    
//     $.get('/fortune', (response) => {
//       $('#fortune-text').text(response);
//     });
// }

// $('#get-fortune-button').on('click', showFortune);
// //show a quote by an author in drop down options

function showLewisQuote(evt) {

    $.get('/', (response) => {
        $('#quote-text').text(response);
    });
}

$('#davy-lewis').on('change', showLewisQuote);
