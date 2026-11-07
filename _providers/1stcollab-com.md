---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/1stcollab-com/vendors/1stcollab-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1stcollab-com-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/1stcollab-com/plans/1stcollab-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/1stcollab-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/1stcollab-com/well-known/1stcollab-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/1stcollab-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/1stcollab-com/well-known/1stcollab-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1stcollab-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/1stcollab-com/hosts/1stcollab-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1stcollab-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.1stcollab.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://help.1stcollab.com/
- group: auth
  href: https://artifacts.apis.io/1stcollab-com/security/1stcollab-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1stcollab-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1stcollab.com/
- group: company
  title: ''
  type: Blog
  url: https://www.1stcollab.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.1stcollab.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.1stcollab.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1stcollab.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.1stcollab.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://www.1stcollab.com/
coverage:
  checked: '2026-10-31'
  detail: 1stCollab does not provide a public API or developer program.
  evidence:
  - status: 200
    url: https://1stcollab.com/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: 1stCollab is an AI‑powered influencer marketplace that connects creators, brands, and managers in a fully automated, performance‑optimized platform. It offers tools for creators to monetize, for brands to discover and run campaigns, and for managers to oversee collaborations. The service provides a web app at app.1stcollab.com with login and signup, and positions itself as the world’s only fully automated influencer marketplace.
image: https://framerusercontent.com/images/zwdZse1dbN974QQxYpFwV2AvBmA.png
layout: provider
modified: '2026-10-31'
name: 1stCollab
nav: Providers
network: true
overview: '1stCollab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Influencer Marketing, Artificial Intelligence, Marketplace, Software-as-a-Service, and Social Media.


  1stCollab''s developer surface includes support, documentation, engineering blog, pricing, signup flow, getting-started guide, and 9 more developer resources.'
plans:
- name: 1Stcollab Com Plans Pricing
  plan_count: 3
  slug: 1stcollab-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: 1Stcollab Com Rate Limits
  slug: 1stcollab-com-rate-limits
scopes:
- name: 1Stcollab Com Scopes
  scope_count: 0
  slug: 1stcollab-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 28.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 1Stcollab Com Authentication
  slug: 1stcollab-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 1Stcollab Com Domain Security
  slug: 1stcollab-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 1stcollab-com
tags:
- Influencer Marketing
- Artificial Intelligence
- Marketplace
- Software-as-a-Service
- Social Media
website: https://1stcollab.com/
---
