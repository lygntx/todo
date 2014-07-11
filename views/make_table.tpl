<!doctype html>
<html>
<head>

	<title>bottle</title>
</head>
<body>
<p>todo list :</p>
<table border="1">
	%for row in rows:
	<tr>
		%for col in row:
		<td>{{col}}</td>
		%end
	</tr>
	%end
</table>
</body>
</html>