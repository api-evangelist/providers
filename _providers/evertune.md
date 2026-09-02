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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.evertune.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evertune.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.evertune.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.evertune.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.evertune.ai/resources/blog
- group: start
  title: ''
  type: Login
  url: https://auth.evertune.ai/u/login/identifier
- group: start
  title: ''
  type: SignUp
  url: https://www.evertune.ai/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evertune.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evertune.ai/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/evertune-ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@evertune-ai/videos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Evertune-AI
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evertune-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evertune-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evertune-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evertune-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/evertune-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evertune-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/evertune-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: 'Evertune is a consumer of the model providers'' APIs rather than a publisher of one — its own FAQ says base-model data is "reachable only through direct API integration with the model provider" — and it ships no developer surface of its own: the pricing page''s two demo-led tiers name no API access, the Intercom help center holds three end-user articles, and app.evertune.ai is a closed SPA whose backend is undocumented; the only machine-readable thing Evertune serves is the Auth0 OIDC discovery document on auth.evertune.ai, which signs users in to that app.'
  evidence:
  - status: 200
    url: https://auth.evertune.ai/.well-known/openid-configuration
  - status: 200
    url: https://www.evertune.ai/pricing
  - status: 200
    url: https://docs.evertune.ai/llms.txt
  - status: 404
    url: https://www.evertune.ai/openapi.json
  - status: 404
    url: https://www.evertune.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Evertune is a Generative Engine Optimization (GEO) and AI brand-intelligence platform that helps brands, marketers, and agencies understand, measure, and influence how they appear in AI-driven recommendations. As discovery shifts from traditional search engines to conversational answer engines like ChatGPT, Claude, Gemini, and Perplexity, Evertune tracks brand visibility and sentiment across 10+ AI models, analyzes how large language models describe a brand versus its competitors, and delivers prescriptive message and content briefs to improve that positioning. The platform combines large-scale prompt testing (100,000+ prompt responses per report via direct base-model API access), the EverPanel consumer panel, daily consumer-app data, an AI Brand Index and AI Brand Score, content activation, and AI advertising. Founded in 2024 by operators who helped scale The Trade Desk, Evertune is backed by Felicis and serves customers including Roku, WPP, athenahealth, and HexClad. Evertune
  is a data consumer of the major model APIs; it does not currently publish a first-party developer API, SDK, or OpenAPI.
image: https://cdn.prod.website-files.com/65fc8aa2e86478511b710078/68b8a3ea1e6fb2d5d5503742_Logo.svg
layout: provider
modified: '2026-08-13'
name: Evertune
nav: Providers
network: true
overview: 'Evertune is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Generative Engine Optimization, AI Search, Brand Monitoring, and Marketing Intelligence.


  Evertune''s developer surface includes documentation, pricing, engineering blog, signup flow, YouTube channel, authentication, and 13 more developer resources.'
plans:
- name: Evertune Plans Pricing
  plan_count: 2
  slug: evertune-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Evertune Rate Limits
  slug: evertune-rate-limits
scopes:
- name: Evertune Scopes
  scope_count: 14
  slug: evertune-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/implicit
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evertune/refs/heads/main/screenshots/evertune-2026-07-25T213740.png
security:
- kind: authentication
  name: Evertune Authentication
  slug: evertune-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Evertune Domain Security
  slug: evertune-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evertune
tags:
- Company
- Generative Engine Optimization
- AI Search
- Brand Monitoring
- Marketing Intelligence
- AI Visibility
- Analytics
- Artificial Intelligence
website: https://www.evertune.ai/
---
