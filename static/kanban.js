$( document ).ready(function() {
    console.log( "ready!" )

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


})



