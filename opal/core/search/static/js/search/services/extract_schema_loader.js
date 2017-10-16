angular.module('opal.services')
    .factory('extractSchemaLoader', function($q, $http, $window, ExtractSchema){
    var load = function(){
      var deferred = $q.defer();
      $http.get('/search/api/extract/').then(function(response) {
  	    var columns = response.data;
  	    deferred.resolve(new ExtractSchema(columns));
      }, function() {
  	    // handle error better
  	    $window.alert('Extract schema could not be loaded');
      });

      return deferred.promise;
    }

    return {load: load};
});
