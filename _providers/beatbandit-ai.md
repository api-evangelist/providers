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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BeatBandit provides AI-powered beat generation services.
  name: BeatBandit API
  slug: beatbandit-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/beatbandit-ai/plans/beatbandit-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beatbandit-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/beatbandit-ai/well-known/beatbandit-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beatbandit-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/beatbandit-ai/hosts/beatbandit-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beatbandit-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/beatbandit-ai/vendors/beatbandit-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beatbandit-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://beatbandit.ai/mcp/support
- group: commercial
  title: ''
  type: Pricing
  url: https://beatbandit.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://beatbandit.ai/sign-in
- group: auth
  href: https://artifacts.apis.io/beatbandit-ai/security/beatbandit-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beatbandit-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beatbandit.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://beatbandit.ai/mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beatbandit.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beatbandit.ai/privacy
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://beatbandit.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'beatbandit-ai is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://beatbandit.ai/social-preview.png
layout: provider
modified: '2026-11-02'
name: BeatBandit
nav: Providers
network: true
overview: 'BeatBandit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Screenwriting, AI Writing Assistant, and Screenplay Formatting.


  BeatBandit''s developer surface includes support, pricing, documentation, and 9 more developer resources.'
plans:
- name: Beatbandit Ai Plans Pricing
  plan_count: 3
  slug: beatbandit-ai-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beatbandit Ai Domain Security
  slug: beatbandit-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beatbandit-ai
tags:
- Screenwriting
- AI Writing Assistant
- Screenplay Formatting
website: https://beatbandit.ai/
---
