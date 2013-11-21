#!/bin/tcsh

cd ~/scratch0/DPG/Upgrade/MiniDAQReco/CMSSW_5_3_8_patch3/src/UserCode/DTDPGAnalysis/test
cmsenv

set infilearray=`eos ls -lh /eos/cms/store/caf/user/dtdqm/InputMiniDAQRuns/dat/ | awk '{print $9}'`

foreach runnumber ($infilearray)

echo "Processing file" $runnumber

grep -q "$runnumber" processedDAQruns.txt

if ($? == 0) then

 echo "File already processed!"

else

 cp RecoMiniDAQ_cfg.py RecoMiniDAQ_TMP_cfg.py

 set outfile = `echo $runnumber | sed "s/dat/root/g"`

 set instring = "s/INPUTNAME/"$runnumber"/g"
 set outstring = "s/OUTPUTNAME/"$outfile"/g"

 sed -i $instring RecoMiniDAQ_TMP_cfg.py
 sed -i $outstring RecoMiniDAQ_TMP_cfg.py

 echo $runnumber >> processedDAQruns.txt

 cmsRun RecoMiniDAQ_TMP_cfg.py

 eos cp /tmp/$outfile /eos/cms/store/caf/user/pellicci/DPG/MiniDAQReco/$outfile

endif


end


echo "Done!"