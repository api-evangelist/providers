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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides programmatic access to CheapChat's comment automation features. Documentation is available on the pricing page, but no machine‑readable contract was found.
  name: CheapChat API
  slug: cheapchat-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cheapchat-tech/plans/cheapchat-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cheapchat-tech-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cheapchat-tech/llms/cheapchat-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cheapchat-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/cheapchat-tech/well-known/cheapchat-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cheapchat-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/cheapchat-tech/hosts/cheapchat-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cheapchat-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/cheapchat-tech/vendors/cheapchat-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cheapchat-tech-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cheapchat.tech/terms-of-service?lang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cheapchat.tech/privacy-policy?lang=en
- group: commercial
  title: ''
  type: Pricing
  url: https://cheapchat.tech/pricing
- group: start
  title: ''
  type: Login
  url: https://app.cheapchat.tech/login
- group: auth
  href: https://artifacts.apis.io/cheapchat-tech/security/cheapchat-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cheapchat-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cheapchat.tech/
coverage:
  checked: '2026-11-04'
  detail: Provider docs are public but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec could be found.
  evidence:
  - status: 200
    url: https://cheapchat.tech/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CheapChat helps sellers turn Instagram and Facebook comments into automated direct messages, building comment and keyword automations, managing conversations, and offering a free starter plan. The platform streamlines social media engagement for businesses, enabling private replies and workflow automation without requiring a credit card to begin.
image: https://cheapchat.tech/og.jpeg
layout: provider
modified: '2026-11-04'
name: CheapChat
nav: Providers
network: true
overview: 'CheapChat is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Messaging, Instagram Automation, Facebook Automation, Comment to DM, and Visual Builder.


  CheapChat''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Cheapchat Tech Plans Pricing
  plan_count: 5
  slug: cheapchat-tech-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cheapchat Tech Domain Security
  slug: cheapchat-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cheapchat-tech
tags:
- Social Messaging
- Instagram Automation
- Facebook Automation
- Comment to DM
- Visual Builder
- No-Code Automation
website: https://cheapchat.tech/
---
