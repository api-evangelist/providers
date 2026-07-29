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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
api_count: 11
apis:
- description: The Authentication API from TruVideo — 2 operation(s) for authentication.
  name: TruVideo Authentication API
  slug: truvideo-authentication-api
- description: The Chat API from TruVideo — 4 operation(s) for chat.
  name: TruVideo Chat API
  slug: truvideo-chat-api
- description: The Customers API from TruVideo — 1 operation(s) for customers.
  name: TruVideo Customers API
  slug: truvideo-customers-api
- description: The Dealers API from TruVideo — 1 operation(s) for dealers.
  name: TruVideo Dealers API
  slug: truvideo-dealers-api
- description: The Files API from TruVideo — 4 operation(s) for files.
  name: TruVideo Files API
  slug: truvideo-files-api
- description: The Messages API from TruVideo — 3 operation(s) for messages.
  name: TruVideo Messages API
  slug: truvideo-messages-api
- description: The Repair Orders API from TruVideo — 5 operation(s) for repair orders.
  name: TruVideo Repair Orders API
  slug: truvideo-repair-orders-api
- description: The Reports API from TruVideo — 2 operation(s) for reports.
  name: TruVideo Reports API
  slug: truvideo-reports-api
- description: The Support API from TruVideo — 1 operation(s) for support.
  name: TruVideo Support API
  slug: truvideo-support-api
- description: The Users API from TruVideo — 1 operation(s) for users.
  name: TruVideo Users API
  slug: truvideo-users-api
- description: The Videos API from TruVideo — 3 operation(s) for videos.
  name: TruVideo Videos API
  slug: truvideo-videos-api
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://truvideo.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truvideo-domain-security.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truvideo-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/truvideo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truvideo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truvideo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truvideo-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/truvideo-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truvideo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/truvideo-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/truvideo-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/truvideo-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/truvideo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truvideo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Truvideo/Documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://truvideo.com/platform/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Truvideo
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/Truvideo/Documentation/blob/master/README.md
- group: commercial
  title: ''
  type: Pricing
  url: https://truvideo.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://truvideo.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://truvideo.com/faqs/
- group: start
  title: ''
  type: Login
  url: https://app.truvideo.com/
created: '2026-07-17'
description: TruVideo is a video-intelligence and omnichannel communication platform for service businesses, built for the automotive service market and expanding into aviation, insurance, and commercial trucking. It lets dealers, service advisors, and technicians capture and share videos, run AI features (noise cancellation, real-time sentiment analysis, and a multilingual virtual assistant), and drive SMS/messaging conversations tied to repair orders. TruVideo's developer surface is SDK-first — modular on-device capture SDKs for iOS, Android, .NET, React Native, and Capacitor — plus a REST Platform API (v2) covering authentication, repair orders, videos, messaging, customers, files, and reporting.
image: https://truvideo.com/wp-content/uploads/2026/04/Line-6.png
layout: provider
mcp_servers:
- description: ''
  name: truvideo-mcp.yml
  slug: truvideo-mcpyml
modified: '2026-07-21'
name: TruVideo
nav: Providers
network: true
overview: 'TruVideo publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Chat API, Customers API, and 8 more. Tagged areas include Company, Commerce, Video, Messaging, and Automotive.


  TruVideo''s developer surface includes authentication, sandbox, documentation, pricing, support, and 18 more developer resources.'
random_paper: 35
score:
  band: thin
  composite: 40.5
  delta: -3.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.9
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 29.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Truvideo Authentication
  slug: truvideo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Truvideo Domain Security
  slug: truvideo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: truvideo
tags:
- Company
- Commerce
- Video
- Messaging
- Automotive
- Communications
- SDK
- Video Intelligence
website: https://truvideo.com/
---
