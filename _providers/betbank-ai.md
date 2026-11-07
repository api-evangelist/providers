---
access_model:
  confidence: medium
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/betbank-ai/plans/betbank-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/betbank-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://betbank.ai/trust
- group: agent
  href: https://artifacts.apis.io/betbank-ai/llms/betbank-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betbank-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/betbank-ai/well-known/betbank-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/betbank-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/betbank-ai/well-known/betbank-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betbank-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/betbank-ai/hosts/betbank-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betbank-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/betbank-ai/vendors/betbank-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betbank-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://betbank.ai/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betbank.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://betbank.ai/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betbank.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://betbank.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://betbank.ai/login
- group: auth
  href: https://artifacts.apis.io/betbank-ai/security/betbank-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/betbank-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/betbank-ai/security/betbank-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betbank-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betbank.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://betbank.ai/api/mcp
  - status: 200
    url: https://betbank.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BetBank provides Australian sports betting analytics, offering positive expected value (EV) bets, arbitrage opportunities, and real‑time odds from over 75 bookmakers. Users can track betting performance with a suite of professional tools, access detailed odds comparison, and leverage advanced analytics to improve wagering strategies across multiple sports.
image: https://betbank.ai/og-image.png
layout: provider
modified: '2026-11-02'
name: BetBank
nav: Providers
network: true
overview: 'BetBank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports Betting, Analytics, Arbitrage, Odds Comparison, and Australian.


  BetBank''s developer surface includes support, pricing, and 14 more developer resources.'
plans:
- name: Betbank Ai Plans Pricing
  plan_count: 2
  slug: betbank-ai-plans-pricing
random_paper: 14
scopes:
- name: Betbank Ai Scopes
  scope_count: 0
  slug: betbank-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betbank Ai Authentication
  slug: betbank-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Betbank Ai Domain Security
  slug: betbank-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Betbank Ai Vulnerability Disclosure
  slug: betbank-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: betbank-ai
tags:
- Sports Betting
- Analytics
- Arbitrage
- Odds Comparison
- Australian
website: https://betbank.ai/
---
