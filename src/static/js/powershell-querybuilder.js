(function(window, jquery){
	var PowerShellQueryBuilder = function() {
		var PowerShellQueryBuilder = function() {
			return new PowerShellQueryBuilder.fn.init();
		},
		context = {};
		
		PowerShellQueryBuilder.fn = PowerShellQueryBuilder.prototype = {
			constructor: PowerShellQueryBuilder,
			init: function(){
			},
			version: '0.1',
			each: function( fnBody ){
				return PowerShellQueryBuilder.each( this, fnBody );
			},
			var: function( name, value ){
				if ( typeof value == 'undefined' ) return this.context[name];
				this.context[name] = value;
			},
			exe: function(){
			
			}
			
		}
		PowerShellQueryBuilder.fn.init.prototype = PowerShellQueryBuilder.fn;
		PowerShellQueryBuilder.each = function( self, fnBody ){
			console.log('each', 'self:', self, ', fnbody:', fnBody, ', this:', this);
			return this;
		}
		return PowerShellQueryBuilder;
	};
	
	window.PSq = PowerShellQueryBuilder;
})(window, $);
