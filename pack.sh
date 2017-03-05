#!/bin/sh

idx="LuaNginxModule.docset/Contents/Resources/Documents/index.html"
echo "cp"
cp -vf Documents/index.html $idx
cp -vf docSet.dsidx LuaNginxModule.docset/Contents/Resources/docSet.dsidx

echo "sed"
sed -i "" -e "s/README.markdown - Grip/Lua Nginx Module/g" $idx
sed -i "" -e "s/README.markdown/Lua Nginx Module/g" $idx

echo "tar"
tar zcf LuaNginxModule.tgz LuaNginxModule.docset
