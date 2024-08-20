import os
from pathlib import Path

from cocotb.runner import get_runner


def test_clock_runner():
    sim = os.getenv("SIM", "verilator")

    proj_path = Path(__file__).resolve().parent

    sources = [proj_path / "counter.sv"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="counter",
    )

    runner.test(hdl_toplevel="counter", test_module="test_counter,")


if __name__ == "__main__":
    test_clock_runner()
