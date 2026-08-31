---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-26'
  detail: The Pathway Genomics brand was retired after OME Ventures acquired the renamed Pathway OME on 2021-01-25 and rebranded it OME Wellness, and the company's own 2008 domain pathwaygenomics.com now sits on Afternic nameservers serving a GoDaddy for-sale parking lander that answers HTTP 200 with the identical 114-byte redirect stub for every path — including /openapi.json and every /.well-known/ path — while its own parked llms.txt states the domain is listed for sale.
  evidence:
  - status: 200
    url: https://www.pathwaygenomics.com/
  - status: 307
    url: https://www.pathwaygenomics.com/lander
  - status: 200
    url: https://www.pathwaygenomics.com/llms.txt
  - status: 200
    url: https://www.pathwaygenomics.com/openapi.json
  - status: 200
    url: https://www.pathwaygenomics.com/.well-known/agent-card.json
  - status: 200
    url: https://www.pathwaygenomics.com/definitely-not-a-real-path-xyz123
  - status: 404
    url: https://api.github.com/orgs/pathwaygenomics
  - status: 302
    url: https://pathwayfit.com/
  - status: 200
    url: https://omewellness.com/
  - status: 403
    url: https://forgeglobal.com/pathway-genomics_stock/
  reason: defunct
  state: none
created: '2026-08-26'
description: Pathway Genomics Corporation was a San Diego, California clinical laboratory and consumer genetics company, incorporated in 2008 and operating a CLIA-certified, CAP-accredited lab at 6777 Nancy Ridge Drive. It sold DNA-based tests direct to consumers and through clinicians, including the PathwayFit diet-and-fitness panel, SkinFit, Cardiac DNA Insight, the Mental Health DNA Insight and Pain Medication DNA Insight pharmacogenomics panels, the BRCATrue and ColoTrue hereditary cancer-risk tests, and the CancerIntercept Detect and Monitor liquid biopsy assays. Its planned 2010 over-the-counter retail launch drew FDA scrutiny, the FDA wrote to the company in September 2015 over its marketing of CancerIntercept Detect, and in December 2015 it agreed to pay roughly $4M to settle US False Claims Act kickback allegations. IBM's Watson Group invested in the company in 2014, and at CES in January 2016 the two debuted OME, a Watson-powered consumer genomic wellness app. The company later
  renamed itself Pathway OME; on 2021-01-25 its assets were acquired by investor OME Ventures amid customer complaints and rebranded as OME Wellness, which today trades as a medical weight-loss brand rather than a genomics business. Pathway Genomics never published a developer program, public API, SDK, CLI, or machine-readable specification. Its original 2008 domain pathwaygenomics.com is now delegated to Afternic nameservers and serves a GoDaddy aftermarket parking lander offering the domain for sale, so it is deliberately not wired as a Website pointer. This profile is retained as a historical record; there is no API surface to enrich.
layout: provider
modified: '2026-08-26'
name: Pathway Genomics
nav: Providers
network: true
overview: Pathway Genomics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Genetic Testing, Clinical Laboratory, and Precision Medicine.
random_paper: 5
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 1
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: pathway-genomics
tags:
- Company
- Genomics
- Genetic Testing
- Clinical Laboratory
- Precision Medicine
- Consumer Health
- Pharmacogenomics
- Liquid Biopsy
- Diagnostics
- Healthcare
- Life Sciences
- Defunct
- Acquired
---
