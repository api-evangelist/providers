---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spotter.com/
- group: other
  title: ''
  type: Product
  url: https://www.spotterstudio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spotter.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spotter.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.spotterstudio.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.spotterstudio.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.spotterstudio.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.spotterstudio.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spotter-dev
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spotter-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/spotter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spotter-rate-limits.yml
coverage:
  checked: '2026-08-13'
  detail: Spotter ships Spotter Studio only as an end-user web app — the app's own backends (bowser/birdo/kirby.api.spotterstudio.com, read out of the SPA bundle) answer HTTP 503 to every anonymous request and publish no contract, and there is no developer portal, API reference, SDK, webhook surface or /llms.txt on any Spotter host.
  evidence:
  - status: 503
    url: https://bowser.api.spotterstudio.com/openapi.json
  - status: 404
    url: https://data-api.api.spotterstudio.com/openapi.json
  - status: 404
    url: https://www.spotter.com/developers
  - status: 404
    url: https://www.spotterstudio.com/llms.txt
  - status: 404
    url: https://www.spotterstudio.com/.well-known/agent-card.json
  - status: 401
    url: https://www.spotterstudio.com/pricing
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Spotter is a creator-economy platform that invests in YouTube creators through capital, catalog licensing, and brand partnerships, and connects brands with top long-form YouTube creators for marketing and content opportunities. Its Spotter Studio product provides AI-assisted tooling that helps creators plan, ideate, and optimize their content and titles. The company reports more than $1 billion invested in creators and over 43 billion monthly views across a network that includes creators such as MrBeast, Critical Role, and Sam and Colby. Spotter is backed by SoftBank Vision Fund. Spotter publishes no public developer API: contract discovery on 2026-08-13 found no OpenAPI, GraphQL SDL, AsyncAPI, MCP server or A2A agent card on any Spotter host, and the Spotter Studio application backends return 503 to anonymous callers. Spotter Studio is a consumer of the YouTube Data and Analytics APIs via Google OAuth, not a provider of one.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spotter.png
layout: provider
modified: '2026-08-13'
name: Spotter
nav: Providers
network: true
overview: 'Spotter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Creator Economy, Media, and YouTube.


  Spotter''s developer surface includes engineering blog, support, signup flow, and 10 more developer resources.'
plans:
- name: Spotter Plans Pricing
  plan_count: 0
  slug: spotter-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Spotter Rate Limits
  slug: spotter-rate-limits
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Spotter Domain Security
  slug: spotter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spotter
tags:
- Company
- Consumer
- Creator Economy
- Media
- YouTube
- Video
- Marketing
- Content
- Creators
- Artificial Intelligence
website: https://www.spotter.com/
---
