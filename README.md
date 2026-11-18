# tariff-pricing-engine

Batch pricing engine for phone + SIM-only plans: 24-month total cost of ownership (TCO), cashback and
Pareto filtering, served through a fast search API.

## Problem

Comparison platforms combine thousands of phones with thousands of SIM-only plans. Every combination has
a different 24-month cost (device price, monthly fee, discounted months, activation fee, cashback), and
users expect filtered results in well under 100 ms. Computing millions of combinations per request is
too slow, so this project separates the work into two parts:

1. **Batch pricing**: compute and rank all combinations ahead of time with Polars.
2. **Serving**: answer filtered searches from precomputed, indexed results via FastAPI.

## Status

| Milestone | Scope | Status |
|---|---|---|
| M0 | Project skeleton, tooling, CI | in progress |
| M1 | Domain models and synthetic data generator | planned |
| M2 | Pricing core: 24-month TCO, property-based tests | planned |
| M3 | Batch pricing with Polars, Pareto filtering, benchmark | planned |
| M4 | Postgres storage and Docker Compose | planned |
| M5 | Search API and load test | planned |
| M6 | Architecture decision records, known limitations | planned |

## Development

Requires [uv](https://docs.astral.sh/uv/) and Python 3.13+.

```bash
uv sync               # install dependencies
uv run pytest         # run tests
uv run ruff check .   # lint
uv run mypy src tests # type check
```

## License

MIT
