import matplotlib.pyplot as plt

def plot_distances_lin(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height):
        
        '''
        Plot the calculated distances as a function of redshift in a linear scale.
        '''
        
        fig, ax = plt.subplots(figsize=(width, height))
        
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(width=3)
        ax.tick_params(axis='both', labelsize=12)

        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
   
        if plot_rz:
            ax.plot(z_array, rz_array, label='Comoving Distance', color=colors['gray'], ls='-', lw=3)
        if plot_trz:
            ax.plot(z_array, trz_array, label='Transverse Comoving Distance', color=colors['gray'], ls='-.', lw=3)
        if plot_DLz:
            ax.plot(z_array, DLz_array, label='Luminosity Distance', color=colors['gray'], ls='--', lw=3)
        if plot_DAz:
            ax.plot(z_array, DAz_array, label='Angular Diameter Distance', color=colors['gray'], ls=':', lw=3)

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Distance [Mpc]', size=15)
        
        return fig


def plot_distances_log(plot_rz, plot_trz, plot_DLz, plot_DAz, z_array, rz_array, trz_array, DLz_array, DAz_array, width, height):
        
        '''
        Plot the calculated distances as a function of redshift in a semi-log scale.
        '''
        
        fig, ax = plt.subplots(figsize=(width, height))
        
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(axis='both', labelsize=12, width=3, colors=colors['orange'])
        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
       
        if plot_rz:
            ax.plot(z_array, rz_array, label='Comoving Distance', color=colors['gray'], ls='-', lw=3)
        if plot_trz:
            ax.plot(z_array, trz_array, label='Transverse Comoving Distance', color=colors['gray'], ls='-.', lw=3)
        if plot_DLz:
            ax.plot(z_array, DLz_array, label='Luminosity Distance', color=colors['gray'], ls='--', lw=3)
        if plot_DAz:
            ax.plot(z_array, DAz_array, label='Angular Diameter Distance', color=colors['gray'], ls=':', lw=3)

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Distance [Mpc]', size=15)
        
        ax.set_yscale('log')
        ax.spines['left'].set_color(colors['orange'])
        ax.yaxis.label.set_color(colors['orange'])

        ax.tick_params(axis='y', colors=colors['orange'], width=1.5, which='both')
      
        return fig


def plot_comoving_volume_lin(plot_VCz, z_array, VCz_array, width, height):
        
        '''
        Plot the calculated comoving volume as a function of redshift in a linear scale.
        '''
        
        fig, ax = plt.subplots(figsize=(width, height))
        
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(width=3)
        ax.tick_params(axis='both', labelsize=12)

        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
   
        if plot_VCz:
            ax.plot(z_array, VCz_array, label='Comoving Volume', color=colors['gray'], ls='-', lw=3)
        

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Comoving Volume [$\mathrm{Gpc^3}$]', size=15)
        
        return fig

def plot_comoving_volume_log(plot_VCz, z_array, VCz_array, width, height):
        
        '''
        Plot the calculated comoving volume as a function of redshift in a semi-log scale.
        '''
        
        fig, ax = plt.subplots(figsize=(width, height))
        
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(width=3)
        ax.tick_params(axis='both', labelsize=12)

        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
   
        if plot_VCz:
            ax.plot(z_array, VCz_array, label='Comoving Volume', color=colors['gray'], ls='-', lw=3)
        

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Comoving Volume [$\mathrm{Gpc^3}$]', size=15)
        
        ax.set_yscale('log')
        ax.spines['left'].set_color(colors['orange'])
        ax.yaxis.label.set_color(colors['orange'])

        ax.tick_params(axis='y', colors=colors['orange'], width=1.5, which='both')
        
        return fig


def plot_lookback_time_lin(plot_tlz, z_array, tlz_array, width, height):
        
        '''
        Plot the calculated lookback time as a function of redshift in a linear scale.
        '''
        
        fig, ax = plt.subplots(figsize=(width, height))
        
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(width=3)
        ax.tick_params(axis='both', labelsize=12)

        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
   
        if plot_tlz:
            ax.plot(z_array, tlz_array, label='Lookback Time', color=colors['gray'], ls='-', lw=3)
        

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Lookback Time [$\mathrm{Gyr}$]', size=15)
        
        return fig

def plot_lookback_time_log(plot_tlz, z_array, tlz_array, width, height):
        
        '''
        Plot the calculated lookback time as a function of redshift in a semi-log scale.
        '''
        
        fig, ax = plt.subplots(figsize=(width, height))
        
        colors = {
         'orange' : '#ffc345',
         'gray' : '#333333',
         'white' : '#FFFFFF',
        }
        
        ax.spines['bottom'].set_color(colors['orange'])
        ax.spines['top'].set_color(colors['orange']) 
        ax.spines['right'].set_color(colors['orange'])
        ax.spines['left'].set_color(colors['orange'])

        ax.tick_params(axis='x', colors=colors['orange'])
        ax.tick_params(axis='y', colors=colors['orange'])

        ax.yaxis.label.set_color(colors['orange'])
        ax.xaxis.label.set_color(colors['orange'])
        
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(3)

        ax.tick_params(width=3)
        ax.tick_params(axis='both', labelsize=12)

        ax.set_facecolor(colors['white'])
        fig.patch.set_facecolor(colors['white'])
   
        if plot_tlz:
            ax.plot(z_array, tlz_array, label='Lookback Time', color=colors['gray'], ls='-', lw=3)
        

        legend = plt.legend(frameon = 1)
        plt.setp(legend.get_texts(), color=colors['gray'])
        frame = legend.get_frame()
        frame.set_facecolor(colors['white'])
        frame.set_edgecolor(colors['white'])

        ax.set_xlabel('Redshift', size=15)
        ax.set_ylabel('Lookback Time [$\mathrm{Gyr}$]', size=15)
        
        ax.set_yscale('log')
        ax.spines['left'].set_color(colors['orange'])
        ax.yaxis.label.set_color(colors['orange'])

        ax.tick_params(axis='y', colors=colors['orange'], width=1.5, which='both')
        
        return fig
