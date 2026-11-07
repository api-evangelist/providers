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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/conthunt-app/plans/conthunt-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/conthunt-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/conthunt-app/llms/conthunt-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conthunt-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/conthunt-app/well-known/conthunt-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/conthunt-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/conthunt-app/hosts/conthunt-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conthunt-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/conthunt-app/vendors/conthunt-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conthunt-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conthunt.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conthunt.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://conthunt.app/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://conthunt.app/docs
- group: company
  title: ''
  type: Blog
  url: https://conthunt.app/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://conthunt.app/docs/integrations/mcp
- group: auth
  href: https://artifacts.apis.io/conthunt-app/security/conthunt-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conthunt-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conthunt.app/
coverage:
  checked: '2026-11-04'
  detail: Documentation page provides HTML docs but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://conthunt.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: ContHunt helps users discover and analyze viral short-form videos from platforms like TikTok, Instagram, and YouTube using AI. It provides insights into virality patterns, copy winning UGC ads, and download short reels, empowering content creators and marketers to stay ahead of trends.
image: https://conthunt.app/og-default.jpg
layout: provider
modified: '2026-11-04'
name: ContHunt
nav: Providers
network: true
overview: 'ContHunt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Artificial Intelligence, Analytics, and Marketing.


  ContHunt''s developer surface includes pricing, documentation, engineering blog, getting-started guide, and 9 more developer resources.'
plans:
- name: Conthunt App Plans Pricing
  plan_count: 3
  slug: conthunt-app-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Conthunt App Domain Security
  slug: conthunt-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conthunt-app
tags:
- Company
- Video
- Artificial Intelligence
- Analytics
- Marketing
- Social Media
website: https://conthunt.app/
---
