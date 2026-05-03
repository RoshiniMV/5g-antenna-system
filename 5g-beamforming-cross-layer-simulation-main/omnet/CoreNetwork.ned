simple CoreNetwork
{
    parameters:
        double latency = default(5ms);
        double bandwidth = default(10Gbps);

    gates:
        input in[];
        output out[];
}
