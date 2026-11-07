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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: CurrencyFair API for international money transfers
  name: CurrencyFair API
  slug: currencyfair-api
- baseURL: https://api.currencyfair.com/
  baseurl_source: declared
  description: The CurrencyFair API from Currencyfair — 209 operation(s) for currencyfair.
  name: Currencyfair Currency Fair API
  slug: currencyfair-currencyfair-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/currencyfair/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/currencyfair/conformance/currencyfair-conformance.yml
  title: ''
  type: Conformance
  url: conformance/currencyfair-conformance.yml
- group: agent
  href: https://artifacts.apis.io/currencyfair/well-known/currencyfair-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/currencyfair-well-known.yml
- group: other
  href: https://artifacts.apis.io/currencyfair/hosts/currencyfair-hosts.yml
  title: ''
  type: Hosts
  url: hosts/currencyfair-hosts.yml
- group: other
  href: https://artifacts.apis.io/currencyfair/vendors/currencyfair-vendors.yml
  title: ''
  type: Vendors
  url: vendors/currencyfair-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.currencyfair.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.currencyfair.com/en-us/trust/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://blog.currencyfair.com/consumer/tag/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.currencyfair.com/trust/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.currencyfair.com/login/login
- group: auth
  href: https://artifacts.apis.io/currencyfair/security/currencyfair-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/currencyfair-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.currencyfair.com
- group: company
  title: ''
  type: Blog
  url: https://blog.currencyfair.com/consumer
- group: operate
  title: ''
  type: Support
  url: https://support.currencyfair.com/s/?language=en_US
- group: docs
  title: ''
  type: Documentation
  url: https://support.currencyfair.com/s/?language=en_US
created: '2026-10-12'
description: Currencyfair is a fintech platform that enables individuals and businesses to send money internationally with lower fees and competitive exchange rates. Founded in 2009, it offers multi‑currency accounts, rate alerts, and integrations such as Xero, facilitating cross‑border payments, tuition fees, property purchases, and payroll. The service operates in over 150 countries, supporting more than 20 currencies, and is authorised as a payment institution.
layout: provider
modified: '2026-10-12'
name: Currencyfair
nav: Providers
network: true
overview: 'Currencyfair is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Currency Fair API, and 1 more. Tagged areas include Company, Fintech, Money Transfer, International Payments, and Foreign Exchange.


  The Currencyfair catalog on APIs.io includes 1 Spectral governance ruleset.


  Currencyfair''s developer surface includes engineering blog, support, documentation, and 12 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Currencyfair API Rules
  rule_count: 59
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 16
  slug: currencyfair-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 45.2
    developer_ergonomics: 14.8
    discoverability: 62.5
    operational_transparency: 5.3
  previous_composite: 35.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/currencyfair/currencyfair-2026-11-03T125912.png
security:
- kind: domain-security
  name: Currencyfair Domain Security
  slug: currencyfair-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: currencyfair
tags:
- Company
- Fintech
- Money Transfer
- International Payments
- Foreign Exchange
website: https://www.currencyfair.com
---
