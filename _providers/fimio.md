---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://fimio.xyz/'', ''status'': 302, ''note'': ''declared website redirects to https://www.google.com/ — a different registrable domain (fimio.xyz -> google.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://fimio.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fimio-xyz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fimio
created: '2026-07-17'
description: 'Fimio was a developer-tooling startup founded in 2022 in Oakland, California by Omoju Miller (formerly of Google and GitHub). Its first product was an ML-trained fraud-detection / malicious-smart-contract reputation API for Web3 builders (Ethereum), with data supported by Spice AI, released as an alpha. The company later repositioned around "collaborative tooling for serverful applications" and "reproducible builds made easy." Fimio appears to be defunct: as of the enrichment probe both fimio.xyz and www.fimio.xyz 302-redirect to google.com, the docs/api subdomains do not resolve, the blog returns 404, and the GitHub organization (fimio-xyz) was archived on 2026-01-27 with only Careers and feedback repositories and no published API artifacts. It was backed by a ~$2.19M seed led by Neo with Redpoint Ventures, Protocol Labs, The House Fund and angel investors.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fimio.png
layout: provider
modified: '2026-07-19'
name: Fimio
nav: Providers
network: true
overview: Fimio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Web3, Fraud Detection, and Smart Contracts.
random_paper: 7
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fimio/refs/heads/main/screenshots/fimio-2026-07-25T214459.png
slug: fimio
tags:
- Company
- Developer Tools
- Web3
- Fraud Detection
- Smart Contracts
- Ethereum
- Reproducible Builds
- Defunct
website: https://fimio.xyz/
---
