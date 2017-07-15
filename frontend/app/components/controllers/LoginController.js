// HomeController.js
// For distribution, all controllers
// are concatanated into single app.js file
// by using Gulp

'use strict';

angular.module('aliereApp.login', ['ngRoute'])

// Routing configuration for this module
.config(['$routeProvider',function($routeprovider){
	$routeprovider.when('/', {
		controller: 'LoginController',
		templateUrl: 'components/views/loginView.html'
	});
}])

// Controller definition for this module
.controller('LoginController', ['$scope', function($scope) {
	init();

  function onSuccess(googleUser) {
  	$scope.name = googleUser.getBasicProfile().getName();
    console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
  }

  function onFailure(error) {
    console.log(error);
  }

  function renderButton() {
    gapi.signin2.render('my-signin2', {
      'scope': 'profile email',
      'width': 240,
      'height': 50,
      'longtitle': true,
      'theme': 'dark',
      'onsuccess': onSuccess,
      'onfailure': onFailure
    });
  }
  window.renderButton = renderButton;

  $scope.signOut = function(googleUser) {
  	console.log('hi');
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
    	window.localStorage.removeItem("username");
      console.log('User signed out.');
    });
  }

	function init(){
		console.log('hey');
	};

	this.message = "Hello Home!";

}]);