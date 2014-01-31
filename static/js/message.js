$(function() {
	$('#id_body').keydown(down);
	$('#id_body').keyup(up);
	$('#id_tag').change(change);
	$('.re').click(setInit);
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
	if (submit_key(e))
		$('#form').submit();
}

change = function() {
	val = $('#id_tag').val();
	if (val != '')
		$('#id_tag_create').prop('disabled', true);
	else
		$('#id_tag_create').prop('disabled', false);
}

setInit = function(e) {
	id = e.target.id;

	body_id = $('#id_body_' + id).val()
	tag_id = $('#id_tag_' + id).val()

	$('#id_ref').val(body_id);

	if (tag_id) 
		$('#id_tag').val(tag_id);
	else
		$('#id_tag').val('');
	change();

	$('#id_body').focus();
}
