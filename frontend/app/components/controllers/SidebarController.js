'use strict';

angular.module('aliereApp.sidebar', ['ngRoute'])

// Controller definition for this module
.controller('SidebarController', ['$scope', '$http', function($scope, $http) {

	getUserData();
	getFundData();
	//console.log(window.localStorage.getItem('full-name'));
	$scope.fullname = window.localStorage.getItem('full-name');

	function getUserData() {
		$http( {
			method: 'GET',
			url: 'http://127.0.0.1:5000/user/data?user=tylersco'
		}).then(function success(response) {
			$scope.userData = response;
			console.log(response);
			console.log(response.data.investorFunds[0].fundName);
		}, function error(response) {
			console.log(response);
		});
	};

	function getFundData() {
		$http( {
			method: 'GET',
			url: 'http://127.0.0.1:5000/fund/data?name=Neptune'
		}).then(function success(response) {
			$scope.fundData = response;
			console.log(response);
		}, function error(response) {
			console.log(response);
		});
	}

	function init(){
		$http( {
			method: 'GET',
			url: 'http://127.0.0.1:5000/user/data?user=jerrygong'
		}).then(function successCallback(response) {
			$scope.data = response;
			console.log($scope.data);
			console.log($scope.data.data.playerFunds);
		}, function errorCallback(response) {
			console.log(response);
		});
	};

	this.message = "Hello Home!";

}]);