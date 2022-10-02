//Type node w4_jacob_garrison.js in the command line to run
//Must have node and npm express installed
//To download type: npm install express --save

//This is a simple RESTful app that uses express to create a server and serve up a web page

//Setup Express Server
var express = require("express");
var http = require("http");
var app = express();

//Launch Server on http://localhost:55555
http.createServer(app).listen(55555);

//Print URL for accessing web page
console.log('Server running at http://localhost:55555/');

//Product items for sale
var products = [
    { id: 0, name: 'Gaming Monitor', description: '4K, 240Hz, Ultrawide Gaming Monitor', price: 225.00 },
    { id: 1, name: 'Mechanical Keyboard', description: 'Sleek and responsive mechanical keyboard', price: 70.00 },
    { id: 2, name: 'Gaming Mouse', description: 'High DPI, lightweight, and bluetooth capable', price: 65.00 }
    ]; 

//The navigation links call to each route
//1. HTTP Method: GET - Route: /home - Description: Home page - CRUD: Read
//2. HTTP Method: GET - Route: /contact - Description: Contact Page - CRUD: Read
//3. HTTP Method: GET - Route: /products - Description: Products Page - CRUD: Read
//4. HTTP Method: GET - Route: /products/0 - Description: Gaming Monitor - CRUD: Read
//5. HTTP Method: GET - Route: /products/1 - Description: Mechanical Keyboard - CRUD: Read
//6. HTTP Method: GET - Route: /products/2 - Description: Gaming Mouse - CRUD: Read
app.get("/", function(req, res) {
	var msg=""
	msg += '<center><h1>Computer Center</h1></center>'
    msg += '<center><a href="/home">Home</a> <br /></center>'
    msg += '<center><a href="/contact">Contact</a> <br /></center>'
  	msg += '<center><a href="/products">Products</a> <br /></center>'
	  msg += '<center><a href="/products/0">Gaming Monitor</></center>'
    msg += '<center><a href="/products/1">Mechanical Keyboard</></center>'
    msg += '<center><a href="/products/2">Gaming Mouse</></center>'
	
	res.send(msg);
});

//Route for home page via HTTP 'GET' request
app.get("/home", function(req, res) {
	res.send("Your one stop shop for all your computer needs!");
});

//Route for contact page catalog via HTTP 'GET' request
app.get("/contact", function(req, res) {
	res.send("Please contact support@shop.com for questions regarding an item or your order.");
});

//Load and display product catalog via HTTP 'GET' request
app.get("/products", function(req, res) {
	res.send(JSON.stringify(products));
});

//Load and display item id via HTTP 'GET' for URI '/products/:id'
app.get('/products/:id', function(req, res) {

    //If not a number and not in range, return error
    if (isNaN(req.params.id) == true || req.params.id > products.length - 1 || req.params.id < 0) {
            res.statusCode = 404;
            res.end('Please enter a valid product ID.');
    } else {
        res.send(JSON.stringify(products[req.params.id]));
    }
});
