from dataclasses import dataclass
import background as bg
import numpy as np

@dataclass
class distanceParms:
    """
    Class that computes distance measures from the given input parameters.
    """

    redshift: float
    H0: float
    ΩM: float
    ΩDE: float
    ΩR: float
    w0: float
    wa: float

    def comovingDistance(self) -> float:
        return bg.comoving_distance(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                    self.ΩR, self.w0, self.wa)

    def transverseComovingDistance(self) -> float:
        return bg.transverse_comoving_distance(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                    self.ΩR, self.w0, self.wa)

    def angularDiameterDistance(self) -> float:
        return bg.angular_diameter_distance(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                    self.ΩR, self.w0, self.wa)

    def luminosityDistance(self) -> float:
        return bg.luminosity_distance(self.redshift, self.H0, self.ΩM, self.ΩDE,
                                      self.ΩR, self.w0, self.wa)

    def comovingVolume(self) -> float:
        return 1e-9*bg.comoving_volume(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                       self.ΩR, self.w0, self.wa)
    
    def properSeparation(self) -> float:
        return bg.proper_separation(180/3600/np.pi, self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                    self.ΩR, self.w0, self.wa)

    def lookbackTime(self) -> float:
        return bg.lookback_time(self.redshift, self.H0, self.ΩM, self.ΩDE, 
                                self.ΩR, self.w0, self.wa)

