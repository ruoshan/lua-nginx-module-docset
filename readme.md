## How to generate the docset

the index.html in the docset is converted from the github's `readme.markdown`
[file](https://github.com/openresty/lua-nginx-module/blob/master/README.markdown),
you can use the [grip](https://github.com/joeyespo/grip) to do the job.
Invoke this command `grip --export README.markdown; mv README.html index.html`, and you're set.

Use the script `gen.py` to generate the right dosSet.dsidx.

There would be all.
