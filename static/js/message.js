$(function() {
	$('.class_form_input').keydown(down);
	$('.class_form_input').keyup(up);
	$('#id_tag').change(change);
	$('.class_re_parts').click(setInit);
	$('#id_body').focus();
});

submit_key = function(e) {
	if (e.altKey || e.ctrlKey)
		if (e.keyCode == 13)
			return true;
};

down = function(e) {
	if (submit_key(e))
		return false;
};

up = function(e) {
	if (submit_key(e)) {
		var text = $('#id_body').val();
		text = text.replace(/^[ 　]*/gim, "").replace(/[ 　]*$/gim, "").replace(/[\n]*$/gim, "").replace(/[\r\n]*$/gim, "");
		if (text.length != 0)
			$('#id_form_form').submit();
	}
}

change = function() {
	var val = $('#id_tag').val();
	if (val != '') {
		$('#id_tag_create').prop('readonly', true);
		$('#id_tag_create').css({'background-color' : '#F0F0F0'});
	}
	else {
		$('#id_tag_create').prop('readonly', false);
		$('#id_tag_create').css({'background-color' : '#FFFFFF'});
	}
}

setInit = function(e) {
	var id = e.target.id.split('_')[3];

	var body_id = $('#id_body_' + id).val()
	var tag_id = $('#id_tag_' + id).val()

	$('#id_ref').val(body_id);

	if (tag_id) 
		$('#id_tag').val(tag_id);
	else
		$('#id_tag').val('');
	change();

	$('#id_body').focus();
}
