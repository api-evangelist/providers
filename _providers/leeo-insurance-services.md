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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Leeo Insurance Services Agentic Access
  operation_count: 7
  slug: leeo-insurance-services-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- description: Daily and weekly aggregated driver scorecards.
  name: LEEO Insurance Services Aggregates API
  slug: leeo-insurance-services-aggregates-api
- description: Fleet driver roster.
  name: LEEO Insurance Services Drivers API
  slug: leeo-insurance-services-drivers-api
- description: Generated fleet report links.
  name: LEEO Insurance Services Reports API
  slug: leeo-insurance-services-reports-api
- description: Trip lists, trip detail, paths, and driving events.
  name: LEEO Insurance Services Trips API
  slug: leeo-insurance-services-trips-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.leeoinsurance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leeoinsurance.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leeoinsurance.com/leeo-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leeoinsurance.com/
- group: operate
  title: ''
  type: Support
  url: https://leeoinsurance.com/contact
- group: company
  title: ''
  type: Blog
  url: https://leeoinsurance.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fairmatic
- group: start
  title: ''
  type: Login
  url: https://app.fairmatic.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leeoinsurance.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leeoinsurance.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://leeoinsurance.com/
- group: build
  title: ''
  type: Packages
  url: packages/leeo-insurance-services-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leeo-insurance-services-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leeo-insurance-services-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leeo-insurance-services-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leeo-insurance-services-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leeo-insurance-services-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leeo-insurance-services-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leeo-insurance-services-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leeo-insurance-services-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leeo-insurance-services-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leeo-insurance-services-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leeo-insurance-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leeo-insurance-services-domain-security.yml
created: '2026-07-17'
description: LEEO Insurance Services is a San Francisco-based managing general agent (MGA) for commercial auto insurance, founded in 2017 and known as Fairmatic until its December 2025 rebrand. LEEO underwrites and prices fleet policies using telematics collected from drivers' phones through its mobile SDK, applying machine learning across underwriting, pricing, and claims, and rewarding safer driving with renewal credits and cashback. It writes fleet classes including non-emergency medical transport, light business auto, and last-mile delivery, selling through brokers. LEEO exposes a read-only REST Fleet Telematics API returning the driver roster, trip histories, trip paths and driving events, and daily and weekly driver safety scorecards, plus native SDKs for Android, iOS, React Native, and MAUI. The company has raised $91M and is backed by Battery Ventures, Foundation Capital, and Aquiline Technology Growth.
image: https://framerusercontent.com/images/YggCBRfzpd8IYRlJTG6UlpdiYQ.png
layout: provider
mcp_servers:
- description: ''
  name: leeo-insurance-services-mcp.yml
  slug: leeo-insurance-services-mcpyml
modified: '2026-07-19'
name: LEEO Insurance Services
nav: Providers
network: true
overview: 'LEEO Insurance Services publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Aggregates API, Drivers API, Reports API, and 1 more. Tagged areas include Company, Insurance, Insurtech, Commercial Auto Insurance, and Telematics.


  LEEO Insurance Services'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 18 more developer resources.'
random_paper: 79
score:
  band: developing
  composite: 47.4
  delta: -3.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.3
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leeo-insurance-services/refs/heads/main/screenshots/leeo-insurance-services-2026-07-25T224822.png
security:
- kind: authentication
  name: Leeo Insurance Services Authentication
  slug: leeo-insurance-services-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Leeo Insurance Services Domain Security
  slug: leeo-insurance-services-domain-security
  summary_line: TLSv1.3 · DMARC
slug: leeo-insurance-services
tags:
- Company
- Insurance
- Insurtech
- Commercial Auto Insurance
- Telematics
- Fleet Management
- Driving Behavior
- Risk Management
- Managing General Agent
- Mobile SDK
website: https://leeoinsurance.com/
---
