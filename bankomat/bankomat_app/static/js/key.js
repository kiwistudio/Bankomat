window.onload = function () {

            var cardnumber = document.getElementById("input");

            var n1 = document.getElementById("n1");
            var n2 = document.getElementById("n2");
            var n3 = document.getElementById("n3");
            var n4 = document.getElementById("n4");
            var n5 = document.getElementById("n5");
            var n6 = document.getElementById("n6");
            var n7 = document.getElementById("n7");
            var n8 = document.getElementById("n8");
            var n9 = document.getElementById("n9");
            var n0 = document.getElementById("n0");
            var bckspc = document.getElementById("bckspc");

            n1.addEventListener("click", function () {
            	if (cardnumber.value.length % 5 == 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '1';
            	}else{
                cardnumber.value = cardnumber.value + '1';
            	};
            }, false)
            n2.addEventListener("click", function () {
                if (cardnumber.value.length % 5 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '2';
            	}else{
                cardnumber.value = cardnumber.value + '2';
            	}
            }, false)
            n3.addEventListener("click", function () {
                if (cardnumber.value.length % 5 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '3';
            	}else{
                cardnumber.value = cardnumber.value + '3';
            	}
            }, false)
            n4.addEventListener("click", function () {
                if (cardnumber.value.length % 4 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '4';
            	}else{
                cardnumber.value = cardnumber.value + '4';
            	}
            }, false)
            n5.addEventListener("click", function () {
                if (cardnumber.value.length % 4 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '5';
            	}else{
                cardnumber.value = cardnumber.value + '5';
            	}
            }, false)
            n6.addEventListener("click", function () {
                if (cardnumber.value.length % 4 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '6';
            	}else{
                cardnumber.value = cardnumber.value + '6';
            	}
            }, false)
            n7.addEventListener("click", function () {
                if (cardnumber.value.length % 4 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '7';
            	}else{
                cardnumber.value = cardnumber.value + '7';
            	}
            }, false)
            n8.addEventListener("click", function () {
                if (cardnumber.value.length % 4 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '8';
            	}else{
                cardnumber.value = cardnumber.value + '8';
            	}
            }, false)
            n9.addEventListener("click", function () {
                if (cardnumber.value.length % 4 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '9';
            	}else{
                cardnumber.value = cardnumber.value + '9';
            	}
            }, false)
            n0.addEventListener("click", function () {
                if (cardnumber.value.length % 4 == 0 && cardnumber.value.length > 0 ) {
            		cardnumber.value = cardnumber.value + '-' + '0';
            	}else{
                cardnumber.value = cardnumber.value + '0';
            	}
            }, false)
            bckspc.addEventListener("click", function () {
                cardnumber.value = cardnumber.value.slice(0, -1)
            }, false)
        }