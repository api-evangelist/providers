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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Notams API from Skymerse — 9 operation(s) for notams.
  name: Skymerse Notams API
  slug: skymerse-notams-api
artifact_total: 6
asyncapis:
- description: ''
  name: Skymerse Watcher Webhooks
  slug: skymerse-watcher-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skymerse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skymerse-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/skymerse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/skymerse-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skymerse-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skymerse-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skymerse-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skymerse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skymerse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skymerse-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/skymerse-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skymerse-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skymerse-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/skymerse-watcher-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/skymerse-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skymerse-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/skymerse-notamify-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://skymerse.gitbook.io/notamify-api
- group: docs
  title: ''
  type: Documentation
  url: https://skymerse.gitbook.io/notamify-api
- group: docs
  title: ''
  type: APIReference
  url: https://skymerse.gitbook.io/notamify-api/active-notams-endpoint
- group: start
  title: ''
  type: GettingStarted
  url: https://skymerse.gitbook.io/notamify-api/basics/quick-start
- group: company
  title: ''
  type: Blog
  url: https://notamify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skymerse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skymerse.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://skymerse.gitbook.io/notamify-api/basics/notamify-api-credits-and-costs
- group: start
  title: ''
  type: SignUp
  url: https://notamify.com/api-manager
- group: operate
  title: ''
  type: Support
  url: https://www.skymerse.com/contact
created: '2026-07-17'
description: 'Skymerse is a Y Combinator-backed aviation company building one AI system for airline flight operations — from planning and monitoring in the operations center to real-time support in the cockpit. Its first product, Notamify, interprets NOTAMs (Notices to Airmen) with specialized aeronautical models and ships the Notamify API V2: a REST API over global NOTAM data with AI-enhanced interpretation, active/nearby/raw/archive NOTAM endpoints, AI NOTAM prioritisation, synchronous and asynchronous flight briefings, and a Watcher API that pushes matching interpreted NOTAMs to signed webhooks. Notamify already serves airline customers and thousands of pilots and aviation professionals, with an official Python SDK and an MCP server for agents.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skymerse.png
layout: provider
mcp_servers:
- description: ''
  name: skymerse-mcp.yml
  slug: skymerse-mcpyml
modified: '2026-07-21'
name: Skymerse
nav: Providers
network: true
overview: 'Skymerse publishes 1 API on the [APIs.io](https://apis.io/) network: Notams API. Tagged areas include Company, Aviation, NOTAM, Flight Operations, and Aeronautical.


  The Skymerse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Skymerse''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 21 more developer resources.'
random_paper: 43
rate_limits:
- limit_count: 2
  name: Skymerse Rate Limits
  slug: skymerse-rate-limits
score:
  band: developing
  composite: 51.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.7
    developer_ergonomics: 75.5
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 51.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Skymerse Authentication
  slug: skymerse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Skymerse Domain Security
  slug: skymerse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skymerse
tags:
- Company
- Aviation
- NOTAM
- Flight Operations
- Aeronautical
- Weather
- AI
- Webhooks
website: https://skymerse.gitbook.io/notamify-api
---
