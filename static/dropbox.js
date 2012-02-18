function hookDropbox(){
  var dropbox = document.getElementById('dropbox')

  dropbox.addEventListener("dragenter", noopHandler, false);
  dropbox.addEventListener("dragexit", noopHandler, false);
  dropbox.addEventListener("dragover", noopHandler, false);
  dropbox.addEventListener("drop", drop, false);
}

function noopHandler(evt){
  evt.stopPropagation();
  evt.preventDefault();
}

function drop(evt){
  evt.stopPropagation();
  evt.preventDefault();

  var files = evt.dataTransfer.files;
  var count = files.length

  if (count > 0)
    handleFiles(files)
}

function handleFiles(files){
  for(var i = 0; i < files.length; i++){
    file = files[i]
    var reader = new FileReader();
     
     // init the reader event handlers
     reader.onload = handleReaderLoad;
     // begin the read operation
     reader.readAsDataURL(file);
  }
}

function handleReaderLoad(evt){

  alert(evt.target.result);
}
