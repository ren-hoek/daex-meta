set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
call vundle#end()            " required

" Set filetype detection on
filetype plugin indent on

" Make colours more suitable for dark background
set background=dark

" remap ctrl+H,J,K,L to move between panes
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-H> <C-W><C-H>
nnoremap <C-L> <C-W><C-L>

" If opening python file remap F9 to run script
autocmd FileType python nnoremap <F9> :exec '!python' shellescape(@%,1)<CR>
autocmd FileType sql vnoremap <F9> :call ExecImpala()<CR>
autocmd FileType sql inoremap <F9> <ESC>:call ExecImpalaAll()<CR>
autocmd FileType sql nnoremap <F9> :call ExecImpalaAll()<CR>

" Turn off swapfile
set noswapfile

" Add line numbering
set nu

" Set leader key
let mapleader = " "

" Quick quit and quit all keys
autocmd FileType * nnoremap <leader>e :qall<cr>
autocmd FileType * nnoremap <leader>q :q<cr>

" Split screen behaviour
set splitbelow
set splitright

" Function to execute impala, range keyword means the function is only
" executed once. Omitting this means it runs for each line in the range with
" a cursor to the line, handy if function need to act seperately on each line
function ExecImpala() range
	:exec "'<,'>w! ~/.impala-exec"
	:silent exec '!perl -i -0pe "s/\/\*.*\*\///s" .impala-exec'
	:silent exec '!perl -i -0pe "s/--.*//g" .impala-exec'
	:exec "!impala-shell -k -i impala.prod-fastda.fjscloud.net:21000 -f ~/.impala-exec -o ~/.impala-res" 
	:exec "sp ~/.impala-res"
endfunction

function ExecImpalaAll() range
	:exec "w! ~/.impala-exec"
	:silent exec '!perl -i -0pe "s/\/\*.*\*\///s" .impala-exec'
	:silent exec '!perl -i -0pe "s/--.*//g" .impala-exec'
	:exec "!impala-shell -k -i impala.prod-fastda.fjscloud.net:21000 -f ~/.impala-exec -o ~/.impala-res" 
	:exec "sp ~/.impala-res"
endfunction

"-------------------File explorer (netrw)-----------------
let g:netrw_liststyle=3
let g:netrw_banner=0
let g:netrw_browse_split=4
let g:netrw_altv=1
let g:netrw_winsize=25

" If this line is uncommented tree view autostarts
"autocmd VimEnter * :Vexplore
autocmd FileType * nnoremap <leader>k :Vexplore<cr>

"Not used but show how functions can be made
"function InitializeTree()
"	Vexplore
"	bw NetrwTreeListing
"	let g:expl_buf_num = bufnr("NetrwTreeListing 1")
"	exec 'e ' . g:expl_buf_num
"endfunction
"
"
"function ToggleTree()
"	if exists("g:expl_buf_num")
"		let expl_win_num = bufwinnr("g:expl_buf_num")
"		exec 'e '. expl_win_num 
"	else
"		exec 'e hello'  
"	endif
"endfunction

"---------------------------------------------------------

"-------------------Auto-indent set to 2------------------
set shiftwidth=2

"-------------------Start Python PEP8 stuff---------------
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h set tabstop=4
au BufRead,BufNewFile *.py,*.pyw set shiftwidth=4
au BufRead,BufNewFile *.py,*.pyw set expandtab
au BufRead,BufNewFile *.py set softtabstop=4

highlight BadWhitespace ctermbg=red guibg=red

au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /^\t\+/
au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /\s\+\s+/
au BufRead,BufNewFile *.py,*.pyw set textwidth=100
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h set fileformat=unix

set encoding=utf-8

let g:ycm_autoclose_preview_window_after_completion=1
let python_highlight_all=1
syntax on

autocmd FileType python set autoindent
set backspace=indent,eol,start

"------------------Impala stuff----------------------------
let g:sql_type_default = 'impala'
autocmd FileType sql setlocal shiftwidth=2 tabstop=2
autocmd FileType sql set autoindent
autocmd FileType sql set nowrap

"------------Full stack development------------------------
"autocmd FileType yaml setlocal shiftwidth=2 tabstop=2
"autocmd FileType javascript setlocal shiftwidth=2 tabstop=2
"autocmd FileType html setlocal shiftwidth=2 tabstop=2
"autocmd FileType css setlocal shiftwidth=2 tabstop=2
au BufRead,BufNewFile *.html,*.css,*.js set tabstop=2 shiftwidth=2
