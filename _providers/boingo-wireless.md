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
  score: 21.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.boingo.com/security
- group: agent
  href: https://artifacts.apis.io/boingo-wireless/well-known/boingo-wireless-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boingo-wireless-well-known.yml
- group: other
  href: https://artifacts.apis.io/boingo-wireless/hosts/boingo-wireless-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boingo-wireless-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boingo.com/terms-of-use-fr/
- group: operate
  title: ''
  type: Support
  url: https://support.boingo.com/s/
- group: auth
  title: ''
  type: Security
  url: https://www.boingo.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boingo.com/privacy-policy-fr/
- group: other
  title: ''
  type: Leadership
  url: https://www.boingo.com/leadership/
- group: auth
  href: https://artifacts.apis.io/boingo-wireless/security/boingo-wireless-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boingo-wireless-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/boingo-wireless/security/boingo-wireless-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boingo-wireless-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boingo.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://my.boingo.com/mcp
  - status: 401
    url: https://support.boingo.com/mcp/v1
  - status: 200
    url: https://www.boingo.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Boingo Wireless designs, builds and operates wireless networks, offering converged 5G, DAS, small cell, Wi‑Fi, private 5G, tower and public‑safety solutions. It provides these services to venues and properties such as airports, sports stadiums, hospitals, military bases, commercial real‑estate and multifamily communities. The company tailors connectivity to the operational needs of each environment to enable reliable, high‑speed wireless access.
image: https://corpsitev2-golden-prod.s3.amazonaws.com/wp-content/uploads/2025/05/Icon-5G-DAS-And-Small-Cells.svg
layout: provider
modified: '2026-10-22'
name: Boingo Wireless
nav: Providers
network: true
overview: 'Boingo Wireless is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Wireless, 5G, DAS, Wi‑Fi, and Venues.


  Boingo Wireless'' developer surface includes support and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boingo Wireless Domain Security
  slug: boingo-wireless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Boingo Wireless Trust Center
  slug: boingo-wireless-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: boingo-wireless
tags:
- Wireless
- 5G
- DAS
- Wi‑Fi
- Venues
- Healthcare
- Military
- Airports
website: https://www.boingo.com/
---
