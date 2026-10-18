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
  href: https://raw.githubusercontent.com/api-evangelist/cellino-biotech/refs/heads/main/hosts/cellino-biotech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellino-biotech-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellino-biotech/refs/heads/main/vendors/cellino-biotech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cellino-biotech-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cellinobio.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cellinobio.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellino-biotech/refs/heads/main/security/cellino-biotech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellino-biotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cellinobio.com/
coverage:
  checked: '2026-10-07'
  detail: No public API documentation or developer program is available on the company's website.
  evidence:
  - status: 200
    url: https://cellinobio.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cellino Biotech is a regenerative medicine company focused on personalized cell therapies using advanced iPSC technology. It offers a platform for patient-specific tissue and organ replacement, leveraging AI-driven bioprocessing to scale autologous treatments for a range of degenerative diseases.
layout: provider
modified: '2026-10-07'
name: Cellino Biotech
nav: Providers
network: true
overview: Cellino Biotech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Regenerative Medicine, Cell Therapy, and Artificial Intelligence.
random_paper: 3
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cellino Biotech Domain Security
  slug: cellino-biotech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cellino-biotech
tags:
- Company
- Biotechnology
- Regenerative Medicine
- Cell Therapy
- Artificial Intelligence
website: https://cellinobio.com/
---
