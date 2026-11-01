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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/compass-inc/hosts/compass-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compass-inc-hosts.yml
- group: auth
  href: https://artifacts.apis.io/compass-inc/security/compass-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compass-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cmpsinc.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.cmpsinc.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Compass, Inc. provides advisory, assistance, and system engineering and integration services to U.S. defense and intelligence customers. Headquartered in Winchester, VA, the company delivers lifecycle management, technical services, and solutions supporting national defense missions. It focuses on intelligence, operations, business, and technology solutions for government and business partners.
layout: provider
modified: '2026-10-23'
name: Compass, Inc.
nav: Providers
network: true
overview: Compass, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defense, Intelligence, Advisory, and Engineering.
random_paper: 13
score:
  band: minimal
  composite: 3.1
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
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compass Inc Domain Security
  slug: compass-inc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: compass-inc
tags:
- Company
- Defense
- Intelligence
- Advisory
- Engineering
website: https://www.cmpsinc.com/
---
