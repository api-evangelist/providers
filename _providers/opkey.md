---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 89
  human_in_the_loop: 6
  name: Opkey Agentic Access
  operation_count: 90
  slug: opkey-agentic-access
  summary_line: 90 operations · 89 acting · 6 human-in-the-loop
api_count: 16
apis:
- description: The official pCloudy MCP server, published by pCloudy as the Python package pcloudy-mcp and run over stdio with uvx. It exposes 36 tools across four groups — device booking, browser booking, app manag
  name: pCloudy MCP Server
  slug: pcloudy-mcp
- description: The Apk Instrumentation API from Opkey — 3 operation(s) for apk instrumentation.
  name: Opkey Apk Instrumentation API
  slug: opkey-apk-instrumentation-api
- description: The Apk Instrumentation Apis API from Opkey — 3 operation(s) for apk instrumentation apis.
  name: Opkey Apk Instrumentation Apis API
  slug: opkey-apk-instrumentation-apis-api
- description: The App Center Api API from Opkey — 5 operation(s) for app center api.
  name: Opkey App Center Api API
  slug: opkey-app-center-api-api
- description: The App Control API from Opkey — 4 operation(s) for app control.
  name: Opkey App Control API
  slug: opkey-app-control-api
- description: The Appium Automation API from Opkey — 11 operation(s) for appium automation.
  name: Opkey Appium Automation API
  slug: opkey-appium-automation-api
- description: The Authentication API from Opkey — 1 operation(s) for authentication.
  name: Opkey Authentication API
  slug: opkey-authentication-api
- description: The Device Booking & Session API from Opkey — 3 operation(s) for device booking & session.
  name: Opkey Device Booking & Session API
  slug: opkey-device-booking-session-api
- description: The Device Interaction API from Opkey — 8 operation(s) for device interaction.
  name: Opkey Device Interaction API
  slug: opkey-device-interaction-api
- description: The File Management API from Opkey — 2 operation(s) for file management.
  name: Opkey File Management API
  slug: opkey-file-management-api
- description: The Generic API from Opkey — 30 operation(s) for generic.
  name: Opkey Generic API
  slug: opkey-generic-api
- description: The Network Simulation API from Opkey — 5 operation(s) for network simulation.
  name: Opkey Network Simulation API
  slug: opkey-network-simulation-api
- description: The Performance API from Opkey — 1 operation(s) for performance.
  name: Opkey Performance API
  slug: opkey-performance-api
- description: The Resigning Apis API from Opkey — 3 operation(s) for resigning apis.
  name: Opkey Resigning Apis API
  slug: opkey-resigning-apis-api
- description: The Session Media & Logs API from Opkey — 5 operation(s) for session media & logs.
  name: Opkey Session Media & Logs API
  slug: opkey-session-media-logs-api
- description: The Xctest Automation API from Opkey — 6 operation(s) for xctest automation.
  name: Opkey Xctest Automation API
  slug: opkey-xctest-automation-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: pCloudy Device Cloud Apk Instrumentation API
  slug: open-opkey-apk-instrumentation-api
- collection_type: open
  name: pCloudy Device Cloud Apk Instrumentation Apis API
  slug: open-opkey-apk-instrumentation-apis-api
- collection_type: open
  name: pCloudy Device Cloud App Center Api API
  slug: open-opkey-app-center-api-api
- collection_type: open
  name: pCloudy Device Cloud App Control API
  slug: open-opkey-app-control-api
- collection_type: open
  name: pCloudy Device Cloud Appium Automation API
  slug: open-opkey-appium-automation-api
- collection_type: open
  name: pCloudy Device Cloud Authentication API
  slug: open-opkey-authentication-api
- collection_type: open
  name: pCloudy Device Cloud Device Booking & Session API
  slug: open-opkey-device-booking-session-api
- collection_type: open
  name: pCloudy Device Cloud Device Interaction API
  slug: open-opkey-device-interaction-api
- collection_type: open
  name: pCloudy Device Cloud File Management API
  slug: open-opkey-file-management-api
- collection_type: open
  name: pCloudy Device Cloud Generic API
  slug: open-opkey-generic-api
- collection_type: open
  name: pCloudy Device Cloud Network Simulation API
  slug: open-opkey-network-simulation-api
- collection_type: open
  name: pCloudy Device Cloud Performance API
  slug: open-opkey-performance-api
- collection_type: open
  name: pCloudy Device Cloud Resigning Apis API
  slug: open-opkey-resigning-apis-api
- collection_type: open
  name: pCloudy Device Cloud Session Media & Logs API
  slug: open-opkey-session-media-logs-api
- collection_type: open
  name: pCloudy Device Cloud Xctest Automation API
  slug: open-opkey-xctest-automation-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/opkey-pcloudy-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opkey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opkey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opkey.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pcloudy.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://content.pcloudy.com/apidocs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pcloudy.com/docs/mobile-app-testing/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.opkey.com/blog
- group: operate
  title: ''
  type: Support
  url: https://customerhub.opkey.com/support/solutions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Smart-Software-Testing-Solutions-Opkey
- group: start
  title: ''
  type: SignUp
  url: https://device.pcloudy.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pcloudy.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opkey.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opkey.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.opkey.com/security-and-trust
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opkey-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/opkey-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/opkey-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/opkey-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/opkey-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opkey-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opkey-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opkey-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opkey-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opkey-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Opkey (Smart Software Testing Solutions, Inc.) is a US-headquartered Cloud Application Lifecycle Management and AI-powered test automation vendor for enterprise packaged applications. Its no-code platform ships pre-built automated tests and change-impact analysis for Oracle Cloud/EBS, Workday, Salesforce, SAP, Coupa, Veeva, UKG/Kronos and Microsoft Dynamics, alongside an agentic layer (Argus AI, Testing/Configuration/Training/Impact-Analysis/PMO agents, Release Advisor and Maestro). Opkey also operates pCloudy, the real-device mobile and browser testing cloud it acquired, which carries the company''s public developer surface: a documented REST API for device booking, app upload/install, device interaction, performance capture, network simulation, Appium/XCTest orchestration and APK instrumentation, plus a published pCloudy MCP server that exposes device booking, app management and QPilot AI test authoring as tools to MCP clients. The core Opkey product help and user guides
  sit behind a customer login; the pCloudy documentation, API reference and release notes are public.'
image: https://content.pcloudy.com/apidocs/pcloudy-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: opkey-pcloudy-mcp.yml
  slug: opkey-pcloudy-mcpyml
modified: '2026-08-04'
name: Opkey
nav: Providers
network: true
overview: 'Opkey publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Apk Instrumentation API, Apk Instrumentation Apis API, App Center Api API, and 12 more. Tagged areas include Company, Testing, Test Automation, Quality Assurance, and DevOps.


  Opkey''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 19 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 50.1
  delta: -1.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 60.2
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opkey/refs/heads/main/screenshots/opkey-2026-08-07T190728.png
security:
- kind: authentication
  name: Opkey Authentication
  slug: opkey-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Opkey Domain Security
  slug: opkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opkey
tags:
- Company
- Testing
- Test Automation
- Quality Assurance
- DevOps
- Continuous Integration
- Mobile Testing
- Device Cloud
- ERP
- Artificial Intelligence
- Agents
- MCP
website: https://www.opkey.com/
---
