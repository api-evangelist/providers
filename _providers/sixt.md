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
    dynamic_client_registration: false
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
  score: 14.4
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: API for Sixt mobility services, providing endpoints for rentals, reservations, and fleet management.
  name: Sixt API
  slug: sixt-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/security/sixt-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sixt-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/well-known/sixt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sixt-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/hosts/sixt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sixt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/vendors/sixt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sixt-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/packages/sixt-packages.yml
  title: ''
  type: SDKs
  url: packages/sixt-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/packages/sixt-packages.yml
  title: ''
  type: Packages
  url: packages/sixt-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sixt.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.sixt.com/help-center/
- group: start
  title: ''
  type: SignUp
  url: https://www.sixt.com/business/register/?register_type=signup&product_type=undefined
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sixt.com/pages/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://about.sixt.com/en/newsroom/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sixt.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sixt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/security/sixt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sixt-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sixt/refs/heads/main/security/sixt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sixt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sixt.com/
coverage:
  checked: 2026-09-23
  detail: Developer documentation page returns empty content, likely JS-rendered without a machine-readable spec.
  evidence:
  - status: 200
    url: https://developers.sixt.com/app/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Sixt is a global mobility services provider offering car rental, ride‑hailing, and subscription services. With a heritage spanning over a century, Sixt operates in more than 110 countries, delivering premium vehicles and flexible booking options through its website and mobile apps. The company emphasizes digital transformation, providing customers with online reservations, fleet management, and a range of mobility solutions tailored to business and leisure travelers.
image: https://img.sixt.com/1200/506112ab-1eaf-40fd-b7ab-ef2dfef01cd5.jpg
layout: provider
modified: '2026-09-23'
name: Sixt
nav: Providers
network: true
overview: 'Sixt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Car Rental, Ride Hailing, and Subscription.


  Sixt''s developer surface includes support, signup flow, documentation, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 58.9
    operational_transparency: 15.8
  previous_composite: 19.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sixt Domain Security
  slug: sixt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sixt Vulnerability Disclosure
  slug: sixt-vulnerability-disclosure
  summary_line: Bugcrowd
slug: sixt
tags:
- Company
- Mobility
- Car Rental
- Ride Hailing
- Subscription
website: https://sixt.com/
---
