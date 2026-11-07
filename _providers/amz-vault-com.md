---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    agent_skills: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides programmatic access to settlement-accurate Amazon P&L and PPC data.
  name: AMZ Vault API
  slug: amz-vault-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/amz-vault-com/plans/amz-vault-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amz-vault-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/amz-vault-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/amz-vault-com/llms/amz-vault-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amz-vault-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/amz-vault-com/well-known/amz-vault-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amz-vault-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/amz-vault-com/hosts/amz-vault-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amz-vault-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/amz-vault-com/vendors/amz-vault-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amz-vault-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.amz-vault.com/security
- group: start
  title: ''
  type: Login
  url: https://www.amz-vault.com/login
- group: auth
  href: https://artifacts.apis.io/amz-vault-com/security/amz-vault-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amz-vault-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amz-vault.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.amz-vault.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.amz-vault.com/field-guide
- group: operate
  title: ''
  type: Support
  url: https://www.amz-vault.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.amz-vault.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amz-vault.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amz-vault.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amz-vault.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://www.amz-vault.com/docs
coverage:
  checked: '2026-11-01'
  detail: Documentation is publicly available but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://www.amz-vault.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AMZ Vault provides settlement-accurate Amazon profit-and-loss (P&L) reporting and full-funnel PPC management, powered by a native AI connection. The platform offers fee-level drill-down P&L, campaign builder, automation with approval gates, and a flat $49 pricing with no percent-of-spend fees. Users can try the whole platform without signup, access detailed analytics, and manage Amazon advertising efficiently.
image: https://www.amz-vault.com/static/og-demo-today.jpg?v=e4b6a454
layout: provider
modified: '2026-11-01'
name: AMZ Vault
nav: Providers
network: true
overview: 'AMZ Vault is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, E-Commerce, Amazon, PPC, and Artificial Intelligence.


  AMZ Vault''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, API reference, and 12 more developer resources.'
plans:
- name: Amz Vault Com Plans Pricing
  plan_count: 1
  slug: amz-vault-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Amz Vault Com Rate Limits
  slug: amz-vault-com-rate-limits
scopes:
- name: Amz Vault Com Scopes
  scope_count: 0
  slug: amz-vault-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 24.3
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 30.5
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
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
  name: Amz Vault Com Authentication
  slug: amz-vault-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Amz Vault Com Domain Security
  slug: amz-vault-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: amz-vault-alexa-listing-optimizer
  slug: amz-vault-com-amz-vault-alexa-listing-optimizer
- name: amz-vault-alexa-ppc-optimizer
  slug: amz-vault-com-amz-vault-alexa-ppc-optimizer
slug: amz-vault-com
tags:
- Finance
- E-Commerce
- Amazon
- PPC
- Artificial Intelligence
- Software-as-a-Service
website: https://www.amz-vault.com/
---
