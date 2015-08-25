$(function () {
	$('.btn').on('mousedown', function () {
		$.get('engines/' + $(this).prop('id'))
	});

	$('.btn').on('mouseup', function () {
		$.get('engines/stop')
	});

});
