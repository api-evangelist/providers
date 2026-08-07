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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Events API from Helika — 1 operation(s) for events.
  name: Helika Events API
  slug: helika-events-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.helika.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.helika.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.helika.io/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.helika.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.helika.io/reference/create_event_v1_events_post
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getlidar
- group: start
  title: ''
  type: Login
  url: https://platform.helika.io/
- group: operate
  title: ''
  type: Support
  url: https://www.helika.io/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.helika.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helika.io/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helika-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/helika-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/helika-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/helika-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helika-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/helika-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/helika-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/helika-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/helika-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/helika-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/helika-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Helika is a game and brand analytics platform, originally built for web3 and blockchain games, that helps studios, sports teams, and entertainment brands collect, unify, and act on player and community engagement data. Its Analytics Service API ingests gameplay and engagement events through a single events endpoint authenticated with an x-api-key header, and is instrumented by first-party Unity, Unreal Engine, and Web SDKs. Helika has since expanded into Helika Evolve, an AI-character platform that lets IP owners deploy brand-safe interactive characters across Discord, web, and social channels. Helika is a Pantera Capital portfolio company operating in the crypto and gaming sector.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helika.png
layout: provider
mcp_servers:
- description: ''
  name: helika-mcp.yml
  slug: helika-mcpyml
modified: '2026-07-19'
name: Helika
nav: Providers
network: true
overview: 'Helika publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Company, Crypto, Gaming, Analytics, and Game Analytics.


  Helika''s developer surface includes documentation, getting-started guide, API reference, support, authentication, and 17 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 41.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 45.7
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 41.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helika/refs/heads/main/screenshots/helika-2026-07-25T220913.png
security:
- kind: authentication
  name: Helika Authentication
  slug: helika-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Helika Domain Security
  slug: helika-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helika
tags:
- Company
- Crypto
- Gaming
- Analytics
- Game Analytics
- Web3
- Events
- AI
- SDK
- Player Data
website: https://www.helika.io/
---
