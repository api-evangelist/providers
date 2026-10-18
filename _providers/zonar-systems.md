---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Fleet management API (no public documentation found)
  name: Zonar API
  slug: zonar-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zonar-systems/refs/heads/main/well-known/zonar-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zonar-systems-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zonar-systems/refs/heads/main/hosts/zonar-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zonar-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zonar-systems/refs/heads/main/vendors/zonar-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zonar-systems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zonar.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zonar.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://partnernetwork.zonar.com/User/Login
- group: other
  title: ''
  type: Leadership
  url: https://www.zonar.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.zonar.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zonar-systems/refs/heads/main/security/zonar-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zonar-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zonar.com
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the API host (https://api.zonar.com/openapi.json returned 0 bytes).
  evidence:
  - status: 0
    url: https://api.zonar.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Zonar provides fleet management technology that improves safety, efficiency, and compliance for transportation companies. Their platform includes telematics, driver tools, predictive maintenance, fuel analytics, and a marketplace of third‑party apps. Zonar serves industries such as construction, utilities, and vocational fleets, offering solutions like asset tracking, dash‑cam video, and electronic logging devices. The company emphasizes safety, regulatory compliance, and operational insight for fleets of all sizes.
layout: provider
modified: '2026-10-13'
name: Zonar Systems
nav: Providers
network: true
overview: 'Zonar Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, Telematics, Safety, and Compliance.


  Zonar Systems'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zonar Systems Domain Security
  slug: zonar-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zonar-systems
tags:
- Company
- Fleet Management
- Telematics
- Safety
- Compliance
website: https://www.zonar.com
---
