import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, Timer
from cocotb.clock import Clock


async def tick(dut):
    await FallingEdge(dut.clk)

async def start_clock(dut):
    cocotb.start_soon(Clock(dut.clk, 2, units="ns").start())
    dut.rst.value = 1
    await tick(dut)
    dut.rst.value = 0


@cocotb.test()
async def test_reset(dut):
    await start_clock(dut)

    await tick(dut)
    assert dut.out.value == 1, "counter is 1 after increment"

    dut.rst.value = 1
    await tick(dut)

    dut._log.info("counter is %s", dut.out.value)
    assert dut.out.value == 0, "counter isn't zero after reset!"


@cocotb.test()
async def test_increment(dut):
    await start_clock(dut)

    assert dut.out.value == 0, "counter starts with 0"
    await tick(dut)
    assert dut.out.value == 1, "counter is 1 after increment"
    await tick(dut)
    assert dut.out.value == 2, "counter is 2 after increment"


@cocotb.test()
async def test_overflow(dut):
    await start_clock(dut)

    for i in range(15):
        dut._log.info("counter is %s", dut.out.value)
        await tick(dut)
    
    assert dut.out.value == 15, "counter is 15"

    await tick(dut)
    assert dut.out.value == 0, "counter overflows to 0"
