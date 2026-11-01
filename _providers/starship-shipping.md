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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: StarShip provides shipping services; the developer portal is at dev.starshipme.com but no machine‑readable API contract was found.
  name: StarShip Shipping API
  slug: starship-shipping-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/starship-shipping/hosts/starship-shipping-hosts.yml
  title: ''
  type: Hosts
  url: hosts/starship-shipping-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://starshipme.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://starshipme.com/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://starshipme.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://starshipme.com/account/login/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.starshipme.com/
- group: auth
  href: https://artifacts.apis.io/starship-shipping/security/starship-shipping-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/starship-shipping-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://starshipme.com/
coverage:
  checked: '2026-10-27'
  detail: The developer portal pages are rendered HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dev.starshipme.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: 'StarShip is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-27'
name: StarShip
nav: Providers
network: true
overview: 'StarShip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Carrier Rates, and Discounted Shipping.


  StarShip''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Starship Shipping Domain Security
  slug: starship-shipping-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starship-shipping
tags:
- Shipping
- Carrier Rates
- Discounted Shipping
website: https://starshipme.com/
---
