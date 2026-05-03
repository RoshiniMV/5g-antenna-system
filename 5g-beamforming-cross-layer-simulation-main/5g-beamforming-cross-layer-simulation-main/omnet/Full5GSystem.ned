package roshini;

import ned.DatarateChannel;

network Full5GSystem
{
    parameters:
        int numUE = default(50);

    submodules:

        gnb: gNB {
            parameters:
                numAntennas = 64;
                txPower = 40;
        }

        scheduler: Scheduler;
        phy: PHYLayer;
        mac: MACLayer;
        mobility: MobilityManager;

        ue[numUE]: UE {
            parameters:
                mobility = true;
                speed = uniform(5,20);
        }

    connections allowunconnected:

        for i=0..numUE-1 {
            ue[i].out --> WirelessChannel --> gnb.in++;
            gnb.out++ --> WirelessChannel --> ue[i].in;
        }
}
