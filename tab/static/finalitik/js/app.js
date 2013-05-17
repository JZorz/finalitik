angular.module('finalitik', ['finalServices']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/', {templateUrl: '/static/finalitik/partials/index.html', controller: FinalCtrl})
            .when('/details', {templateUrl: '/static/finalitik/partials/details.html',   controller: FinalCtrl})
            otherwise({redirectTo: '/'});
    }]);