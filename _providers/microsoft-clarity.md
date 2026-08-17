---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Clarity Agentic Access
  operation_count: 1
  slug: microsoft-clarity-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Microsoft Clarity provides heatmaps, session recordings, and behavioral analytics with API access for custom integrations.
  name: Microsoft Clarity API
  slug: api
- description: 'Project live insights data export. One JWT-authenticated GET returns Clarity dashboard metrics as JSON for the last one to three days, sliced by up to three of nine dimensions. Capped at ten requests '
  name: Microsoft Clarity DataExport API
  slug: microsoft-clarity-dataexport-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Clarity Data Export DataExport API
  slug: open-microsoft-clarity-dataexport-api
- collection_type: open
  name: Microsoft Clarity Data Export API
  slug: open-microsoft-clarity
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-clarity-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-clarity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/microsoft-clarity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-clarity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-clarity-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-clarity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/microsoft-clarity-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-clarity-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-clarity-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-clarity-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-clarity-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-clarity-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-clarity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/microsoft-clarity-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-clarity-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-clarity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-clarity-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/microsoft-clarity-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/microsoft-clarity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-clarity-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-clarity
- group: start
  title: ''
  type: Portal
  url: https://clarity.microsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/clarity/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/clarity/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-data-export-api
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup
- group: commercial
  title: ''
  type: Pricing
  url: https://clarity.microsoft.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://clarity.microsoft.com/
- group: operate
  title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/clarity/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://clarity.microsoft.com/blog/feed
created: '2026-03-13'
description: Microsoft Clarity is a free behavioral analytics service from Microsoft that captures heatmaps, session recordings and frustration signals — rage clicks, dead clicks, excessive scroll, quickback clicks and script errors — for websites and mobile apps. Instrumentation is a client-side tracking tag or a first-party SDK for Android, iOS, Flutter, React Native and Cordova. Data comes back out through the Data Export API, a single JWT-authenticated GET that returns dashboard metrics for the last one to three days broken down by up to three dimensions, and through a first-party Model Context Protocol server that wraps the same endpoint for AI agents. Clarity is free forever with no paid tier; the binding constraint on any integration is a quota of ten API requests per project per day.
finops:
- name: Microsoft Clarity Finops
  service_category: API
  slug: microsoft-clarity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-clarity.png
layout: provider
mcp_servers:
- description: ''
  name: microsoft-clarity-mcp.yml
  slug: microsoft-clarity-mcpyml
modified: '2026-08-13'
name: Microsoft Clarity
nav: Providers
network: true
overview: 'Microsoft Clarity publishes 1 API on the [APIs.io](https://apis.io/) network: DataExport API. Tagged areas include Analytics, Heatmaps, Session Recording, Web Analytics, and Behavioral Analytics.


  Microsoft Clarity''s developer surface includes authentication, changelog, developer portal, documentation, API reference, getting-started guide, pricing, and 28 more developer resources.'
plans:
- name: Microsoft Clarity Plans Pricing
  plan_count: 1
  slug: microsoft-clarity-plans-pricing
random_paper: 148
rate_limits:
- limit_count: 4
  name: Microsoft Clarity Rate Limits
  slug: microsoft-clarity-rate-limits
score:
  band: strong
  composite: 58.8
  delta: 21.6
  facets:
    commercial_clarity: 65.8
    contract_quality: 62.7
    developer_ergonomics: 73.9
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/screenshots/microsoft-clarity-2026-06-20T185449.png
security:
- kind: authentication
  name: Microsoft Clarity Authentication
  slug: microsoft-clarity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Clarity Domain Security
  slug: microsoft-clarity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Clarity Vulnerability Disclosure
  slug: microsoft-clarity-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-clarity
tags:
- Analytics
- Heatmaps
- Session Recording
- Web Analytics
- Behavioral Analytics
- Product Analytics
- User Experience
- Data Export
- MCP
website: https://learn.microsoft.com/en-us/clarity/
---
