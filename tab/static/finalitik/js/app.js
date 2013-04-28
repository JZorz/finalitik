angular.module('finalitik', ['finalServices']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/', {templateUrl: '/templates/tab/index.html', controller: FinalCtrl})
            .when('/details', {templateUrl: '/templates/tab/details.html',   controller: FinalCtrl})
            otherwise({redirectTo: '/'});
    }]);