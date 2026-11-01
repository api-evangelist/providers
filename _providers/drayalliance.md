---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/drayalliance/hosts/drayalliance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drayalliance-hosts.yml
- group: other
  href: https://artifacts.apis.io/drayalliance/vendors/drayalliance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drayalliance-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.drayalliance.com/
- group: auth
  href: https://artifacts.apis.io/drayalliance/security/drayalliance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drayalliance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drayalliance.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.drayalliance.com/about-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drayalliance.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drayalliance.com/shipper-tos
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.drayalliance.com
  - status: 403
    url: https://equityzen.com/company/drayalliance
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Drayalliance provides a technology platform that simplifies drayage logistics for shippers and carriers. Their solution offers real‑time container visibility, automated appointment scheduling, cost‑saving rate negotiations, and end‑to‑end management of drayage operations. By integrating directly with port terminals and offering API access, they enable customers to track shipments, reduce demurrage and detention fees, and improve overall supply‑chain predictability.
layout: provider
modified: '2026-10-24'
name: Drayalliance
nav: Providers
network: true
overview: 'Drayalliance publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Drayage, Supply Chain, API, and Transportation.


  Drayalliance''s developer surface includes documentation and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Drayalliance Domain Security
  slug: drayalliance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drayalliance
tags:
- Logistics
- Drayage
- Supply Chain
- API
- Transportation
website: https://www.drayalliance.com
---
