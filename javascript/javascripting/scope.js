var a = 1, b = 2, c = 3; 
       
(function firstFunction(){  
 c = 6;  

 (function secondFunction(){  
     b = 8;  

     (function thirdFunction(){  
	 var a = 7, c = 9;  

	 (function fourthFunction(){  
	     var a = 1, c = 8;  

	 })();  
     })();  
 })();  
})();  
console.log("a: " + a + ", b: " + b + ", c: " + c);
