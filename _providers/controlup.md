---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.7
  scored_at: '2026-08-06'
api_count: 11
apis:
- description: Organization, identity and governance API for the ControlUp ONE platform — users, invitations, roles and permissions, organization settings, SAML SSO configuration and SSO group mappings, IP allowlist
  name: ControlUp ONE Platform API
  slug: controlup-one-platform-api
- description: 'Event and alert API for the ControlUp ONE platform — list and retrieve events with field projection and cardinality counts over a time range, and read the configured alert definitions for Devices and '
  name: ControlUp Events and Alerts API
  slug: controlup-events-and-alerts-api
- description: Physical endpoint API for ControlUp for Desktops (formerly Edge DX) — devices and device details, alerts, scripts and script actions, surveys, OS errors, events, and a data-access layer for querying c
  name: ControlUp for Desktops API
  slug: controlup-for-desktops-api
- description: Compliance and endpoint-security posture API — list managed devices, retrieve per-device detail including the security score and agent status, and enumerate detected vulnerabilities (CVEs), missing OS
  name: ControlUp for Compliance API
  slug: controlup-for-compliance-api
- description: Historical analytics API for virtual desktop and DaaS estates — host metrics and counts per folder, user activity, machine statistics and AI-driven sizing recommendations for virtualization and Azure,
  name: ControlUp VDI and DaaS Historical API
  slug: controlup-vdi-and-daas-historical-api
- description: Real-time metrics API for VDI and DaaS environments, exposing live metric reads for monitored resources alongside the historical API. Bearer API-key auth.
  name: ControlUp VDI and DaaS Realtime Metrics API
  slug: controlup-vdi-and-daas-realtime-metrics-api
- description: 'Configuration API for the VDI and DaaS product — machine configuration management plus trigger configuration (trigger packs and their follow-up actions, including the RESTful-request webhook action). '
  name: ControlUp VDI and DaaS Configuration API
  slug: controlup-vdi-and-daas-configuration-api
- description: The largest published ControlUp surface — 128 paths and 149 operations covering DaaS IQ, ControlUp's cost-and-capacity intelligence layer for Azure Virtual Desktop, Windows 365 and other DaaS estates.
  name: ControlUp DaaS IQ API
  slug: controlup-daas-iq-api
- description: Synthetic monitoring API (the former Scoutbees product) — create and manage EUC Scouts that log into Citrix, Horizon, AVD and other virtual desktop stacks on a schedule, and Network Scouts that test H
  name: ControlUp Synthetic Monitoring API
  slug: controlup-synthetic-monitoring-api
- description: 'Workflow automation API — list, retrieve, enable/disable and delete flows, list flow runs, manage forms, and enumerate integrations together with their available actions, action input/output schemas, '
  name: ControlUp Workflows API
  slug: controlup-workflows-api
- description: Official Model Context Protocol server published by ControlUp as the npm package @controlup-ai/mcp. Runs locally over stdio via npx, authenticates with a ControlUp API key plus organization ID, and ex
  name: ControlUp MCP Server
  slug: controlup-mcp-server
artifact_total: 18
asyncapis:
- description: ''
  name: Controlup Webhooks
  slug: controlup-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/controlup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/controlup-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.controlup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.controlup.io/
- group: docs
  title: ''
  type: Documentation
  url: https://support.controlup.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.controlup.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.controlup.io/reference/how-to-make-api-requests-1
- group: operate
  title: ''
  type: Support
  url: https://support.controlup.com/
- group: company
  title: ''
  type: Blog
  url: https://www.controlup.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/controlup
- group: operate
  title: ''
  type: Roadmap
  url: https://support.controlup.com/docs/submit-and-vote-on-feature-requests
- group: commercial
  title: ''
  type: Pricing
  url: https://www.controlup.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.controlup.com/free-trial/
- group: start
  title: ''
  type: Login
  url: https://app.controlup.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.controlup.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.controlup.com/privacy-policy/controlup-privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.controlup.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.controlup.com/docs/release-notes
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.controlup.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.controlup.com/
- group: auth
  title: ''
  type: Security
  url: https://trustcenter.controlup.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/controlup-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/controlup-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/controlup-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/controlup-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/controlup-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/controlup-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/controlup-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/controlup-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/controlup-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/controlup-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/controlup-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/controlup-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/controlup-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.controlup.com/docs/controlup-product-version-lifecycle-quick-guide
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/controlup-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/controlup-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/controlup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/controlup-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/controlup-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-dex-platform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-dex-alerts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-dex-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-desktops-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-compliance-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-historical-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-realtime-metrics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-configuration-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-config-triggers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-daas-iq-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-synthetic-monitoring-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-workflows-overlay.yaml
created: '2026-08-04'
description: ControlUp is a Digital Employee Experience (DEX) and Autonomous Endpoint Management (AEM) platform that monitors, scores and remediates the end-user computing estate — physical desktops and laptops, VDI and DaaS (Citrix CVAD / Citrix Cloud, Omnissa Horizon, Azure Virtual Desktop, Windows 365, Parallels RAS), the applications and sessions running on them, and the network path in between. The ControlUp ONE platform spans ControlUp for Desktops, for VDI, for Apps, for Frontline Workers and for Compliance, plus Synthetic Monitoring (Scouts and Hives), Workflows, and Pulse AI. It publishes a public REST API surface at api.controlup.com documented on a ReadMe hub at api.controlup.io, an RFC 9727 /.well-known/api-catalog linkset enumerating twelve OpenAPI definitions, an official Model Context Protocol server on npm (@controlup-ai/mcp) exposing 106 tools across six product domains, PowerShell cmdlets for monitor and agent automation, and llms.txt indexes on both the documentation and
  API hosts.
image: https://www.controlup.com/wp-content/uploads/controlup_prev.webp
layout: provider
mcp_servers:
- description: ''
  name: controlup-mcp.yml
  slug: controlup-mcpyml
modified: '2026-08-04'
name: ControlUp
nav: Providers
network: true
overview: 'ControlUp publishes 10 APIs on the [APIs.io](https://apis.io/) network, including ONE Platform API, Events and Alerts API, for Desktops API, and 7 more. Tagged areas include digital-employee-experience, endpoint-management, vdi, daas, and virtual-desktop.


  The ControlUp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ControlUp''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 46 more developer resources.'
random_paper: 94
rate_limits:
- limit_count: 6
  name: Controlup Rate Limits
  slug: controlup-rate-limits
score:
  band: exemplar
  composite: 68.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.5
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 100.0
  previous_composite: 68.2
  provenance:
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Controlup Authentication
  slug: controlup-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Controlup Domain Security
  slug: controlup-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Controlup Vulnerability Disclosure
  slug: controlup-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Controlup Trust Center
  slug: controlup-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701:2019, SOC 2 Type 2, SOC 3, FIPS 140-2 Level 1, CSA STAR Level 1, GDPR
slug: controlup
tags:
- digital-employee-experience
- endpoint-management
- vdi
- daas
- virtual-desktop
- observability
- monitoring
- synthetic-monitoring
- device-management
- compliance
- vulnerability-management
- workflow-automation
- citrix
- azure-virtual-desktop
- mcp
- agent-native
website: https://www.controlup.com/
---
