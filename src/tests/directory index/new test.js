var url = 'http://spb0281:8001/cases';

asyncTest('create new folder', function() {
  $.when( frame.go(url) ).then(function(_$) {
    
    _$('a#new-folder').click();
    equal(_$('#create-dir-index-dialog').is(":visible"), true, 'Create folder dialog is visible');
    equal(_$('.ui-dialog-title').text(), _$('a#new-folder').text(), 'Create folder title');
      
    _$('#object-name').val('first-dir');
    _$('#create-folder-btn').click();
      
    start();
  });
});

asyncTest('check new folder', function() {
  
  $.when( frame.load() ).then(function(_$) {
      ok(_$('#first-dir').is(":visible"), 'New folder is created');
      
      start();
    });
  
});