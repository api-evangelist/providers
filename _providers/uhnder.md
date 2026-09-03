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
  type: Website
  url: https://www.uhnder.com/
- group: other
  title: ''
  type: Products
  url: https://www.uhnder.com/products/
- group: auth
  title: ''
  type: Compliance
  url: https://www.uhnder.com/quality
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uhnder.com/site/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uhnder.com/site/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: mailto:info@uhnder.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uhnder
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/uhnder_stock/
- group: design
  title: ''
  type: Conformance
  url: conformance/uhnder-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uhnder-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uhnder-domain-security.yml
coverage:
  checked: '2026-08-05'
  detail: Uhnder's S80/S81 product briefs advertise an "ASPICE Qualified SDK with Ready-to-Integrate APIs", but the SDK is only obtainable through a commercial automotive customer relationship — the products page offers no download, registration or documentation link, only info@uhnder.com, and every candidate developer host (developer./docs./api./portal./sdk.uhnder.com) is NXDOMAIN.
  evidence:
  - status: 200
    url: https://www.uhnder.com/products/
  - status: 200
    url: https://www.uhnder.com/images/data/S81_PTB_v1.0_(1)_.pdf
  - status: 404
    url: https://www.uhnder.com/openapi.json
  - status: 404
    url: https://www.uhnder.com/llms.txt
  - status: 404
    url: https://www.uhnder.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/uhnder
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: 'Uhnder is an Austin, Texas fabless semiconductor company founded in 2015 that designs the S80 and S81 77 GHz 4D digital imaging Radar-on-Chip (RoC) for automotive ADAS and automated mobility. Its Digital Code Modulation (DCM) approach on a 28nm RF CMOS process replaces analog FMCW radar with a software-defined sensor, and each RoC ships with an ASPICE-qualified Software Development Kit carrying ready-to-integrate software APIs, on-chip user algorithm support and system tools for Tier-1 and OEM radar stacks. Uhnder is a chip supplier rather than a web-API provider: the SDK and its APIs are embedded interfaces delivered under a commercial customer relationship, and the company publishes no public developer portal, documentation host or machine-readable API contract.'
image: https://www.uhnder.com/images/data/Uhnder_Logo.svg
layout: provider
modified: '2026-08-05'
name: Uhnder
nav: Providers
network: true
overview: 'Uhnder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Automotive, Radar, and ADAS.


  Uhnder''s developer surface includes support and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.7
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uhnder/refs/heads/main/screenshots/uhnder-2026-09-02T164735.png
security:
- kind: domain-security
  name: Uhnder Domain Security
  slug: uhnder-domain-security
  summary_line: TLSv1.2 · DMARC
slug: uhnder
tags:
- Company
- Semiconductors
- Automotive
- Radar
- ADAS
- Sensors
- Embedded
- Autonomous Vehicles
- Hardware
website: https://www.uhnder.com/
---
