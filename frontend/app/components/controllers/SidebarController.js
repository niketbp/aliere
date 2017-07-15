'use strict';

angular.module('aliereApp.sidebar', ['ngRoute'])

// Controller definition for this module
.controller('SidebarController', ['$scope', '$http', function($scope, $http) {

	getUserData();
	getOpenFunds();
	//leaveFund();
	//getFundData();
	//console.log(window.localStorage.getItem('full-name'));
	$scope.fullname = window.localStorage.getItem('full-name');
	$scope.userID = window.localStorage.getItem('username');

	console.log(window.localStorage.getItem('username'));

	let tmp = null;

	function getUserData() {
		$http( {
			method: 'GET',
			url: 'http://127.0.0.1:5000/user/data?user=' + window.localStorage.getItem('username')
		}).then(function success(response) {
			$scope.userData = response;
			tmp = response;
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

	function getOpenFunds() {
		$http({
			method: 'GET',
			url: 'http://127.0.0.1:5000/fund/all'
		}).then(function success(response) {
			$scope.openFunds = [];
			console.log(response);
			response.data.forEach(function(element1) {
				let flag = 0;
				$scope.userData.data.playerFunds.forEach(function(element2) {
					if(element1.fundName == element2.fundName) {
						flag = 1;
					}
				})
				if(flag == 0) {
					$scope.openFunds.push(element1);
				}
			});
			console.log($scope.openFunds);
		}, function error(response) {
			console.log(response);
		});
	}

	$scope.joinFund = function(name) {
		$http({
			method: 'GET',
			url: 'http://127.0.0.1:5000/fund/join?name=' + name + '&username=' + window.localStorage.getItem('username')
		}).then(function success(response) {
			$scope.reload;
			console.log(response);
		}, function error(response) {
			console.log(response);
		});
	}

}]);