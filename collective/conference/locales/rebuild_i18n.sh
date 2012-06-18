#!/bin/sh

PRODUCTNAME='collective.conference'
I18NDOMAIN=$PRODUCTNAME

# List of languages
#LANGUAGES="es fr pt pt-br it"
LANGUAGES="es"

I18NDUDE=i18ndude

#EXCLUDEPOTPLONEFILE=`find ./content ./Extensions -name "*.*py"; find ../profiles/default/types -name "*.xml"`
EXCLUDEPOTPLONEFILE=`find ../profiles/default/types -name "*.xml"`

rm ./rebuild_i18n.log

#[[ ! -f $I18NDUDE ]] && I18NDUDE=i18ndude
#echo using $I18NDUDE

#if test ! -e $I18NDUDE; then
#        echo "You must install i18ndude with buildout"
#        echo "See https://github.com/collective/collective.developermanual/tree/master/source/i18n/localization.txt"
#        exit
#fi

#
# Do we need to merge manual PO entries from a file called manual.pot.
# this option is later passed to i18ndude
#
if test -e ../locales/manual.pot; then
        echo "Manual PO entries detected"
        MERGE="--merge ../locales/manual.pot"
else
        echo "No manual PO entries detected"
        MERGE=""
fi

# Create locales folder structure for languages
#install -d locales
for lang in $LANGUAGES; do
    install -d ./$lang/LC_MESSAGES
    touch ./$lang/LC_MESSAGES/${PRODUCTNAME}.po
done

# Synchronise the .pot with the templates.
$I18NDUDE rebuild-pot --pot ./${PRODUCTNAME}.pot $MERGE --create ${I18NDOMAIN} ../

# Synchronise the resulting .pot with the .po files
$I18NDUDE sync --pot ./${PRODUCTNAME}.pot ./*/LC_MESSAGES/${PRODUCTNAME}.po

# Synchronise the .pot with the templates.
$I18NDUDE rebuild-pot --pot ./plone.pot --create plone ../profiles/default/workflows --exclude=$EXCLUDEPOTPLONEFILE

# Synchronise the resulting .pot with the .po files
#$I18NDUDE sync --pot ./plone.pot ./*/LC_MESSAGES/plone.po

WARNINGS=`find ../ -name "*pt" | xargs $I18NDUDE find-untranslated | grep -e '^-WARN' | wc -l`
ERRORS=`find ../ -name "*pt" | xargs $I18NDUDE find-untranslated | grep -e '^-ERROR' | wc -l`
FATAL=`find ../ -name "*pt"  | xargs $I18NDUDE find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo "There are $WARNINGS warnings (possibly missing i18n markup)"
echo "There are $ERRORS errors (almost definitely missing i18n markup)"
echo "There are $FATAL fatal errors (template could not be parsed, eg. if it\'s not html)"
echo "For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or" 
echo "Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir" 

touch ./rebuild_i18n.log

find ../ -name "*pt" | xargs $I18NDUDE find-untranslated > ./rebuild_i18n.log
