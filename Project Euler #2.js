var fibo_even = 0
for (x=1;x<100;x++){var y =parseInt(((((1+Math.sqrt(5))/2)**x)-(((1-Math.sqrt(5))/2)**x))/Math.sqrt(5)); if (y % 2 == 0){fibo_even += y} if (y > 4000000){break}}
	alert(fibo_even)
