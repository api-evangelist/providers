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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Evolv Participant API is the runtime edge API the client SDKs call to fetch a participant's experiment configuration and allocations for an environment, and to ingest context and behavioral events
  name: Evolv Participant API
  slug: evolv-participant-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.evolv.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.evolv.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.evolv.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evolv-ai
- group: build
  title: ''
  type: SDKs
  url: packages/evolv-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/evolv-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/evolv-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evolv-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/evolv-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evolv-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evolv-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/evolv-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evolv-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evolv-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evolv-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evolv-domain-security.yml
created: '2026-07-17'
description: Evolv AI (formerly Sentient Ascend) is an experience optimization and autonomous experimentation platform that continuously tests and personalizes digital experiences using machine learning. Its Participant API and official client SDKs for JavaScript, iOS, Android, PHP and React allocate visitors to experiment variants, deliver optimized configurations, and ingest behavioral events so AI-driven optimization can evolve web and app experiences without manual A/B-test management. Enterprises use Evolv AI to automate conversion-rate optimization and personalization across their digital properties.
image: https://evolv.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: evolv-mcp.yml
  slug: evolv-mcpyml
modified: '2026-07-19'
name: Evolv
nav: Providers
network: true
overview: 'Evolv publishes 1 API on the [APIs.io](https://apis.io/) network: Participant API. Tagged areas include Experimentation, Optimization, Personalization, A/B Testing, and Machine Learning.


  Evolv''s developer surface includes documentation, CLI, authentication, sandbox, changelog, and 11 more developer resources.'
random_paper: 76
score:
  band: emerging
  composite: 20.7
  delta: -2.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 23.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evolv/refs/heads/main/screenshots/evolv-2026-07-25T213820.png
security:
- kind: authentication
  name: Evolv Authentication
  slug: evolv-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Evolv Domain Security
  slug: evolv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evolv
tags:
- Experimentation
- Optimization
- Personalization
- A/B Testing
- Machine Learning
- Conversion Rate Optimization
- Experience Optimization
- Analytics
- Company
website: https://www.evolv.ai
---
