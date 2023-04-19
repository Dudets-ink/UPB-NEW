$(function(){
    async function toDoList(){
        let input = $('#input-note');
        let formAdd = $("#form-list")
        let note = $("<li></li>");

        formAdd.submit(function(event){
            event.preventDefault()

            if (input.val().trim()){
                let val = input.val()
                note.html(val);
                note.addClass("note");  
                if ($("#notes li").last().attr('id') != undefined) {
                    id = $("#notes li").last().attr('id').split('-')[1] 
                    note.attr('id', `note-${parseInt(id)+1}`);
                }else {
                    note.attr('id', 'note-1');  
                };
                $.ajax({
                    type:'POST',
                    data: {"noteVal":note.html(), "noteId":note.attr('id')},
                    success: function(){
                        $("#notes").load(location.href + " #notes>*", "");
                    }
                }).done(function(){
                    input.val('');
                })
            } else {
                alert('Wrong input...')
            }
            });

    };

    toDoList();

});

function delNote(noteId){
    $.ajax({
        type: 'DELETE',
        data: {'noteId': noteId},
        success: function (){
            $("#notes").load(location.href + " #notes>*", "");
        }
    });
};
