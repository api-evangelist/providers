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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 89
  human_in_the_loop: 6
  name: Opkey Agentic Access
  operation_count: 90
  slug: opkey-agentic-access
  summary_line: 90 operations · 89 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: The public REST API for pCloudy, the real-device mobile and browser testing cloud operated by Opkey. It follows resource-oriented URLs, defaults every method to POST except authentication, and returns
  name: pCloudy Device Cloud API
  slug: pcloudy-api
- description: The official pCloudy MCP server, published by pCloudy as the Python package pcloudy-mcp and run over stdio with uvx. It exposes 36 tools across four groups — device booking, browser booking, app manag
  name: pCloudy MCP Server
  slug: pcloudy-mcp
artifact_total: 6
common:
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
overview: 'Opkey publishes 1 API on the [APIs.io](https://apis.io/) network: pCloudy Device Cloud API. Tagged areas include Company, Testing, Test Automation, Quality Assurance, and DevOps.


  Opkey''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 18 more developer resources.'
random_paper: 100
score:
  band: developing
  composite: 51.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 66.4
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
