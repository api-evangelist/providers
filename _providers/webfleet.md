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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Vehicle tracking and fleet management API documented at the developer portal.
  name: Webfleet API
  slug: webfleet-api
artifact_total: 2
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.webfleet.com/en_us/webfleet/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.webfleet.com/en_us/webfleet/legal/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.webfleet.com/web
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/webfleet/refs/heads/main/changelog/webfleet-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/webfleet-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/webfleet/refs/heads/main/well-known/webfleet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webfleet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/webfleet/refs/heads/main/hosts/webfleet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webfleet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/webfleet/refs/heads/main/vendors/webfleet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/webfleet-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.webfleet.com/en_us/help/whats-new/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webfleet/refs/heads/main/security/webfleet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webfleet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.webfleet.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.webfleet.com/en_us/webfleet/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.webfleet.com/en_us/webfleet/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.webfleet.com/en_us/webfleet/contact
- group: company
  title: ''
  type: Blog
  url: https://www.webfleet.com/en_us/webfleet/blog/
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL spec found on api.webfleet.com or developers.webfleet.com.
  evidence:
  - status: 401
    url: https://api.webfleet.com/openapi.json
  - status: 404
    url: https://developers.webfleet.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Webfleet provides vehicle tracking and fleet management solutions, offering GPS tracking, driver safety, workflow optimization, compliance, sustainability, and maintenance tools for trucks, vans, cars, and assets. Their platform includes real‑time location, driver coaching, video telematics, route optimization, and integration with various industry services, serving businesses of all sizes across multiple sectors.
image: https://media.webfleet.com/f_auto,q_auto/branding/wf/wf-social.png
layout: provider
modified: '2026-10-13'
name: Webfleet
nav: Providers
network: true
overview: 'Webfleet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, GPS Tracking, Vehicle Telematics, and Logistics.


  Webfleet''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Webfleet Domain Security
  slug: webfleet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: webfleet
tags:
- Company
- Fleet Management
- GPS Tracking
- Vehicle Telematics
- Logistics
website: https://www.webfleet.com
---
