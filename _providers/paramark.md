---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - https://paramark.com/pricing
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Paramark's production API, offered as a feature of the Advanced and Enterprise tiers. The service is live and answers anonymously at GET /healthz (HTTP 200 {"status":"ok"}) and is a FastAPI applicatio
  name: Paramark API
  slug: paramark-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paramark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paramark.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://paramark.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://paramark.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paramark.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paramark-inc
- group: start
  title: ''
  type: Login
  url: https://signin.paramark.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paramark-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paramark-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paramark-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/paramark-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/paramark-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paramark-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paramark-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paramark-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/paramark-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paramark-llms.txt
created: '2026-07-17'
description: 'Paramark is a marketing measurement and forecasting platform that helps growth and finance teams understand the true incremental impact of their marketing spend. Founded in 2022 by Pranav Piyush and Pete Belknap and backed by Greylock, Paramark combines incrementality testing, marketing mix modeling (MMM), and scenario planning in one place, augmented by human growth advisors and AI agents. Rather than relying on last-touch attribution, the platform uses statistics and machine learning to quantify each channel''s incremental contribution across search, social, TV, and out-of-home, giving marketers defensible ROI numbers to bring to their finance teams. Paramark maintains an open-source Marketing Mix Modeling workbench and forks of the major MMM libraries under its paramark-inc GitHub organization. Paramark runs a production API at api.paramark.com, but publishes no developer portal and no public contract: its FastAPI-generated OpenAPI, /docs and /redoc all answer HTTP 401 behind
  an HTTP Basic challenge, and API access is sold as a feature of the Advanced ($150k/yr) and Enterprise ($220k/yr) tiers, where MCP servers are listed as coming soon. What Paramark does publish anonymously and machine-readably is its identity layer: full OpenID Connect and OAuth 2.0 authorization server metadata at signin.paramark.com, with PKCE, device code and dynamic client registration.'
image: https://framerusercontent.com/images/V0dFY5kITNK8vNXgA2K3xW0y6k.png
layout: provider
modified: '2026-08-12'
name: Paramark
nav: Providers
network: true
overview: 'Paramark publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Application, Marketing, Analytics, and Measurements.


  Paramark''s developer surface includes pricing, engineering blog, authentication, and 14 more developer resources.'
plans:
- name: Paramark Plans Pricing
  plan_count: 3
  slug: paramark-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Paramark Rate Limits
  slug: paramark-rate-limits
scopes:
- name: Paramark Scopes
  scope_count: 0
  slug: paramark-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.4
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paramark/refs/heads/main/screenshots/paramark-2026-08-07T191427.png
security:
- kind: authentication
  name: Paramark Authentication
  slug: paramark-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Paramark Domain Security
  slug: paramark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Paramark Trust Center
  slug: paramark-trust-center
  summary_line: trust center published
slug: paramark
tags:
- Company
- Application
- Marketing
- Analytics
- Measurements
- Marketing Mix Modeling
- Incrementality
- Advertising
- Artificial Intelligence
website: https://paramark.com/
---
