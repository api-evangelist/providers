---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Accessibe Agentic Access
  operation_count: 7
  slug: accessibe-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 2
apis:
- description: 'The Partners API allows accessiBe partners to manage accessWidget licenses programmatically across their accounts, with full control over the license lifecycle: create, retrieve, list, filter and upda'
  name: accessiBe Partners API License
  slug: partners-api
- description: The accessFlow Model Context Protocol server connects AI clients such as GitHub Copilot and Cursor directly to accessFlow accessibility data. It exposes three tools — getMostUrgentIssues, getIssueReme
  name: accessFlow MCP Server
  slug: accessflow-mcp
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accessibe-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/accessibe-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accessibe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accessibe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.accessibe.com/api/v1/partners/docs
- group: docs
  title: ''
  type: Documentation
  url: https://accessibe.com/support
- group: docs
  title: ''
  type: APIReference
  url: https://dashboard.accessibe.com/api/v1/partners/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://accessibe.com/accessflow-integrate
- group: operate
  title: ''
  type: Support
  url: https://accessibe.com/support
- group: company
  title: ''
  type: Blog
  url: https://accessibe.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://accessibe.com/pricing/accesswidget
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.accessibe.com/app/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.accessibe.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accessibe.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accessibe.com/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accessibe.com
- group: auth
  title: ''
  type: Compliance
  url: https://accessibe.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.accessibe.com/hc/en-us/categories/15274937179922-Release-Notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/accessibe-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accessibe-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/accessibe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/accessibe-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/accessibe-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/accessibe-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accessibe-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accessibe-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/accessibe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accessibe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accessibe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accessibe-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accessibe-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/accessibe-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/accessibe-partners-overlay.yaml
created: '2026-07-31'
description: accessiBe is a web accessibility technology company whose products help organizations make websites and web applications usable by people with disabilities and compliant with WCAG, the ADA, Section 508, AODA and the European Accessibility Act. Its portfolio spans accessWidget (an AI-driven remediation layer and end-user accessibility interface installed via an embed script), accessScan (a free single-URL compliance checker), accessFlow (a developer-first accessibility testing and monitoring platform with an SDK for Playwright, Cypress and Selenium plus CI/CD integrations), and accessServices (expert audits, user testing by people with disabilities, file and PDF remediation, and VPAT authoring). Developer surfaces include a documented Partners API for programmatic accessWidget license management and a first-party accessFlow MCP server that connects IDE AI assistants to accessibility audit findings and remediation guidance.
image: https://accessibe.com/wp-content/uploads/2026/01/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: accessibe-mcp.yml
  slug: accessibe-mcpyml
modified: '2026-07-31'
name: accessiBe
nav: Providers
network: true
overview: 'accessiBe publishes 1 API on the [APIs.io](https://apis.io/) network: Partners API License. Tagged areas include Company, Accessibility, Web Accessibility, WCAG, and ADA Compliance.


  accessiBe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 26
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 56.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
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
  name: Accessibe Authentication
  slug: accessibe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Accessibe Domain Security
  slug: accessibe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accessibe Trust Center
  slug: accessibe-trust-center
  summary_line: SOC 2, GDPR
slug: accessibe
tags:
- Company
- Accessibility
- Web Accessibility
- WCAG
- ADA Compliance
- Compliance
- Developer Tools
- Testing
- Quality Assurance
- Artificial Intelligence
website: https://accessibe.com
---
