simple gNB
{
    parameters:
        int numAntennas;
        double txPower;
        double frequency = default(28GHz);
        double bandwidth = default(100MHz);

    gates:
        input in[];
        output out[];

    submodules:
        beamformer: BeamformingUnit;
        mac: MACLayer;
        phy: PHYLayer;
}
