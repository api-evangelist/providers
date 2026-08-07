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
api_count: 2
apis:
- description: Track user events used as experiment and feature-flag goals.
  name: Apptimize Events API
  slug: apptimize-events-api
- description: Retrieve variant assignments and experiment data for a user.
  name: Apptimize Experiments API
  slug: apptimize-experiments-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: http://apptimize.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apptimize.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://apptimize.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://apptimize.com/docs/apis/rest-api.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@apptimize.com
- group: build
  title: ''
  type: Packages
  url: packages/apptimize-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apptimize-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apptimize-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apptimize-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apptimize-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apptimize-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apptimize-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apptimize-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/apptimize-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apptimize-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apptimize-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Apptimize is a mobile-first A/B testing, multivariate testing, and feature management platform for optimizing user experiences across iOS, Android, web, and server-side channels. Product teams use Apptimize to run experiments, ship feature flags with controlled rollouts, deliver instant updates without app-store releases, and set dynamic variables that can be changed on the fly. Apptimize ships client and server SDKs for iOS/tvOS/watchOS, Android, Web, React Native, Python, Flutter, and Roku, plus a REST API for retrieving variant assignments and tracking events from any device or backend. Apptimize was acquired by Airship in 2019; its developer documentation and SDKs remain published at apptimize.com/docs, and the marketing site now redirects to airship.com.
image: https://apptimize.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: apptimize-mcp.yml
  slug: apptimize-mcpyml
modified: '2026-07-18'
name: Apptimize
nav: Providers
network: true
overview: 'Apptimize publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and Experiments API. Tagged areas include Company, A/B Testing, Feature Flags, Feature Management, and Experimentation.


  Apptimize''s developer surface includes documentation, API reference, support, authentication, and 13 more developer resources.'
random_paper: 75
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 65.1
    developer_ergonomics: 49.5
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 35.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apptimize/refs/heads/main/screenshots/apptimize-2026-07-25T200851.png
security:
- kind: authentication
  name: Apptimize Authentication
  slug: apptimize-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apptimize Domain Security
  slug: apptimize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apptimize
tags:
- Company
- A/B Testing
- Feature Flags
- Feature Management
- Experimentation
- Mobile
- SDK
- Optimization
website: http://apptimize.com
---
