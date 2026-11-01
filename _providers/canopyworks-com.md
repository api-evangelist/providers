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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference for Canopy Works RTLS platform (no machine-readable spec found)
  name: Canopy Works API
  slug: canopy-works-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/canopyworks-com/well-known/canopyworks-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canopyworks-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/canopyworks-com/hosts/canopyworks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canopyworks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canopyworks-com/vendors/canopyworks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canopyworks-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canopyworks.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.canopyworks.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canopyworks.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.canopyworks.com/news/2026-healthcare-events
- group: docs
  title: ''
  type: Documentation
  url: https://docs.canopyworks.com/
- group: auth
  href: https://artifacts.apis.io/canopyworks-com/security/canopyworks-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canopyworks-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/canopyworks-com/security/canopyworks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canopyworks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.canopyworks.com/
coverage:
  checked: '2026-10-29'
  detail: Docs site renders via JavaScript and no OpenAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://docs.canopyworks.com/
  - status: 0
    url: https://api.canopyworks.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Canopy Works provides a safety‑grade real‑time location system (RTLS) platform for hospitals and health systems. The platform combines discreet hardware buttons, real‑time alerts and integrated service to give staff immediate support and give leaders data for safety decisions. It is deployed across 1,000+ locations protecting more than 350,000 healthcare workers.
image: https://cdn.prod.website-files.com/6834be9610c435d07583a365/685c465af65e42202252a387_cpy_og_img.jpg
layout: provider
modified: '2026-10-29'
name: Canopy
nav: Providers
network: true
overview: 'Canopy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Hospital, RTLS, Staff Safety, and Real‑time Alerts.


  Canopy''s developer surface includes documentation and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canopyworks Com Domain Security
  slug: canopyworks-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canopyworks Com Vulnerability Disclosure
  slug: canopyworks-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: canopyworks-com
tags:
- Healthcare
- Hospital
- RTLS
- Staff Safety
- Real‑time Alerts
- Safety Platform
website: https://www.canopyworks.com/
---
