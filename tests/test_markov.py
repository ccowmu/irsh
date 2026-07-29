import os
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
MARKOV = ROOT / "bin" / "markov"

PERC_LINES = """\
Popped a Perc 30, got straight to fuckin'
We smokin' Serge Ibaka, spinal fluid infused, quick-release Percs
Blacked out on the Percocet, ordered a Desert Eagle off Amazon
Lil' bro was emaciated, the Percs done ate lil' cuzzo ass up
If this watch breaks, the foreign exchange market will take a twenty-eight percent hit, people will die
Slurpin' a quick-release Perc off the plate, like a pinto bean
Turns out I'm one-hundred percent Him-alayan
I have more Percs than there are stars in the Leo Cluster
I need my percs!
I need my percs!
One perc is never enough (Yo!)
I knew the perc was fake
Unholy doses of Percocet and Hennessy got me shitting in the bed more than the Oakland A's
Percs put me on the wrong side of history almost every time
That perc eating my ass up
Ah, I remember when I took my first perc
"""


class MarkovTests(unittest.TestCase):
    def test_small_filtered_corpus_does_not_collapse_to_one_result(self):
        outputs = set()
        env = os.environ | {"PYTHONPATH": str(ROOT)}

        for _ in range(20):
            result = subprocess.run(
                [MARKOV],
                cwd=ROOT,
                env=env,
                input=PERC_LINES,
                text=True,
                capture_output=True,
                check=True,
            )
            outputs.add(result.stdout.strip())

        self.assertGreaterEqual(len(outputs), 3)


if __name__ == "__main__":
    unittest.main()
