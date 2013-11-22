#!/bin/tcsh

cd /afs/cern.ch/user/p/pellicci/scratch0/DPG/Upgrade/CMSSW_5_3_8/src/UserCode/DTDPGAnalysis/test
cmsenv

set infilearray=`eos ls -lh /eos/cms/store/caf/user/pellicci/DPG/MiniDAQReco/ | awk '{print $9}'`

touch processedNtupleRuns.txt

foreach runnumber ($infilearray)

echo "Processing file" $runnumber

grep -q "$runnumber" processedNtupleRuns.txt

if ($? == 0) then

 echo "File already processed!"

else

 cp dtTTreeGeneratorTest_TEMPLATE_cfg.py dtTTreeGeneratorTest_TMP_cfg.py

 set outfile = `echo $runnumber`

 set instring = "s/INPUTNAME/"$runnumber"/g"
 set outstring = "s/OUTPUTNAME/"$outfile"/g"

 sed -i $instring dtTTreeGeneratorTest_TMP_cfg.py
 sed -i $outstring dtTTreeGeneratorTest_TMP_cfg.py

 echo $runnumber >> processedNtupleRuns.txt

cmsRun dtTTreeGeneratorTest_TMP_cfg.py

eos cp /tmp/$outfile /eos/cms/store/caf/user/pellicci/DPG/MiniDAQNtuples/$outfile

endif


end


echo "Done!"
