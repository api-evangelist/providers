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
- description: API for Black Forest Labs FLUX models
  name: BFL API
  slug: bfl-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blackforestlabs01de/refs/heads/main/conformance/blackforestlabs01de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blackforestlabs01de-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackforestlabs01de/refs/heads/main/well-known/blackforestlabs01de-bfl-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blackforestlabs01de-bfl-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackforestlabs01de/refs/heads/main/well-known/blackforestlabs01de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blackforestlabs01de-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackforestlabs01de/refs/heads/main/hosts/blackforestlabs01de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackforestlabs01de-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackforestlabs01de/refs/heads/main/vendors/blackforestlabs01de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackforestlabs01de-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackforestlabs01de/refs/heads/main/security/blackforestlabs01de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackforestlabs01de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/blackforestlabs01de
created: '2026-09-29'
description: Black Forest Labs (bfl.ai) is a frontier AI lab offering the FLUX model API. The site provides API documentation and an OpenAPI spec at https://api.bfl.ai/openapi.json.
layout: provider
modified: '2026-09-29'
name: Blackforestlabs01de
nav: Providers
network: true
overview: Blackforestlabs01de publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Data, Artificial Intelligence, and Research.
random_paper: 14
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackforestlabs01De Domain Security
  slug: blackforestlabs01de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blackforestlabs01de
tags:
- Company
- Technology
- Data
- Artificial Intelligence
- Research
website: https://equityzen.com/company/blackforestlabs01de
---
