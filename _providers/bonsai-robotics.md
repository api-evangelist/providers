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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Bonsai Robotics provides autonomous farm robot solutions; API documentation is not publicly machine‑readable.
  name: Bonsai Robotics API
  slug: bonsai-robotics-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-robotics/refs/heads/main/hosts/bonsai-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonsai-robotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-robotics/refs/heads/main/vendors/bonsai-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonsai-robotics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bonsai-robotics/refs/heads/main/security/bonsai-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonsai-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-10-02'
  detail: Developer pages return HTML shells and no machine‑readable OpenAPI spec was found despite probing common spec URLs.
  evidence:
  - status: 404
    url: https://bonsairobotics.ai/openapi.json
  - status: 301
    url: https://bonsairobotics.ai/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Bonsai Robotics is a full‑stack physical AI company building the intelligence layer for autonomous machines in rugged, off‑road environments. It offers vision‑based automation solutions for agriculture, mining, construction and other sectors, enabling autonomous vehicles and equipment to operate without GPS or cellular connections.
layout: provider
modified: '2026-10-02'
name: Bonsai Robotics
nav: Providers
network: true
overview: Bonsai Robotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 10
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonsai Robotics Domain Security
  slug: bonsai-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bonsai-robotics
tags:
- Company
website: https://www.nasdaqprivatemarket.com/
---
