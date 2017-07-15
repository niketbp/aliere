'use strict';

// Defining Angular app model with all other dependent modules
let app = angular.module('aliereApp',['ngRoute','aliereApp.dashboard','aliereApp.login', 'aliereApp.sidebar', 'aliereApp.feed', 'chart.js']);

app.config(function($routeProvider) {
	// Declaration of the default route if neither of the controllers
	// is supporting the request path
	$routeProvider.otherwise({ redirectTo: '/'});
})

.controller('MainController', ['$rootScope', '$scope', '$window', function($rootScope, $scope, $window) {
	$rootScope.logout = true;

	if (!window.localStorage.getItem('username')) {
		$rootScope.logout = false;
	}

	$scope.signOut = function() {
    //var auth2 = gapi.auth2.getAuthInstance();
    //auth2.signOut().then(function () {
    	window.localStorage.removeItem("username");
    	$rootScope.logout = false;
      console.log('User signed out.');
      window.location.href = "/#";
    //});
  }
}]);
