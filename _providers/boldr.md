---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://shopboldr.com/
- group: company
  title: ''
  type: Blog
  url: https://shopboldr.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://shopboldr.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shopboldr.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shopboldr.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/boldr-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boldr-domain-security.yml
created: '2026-07-17'
description: Boldr is a Techstars-backed consumer hardware company building energy-saving smart home climate control devices. Its two products are Kelvin, a smart infrared heater, and Klima, a smart thermostat controller for mini-split air conditioners that also monitors appliance health so units last longer with fewer issues. Both devices are managed through the Boldr mobile app, which lets homeowners control climate settings remotely and track energy usage to lower utility bills. Boldr also runs Boldr Pro, a program for HVAC contractors. The company sells direct to consumers through a Shopify-hosted online store at shopboldr.com and does not currently publish a first-party developer API; its only public machine-readable surface is the Shopify Customer Account OIDC discovery served at the storefront host.
image: https://shopboldr.com/cdn/shop/files/Shopify_1200x1200.jpg?v=1726039985
layout: provider
modified: '2026-07-18'
name: Boldr
nav: Providers
network: true
overview: 'Boldr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, Energy, Climate Control, and IoT.


  Boldr''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boldr/refs/heads/main/screenshots/boldr-2026-08-07T162705.png
security:
- kind: domain-security
  name: Boldr Domain Security
  slug: boldr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boldr
tags:
- Company
- Smart Home
- Energy
- Climate Control
- IoT
- Consumer Hardware
- Thermostat
- HVAC
- E-Commerce
website: https://shopboldr.com/
---
