---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer API for managing email domains, mailboxes, tags, analytics, and warmup scores.
  name: Aerosend API
  slug: aerosend-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aerosend-io/plans/aerosend-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aerosend-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aerosend-io/llms/aerosend-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerosend-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/aerosend-io/well-known/aerosend-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aerosend-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aerosend-io/hosts/aerosend-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aerosend-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aerosend-io/vendors/aerosend-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aerosend-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.aerosend.io/signup
- group: auth
  href: https://artifacts.apis.io/aerosend-io/security/aerosend-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerosend-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aerosend.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.aerosend.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aerosend.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerosend.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerosend.io/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.aerosend.io/blog/
created: '2026-10-31'
description: Aerosend provides an email deliverability platform for cold email outreach, offering domain burn alerts, deliverability checking tools, and integrations with cold‑email services. Founded in 2024 by Namit Jindal and Prabhu Rengaswamy, the company builds private infrastructure to improve reply rates and inbox placement for high‑volume campaigns. It offers a suite of tools including domain monitoring, data tools, pricing plans, and a developer API for programmatic access.
image: https://www.aerosend.io/wp-content/uploads/2026/03/aerosend-og-image-1.png
layout: provider
modified: '2026-10-31'
name: Aerosend
nav: Providers
network: true
overview: 'Aerosend is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Deliverability, Cold Email, Software-as-a-Service, and Marketing.


  Aerosend''s developer surface includes signup flow, API reference, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Aerosend Io Plans Pricing
  plan_count: 2
  slug: aerosend-io-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 22.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerosend Io Domain Security
  slug: aerosend-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aerosend-io
tags:
- Email Deliverability
- Cold Email
- Software-as-a-Service
- Marketing
website: https://aerosend.io/
---
