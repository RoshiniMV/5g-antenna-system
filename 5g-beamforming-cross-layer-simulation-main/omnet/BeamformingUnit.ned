simple BeamformingUnit
{
    parameters:
        int antennas = default(64);
        double steeringAngle = default(30);

    gates:
        input in;
        output out;
}
