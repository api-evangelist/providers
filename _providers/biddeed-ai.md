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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/biddeed-ai/plans/biddeed-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/biddeed-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/biddeed-ai/llms/biddeed-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biddeed-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/biddeed-ai/well-known/biddeed-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/biddeed-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/biddeed-ai/well-known/biddeed-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biddeed-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/biddeed-ai/hosts/biddeed-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biddeed-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/biddeed-ai/vendors/biddeed-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biddeed-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biddeed.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://biddeed.ai/support
- group: start
  title: ''
  type: SignUp
  url: https://biddeed.ai/sign-up
- group: auth
  title: ''
  type: Security
  url: https://biddeed.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biddeed.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://biddeed.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://biddeed.ai/blog
- group: auth
  href: https://artifacts.apis.io/biddeed-ai/security/biddeed-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/biddeed-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/biddeed-ai/security/biddeed-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biddeed-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biddeed.ai/
coverage:
  checked: '2026-11-02'
  detail: The site provides no public API documentation or machine‑readable contracts.
  evidence:
  - status: 200
    url: https://biddeed.ai/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: BidDeed.AI provides AI‑powered foreclosure and tax deed intelligence across all 67 Florida counties. The platform offers real‑time property record searches, auction forecasts, zoning analysis, and automated alerts for investors and professionals seeking to acquire distressed real‑estate assets.
image: https://biddeed.ai/opengraph-image?42c8d658df92f9dd
layout: provider
modified: '2026-11-02'
name: BidDeed.AI
nav: Providers
network: true
overview: 'BidDeed.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Artificial Intelligence, Foreclosure, TaxDeed, and Florida.


  BidDeed.AI''s developer surface includes support, signup flow, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Biddeed Ai Plans Pricing
  plan_count: 7
  slug: biddeed-ai-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biddeed Ai Domain Security
  slug: biddeed-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Biddeed Ai Vulnerability Disclosure
  slug: biddeed-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: biddeed-ai
tags:
- Real Estate
- Artificial Intelligence
- Foreclosure
- TaxDeed
- Florida
website: https://biddeed.ai/
---
