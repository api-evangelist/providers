---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 9.6
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: npm-compatible package registry API implemented by vsr, vlt's serverless registry. Exposes package publish/install endpoints (packuments, tarballs, dist-tags), user and token management, granular acce
  name: vlt Serverless Registry (vsr) API
  slug: vlt-serverless-registry-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vlt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vlt-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/vlt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vlt-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vlt-llms.txt
- group: build
  title: ''
  type: CLI
  url: cli/vlt-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vlt-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vlt-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vlt-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vlt-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.vlt.io/security
- group: commercial
  title: ''
  type: Plans
  url: plans/vlt-plans.yml
- group: company
  title: ''
  type: Website
  url: https://www.vlt.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vlt.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vlt.io/cli
- group: company
  title: ''
  type: Blog
  url: https://www.vlt.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vlt.io/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vlt.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.vlt.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.vlt.io/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vlt.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vlt.io/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.vlt.io/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vlt.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vltpkg
- group: operate
  title: ''
  type: Support
  url: https://www.vlt.io/contact
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/qdbXTqxZzZ
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/vltpkg/vsr/blob/main/info/ROADMAP.md
- group: company
  title: ''
  type: About
  url: https://www.vlt.io/about
- group: company
  title: ''
  type: Careers
  url: https://www.vlt.io/careers
- group: company
  title: ''
  type: Press
  url: https://www.vlt.io/press
- group: other
  title: ''
  type: Benchmarks
  url: https://benchmarks.vlt.sh/
created: '2026-07-17'
description: vlt (pronounced "volt") is a JavaScript package management company started by the creator of npm and former members of the npm core team, and backed by Accel. It ships the open source vlt package manager CLI, the npm-compatible vlt serverless registry (vsr) that runs on Cloudflare's edge network, and a hosted registry platform at vlt.io with user, token, and access management exposed through an npm-compatible registry API at registry.vlt.io.
image: https://github.com/vltpkg.png
layout: provider
modified: '2026-07-21'
name: vlt
nav: Providers
network: true
overview: 'vlt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, JavaScript, Package Management, Package Registry, and Developer Tools.


  vlt''s developer surface includes CLI, changelog, authentication, documentation, getting-started guide, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Vlt Plans
  plan_count: 4
  slug: vlt-plans
random_paper: 36
score:
  band: thin
  composite: 42.9
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 42.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Vlt Authentication
  slug: vlt-authentication
  summary_line: http-bearer/oidc-exchange · 4 schemes
- kind: domain-security
  name: Vlt Domain Security
  slug: vlt-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Vlt Vulnerability Disclosure
  slug: vlt-vulnerability-disclosure
  summary_line: disclosure policy published
slug: vlt
tags:
- Company
- JavaScript
- Package Management
- Package Registry
- Developer Tools
- CLI
- Serverless
- npm
- Dependency Management
- Open Source
website: https://www.vlt.io/
---
