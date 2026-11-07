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
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Branchly API provides endpoints for embedding AI tools and analytics.
  name: Branchly API
  slug: branchly-api
artifact_total: 4
asyncapis:
- description: ''
  name: Branchly Io Webhooks
  slug: branchly-io-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/branchly-io/plans/branchly-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/branchly-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/branchly-io/asyncapi/branchly-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/branchly-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/branchly-io/conformance/branchly-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/branchly-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/branchly-io/llms/branchly-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/branchly-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/branchly-io/well-known/branchly-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branchly-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/branchly-io/hosts/branchly-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branchly-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/branchly-io/vendors/branchly-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branchly-io-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://branchly.io/news
- group: company
  title: ''
  type: Blog
  url: https://branchly.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.branchly.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.branchly.io/public/docs
- group: auth
  href: https://artifacts.apis.io/branchly-io/security/branchly-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branchly-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branchly.io/
created: '2026-11-02'
description: branchly provides an AI layer for websites, enabling visitors to get answers within seconds and turning every question into valuable insights. It offers a conversational AI interface that integrates with website content, delivering real-time responses, analytics, and conversion optimization tools for businesses seeking to enhance user engagement and support.
image: https://branchly.io/cdn-cgi/image/width=1200,height=630,fit=crop,format=jpeg,background=%23FDFCFC/https://branchly.io/_astro/hero_dashboard.BUV7hMSL.png
layout: provider
modified: '2026-11-02'
name: branchly
nav: Providers
network: true
overview: 'branchly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Conversational AI, Analytics, Website Optimization, and Customer Engagement.


  The branchly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  branchly''s developer surface includes engineering blog, documentation, API reference, and 10 more developer resources.'
plans:
- name: Branchly Io Plans Pricing
  plan_count: 4
  slug: branchly-io-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 9.5
    discoverability: 67.0
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Branchly Io Domain Security
  slug: branchly-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: branchly-io
tags:
- Artificial Intelligence
- Conversational AI
- Analytics
- Website Optimization
- Customer Engagement
- Company
website: https://branchly.io/
---
