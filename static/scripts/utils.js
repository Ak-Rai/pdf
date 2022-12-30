$(document).ready(function(){
    $('#fileForm').submit(function(event){
    event.preventDefault();
    $(this).ajaxSubmit({
        target:'#targetLayer',
        beforeSubmit:function(){
            $('#process').css('display', 'block');
        },
        success:function(data){
            $('#process').css('display', 'none');
            $('#fileForm').find('[type=file]').val('');
            $('#targetLayer').show();
            $('#targetLayer').append(data.htmlresponse);
        }
    })
    })
});






