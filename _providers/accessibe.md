---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Accessibe Agentic Access
  operation_count: 7
  slug: accessibe-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: The accessFlow Model Context Protocol server connects AI clients such as GitHub Copilot and Cursor directly to accessFlow accessibility data. It exposes three tools — getMostUrgentIssues, getIssueReme
  name: accessFlow MCP Server
  slug: accessflow-mcp
- baseURL: https://dashboard.accessibe.com/api/v1/partners
  baseurl_source: declared
  description: The Accounts API from accessiBe — 5 operation(s) for accounts.
  name: accessiBe Accounts API
  slug: accessibe-accounts-api
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
  name: accessiBe MCP Server
  slug: accessibe-mcp-server
modified: '2026-07-31'
name: accessiBe
nav: Providers
network: true
overview: 'accessiBe publishes 1 API on the [APIs.io](https://apis.io/) network: Accounts API. Tagged areas include Company, Accessibility, Web Accessibility, WCAG, and ADA Compliance.


  accessiBe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 44.4
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accessibe/refs/heads/main/screenshots/accessibe-2026-08-07T160757.png
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
