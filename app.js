/**
 * Created by dasa on 28.7.16.
 */



    var app = angular.module("MyApp", []);

    app.controller('AppCtrl', function ($scope, $timeout) {

        function add(x, y) {
            return $timeout(function () {
                return x + y;
            }, 100);
        }

        var startTime = Date.now();
        var promise = add(5, 2);
        promise.then(function (result) {
            $scope.result = result;

        })

    });
