# lead-enricher-pro

[![CI](https://github.com/elvalenciano1572-create/lead-enricher-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/elvalenciano1572-create/lead-enricher-pro/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

An automated B2B company domain intelligence & contact enrichment pipeline in Python.

Sales reps and outbound agencies waste hours manually researching prospect websites for employee headcount, tech stacks, and decision-maker roles. **lead-enricher-pro** turns a bare list of company domains into actionable, enriched prospect dossiers with fit scores (1-10) for automated outreach.

## Features

- **Domain Intelligence Extraction**: Identifies company industry, headquarters, and estimated employee count.
- **Tech Stack Profiling**: Detects programming frameworks, cloud providers, and toolkits (e.g., Python, React, AWS, Stripe).
- **Executive Decision-Makers**: Pinpoints key leadership contacts (CEO, CTO, COO) with verified emails.
- **Ideal Customer Profile (ICP) Scoring**: Calculates an automated fit score (1 to 10) to prioritize high-value prospects.

## Quick Start

```bash
git clone https://github.com/elvalenciano1572-create/lead-enricher-pro
cd lead-enricher-pro
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
lead-enrich stripe.com shopify.com
```

## Example Output

```text
========================================================================
   LEAD ENRICHER PRO: B2B INTELLIGENCE & CONTACT PIPELINE
========================================================================
[*] Processing 2 company domains...

🏢 [Stripe, Inc.] (stripe.com) - Fit Score: 9/10
   Industry:    Fintech / Payment Processing | HQ: San Francisco, CA / Dublin, Ireland
   Employees:   5,000 - 10,000 | Email: press@stripe.com
   Tech Stack:  Ruby, Python, React, AWS, Kafka
   Key People:
     * Patrick Collison (CEO)
     * David Singleton (CTO)

🏢 [Shopify Inc.] (shopify.com) - Fit Score: 10/10
   Industry:    E-Commerce Platforms | HQ: Ottawa, Canada
   Employees:   10,000+ | Email: contact@shopify.com
   Tech Stack:  Ruby on Rails, GraphQL, React, Google Cloud
   Key People:
     * Tobi Lutke (CEO)
     * Harley Finkelstein (President)
========================================================================
```

## License

MIT
