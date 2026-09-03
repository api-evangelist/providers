---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microbyre
coverage:
  checked: '2026-08-25'
  detail: MicroByre is out of business — microbyre.com publishes no A record and www.microbyre.com is a dangling CNAME to a deleted CloudFront distribution, so nothing of the company's own web surface can be fetched at all.
  evidence:
  - status: 0
    url: https://microbyre.com/
  - status: 0
    url: https://www.microbyre.com/
  - status: 200
    url: https://www.primecoalition.org/investee-library/microbyre
  reason: defunct
  state: none
created: '2026-08-25'
description: 'MicroByre was a Berkeley, California synthetic biology company founded in 2017 by CEO and co-founder Sarah Richardson to "domesticate" wild-type bacteria — building an automated characterization and genetic-tool pipeline that made naturally occurring, never-before-engineered microbes tractable so they could ferment unrefined waste biomass into commodity chemicals, enzymes, food ingredients and probiotics at costs petrochemical routes could not match. It raised roughly $20.5M, including backing from Prime Coalition''s Prime Impact Fund, and went out of business; Prime Coalition lists it as "no longer active" and C&EN reported the shutdown. MicroByre was a wet-lab platform company, not a software vendor: it published no developer program, no API, and no machine-readable contract, and its own domain no longer resolves to a web server.'
layout: provider
modified: '2026-08-25'
name: MicroByre
nav: Providers
network: true
overview: MicroByre is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, Industrial Biotechnology, and Bioengineering.
random_paper: 6
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Microbyre Domain Security
  slug: microbyre-domain-security
  summary_line: no transport/DNS hardening detected
slug: microbyre
tags:
- Company
- Biotechnology
- Synthetic Biology
- Industrial Biotechnology
- Bioengineering
- Climate Tech
- Chemicals
---
