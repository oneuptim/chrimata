$(document).ready(function(){
    $('#stocks').click(function(){
        $('.stocks').show();
        return false;
    });

    $('#stocks_min').click(function(){
        $('.stocks').hide();
        return false;
    });functions.js
    $('#commodities').click(function(){
        $('.commodities').show();
        return false;
    });

    $('#commodities_min').click(function(){
        $('.commodities').hide();
        return false;
    });
    $('#cryptocurrencies').click(function(){
        $('.cryptocurrencies').show();
        return false;
    });

    $('#cryptocurrencies_min').click(function(){
        $('.cryptocurrencies').hide();
        return false;
    });
    $('#markets').click(function(){
        $('.markets').show();
        return false;
    });

    $('#markets_min').click(function(){
        $('.markets').hide();
        return false;
    });
});
