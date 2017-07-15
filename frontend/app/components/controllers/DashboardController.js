// HomeController.js
// For distribution, all controllers
// are concatanated into single app.js file
// by using Gulp

'use strict';

angular.module('aliereApp.dashboard', ['ngRoute'])

// Routing configuration for this module
.config(['$routeProvider',function($routeprovider){
	$routeprovider.when('/dashboard', {
		controller: 'DashboardController',
		templateUrl: 'components/views/dashboardView.html'
	});
}])

// Controller definition for this module
.controller('DashboardController', ['$scope', function($scope) {
	init();

	function init(){
		console.log('hey dashboard');
	};

	this.message = "Hello Dashboard!";

}]);