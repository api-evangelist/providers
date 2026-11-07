---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/pax-technology/well-known/pax-technology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pax-technology-well-known.yml
- group: other
  href: https://artifacts.apis.io/pax-technology/hosts/pax-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pax-technology-hosts.yml
- group: other
  href: https://artifacts.apis.io/pax-technology/vendors/pax-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pax-technology-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pax.us/support/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pax.us/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/pax-technology/security/pax-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pax-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pax.us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pax.us/support/developer-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pax.us/support/developer-portal/
- group: operate
  title: ''
  type: Support
  url: https://www.pax.us/support/
- group: company
  title: ''
  type: Blog
  url: https://www.pax.us/about/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pax.us/terms-conditions/
coverage:
  checked: '2026-10-13'
  detail: Developer portal at https://developer.pax.us returns HTML with JavaScript rendering and no machine‑readable spec.
  evidence:
  - status: 200
    url: https://developer.pax.us
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: PAX Technology Inc. designs, manufactures and sells a broad range of point‑of‑sale (POS) terminals, payment solutions and services for merchants worldwide. Their portfolio includes countertop, mobile, unattended and integrated devices, as well as software platforms like PAXSTORE for app development and management. The company focuses on secure, reliable payment technology and supports a global merchant base across retail, hospitality and transportation sectors.
image: https://www.pax.us/wp-content/uploads/2023/03/pax-technology.jpg
layout: provider
modified: '2026-10-13'
name: PAX Technology
nav: Providers
network: true
overview: 'PAX Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Point-of-Sale, Fintech, and Hardware.


  PAX Technology''s developer surface includes documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 15.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pax-technology/pax-technology-2026-11-03T141008.png
security:
- kind: domain-security
  name: Pax Technology Domain Security
  slug: pax-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pax-technology
tags:
- Company
- Payments
- Point-of-Sale
- Fintech
- Hardware
website: https://www.pax.us
---
