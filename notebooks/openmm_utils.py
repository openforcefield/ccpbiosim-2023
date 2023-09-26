import openmm
import openmm.unit
from openff.interchange import Interchange


def run_openmm(
    interchange: Interchange,
    reporter_frequency: int = 100,
    trajectory_name="preview.dcd",
):
    simulation = interchange.to_openmm_simulation(
        integrator=openmm.LangevinIntegrator(
            300 * openmm.unit.kelvin,
            1 / openmm.unit.picosecond,
            0.002 * openmm.unit.picoseconds,
        ),
    )

    dcd_reporter = openmm.app.DCDReporter(trajectory_name, reporter_frequency)
    simulation.reporters.append(dcd_reporter)

    simulation.context.setVelocitiesToTemperature(300 * openmm.unit.kelvin)
    simulation.runForClockTime(1.0 * openmm.unit.minute)
