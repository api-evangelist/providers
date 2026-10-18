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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celltivity-scientific/refs/heads/main/hosts/celltivity-scientific-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celltivity-scientific-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celltivity-scientific/refs/heads/main/vendors/celltivity-scientific-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celltivity-scientific-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.celltivity.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.celltivity.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.celltivity.com/news
- group: start
  title: ''
  type: Login
  url: https://www.celltivity.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celltivity-scientific/refs/heads/main/security/celltivity-scientific-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celltivity-scientific-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.celltivity.com
coverage:
  checked: '2026-10-07'
  detail: The company provides only a marketing website with no developer program or public API documentation.
  evidence:
  - status: 200
    url: https://www.celltivity.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: CellTivity Scientific is a medical technology company developing point‑of‑care biopsy imaging tools for cancer diagnostics. Their Van Gogh™ system provides real‑time metabolic imaging of fresh biopsy tissue, enabling clinicians to assess sample adequacy instantly and improve diagnostic yield. Founded in 2025 and rebranded from Aquyre Biosciences, the firm aims to accelerate cancer detection and streamline pathology workflows.
image: https://cdn.prod.website-files.com/6758866482544aeba0adc14d/68c0c425a2ca1619cbc60376_7f8ca94918848b6a288fc41d10b726f2_CellTivity%20Scientific%20Open%20Graph.jpg
layout: provider
modified: '2026-10-07'
name: CellTivity Scientific
nav: Providers
network: true
overview: CellTivity Scientific is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Technology, CancerDiagnostics, BiopsyImaging, RealTimeImaging, and Metabolism.
random_paper: 21
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Celltivity Scientific Domain Security
  slug: celltivity-scientific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celltivity-scientific
tags:
- Medical Technology
- CancerDiagnostics
- BiopsyImaging
- RealTimeImaging
- Metabolism
website: https://www.celltivity.com
---
