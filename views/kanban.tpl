

<head>
	<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
	<script src="/static/kanban.js"></script>
	<link rel="stylesheet" href="/static/kanban.css" type="text/css">
	<link rel="stylesheet" href="/static/css/font-awesome.css" type="text/css">​
	<title>
		{{name}}'s Kanban
	</title>
</head>

<div id="postit_master" class="postit">
	<div class="fa fa-times close_icon">
	</div>
	<div contenteditable="true">
		Enter Text Here
	</div>
</div>

<script>
NUMBER_ISSUES = {{number_issues}}
</script>

<table id="kanban_table">
	<tr id="kanban_table_header">
		<th> To Do </th>
		<th> In Progress </th>
		<th> Done </th>
	</tr>
    <tr>
    	<td class="kanban_col" id="col_todo"></td>
    	<td class="kanban_col" id="col_inprogress"></td>
    	<td class="kanban_col" id="col_done"></td>
    </tr>
</table>