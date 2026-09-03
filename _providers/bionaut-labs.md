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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bionaut-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bionautlabs.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bionaut-labs
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bionaut-labs_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bionaut-labs-llms.txt
coverage:
  checked: '2026-08-07'
  detail: Bionaut Labs builds a magnetically steered micro-robot drug-delivery device regulated as a medical device, and its entire website now serves the same 790-byte logo placeholder for every path — /newsroom, /team/*, /.well-known/* and /openapi.json all return byte-identical HTML to a nonsense control path — so there is no developer surface, and no documentation surface at all, to read.
  evidence:
  - status: 200
    url: https://www.bionautlabs.com/
  - status: 200
    url: https://bionautlabs.com/.well-known/agent-card.json
  - status: 200
    url: https://bionautlabs.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/bionaut-labs/repos
  - status: 0
    url: https://api.bionautlabs.com/
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: 'Bionaut Labs is a clinical-stage medical robotics company headquartered in Los Angeles, California, developing "Bionauts" — remote-controlled, magnetically steered microscale robots roughly the size of a grain of rice that travel through tissue to deliver drugs, biologics and nucleic acids directly to targets deep in the brain and central nervous system. Founded in 2016 by CEO Michael Shpigelmacher, the company is pursuing treatments for malignant glioma, Dandy-Walker syndrome, Parkinson''s disease and Huntington''s disease, and has raised more than $80 million from investors including Khosla Ventures. Its product is a therapeutic device and navigation platform regulated as a medical device, not software sold to developers: Bionaut Labs operates no public API, developer portal, SDK or machine-readable contract of any kind.'
image: https://www.bionautlabs.com/images/bionaut-logo.svg
layout: provider
modified: '2026-08-07'
name: Bionaut Labs
nav: Providers
network: true
overview: Bionaut Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Robotics, Healthcare, and Biotechnology.
random_paper: 20
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bionaut-labs/refs/heads/main/screenshots/bionaut-labs-2026-08-07T162512.png
security:
- kind: domain-security
  name: Bionaut Labs Domain Security
  slug: bionaut-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bionaut-labs
tags:
- Company
- Medical Devices
- Robotics
- Healthcare
- Biotechnology
- Drug Delivery
- Neurology
- Micro-Robotics
- Life Sciences
website: https://www.bionautlabs.com/
---
