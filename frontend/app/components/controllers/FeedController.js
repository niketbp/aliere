'use strict';

angular.module('aliereApp.feed', ['ngRoute'])
// Controller definition for this module
.controller('FeedController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams) {

	const fundName = 'Leo';
	$scope.proposals = [];
	$scope.votes = {};
	$scope.userVotes = {};

	getFundProposals();

	function getFundProposals() {
		$http({
			method: 'GET',
			url: `http://127.0.0.1:5000/fund/data?name=${fundName}`
		}).then(function successfulCallback(response) {
			$scope.proposals = response.data.proposals;
			console.log(response);
		}, function(response){
			console.log(response);
		});
	}


	$scope.addProposal = function(proposal) {
		const data = {
			name: proposal.name,
			ticker: proposal.stock,
			shares: proposal.shares,
			transaction: 'buy',
			user: window.localStorage.getItem('username'),
			fund: 'Leo',// testing
		};
		console.log(data);

		$http({
			method: 'GET',
			url: `http://127.0.0.1:5000/proposal/create?name=${data.name}&ticker=${data.ticker}&shares=${data.shares}&transaction=${data.transaction}&user=${data.user}&fund=${data.fund}`,
		}).then(function successfulCallback(response) {
			//reload feed
			getFundProposals();
		console.log(response)
		}, function(response) {
			console.log(response)
		});
	};

	function updateTickerTable() {
		for (let i = 0; i < $scope.proposals.length; i++) {
			$scope.votes[$scope.proposals[i].ticker] = $scope.proposals[i].numVotes;
		}
	}

	/*function updateUserVoteTable() {
		for (let i = 0; i < $scope.proposals.length; i++) {
			$scope.userVotes[$scope.proposals[i].ticker] = 0;
		}
	}*/

	$scope.votes = {
		'MSFT': 85,
	};

	$scope.userVotes = {
		'MSFT': 0,
	};

	$scope.currentStocks = [{
		name: 'AAPL',
		price: 111.06,
		change: 0.65,
		shares: '100 shares'
	}, {
		name: 'MSFT',
		price: 72.78,
		change: 1.01,
		shares: '50 shares'
	}, {
		name: 'SNAP',
		price: 15.27,
		change: -0.42,
		shares: '100 shares'
	}
	];

	$scope.incrementVote = function(key) {
/*		if ($scope.userVotes[key] < 1) {
			$scope.votes[key] += 1;
			$scope.userVotes[key] += 1;
		}*/
		key++;
		//$scope.votes[key]++;
	};

	$scope.decrementVote = function(key) {
/*		if ($scope.userVotes[key] > 0) {
			$scope.votes[key] -= 1;
			$scope.userVotes[key] -= 1;
		}*/
		key--;
	};
}]);

