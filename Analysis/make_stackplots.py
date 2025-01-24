import os

era = "Run3_2022"
ver = "tau_corr"
indir = f"/eos/user/t/toakhter/HH_bbtautau_Run3/histograms/{ver}/{era}/merged/"
plotdir = f"/eos/user/t/toakhter/HH_bbtautau_Run3/histograms/{ver}/{era}/plots/"

varnames = ["PV_npvs", "tau1_pt", "tau2_pt", "tau1_mass", "tau2_mass"]#["lep1_pt", "lep1_eta", "lep2_pt", "lep2_eta", "bjet1_btagPNetB", "bjet2_btagPNetB"]
channellist = ["eE", "eMu", "muMu", "eTau", "muTau", "tauTau"]

for var in varnames:
    for channel in channellist:
        filename = os.path.join(indir, var, f"{var}.root")#f"tmp/all_histograms_{var}_Central.root")
        print("Loading fname ", filename)
        os.makedirs(plotdir, exist_ok=True)
        outname = os.path.join(plotdir, f"HHbbtautau_{channel}_{var}_StackPlot.pdf")
        os.system(f"python3 HistPlotter.py --inFile {filename} --bckgConfig ../config/HH_bbtautau/{era}/background_samples.yaml --globalConfig ../config/HH_bbtautau/global.yaml --sigConfig ../config/{era}/samples.yaml --outFile {outname} --var {var} --category inclusive --channel {channel} --uncSource Central --wantData True --year {era} --wantQCD False --rebin False --analysis HH_bbtautau --qcdregion OS_Iso")