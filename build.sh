RELEASE=MeleeQuickMod
VERSION=`python3 -c 'import version; print(version.VERSION.strip())'`
rm -rf $RELEASE
mkdir -p $RELEASE/mods
echo "./meleequickmod.py -h" > $RELEASE
cp meleequickmod.py $RELEASE/
cp gcm.py $RELEASE/
cp fs_helpers.py $RELEASE/
rm -rf meleequickmod_linux_$VERSION.zip
zip -r meleequickmod_linux_$VERSION.zip $RELEASE
rm -rf $RELEASE
