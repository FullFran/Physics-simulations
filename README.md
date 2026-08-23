# Physics-simulations — archived

Coursework simulations from *Diseño de nuevos materiales* (master's, 2024).
This repo is read-only. The parts worth keeping are being rewritten from the
equations in [first-principles](https://github.com/FullFran/first-principles).

| Folder | Status |
|---|---|
| `Cristal_multicapa/` | **Rewritten** → [`first-principles/tmm`](https://github.com/FullFran/first-principles/tree/main/tmm) |
| `Iter_rad_material/` | Queued — photon transport by ray tracing |
| `Magnetic Mirrors/` | Queued — charged particle in a magnetic bottle |

## Known defects in `Cristal_multicapa/funciones.py`

Recorded on purpose, because the failures teach more than the code does.

| Probe | This repo | Correct |
|---|---|---|
| Air → glass, single interface | R = 0.000000 | 0.04 |
| Absorbing film at 30° | A = −0.247579 | 0 < A < 1 |
| Glass → air past the critical angle | nan | 1.0 |

`multicapa()` hardcodes `n[0]` as the exit medium, so the substrate index is
silently discarded. `snell_law()` goes through `np.arcsin`, which can
represent neither a complex angle nor an angle past total internal reflection.

All three broken cases still satisfied R + T = 1 to six decimals. Energy
conservation is necessary and nowhere near sufficient — that lesson is why the
rewrite was worth doing, and the corrected version ships with 45 property
tests covering exactly these cases.
