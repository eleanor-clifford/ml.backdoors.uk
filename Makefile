build:
	make clean
	cd diagram && pdflatex -shell-escape main.tex && cd ..
	mkdir -p out
	pdf2svg diagram/main-figure0.pdf out/overview.svg
	rm -f diagram/main-figure* diagram/main.aux* diagram/main.out diagram/main.log diagram/main.pdf
	cd table && python3 make_table.py && cd ..
	<templates/index.html ./scripts/subst_into_template.sh \
			TABLE table/table.html \
			TABLE_LEGEND table/table_legend.html \
		> out/index.html
	cp -r static/* out/ || true
	cp -r static/.[!.]* out/ || true
clean:
	rm -rf out/

deploy:
	rsync -a --delete out/* pip:/public/societies/mlbackdoors/public_html/
	rsync -a --delete out/.[!.]* pip:/public/societies/mlbackdoors/public_html/

all:
	make clean && make build && make deploy
