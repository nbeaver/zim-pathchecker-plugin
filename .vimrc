if has('autocmd')
    autocmd BufNewFile,BufRead *.py setlocal noexpandtab
    autocmd BufNewFile,BufRead *.py setlocal shiftwidth=4
    autocmd BufNewFile,BufRead *.py setlocal tabstop=4
endif
