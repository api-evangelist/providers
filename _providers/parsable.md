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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Token-authenticated JSON API for the Parsable Connected Worker platform. All calls are HTTP POSTs to https://api.parsable.net/api/<MODULE> carrying a `{ "method", "arguments" }` envelope and an Author
  name: Parsable Connected Worker API
  slug: parsable-connected-worker-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/parsable-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://parsable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.parsable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.parsable.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.parsable.com/
- group: other
  title: ''
  type: Product
  url: https://parsable.com/product/
- group: start
  title: ''
  type: Login
  url: https://go.parsable.com/login
- group: start
  title: ''
  type: SignUp
  url: https://parsable.com/get-demo/
- group: operate
  title: ''
  type: Support
  url: https://parsable.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://parsable.com/parsable-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://parsable.com/parsable-blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parsable
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parsable.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://parsable.com/compliance/
- group: operate
  title: ''
  type: StatusPage
  url: https://parsable.statuspage.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/parsable-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parsable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parsable-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parsable-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parsable-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/parsable-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/parsable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parsable-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parsable-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parsable-llms.txt
created: '2026-07-17'
description: Parsable is a Connected Worker platform for manufacturing and industrial operations. Its mobile-first software replaces paper-based standard operating procedures with digital work instructions, guiding frontline workers through audits, inspections, maintenance, safety, quality, and production workflows while capturing real-time execution data. The platform surfaces analytics and insights that help enterprises like Coca-Cola, Grupo Bimbo, and other global CPG and industrial manufacturers reduce downtime, standardize processes, and drive continuous improvement. Parsable exposes a token-authenticated JSON API (api.parsable.net) organized into 17 modules for jobs, templates, field data, messaging, reporting, and analytics, plus an oclif-based command-line tool (parsable-cli) for administration and data integration. Originally founded as Wearable Intelligence, Parsable is headquartered in Lincoln, RI.
image: https://parsable.com/wp-content/uploads/2021/03/parsable-logo.png
layout: provider
modified: '2026-07-20'
name: Parsable
nav: Providers
network: true
overview: 'Parsable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Connected Worker, Manufacturing, Industrial, and Digital Work Instructions.


  Parsable''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, CLI, and 18 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 30.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Parsable Authentication
  slug: parsable-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Parsable Domain Security
  slug: parsable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Parsable Trust Center
  slug: parsable-trust-center
  summary_line: SOC 2, GDPR
slug: parsable
tags:
- Company
- Connected Worker
- Manufacturing
- Industrial
- Digital Work Instructions
- Frontline Operations
- Workflow
- Analytics
website: https://parsable.com
---
