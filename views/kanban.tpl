

<head>
	<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
	<script src="/static/kanban.js"></script>
    <script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
	<link rel="stylesheet" href="/static/kanban.css" type="text/css">
	<link rel="stylesheet" href="/static/css/font-awesome.css" type="text/css">​
	<title>
		{{name}}'s Kanban
	</title>
</head>

<div id="postit_master" class="postit">
    <div class="postit_header">
        <div class="fa fa-times close_icon"></div>
        <div> Task Num</div>
	</div>
	<div class="postit_content" contenteditable="true">
		Enter Text Here
	</div>
</div>

<div id="postit_master_tracker" class="postit">
    <div class="postit_header">
        <div class="priority"></div>
        <div class="project"></div>
        <div class="author"></div>
        <div class="assigned_to"></div>
        <div class="title"></div>
	</div>
	<div class="postit_content" contenteditable="true">
		Enter Text Here
	</div>
</div>

<script>
NUMBER_ISSUES = {{number_issues}}
OPERATION_MODE = "{{operation_mode}}"
ISSUES = "{{issues}}"
NAME = "{{name}}"
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
</body>