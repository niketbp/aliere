// HomeController.js
// For distribution, all controllers
// are concatanated into single app.js file
// by using Gulp

'use strict';

angular.module('aliereApp.login', ['ngRoute'])

// Routing configuration for this module
.config(['$routeProvider',function($routeprovider){
	$routeprovider.when('/login', {
		controller: 'LoginController',
		templateUrl: 'components/views/loginView.html'
	});
}])

// Controller definition for this module
.controller('LoginController', ['$scope', '$rootScope', '$window', function($scope, $rootScope, $window) {
/*  function renderButton() {
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
*/
	function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
    	window.localStorage.removeItem("username");
    	$rootScope.logout = false;
      console.log('User signed out.');
      window.location.href = "/#";
    });
  }

  function onSuccess(googleUser) {
  	window.localStorage.setItem("username", googleUser.getBasicProfile().getName());
  	$rootScope.logout = true;
  	//window.localStorage.setItem("auth", JSON.stringify(gapi.auth2));
  	$window.location.href = "/#/dashboard";
    console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
  }

   function onFailure(error) {
    console.log(error);
  }

	$scope.options = {
    'width': 240,
    'height': 50,
    'longtitle': true,
    'theme': 'dark',
    'onsuccess': onSuccess,
    'onfailure': onFailure,
  };

	this.message = "Hello Home!";

}])

.directive('googleSignInButton', function() {
  return {
    scope: {
      buttonId: '@',
      options: '&'
    },
    template: '<div></div>',
    link: function(scope, element, attrs) {
      var div = element.find('div')[0];
      div.id = attrs.buttonId;
      gapi.signin2.render(div.id, scope.options()); //render a google button, first argument is an id, second options
    }
  }
});
