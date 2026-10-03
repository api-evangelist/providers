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
  href: https://raw.githubusercontent.com/api-evangelist/armadaaeronauticsinc/refs/heads/main/hosts/armadaaeronauticsinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/armadaaeronauticsinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/armadaaeronauticsinc/refs/heads/main/vendors/armadaaeronauticsinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/armadaaeronauticsinc-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/armadaaeronauticsinc/refs/heads/main/security/armadaaeronauticsinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/armadaaeronauticsinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://armadaaero.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/armadaaeronauticsinc
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Armada Aeronautics Inc. is a mobility company focused on developing modern transportation solutions for urban and rural environments. It aims to reduce traffic congestion, environmental impact, and fuel waste by offering innovative, accessible, and environmentally friendly transportation technologies. Based in Santa Clara, CA, the company provides solutions that integrate with existing infrastructure and target a $500 billion US market opportunity.
layout: provider
modified: '2026-09-26'
name: Armadaaeronauticsinc
nav: Providers
network: true
overview: Armadaaeronauticsinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Transportation, Urban, and Innovation.
random_paper: 20
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
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
  name: Armadaaeronauticsinc Domain Security
  slug: armadaaeronauticsinc-domain-security
  summary_line: no transport/DNS hardening detected
slug: armadaaeronauticsinc
tags:
- Company
- Mobility
- Transportation
- Urban
- Innovation
website: http://armadaaero.com
---
