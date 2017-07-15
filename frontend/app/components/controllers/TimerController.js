'use strict';

angular.module('aliereApp.timer', ['ngRoute'])

.controller('TimerController', ['$scope', '$http', '$interval', function($scope, $http, $interval) {
  $scope.timer = 300;

  if($scope.myInterval){
  	$interval.cancel($scope.myInterval);
  }
  $scope.onInterval = function(){
    if ($scope.timer > 0) {
      $scope.timer--;
    } else if ($scope.timer == 0) {
      alert('Making transaction...')
      $scope.timer = 300;
    }
  };
  $scope.myInterval = $interval($scope.onInterval,1000);

}]);

app.filter('mmss', function () {
  return function (time) {
    var elapsed = parseInt(time, 10); 
    var minutes = Math.floor(elapsed / 60);
    var seconds = elapsed - (minutes * 60);

    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}
    var time = minutes+':'+seconds;
    return time;
  }
});