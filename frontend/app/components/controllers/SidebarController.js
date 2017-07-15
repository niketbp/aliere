'use strict';

angular.module('aliereApp.sidebar', ['ngRoute'])

// Controller definition for this module
.controller('SidebarController', ['$scope', '$http', function($scope, $http) {

	init();

	function init(){
		$http( {
			method: 'GET',
			url: 'http://127.0.0.1:5000/user/data'
		}).then(function successCallback(response) {
			console.log(response);
		}, function errorCallback(response) {
			console.log(response);
		});
	};

	this.message = "Hello Home!";

}]);