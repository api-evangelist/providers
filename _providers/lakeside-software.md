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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The SysTrack API provides programmatic REST access to SysTrack data on a cloud tenant or on-premises installation — enumerating groups, listing the systems within a group, retrieving sensor data for a
  name: SysTrack API
  slug: systrack-api
- description: The Ingest API lets SysTrack cloud customers import external user and device attributes from CSV files — department, asset tag, purchase date, employee ID and other business-owned fields — and surface
  name: SysTrack Ingest API
  slug: systrack-ingest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Lakeside Software Webhooks
  slug: lakeside-software-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lakeside-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lakesidesoftware.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.lakesidesoftware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.lakesidesoftware.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.lakesidesoftware.com/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.lakesidesoftware.com/docs/systrack-api-1
- group: operate
  title: ''
  type: Support
  url: https://documentation.lakesidesoftware.com/docs/contact-lakeside-support
- group: company
  title: ''
  type: Blog
  url: https://www.lakesidesoftware.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.lakesidesoftware.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lakesidesoftware.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lakesidesoftware.com/privacy-statement/
- group: auth
  title: ''
  type: TrustCenter
  url: security/lakeside-software-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/lakeside-software-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lakeside-software-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lakeside-software-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lakeside-software-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lakeside-software-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lakeside-software-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lakeside-software-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/lakeside-software-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lakeside-software-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lakeside-software-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lakeside-software-packages.yml
created: '2026-07-17'
description: Lakeside Software builds SysTrack, a digital employee experience (DEX) platform that instruments Windows, macOS, Linux, Android and virtual endpoints with a local agent to collect high-frequency telemetry on device health, application performance, resource contention and end-user sentiment. SysTrack is delivered as a SaaS cloud tenant and as an on-premises deployment, and exposes programmatic access through the SysTrack API (groups, systems, sensors, automations and an audit trail), a legacy Data API, and an Ingest API for importing external user and device attributes from CSV. The platform ships webhook notifications for sensor, anomaly and data-egress events with HMAC-SHA256 signed-secret verification, a Power BI connector, and SysTrack AI — which exposes a DEX Analytics MCP Server alongside A2A, Microsoft Teams and voice channels for agentic and natural-language access to endpoint analytics. Lakeside Software is a portfolio company of Insight Partners.
image: https://www.lakesidesoftware.com/wp-content/uploads/2025/09/16x9_Lakeside_Logo_Newsroom.png
layout: provider
mcp_servers:
- description: ''
  name: lakeside-software-mcp.yml
  slug: lakeside-software-mcpyml
modified: '2026-07-19'
name: Lakeside Software
nav: Providers
network: true
overview: 'Lakeside Software publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Employee Experience, Endpoint Monitoring, IT Operations, and Observability.


  The Lakeside Software catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lakeside Software''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 115
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 48.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lakeside-software/refs/heads/main/screenshots/lakeside-software-2026-07-25T224431.png
security:
- kind: authentication
  name: Lakeside Software Authentication
  slug: lakeside-software-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Lakeside Software Domain Security
  slug: lakeside-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lakeside Software Trust Center
  slug: lakeside-software-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type 2
slug: lakeside-software
tags:
- Company
- Digital Employee Experience
- Endpoint Monitoring
- IT Operations
- Observability
- Device Management
- End User Computing
- Analytics
- Virtual Desktop
- ITSM
website: https://www.lakesidesoftware.com/
---
