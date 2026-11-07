---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    error_semantics: documented
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
  score: 24.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arithym provides a precision math engine accessible via an MCP endpoint. The API requires an API key and OAuth authentication.
  name: Arithym MCP
  slug: arithym-mcp
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/arithym-xyz/rate-limits/arithym-xyz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arithym-xyz-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arithym-xyz/plans/arithym-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arithym-xyz-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/arithym-xyz/authentication/arithym-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arithym-xyz-authentication.yml
- group: design
  href: https://artifacts.apis.io/arithym-xyz/errors/arithym-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arithym-xyz-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/arithym-xyz/well-known/arithym-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arithym-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/arithym-xyz/hosts/arithym-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arithym-xyz-hosts.yml
- group: auth
  href: https://artifacts.apis.io/arithym-xyz/security/arithym-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arithym-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arithym.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://arithym.xyz/docs.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arithym.xyz/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arithym.xyz/legal/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arithym-io
coverage:
  checked: '2026-11-02'
  detail: API requires authentication via OAuth to access the MCP endpoint, preventing contract discovery.
  evidence:
  - status: 200
    url: https://arithym.xyz/.well-known/oauth-protected-resource
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Arithym is a precision math engine and verified scientific reference for AI agents. One connected tool covers everything from basic arithmetic to physics simulations — 209 methods across 22 domains, backed by a curated knowledge base of 981 entries, including 79 CODATA 2022 physics constants with SI dimensional metadata, all 118 elements, 385 exact unit definitions, 52 engineering materials, and 30 exact trigonometric values including radical expressions. One tool call, exact answer, zero token waste.
image: https://arithym.xyz/logo.svg
layout: provider
modified: '2026-11-01'
name: Arithym
nav: Providers
network: true
overview: 'Arithym is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Math, Precision, Engineering, and Science.


  Arithym''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Arithym Xyz Plans Pricing
  plan_count: 4
  slug: arithym-xyz-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Arithym Xyz Rate Limits
  slug: arithym-xyz-rate-limits
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 34.2
  previous_composite: 26.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arithym Xyz Authentication
  slug: arithym-xyz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arithym Xyz Domain Security
  slug: arithym-xyz-domain-security
  summary_line: TLSv1.3
slug: arithym-xyz
tags:
- Artificial Intelligence
- Math
- Precision
- Engineering
- Science
website: https://arithym.xyz/
---
