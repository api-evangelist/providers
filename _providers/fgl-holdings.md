---
access_model:
  confidence: high
  label: No public API — integration is an appointment-gated distribution relationship
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - probe
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The only machine-readable API surface F&G Annuities & Life publishes. auth.fglife.com is an Auth0 custom domain fronting the prod.fglife.auth0.com tenant, serving a complete OpenID Connect discovery d
  name: F&G Identity (auth.fglife.com)
  slug: fgl-holdings-identity
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/fgl-holdings/finops/fgl-holdings-finops.yml
  title: ''
  type: FinOps
  url: finops/fgl-holdings-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.fglife.com
- group: company
  title: ''
  type: Blog
  url: https://blog.fglife.com
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.fglife.com/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://www.fglife.com/contact/agent-support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fglife.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fglife.com/website-terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FGLife
- group: auth
  href: https://artifacts.apis.io/fgl-holdings/security/fgl-holdings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fgl-holdings-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/fgl-holdings/well-known/fgl-holdings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fgl-holdings-well-known.yml
- group: auth
  href: https://artifacts.apis.io/fgl-holdings/authentication/fgl-holdings-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fgl-holdings-authentication.yml
- group: auth
  href: https://artifacts.apis.io/fgl-holdings/scopes/fgl-holdings-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fgl-holdings-scopes.yml
- group: design
  href: https://artifacts.apis.io/fgl-holdings/conformance/fgl-holdings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fgl-holdings-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fgl-holdings/llms/fgl-holdings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fgl-holdings-llms.txt
- group: commercial
  href: https://artifacts.apis.io/fgl-holdings/plans/fgl-holdings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fgl-holdings-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fgl-holdings/rate-limits/fgl-holdings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fgl-holdings-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: 'F&G is an insurance carrier, not a software vendor — it sells annuities and life policies through appointed agents and ships no software product, so there is no developer program: the humanURL this record carried, developer.fglife.com, does not resolve in DNS, and api.fglife.com is a live Azure Front Door that answers a bare JSON 404 to every public path including /openapi.json, /swagger.json, /api-docs, /graphql and the full /.well-known/ named list; the only machine-readable document on the estate is the OpenID Connect discovery doc at auth.fglife.com gating the appointment-only SalesLink portal.'
  evidence:
  - status: 0
    url: https://developer.fglife.com/
  - status: 404
    url: https://api.fglife.com/openapi.json
  - status: 200
    url: https://www.fglife.com/sitemap.xml
  - status: 200
    url: https://auth.fglife.com/.well-known/openid-configuration
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: FGL Holdings is the legacy holding-company name for F&G Annuities & Life, Inc., a US life insurance and annuity carrier headquartered in Des Moines, Iowa and majority-owned by Fidelity National Financial (FNF). F&G issues fixed indexed annuities (FIA), multi-year guaranteed annuities (MYGA), registered index-linked annuities (RILA), indexed universal life insurance, and pension risk transfer group annuities, distributing exclusively through appointed independent agents, Independent Marketing Organizations (IMOs) and bank/broker-dealer partners. F&G publishes NO public developer API, no developer portal and no machine-readable product contract — verified by direct probe on 2026-09-14. What it does serve anonymously is a complete OpenID Connect discovery document at auth.fglife.com, the first-party authorization server gating its SalesLink financial-professional portal.
finops:
- has_sources: true
  method: generated
  name: Fgl Holdings Finops
  primary_unit: not applicable
  service_category: Insurance / Annuities
  slug: fgl-holdings-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fgl-holdings.png
layout: provider
modified: '2026-09-14'
name: FGL Holdings
nav: Providers
network: true
overview: 'FGL Holdings is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Annuities, Financial Services, Life Insurance, and Retirement.


  FGL Holdings'' developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Fgl Holdings Plans Pricing
  plan_count: 0
  slug: fgl-holdings-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Fgl Holdings Rate Limits
  slug: fgl-holdings-rate-limits
scopes:
- name: Fgl Holdings Scopes
  scope_count: 14
  slug: fgl-holdings-scopes
  summary_line: 14 scopes
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fgl-holdings/fgl-holdings-2026-06-20T181145.png
security:
- kind: authentication
  name: Fgl Holdings Authentication
  slug: fgl-holdings-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fgl Holdings Domain Security
  slug: fgl-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fgl-holdings
tags:
- Insurance
- Annuities
- Financial Services
- Life Insurance
- Retirement
- Pension-Risk-Transfer
website: https://www.fglife.com
---
