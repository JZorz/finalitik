angular.module('finalServices', ['ngResource']).
    factory('Tab', function($resource){
        return $resource('api/v1/tab', {}, {
            query: {method:'GET', isArray:false}
        });
    });