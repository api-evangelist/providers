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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Gamesight Agentic Access
  operation_count: 14
  slug: gamesight-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 2
apis:
- description: The Measurement API from Gamesight — 3 operation(s) for measurement.
  name: Gamesight Measurement API
  slug: gamesight-measurement-api
- description: The Reporting API from Gamesight — 9 operation(s) for reporting.
  name: Gamesight Reporting API
  slug: gamesight-reporting-api
artifact_total: 8
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/gamesight-measurement-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gamesight-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gamesight-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gamesight-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gamesight-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gamesight-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/gamesight-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://gamesight.io/gdpr
- group: auth
  title: ''
  type: TrustCenter
  url: security/gamesight-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gamesight-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gamesight-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gamesight.io/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gamesight-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gamesight-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gamesight-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/gamesight-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gamesight-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gamesight-sandbox.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gamesight.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gamesight.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gamesight.io/reference/measurement-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gamesight.io/docs/rest-api-quick-start
- group: operate
  title: ''
  type: Support
  url: mailto:support@gamesight.io
- group: company
  title: ''
  type: Blog
  url: https://blog.gamesight.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gamesight
- group: start
  title: ''
  type: SignUp
  url: https://console.gamesight.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gamesight.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://gamesight.io/
created: '2026-07-17'
description: Gamesight is a performance marketing platform for PC and console games, giving game publishers the data, technology, and expertise to reach players across a title's lifecycle. Its Marketing Measurement suite delivers attribution for PC, console, and web games, cost aggregation from ad networks, and incrementality testing, while its Creator Marketing products run influencer campaigns, creator programs, and creator-led playtests. Developers integrate via a REST Measurement (ingest) API that streams in-game events with device identifiers, a Reporting API that pulls marketing analytics into a data warehouse, and a web measurement JavaScript SDK. The platform processes over a billion gaming data points daily and is SOC 2, GDPR, and CCPA compliant.
image: https://console.gamesight.io/images/meta/gamesight-facebook.png
layout: provider
mcp_servers:
- description: ''
  name: gamesight-mcp.yml
  slug: gamesight-mcpyml
modified: '2026-07-19'
name: Gamesight
nav: Providers
network: true
overview: 'Gamesight publishes 2 APIs on the [APIs.io](https://apis.io/) network: Measurement API and Reporting API. Tagged areas include Company, Gaming, Marketing, Analytics, and Attribution.


  Gamesight''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 22 more developer resources.'
random_paper: 25
rate_limits:
- limit_count: 2
  name: Gamesight Rate Limits
  slug: gamesight-rate-limits
score:
  band: developing
  composite: 54.0
  delta: -0.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.7
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 57.9
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gamesight/refs/heads/main/screenshots/gamesight-2026-07-25T215419.png
security:
- kind: authentication
  name: Gamesight Authentication
  slug: gamesight-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gamesight Domain Security
  slug: gamesight-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Gamesight Trust Center
  slug: gamesight-trust-center
  summary_line: SOC 2, GDPR, CCPA
slug: gamesight
tags:
- Company
- Gaming
- Marketing
- Analytics
- Attribution
- Measurement
- Advertising
- Creators
- Game Development
website: https://gamesight.io/
---
