'use strict';

angular.module('aliereApp.feed', ['ngRoute'])

// Controller definition for this module
.controller('FeedController', ['$scope', function($scope) {

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

}]);