library('miniCRAN')

imperial <-c(CRAN = 'https://cran.ma.imperial.ac.uk/')
pkgs <- unique(read.csv('pkgs.txt', header = FALSE, stringsAsFactors = FALSE)$V1)

pkgList <- pkgDep(pkgs, repos = imperial, type = "source", suggests = FALSE)
pkgList
dir.create(pth <- file.path('/data', "miniCRAN"))
pth
makeRepo(pkgList, path = pth, repos = imperial, type = c("source"))
