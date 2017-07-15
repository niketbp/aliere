'use strict';

// Defining Angular app model with all other dependent modules
let app = angular.module('aliereApp',['ngRoute','aliereApp.home','aliereApp.login', 'aliereApp.sidebar', 'aliereApp.feed']);

app.config(function($routeProvider) {

	// Declaration of the default route if neither of the controllers
	// is supporting the request path
	$routeProvider.otherwise({ redirectTo: '/'});
});
