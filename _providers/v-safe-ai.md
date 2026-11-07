---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Israeli Company Risk Intelligence API
  name: V-Safe AI API
  slug: v-safe-ai-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/v-safe-ai/plans/v-safe-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/v-safe-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/v-safe-ai/authentication/v-safe-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/v-safe-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/v-safe-ai/errors/v-safe-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/v-safe-ai-problem-types.yml
- group: other
  href: https://artifacts.apis.io/v-safe-ai/hosts/v-safe-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/v-safe-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/v-safe-ai/vendors/v-safe-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/v-safe-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/v-safe-ai/security/v-safe-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/v-safe-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://v-safe.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://v-safe.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://v-safe.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://v-safe.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://v-safe.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://v-safe.ai/get-api-key
- group: commercial
  title: ''
  type: TermsOfService
  url: https://v-safe.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://v-safe.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://v-safe.ai/support
- group: company
  title: ''
  type: Blog
  url: https://v-safe.ai/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://v-safe.ai/roadmap
coverage:
  checked: '2026-10-31'
  detail: API host https://api.v-safe.ai/ redirects to a login page, indicating authentication is required to access the API.
  evidence:
  - status: 302
    url: https://api.v-safe.ai/
  reason: auth-required
  state: gated
created: '2026-10-31'
description: V‑Safe provides a risk‑intelligence API focused on Israeli companies. A single API call returns a 0‑100 risk score with a full evidence trail across eight independent layers, including registry data, insolvency, sanctions, adverse media, cyber hygiene, legal‑entity identity, and market distress. Built for compliance teams and AI agents, the service runs on Israeli‑hosted infrastructure to access government sources that block foreign IPs.
layout: provider
modified: '2026-10-31'
name: v-safe-ai
nav: Providers
network: true
overview: 'v-safe-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Risk Management, Compliance, Israeli, and Artificial Intelligence.


  v-safe-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, support, and 10 more developer resources.'
plans:
- name: V Safe Ai Plans Pricing
  plan_count: 9
  slug: v-safe-ai-plans-pricing
random_paper: 9
scopes:
- name: V Safe Ai Scopes
  scope_count: 0
  slug: v-safe-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 62.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 33.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: V Safe Ai Authentication
  slug: v-safe-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: V Safe Ai Domain Security
  slug: v-safe-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: v-safe-ai
tags:
- Company
- Risk Management
- Compliance
- Israeli
- Artificial Intelligence
website: https://v-safe.ai/
---
