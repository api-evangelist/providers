---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://dev.zemanta.com/one/api/
  - https://intercom.help/outbrain_dsp/en/articles/8225692-zemanta-api
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Teads DSP REST Campaign Management API, formerly the Zemanta One API. It lets Teads DSP clients programmatically create and manage accounts, campaigns, budgets, campaign goals, ad groups, ad group
  name: Teads DSP API (Zemanta One)
  slug: teads-dsp-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zemanta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zemanta.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vault.pactsafe.io/s/9ac72792-c7df-4d0d-832d-0ca873f73a64/legal.html#terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outbrain.com/privacy/privacy-policy-outbrain-dsp/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zemanta.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.zemanta.com/one/api/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.zemanta.com/one/api/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/outbrain_dsp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zemanta
- group: start
  title: ''
  type: Login
  url: https://one.zemanta.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/zemanta-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zemanta-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zemanta-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zemanta-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zemanta-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zemanta-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zemanta-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zemanta-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zemanta-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/zemanta-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zemanta-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zemanta-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zemanta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/zemanta-vulnerability-disclosure.yml
created: '2026-07-17'
description: Zemanta is a native advertising and content-recommendation technology company founded in 2007 (Ljubljana, Slovenia and New York), best known for Zemanta One, a self-serve programmatic demand-side platform (DSP) for native advertising. Outbrain acquired Zemanta in 2017 and the DSP now trades as Teads DSP. The product line survived both the acquisition and the rebrand, and its API is live — the Teads DSP REST Campaign Management API, the former Zemanta One API, is still served from Zemanta-owned hosts, with the API endpoint at https://oneapi.zemanta.com/rest/v1 and a complete public reference at https://dev.zemanta.com/one/api/. The API covers accounts, credits, campaigns, budgets, goals, ad groups, ads, creatives, video assets, bid modifiers, measurement services, conversion definitions, audiences, publisher groups, deals, keyword lists, reporting and real-time statistics. Authentication is two-legged OAuth 2.0 client credentials; access is granted through a sales relationship
  rather than self-service sign-up. The console host one.zemanta.com 301-redirects every path to the matching path on dsp.outbrain.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zemanta.png
layout: provider
modified: '2026-08-12'
name: Zemanta
nav: Providers
network: true
overview: 'Zemanta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Native Advertising, Programmatic, and DSP.


  Zemanta''s developer surface includes documentation, API reference, support, authentication, and 20 more developer resources.'
plans:
- name: Zemanta Plans Pricing
  plan_count: 0
  slug: zemanta-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Zemanta Rate Limits
  slug: zemanta-rate-limits
scopes:
- name: Zemanta Scopes
  scope_count: 0
  slug: zemanta-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.7
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 25.7
  provenance:
    conformance: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Zemanta Authentication
  slug: zemanta-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zemanta Domain Security
  slug: zemanta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zemanta Vulnerability Disclosure
  slug: zemanta-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zemanta
tags:
- Company
- Advertising
- Native Advertising
- Programmatic
- DSP
- AdTech
- Content Recommendation
- Marketing
- Campaign Management
- Demand-Side Platform
- Media Buying
website: https://zemanta.com
---
