import yaml
from os import listdir

files = sorted(listdir('entries/'))

with open("table.html", "w") as html_file:
	html_file.write('<table style="width: 100%">\n')
	html_file.write(open("table_header.html").read())
	html_file.write("<tbody>\n")
	for file in files:
		entry = yaml.safe_load(open(f"entries/{file}"))
		entry_html=f"\t<tr><td><a class=\"nounderline\" href=\"{entry['link']}\">{entry['name']}</a></td><td>{entry['insertion']}</td>"

		positions = [""] * 24
		for k,vs in entry.items():
			if k == "detectable":
				background = "#ff5555"
			elif k == "partially-detectable":
				background = "#f1fa8c"
			elif k == "undetectable":
				background = "#50fa7b"
			elif k == "detectable-later":
				background = "#8be9fd"
			elif k == "na":
				background = "#44475a"
			else:
				continue

			for v in vs:
				positions[v - 1] = background

		for p in positions:
			if p != "":
				entry_html += f'<td style="min-width: 10pt; background: {p}"></td>'
			else:
				entry_html += f'<td style="min-width: 10pt;"></td>'
		entry_html += "</tr>\n"
		html_file.write(entry_html)
	html_file.write("</tbody>\n</table>\n")
