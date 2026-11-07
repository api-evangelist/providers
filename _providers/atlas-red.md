---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API providing real‑estate data, listings, permits, and market analytics.
  name: RED Atlas API
  slug: red-atlas-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/atlas-red/plans/atlas-red-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atlas-red-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://atlas.red/notices/security
- group: agent
  href: https://artifacts.apis.io/atlas-red/llms/atlas-red-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlas-red-llms.txt
- group: auth
  href: https://artifacts.apis.io/atlas-red/well-known/atlas-red-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atlas-red-security.txt
- group: auth
  href: https://artifacts.apis.io/atlas-red/well-known/atlas-red-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atlas-red-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/atlas-red/well-known/atlas-red-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atlas-red-app-security.txt
- group: auth
  href: https://artifacts.apis.io/atlas-red/well-known/atlas-red-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atlas-red-api-security.txt
- group: agent
  href: https://artifacts.apis.io/atlas-red/well-known/atlas-red-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlas-red-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlas-red/hosts/atlas-red-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-red-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atlas-red/security/atlas-red-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/atlas-red-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/atlas-red/security/atlas-red-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-red-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlas.red/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atlas.red/en
- group: docs
  title: ''
  type: Documentation
  url: https://api.atlas.red/en/docs?section=credit-costs
- group: docs
  title: ''
  type: APIReference
  url: https://api.atlas.red/en/docs?section=credit-costs
- group: start
  title: ''
  type: GettingStarted
  url: https://atlas.red/en/about
- group: operate
  title: ''
  type: Support
  url: https://atlas.red/en/contact
- group: company
  title: ''
  type: Blog
  url: https://atlas.red/en/pr/news
- group: commercial
  title: ''
  type: Pricing
  url: https://atlas.red/en/pr/pricing
- group: start
  title: ''
  type: SignUp
  url: https://atlas.red/en/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlas.red/en/notices/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlas.red/
coverage:
  checked: '2026-11-02'
  detail: API documentation is publicly available but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://api.atlas.red/en/docs?section=credit-costs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: RED Atlas Inc is Puerto Rico’s most advanced real‑estate data platform, delivering property records, permits, live listings, and market analytics through an AI‑enhanced API. Users can query property details, valuation, and permitting information via natural‑language prompts or direct API calls, with integrations for Claude, ChatGPT, Gemini, and Grok. The service offers free credits, tiered subscription plans, and enterprise options, supporting developers, brokers, lenders, and government agencies.
image: https://atlas.red/landing/logos/atlas-api.svg
layout: provider
modified: '2026-11-01'
name: RED Atlas Inc
nav: Providers
network: true
overview: 'RED Atlas Inc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Puerto Rico, Data Platform, AI Integration, and Property Records.


  RED Atlas Inc''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Atlas Red Plans Pricing
  plan_count: 5
  slug: atlas-red-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Atlas Red Rate Limits
  slug: atlas-red-rate-limits
scopes:
- name: Atlas Red Scopes
  scope_count: 0
  slug: atlas-red-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 35.3
  provenance:
    conformance: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlas Red Authentication
  slug: atlas-red-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atlas Red Domain Security
  slug: atlas-red-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Atlas Red Vulnerability Disclosure
  slug: atlas-red-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: atlas-red
tags:
- Real Estate
- Puerto Rico
- Data Platform
- AI Integration
- Property Records
website: https://atlas.red/
---
