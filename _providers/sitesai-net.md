---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST API for SitesAI app, providing access to AI connector tools and other resources.
  name: SitesAI REST API
  slug: sitesai-rest-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/sitesai-net/plans/sitesai-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sitesai-net-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/sitesai-net/authentication/sitesai-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sitesai-net-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sitesai-net/scopes/sitesai-net-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sitesai-net-scopes.yml
- group: agent
  href: https://artifacts.apis.io/sitesai-net/llms/sitesai-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sitesai-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/sitesai-net/well-known/sitesai-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sitesai-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/sitesai-net/hosts/sitesai-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sitesai-net-hosts.yml
- group: auth
  href: https://artifacts.apis.io/sitesai-net/security/sitesai-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sitesai-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sitesai.net/
- group: company
  title: ''
  type: Blog
  url: https://sitesai.net/blog
- group: docs
  title: ''
  type: Documentation
  url: https://sitesai.net/blog
- group: start
  title: ''
  type: Login
  url: https://app.sitesai.net/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://sitesai.net/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sitesai.net/privacy
- group: operate
  title: ''
  type: Support
  url: https://sitesai.net/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sitesai.net/terms
coverage:
  checked: '2026-10-30'
  detail: Documentation describes a REST API at /api/ai/v1 but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://sitesai.net/blog/ai-connector-142-tools-and-an-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: SitesAI provides cloud-based estimating and field management software for civil and earthmoving teams in Australia. It enables users to generate cut‑and‑fill calculations from PDF plans, manage crews, equipment, safety compliance, digital dockets, and project quotes, all through a web app and AI‑powered connectors.
image: https://sitesai.net/assets/og-image.png
layout: provider
modified: '2026-10-30'
name: sitesai-net
nav: Providers
network: true
overview: 'sitesai-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Earthworks, Estimating, and Field-Software.


  sitesai-net''s developer surface includes authentication, engineering blog, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Sitesai Net Plans Pricing
  plan_count: 10
  slug: sitesai-net-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Sitesai Net Rate Limits
  slug: sitesai-net-rate-limits
scopes:
- name: Sitesai Net Scopes
  scope_count: 3
  slug: sitesai-net-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sitesai Net Authentication
  slug: sitesai-net-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sitesai Net Domain Security
  slug: sitesai-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sitesai-net
tags:
- Company
- Construction
- Earthworks
- Estimating
- Field-Software
website: https://sitesai.net/
---
