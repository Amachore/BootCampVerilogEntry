import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 39.7 ns (~25.175 MHz VGA clock)
    clock = Clock(dut.clk, 39.7, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize control signals
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    
    # Wait for a few cycles while in reset
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    dut._log.info("Reset complete")

    # Let the VGA and audio engine run for a few hundred cycles
    await ClockCycles(dut.clk, 500)
    
    dut._log.info("Test passed successfully!")
