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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avalonholographics/refs/heads/main/hosts/avalonholographics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avalonholographics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avalonholographics/refs/heads/main/vendors/avalonholographics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avalonholographics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avalonholographics/refs/heads/main/security/avalonholographics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avalonholographics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/avalonholographics
coverage:
  checked: 2026-09-26
  detail: The company website returns a JavaScript shell and cannot be rendered to extract API information.
  evidence:
  - status: 202
    url: http://www.avalonholographics.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avalonholographics is a technology company that focuses on holographic display solutions and related services. It was initially added to the API Evangelist network as a stub from secondary-market harvesting, and is slated for full profiling in the pipeline. The company aims to provide advanced holographic imaging for various applications, though detailed public information is currently limited.
layout: provider
modified: '2026-09-26'
name: Avalonholographics
nav: Providers
network: true
overview: Avalonholographics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Holography, Displays, Imaging, Technology, and Startups.
random_paper: 10
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avalonholographics Domain Security
  slug: avalonholographics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avalonholographics
tags:
- Holography
- Displays
- Imaging
- Technology
- Startups
- Company
website: https://equityzen.com/company/avalonholographics
---
