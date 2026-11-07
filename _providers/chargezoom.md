---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/chargezoom/plans/chargezoom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chargezoom-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/chargezoom/well-known/chargezoom-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chargezoom-well-known.yml
- group: other
  href: https://artifacts.apis.io/chargezoom/hosts/chargezoom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chargezoom-hosts.yml
- group: other
  href: https://artifacts.apis.io/chargezoom/vendors/chargezoom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chargezoom-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.chargezoom.com/
- group: auth
  href: https://artifacts.apis.io/chargezoom/security/chargezoom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargezoom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chargezoom.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chargezoom.com/developer-resources
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chargezoom.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.chargezoom.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.chargezoom.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chargezoom.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chargezoom.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chargezoom.com/privacy-policy
coverage:
  checked: '2026-10-08'
  detail: Chargezoom's documentation pages return HTML and no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found.
  evidence:
  - status: 404
    url: https://api.chargezoom.com/openapi.json
  - status: 404
    url: https://www.chargezoom.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chargezoom provides an AI‑powered autonomous accounts receivable (AR) platform that automates the entire invoice‑to‑cash cycle. Their solution combines AR outreach, payment processing, and customer portal features into a single graph‑based system, reducing manual work and exceptions for enterprises. With integrations for major accounting software, credit‑card vaults, and recurring billing, Chargezoom helps businesses accelerate cash flow, improve collection rates, and deliver a seamless payment experience for both B2B and B2C customers.
image: https://cdn.prod.website-files.com/67d327cda5426471be9ac016/67fedf3cf84d192cf458371d_chargezoom.com.jpg
layout: provider
modified: '2026-10-08'
name: Chargezoom
nav: Providers
network: true
overview: 'Chargezoom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Automation, and Artificial Intelligence.


  Chargezoom''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Chargezoom Plans Pricing
  plan_count: 3
  slug: chargezoom-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 24.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chargezoom/chargezoom-2026-11-03T123857.png
security:
- kind: domain-security
  name: Chargezoom Domain Security
  slug: chargezoom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chargezoom
tags:
- Company
- Fintech
- Payments
- Automation
- Artificial Intelligence
website: https://www.chargezoom.com/
---
