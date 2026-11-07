---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BetaFinds provides a platform API referenced at https://betafinds.com/api, but no public OpenAPI spec is available.
  name: BetaFinds API
  slug: betafinds-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/betafinds-com/llms/betafinds-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betafinds-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/betafinds-com/well-known/betafinds-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betafinds-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/betafinds-com/hosts/betafinds-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betafinds-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betafinds.com/terms
- group: auth
  title: ''
  type: Security
  url: https://betafinds.com/categories/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betafinds.com/privacy
- group: start
  title: ''
  type: Login
  url: https://betafinds.com/login
- group: auth
  href: https://artifacts.apis.io/betafinds-com/security/betafinds-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betafinds-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betafinds.com/
coverage:
  checked: '2026-11-02'
  detail: No public OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published; only HTML pages are available.
  evidence:
  - status: 404
    url: https://betafinds.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BetaFinds is a platform that discovers, curates, and showcases early-stage startups. Users can browse startup listings, upvote projects, and engage in community discussions. The site provides searchable startup data, categories such as AI, and integrates a sign‑in portal for contributors. It aims to connect founders with early adopters and investors, fostering visibility for emerging companies.
image: https://betafinds.com/opengraph-image
json_schemas:
- name: Betafinds Com Mcp Tools
  property_count: 0
  slug: betafinds-com-mcp-tools
layout: provider
modified: '2026-11-02'
name: BetaFinds
nav: Providers
network: true
overview: BetaFinds is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Startups, Platform, Community, and Discovery.
plans:
- name: Betafinds Com Plans Pricing
  plan_count: 0
  slug: betafinds-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Betafinds Com Rate Limits
  slug: betafinds-com-rate-limits
scopes:
- name: Betafinds Com Scopes
  scope_count: 0
  slug: betafinds-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betafinds Com Authentication
  slug: betafinds-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Betafinds Com Domain Security
  slug: betafinds-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: betafinds-com
tags:
- Company
- Startups
- Platform
- Community
- Discovery
website: https://betafinds.com/
---
