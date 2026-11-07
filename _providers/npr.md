---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 2
  name: Npr Agentic Access
  operation_count: 18
  slug: npr-agentic-access
  summary_line: 18 operations · 12 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Audio recommendations tailored to a user's preferences.
  name: NPR Listening
  slug: listening
- baseURL: https://listening.api.npr.org/
  baseurl_source: declared
  description: The Authorization API from NPR — 4 operation(s) for authorization.
  name: NPR Authorization API
  slug: npr-authorization-api
- baseURL: https://listening.api.npr.org/
  baseurl_source: declared
  description: The Identity API from NPR — 3 operation(s) for identity.
  name: NPR Identity API
  slug: npr-identity-api
- baseURL: https://listening.api.npr.org/
  baseurl_source: declared
  description: The Stationfinder API from NPR — 2 operation(s) for stationfinder.
  name: NPR Stationfinder API
  slug: npr-stationfinder-api
artifact_total: 15
collections:
- collection_type: open
  name: NPR Identity Service Authorization API
  slug: open-npr-authorization-api
- collection_type: open
  name: NPR Service Authorization Identity API
  slug: open-npr-identity-api
- collection_type: open
  name: NPR Identity Service Authorization Stationfinder API
  slug: open-npr-stationfinder-api
common:
- group: commercial
  href: https://artifacts.apis.io/npr/plans/npr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/npr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/npr/rate-limits/npr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/npr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/npr/finops/npr-finops.yml
  title: ''
  type: FinOps
  url: finops/npr-finops.yml
- group: other
  href: https://artifacts.apis.io/npr/capabilities/npr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/npr-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/npr/agentic-access/npr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/npr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/npr/security/npr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/npr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/npr/authentication/npr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/npr-authentication.yml
- group: auth
  href: https://artifacts.apis.io/npr/scopes/npr-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/npr-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/npr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/npr
- group: company
  title: ''
  type: Website
  url: https://www.npr.org/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.npr.org/
created: '2024-04-14'
description: National Public Radio (NPR) APIs. The APIs support station finding, authentication, user management, and listening with audio recommendations tailored to a user's preferences.
finops:
- has_sources: true
  method: generated
  name: Npr Finops
  primary_unit: request
  service_category: Media / Public Broadcasting
  slug: npr-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/npr.png
layout: provider
modified: '2026-05-19'
name: NPR
nav: Providers
network: true
overview: 'NPR publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Listening, Authorization API, Identity API, and 1 more. Tagged areas include Media, News, and Radio.


  The NPR catalog on APIs.io includes 1 Spectral governance ruleset.


  NPR''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Npr Plans Pricing
  plan_count: 1
  slug: npr-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Npr Rate Limits
  slug: npr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: NPR API Rules
  rule_count: 64
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 4
  slug: npr-rules
scopes:
- name: Npr Scopes
  scope_count: 5
  slug: npr-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 47.6
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 7.9
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/npr/npr-2026-06-20T190453.png
security:
- kind: authentication
  name: Npr Authentication
  slug: npr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Npr Domain Security
  slug: npr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: npr
tags:
- Media
- News
- Radio
website: https://www.npr.org/
---
