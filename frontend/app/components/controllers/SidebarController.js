'use strict';

angular.module('aliereApp.sidebar', ['ngRoute'])

// Controller definition for this module
.controller('SidebarController', ['$scope', '$http', function($scope, $http) {

	getUserData();
	//leaveFund();
	//getFundData();
	//console.log(window.localStorage.getItem('full-name'));
	$scope.fullname = window.localStorage.getItem('full-name');
	$scope.userID = window.localStorage.getItem('username');

	console.log(window.localStorage.getItem('username'));

	function getUserData() {
		$http( {
			method: 'GET',
			url: 'http://127.0.0.1:5000/user/data?user=' + window.localStorage.getItem('username')
		}).then(function success(response) {
			$scope.userData = response;
			console.log(response);
			console.log(response.data.playerFunds[0].fundName);
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

	function leaveFund() {
		$http( {
			method: 'GET',
			url: 'http://127.0.0.1:5000/fund/leave?name=Voyager&username=' + window.localStorage.getItem('username')
		}).then(function success(response) {
			console.log(response);
		}, function error(response) {
			console.log(response);
		});
	}

	$scope.joinFund = function() {
		$http({
			method: 'GET',
			url: 'http://127.0.0.1:5000/fund/join?name=Voyager&username=' + window.localStorage.getItem('username')
		}).then(function success(response) {
			console.log(response);
		}, function error(response) {
			console.log(response);
		});
	}

}]);