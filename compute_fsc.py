from emda.core import iotools, restools, fsc, plotter
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker


### set plot properties#####

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['figure.figsize'] = 3.5,2.75
params = {'legend.fontsize': 6,
          'legend.handlelength': 2}


plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.fancybox'] = True
mpl.rcParams['axes.linewidth'] = 0.3

mpl.rcParams['axes.labelsize'] = 8
mpl.rcParams['xtick.labelsize'] = 6
mpl.rcParams['ytick.labelsize'] = 6
mpl.rcParams['xtick.major.width'] = 0.3
mpl.rcParams['ytick.major.width'] = 0.3
mpl.rcParams['xtick.minor.width'] = 0.3
mpl.rcParams['ytick.minor.width'] = 0.3
mpl.rcParams['xtick.major.size'] = 2
mpl.rcParams['ytick.major.size'] = 2
mpl.rcParams['xtick.minor.size'] = 1 # half of the major ticks length
mpl.rcParams['ytick.minor.size'] = 1

plt.rcParams.update(params)

colors={"FF99SB":"#66CCEE","FF99SB-disp":"#AA3377","FF14SB":"#4477AA","FF19SB":"#228833","IDPSFF":"#BBBBBB","target":"#fe6100"}



####################################



def plot_nlines(
    res_arr,
    fsc_arr,
    mapname="FSC_mapname",
    fscline=0.143 #fsc threshold for precision estimate
):
 

        
    bin_arr = np.arange(len(res_arr))
 
    fig, ax = plt.subplots()
    
    ax.plot(bin_arr, fsc_arr, linewidth=0.8, color="#AA3377")    
    ax.axhline(y=fscline, ls='dashed', lw =0.5, color='k',label='FSC = 0.143')
   
   
    pos = np.array(ax.get_xticks(), dtype=np.int)
    n_bins = res_arr.shape[0]
   
    
    pos = np.delete(pos, np.where(pos <0))
    pos = np.delete(pos, np.where(pos > n_bins))
 
    
    label_format = '{:5.1f}'
    ax.xaxis.set_major_locator(mticker.FixedLocator(pos))
    ax.set_xticklabels([label_format.format(res_arr[x]) for x in pos])


    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("precision [$\AA$]")
    plt.legend(loc=0)
    plt.ylabel("Fourier Shell Correlation")
    leg=ax.legend(loc='best',frameon=1,framealpha=0.7)
    
    ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
    fig.tight_layout()
    fig.savefig(mapname+'.png',dpi=600, transparent=True)
    plt.savefig(mapname+'.svg', transparent=True)
    plt.close(fig)



###########################################
# P:\Lif\LIF_synthetic_data\figures\2022-07\Figure_8\FourierShellCorr\case-I\FF14SB\L-corner\th0.400_L-BFGS-B_ref_15
# truth
uc, ar1, org = iotools.read_map('3D_density_map_h1.mrc')
uc, ar2, org = iotools.read_map('3D_density_map_h2.mrc')
hf1 = np.fft.fftshift(np.fft.fftn(ar1)) # Fourier transform of half maps
hf2 = np.fft.fftshift(np.fft.fftn(ar2))
nbin, res_arr, bin_idx = restools.get_resolution_array(uc,hf1)
bin_fsc,_,_,_,_,_ = fsc.halfmaps_fsc_variance(hf1,hf2,bin_idx,nbin)

res_fsc=np.column_stack([res_arr, bin_fsc])
np.savetxt('FSC_mapname.txt', res_fsc, delimiter='\t', header='precision[A]    FSC',fmt='%.3f')
plot_nlines(res_arr,bin_fsc)
