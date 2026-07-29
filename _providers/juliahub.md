---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Programmatic access to the JuliaHub platform — jobs, datasets, applications, projects, and package registries — via the official JuliaHub.jl Julia client and the jh CLI, authenticated with OAuth2 / Op
  name: JuliaHub Platform API
  slug: juliahub-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://juliahub.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://juliahub.com/products/juliahub
- group: docs
  title: ''
  type: Documentation
  url: https://docs.juliahub.com
- group: docs
  title: ''
  type: APIReference
  url: https://help.juliahub.com/julia-api/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.juliahub.com/julia-api/stable/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.juliahub.com
- group: operate
  title: ''
  type: Support
  url: https://juliahub.com/company/contact-us
- group: company
  title: ''
  type: Blog
  url: https://juliahub.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JuliaComputing
- group: commercial
  title: ''
  type: Pricing
  url: https://juliahub.com/pricing/juliahub
- group: start
  title: ''
  type: SignUp
  url: https://juliahub.com/ui/Register
- group: start
  title: ''
  type: Login
  url: https://juliahub.com/ui/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://juliahub.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://juliahub.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/juliahub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/juliahub-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/juliahub-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/juliahub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/juliahub-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/juliahub-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/juliahub-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/juliahub-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/juliahub-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/juliahub-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://trust.juliahub.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/juliahub-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juliahub-domain-security.yml
created: '2026-07-17'
description: JuliaHub is the company behind the Julia programming language, offering a cloud platform for large-scale, reproducible Julia computing — batch jobs, dataset management, application hosting, and a private package server — alongside modeling and simulation products (Dyad / JuliaSim) and pharmaceutical modeling (Pumas). The JuliaHub platform is accessed programmatically via the official JuliaHub.jl Julia client and the `jh` command-line interface, authenticated with OpenID Connect / OAuth2 (device flow) through a Dex identity provider.
image: https://framerusercontent.com/images/6SuSTR7C9szjs3GPdl4LbMOEM.webp
layout: provider
modified: '2026-07-19'
name: Juliahub
nav: Providers
network: true
overview: 'Juliahub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Julia, Scientific Computing, Cloud Computing, Modeling and Simulation, and High Performance Computing.


  Juliahub''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 5
scopes:
- name: Juliahub Scopes
  scope_count: 5
  slug: juliahub-scopes
  summary_line: 5 scopes · deviceCode/authorizationCode
score:
  band: thin
  composite: 38.1
  delta: 1.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 37.1
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/juliahub/refs/heads/main/screenshots/juliahub-2026-07-25T223308.png
security:
- kind: authentication
  name: Juliahub Authentication
  slug: juliahub-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Juliahub Domain Security
  slug: juliahub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Juliahub Trust Center
  slug: juliahub-trust-center
  summary_line: SOC 2, PCI DSS, GDPR, CCPA
slug: juliahub
tags:
- Julia
- Scientific Computing
- Cloud Computing
- Modeling and Simulation
- High Performance Computing
- Data Science
- Developer Tools
- Package Registry
- Company
website: https://juliahub.com
---
