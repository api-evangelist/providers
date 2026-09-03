---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/csr-biotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://csr-biotech.com
created: '2026-07-17'
description: CSR Biotech (超视计 / Chaoshiji) is a Chinese life-sciences instrumentation company that develops super-resolution optical microscopy systems for advanced biological research. Its product line includes the HIS-SIM and MI-SIM structured-illumination microscopes and the SIM-Ultimate platform, delivering live-cell imaging down to roughly 60nm resolution across many imaging modes. The company was surfaced as a portfolio company of Qiming Venture Partners and added to the API Evangelist network as a stub. As a scientific-instruments maker, CSR Biotech publishes no public developer portal, documentation, or API surface at this time; this profile captures its identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/csr-biotech.png
layout: provider
modified: '2026-07-18'
name: CSR Biotech
nav: Providers
network: true
overview: CSR Biotech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Microscopy, Super-Resolution Imaging, Life Sciences, and Scientific Instruments.
random_paper: 15
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/csr-biotech/refs/heads/main/screenshots/csr-biotech-2026-07-25T210839.png
security:
- kind: domain-security
  name: Csr Biotech Domain Security
  slug: csr-biotech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: csr-biotech
tags:
- Company
- Microscopy
- Super-Resolution Imaging
- Life Sciences
- Scientific Instruments
- Biotechnology
website: https://csr-biotech.com
---
