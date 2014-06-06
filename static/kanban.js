$( document ).ready(function() {
    console.log( "ready!" )

if (OPERATION_MODE=="standalone") {

	$('.kanban_col').mousedown(function(e) {
		elements_under_point = $(document.elementFromPoint(e.pageX, e.pageY))
		if (!elements_under_point.is('.kanban_col')) {
			return
		}
		var new_postit = $('#postit_master').clone()
		new_postit.attr("id", "postit_" + (NUMBER_ISSUES+1))
		new_postit.select('.close_icon').click(function(e){
			console.log("closing")
			elements_under_point = $(document.elementFromPoint(e.pageX, e.pageY))
			if (!elements_under_point.is('.close_icon')) {
				console.log("not close icon", elements_under_point)
				return
			}
	        if (!confirm("this will remove the post it")) {
	            return
	        }
			new_postit.remove()
			console.log("finished")
		})
	    
	    new_postit.draggable()
	    
		NUMBER_ISSUES+=1
		$(this).append(
			new_postit		
		)
	})
}

if (OPERATION_MODE=="tracker") {
	$.post('/issues',{'project_name':NAME}, function(data){
		data = ($.parseJSON(data))
		$.each(data, function(e, issue){
			console.log(issue)
			var new_postit = $('#postit_master_tracker').clone()
			new_postit.attr("id", issue.id)
			//new_postit.draggable()
			new_postit.find('.postit_content').text(issue.subject)
			new_postit.find('.author').text("author: " + issue.author)
			new_postit.find('.assigned_to').text("assigned: " + issue.assigned_to)
			new_postit.find('.priority').text("priority: " + issue.priority)
			new_postit.find('.project').text(issue.project + ':')
			new_postit.attr("href", SITE_BASE_URL + '/issues/' + issue.id)
			var col = $('#' + issue.col)
			$(col).append(new_postit)
		})
	})
}

})



