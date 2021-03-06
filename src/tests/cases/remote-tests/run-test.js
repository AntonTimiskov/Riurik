module('run test');

//window.parent.$(window.parent.document).trigger('complete');

function triggerComplete(){
  $(document).trigger('complete');
}

var test_content = " \
asyncTest('test', function() { \
  $.when( frame.go( contexter.URL(context, 'hello') )).then(function(_$) { \
    equal($.trim(_$('body').text()), 'Hello world!'); \
    $(document).trigger('complete'); \
    console.log( window.parent ); \
    start(); \
  }); \
});";

QUnit.setup(function() {
  with(context) {
    context.test_name = 'first-example.js';
    context.suite_name = 'remote-tests';
    context.suite_path = root.concat('/', suite_name);
    context.test_path = suite_path.concat('/',  test_name);
    context.test_context = 'django-app';
    context.test_content = test_content;
    context.start = getLogs('last');
    
    var path = 'actions/test/run/?path='.concat(test_path, '&context=', test_context);
    context.URL = contexter.URL(context, path.concat("&content=", escape(test_content)));
    
    create_test( test_name, context.suite_path );
  }
});

asyncTest('test is pushed to run on remote server', function() {
  $('#frame').attr('src', context.URL);
  $('#frame').unbind('load');
  $('#frame').load(function() {
    $(document).bind('complete', function(){
      alert('Complete');    
      start();
    });
  });
});
/*
QUnit.teardown(function() {
  delete_test( context.test_path );
});*/