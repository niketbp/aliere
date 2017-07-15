// HomeController.js
// For distribution, all controllers
// are concatanated into single app.js file
// by using Gulp

'use strict';

angular.module('aliereApp.home', ['ngRoute'])

// Routing configuration for this module
.config(['$routeProvider',function($routeprovider){
	$routeprovider.when('/', {
		controller: 'HomeController',
		templateUrl: 'components/views/homeView.html'
	});
}])

// Controller definition for this module
.controller('HomeController', ['$scope', function($scope) {
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

/*	function onSignIn(googleUser) {
	  var profile = googleUser.getBasicProfile();
	  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
	  //console.log('Name: ' + profile.getName());
	  console.log('Image URL: ' + profile.getImageUrl());
	  window.localStorage.setItem("username", profile.getName());
	  console.log(window.localStorage.getItem("username"));
	  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
	};*/

	/*window.onSignIn = onSignIn;*/

	function init(){
		console.log('hey');
	};

	this.message = "Hello Home!";

}]);