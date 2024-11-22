import os


indir = "/eos/user/t/toakhter/HH_bbtautau_Run3/histograms/HLT/Run3_2022/merged/"

varnames = ["tau1_pt"]#["PV_npvs"]#["lep1_pt", "lep1_eta", "lep2_pt", "lep2_eta", "bjet1_btagPNetB", "bjet2_btagPNetB"]
channellist = ["tauTau"]#["e", "eE", "eMu", "mu", "muMu", "tauTau"]

for var in varnames:
    for channel in channellist:
        filename = os.path.join(indir, var, f"tmp/all_histograms_{var}_Central.root")
        print("Loading fname ", filename)
        outname = f"HHbbtautau_{channel}_{var}_StackPlot.pdf"
        os.system(f"python3 HistPlotter.py --inFile {filename} --bckgConfig ../config/HH_bbtautau/background_samples.yaml --globalConfig ../config/HH_bbtautau/global.yaml --sampleConfig ../config/Run3_2022/samples.yaml --outFile {outname} --var {var} --category inclusive --channel {channel} --uncSource Central --wantData True --year Run3_2022 --wantQCD False --rebin False")