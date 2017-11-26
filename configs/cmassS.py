import baofast
import math

class cmassS(baofast.configuration):

    def dataDir(self):
        """Directory of catalog files."""
        return 'data/'

    def outputLocation(self):
        return self.dataDir()

    def inputFilesRandom(self):
        return [self.dataDir() + "randoms_DR9_CMASS_South.fits"]

    def inputFilesObserved(self):
        return [self.dataDir() + "galaxies_DR9_CMASS_South.fits"]

    def catalogRandom(self):
        return baofast.wrapRandomSDSS(self.inputFilesRandom(), shiftRA=True)

    def catalogObserved(self):
        return baofast.wrapObservedSDSS(self.inputFilesObserved(), shiftRA=True)

    def binningZ(self): return {"bins":900, "range":(0.43,0.7)}
    def binningRA(self): return {"bins": 2200, "range":(-50,50)}
    def binningDec(self): return {"bins":800, "range":(-10,20)}
    def binningTheta(self): return {"bins":3142, "range":(0,math.pi)}

    def chunkSize(self): return 2000


    '''Configuration affecting only the "integration" routine.'''

    def omegasMKL(self):
        '''Cosmology parameters (\Omega_M, \Omega_K, \Omega_\Lambda).'''
        return (0.274, 0, 0.726)

    def H0(self):
        '''Hubble constant in (h km/s / Mpc)'''
        return 100.

    def lightspeed(self):
        '''Speed of light in km/s'''
        return 299792

    def binningS(self): return {"bins":1200, "range":(0,6000)}
