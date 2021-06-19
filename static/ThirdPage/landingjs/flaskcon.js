function onClickedEstimatePrice() {

    console.log("Estimate price button clicked");
    var year = document.getElementById("a");
    var kilo= document.getElementById("b");
    var mille = document.getElementById("c");
    var engine = document.getElementById("d");
    var power = document.getElementById("e");
    var seats=document.getElementById("f");
    var name=document.getElementById("carsName");
    var loc=document.getElementById("carsLoc");
    var fuel=document.getElementById("carsFuel");
    var trans=document.getElementById("carsTrans");
    var owner=document.getElementById("carsOwner");
    var estPrice = document.getElementById("EstimatedPrice");

    var url = "predict_price";

    $.post(url, {

        kilo  : parseFloat(kilo.value),
        mille : parseFloat(mille.value),
        engine: parseFloat(engine.value),
        power : parseFloat(power.value),
        seats : seats.value,
        year  : year.value,
        name  :name.value,
        location: loc.value,
        fuel  : fuel.value,
        Trans : trans.value,
        owner : owner.value

    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  function onPageLoad() {
    console.log( "document loaded" );
    var url = "get_location_names"; 
    
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
			console.log("Got Data");
            var locations = data.locations;
            var carsLoc = document.getElementById("carsLoc");
            $('#carsLoc').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#carsLoc').append(opt);
            }
        }
    });
    var url = "get_car_names"; 
    
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.name;
            var carsName = document.getElementById("carsName");
            $('#carsName').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#carsName').append(opt);
            }
        }
    });
    var url = "get_car_Transmission"; 
    
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.transmission;
            var carsLoc = document.getElementById("carsLoc");
            $('#carsTrans').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#carsTrans').append(opt);
            }
        }
    });
    var url = "get_car_Fuel_Type"; 
    
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.fuel_type;
            var carsLoc = document.getElementById("carsLoc");
            $('#carsFuel').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#carsFuel').append(opt);
            }
        }
    });
    var url = "get_car_Owner_Type"; 
    
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.Owner_Type;
            var carsLoc = document.getElementById("carsLoc");
            $('#carsOwner').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#carsOwner').append(opt);
            }
        }
    });
  }
  window.onload = onPageLoad;