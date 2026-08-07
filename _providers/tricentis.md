---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 271
  human_in_the_loop: 5
  name: Tricentis Agentic Access
  operation_count: 507
  slug: tricentis-agentic-access
  summary_line: 507 operations · 271 acting · 5 human-in-the-loop
api_count: 9
apis:
- description: The core Tricentis qTest test management REST API — projects, releases, modules, requirements, test cases, test steps, test cycles, test suites, test runs, test logs, defects, attachments, users, fiel
  name: qTest Manager API v3
  slug: qtest-manager
- description: The Tricentis qTest Parameters REST API for data-driven testing — parameters, parameter values, datasets, dataset rows and asynchronous tasks, scoped per qTest project.
  name: qTest Parameters API
  slug: qtest-parameters
- description: The Tricentis qTest Pulse REST API for event-driven test automation orchestration — rules, triggers, actions, constants, executions and projects.
  name: qTest Pulse API
  slug: qtest-pulse
- description: The Tricentis qTest Scenario REST API for BDD/Gherkin assets — features and steps synchronized between qTest and Jira.
  name: qTest Scenario API
  slug: qtest-scenario
- description: The Tricentis qTest Explorer Sessions REST API for exploratory testing — sessions, screens, application and system information, resources, coverage, view settings and script generation.
  name: qTest Explorer Sessions API
  slug: qtest-sessions
- description: The Tricentis qTest Data Export API, which issues signed access to exported qTest data files for downstream analytics and reporting warehouses.
  name: qTest Data Export API
  slug: qtest-data-export
- description: The Tricentis Analytics OData v4 API exposing quality-engineering entity sets — projects, releases, builds, defects, folders, execution summaries, test runs, run logs, requirements and traceability li
  name: Tricentis Analytics API
  slug: analytics
- description: The Tricentis NeoLoad Web REST API for continuous performance testing — workspaces, projects, test settings, test results, scenarios, SLA profiles, monitors, infrastructure providers, zones and resour
  name: NeoLoad API v3
  slug: neoload
- description: The Tricentis Test Management for Jira (TTM4J) REST API — test-case folders, test cases, test-case search (including JQL), requirements linking, automation results, test cycles and jobs, scoped by Jir
  name: Tricentis Test Management for Jira API
  slug: ttm4j
artifact_total: 17
asyncapis:
- description: ''
  name: Tricentis Qtest Webhooks
  slug: tricentis-qtest-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tricentis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tricentis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tricentis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tricentis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tricentis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tricentis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tricentis.com/all/home.htm
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.tricentis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.qasymphony.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tricentis.com/qtest-saas/content/apis/overview/how_to_use_interactive_api_documentation.htm
- group: company
  title: ''
  type: Blog
  url: https://www.tricentis.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.tricentis.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://shiftsync.tricentis.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tricentis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tricentis.com/products/unified-test-management-qtest/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.tricentis.com/software-testing-tool-trial-demo/qtest-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tricentis.com/legal-information/general-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tricentis.com/legal-information/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tricentis.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.tricentis.com/trust/security
- group: auth
  title: ''
  type: Security
  url: https://www.tricentis.com/trust/vulnerability-disclosure-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tricentis.com/qtest-saas/content/release_notes_and_announcements/release_notes_landing_page.htm
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tricentis-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tricentis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tricentis-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tricentis-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tricentis-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tricentis-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tricentis-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tricentis-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tricentis-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.tricentis.com/qtest-saas/content/release_notes_and_announcements/end_of_support_announcements.htm
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tricentis-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tricentis-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/tricentis-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tricentis-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/tricentis-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tricentis-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tricentis-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tricentis-qtest-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tricentis-qtest-manager-overlay.yaml
created: '2026-08-02'
description: Tricentis is an enterprise continuous testing and quality engineering company, founded in Austria in 2007 and headquartered in Vienna with US operations in Austin, Texas. Its platform spans model-based UI and API test automation (Tosca, Tosca Cloud), AI-driven test management (qTest), performance testing (NeoLoad), Jira-native test management (Tricentis Test Management for Jira), SAP change impact analysis (LiveCompare), data and ETL validation (Data Integrity), regulated-industry validation (Vera), and quality analytics. Tricentis exposes machine-readable REST contracts for qTest Manager, Parameters, Pulse, Scenario, Sessions, Data Export and Analytics, for NeoLoad Web, and for Tricentis Test Management for Jira, and it was among the first enterprise quality-engineering vendors to ship remote Model Context Protocol (MCP) servers plus an open-source, Apache-2.0 catalog of agent skills for driving Tosca and qTest from AI coding assistants.
image: https://be.tricentis.com/media-assets/2022/08/Tricentis-Logo-1-1120x446-1.png
layout: provider
mcp_servers:
- description: ''
  name: tricentis-mcp.yml
  slug: tricentis-mcpyml
modified: '2026-08-02'
name: Tricentis
nav: Providers
network: true
overview: 'Tricentis publishes 9 APIs on the [APIs.io](https://apis.io/) network, including qTest Manager API v3, qTest Parameters API, qTest Pulse API, and 6 more. Tagged areas include Company, Testing, Test Automation, Quality Engineering, and Test Management.


  The Tricentis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tricentis'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 35 more developer resources.'
random_paper: 77
scopes:
- name: Tricentis Scopes
  scope_count: 1
  slug: tricentis-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 62.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.9
    developer_ergonomics: 87.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 12.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Tricentis Authentication
  slug: tricentis-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Tricentis Domain Security
  slug: tricentis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tricentis Vulnerability Disclosure
  slug: tricentis-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Tricentis Trust Center
  slug: tricentis-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO 9001, GDPR
slug: tricentis
tags:
- Company
- Testing
- Test Automation
- Quality Engineering
- Test Management
- Performance Testing
- Continuous Testing
- DevOps
- SAP
- Data Integrity
- Agentic Testing
website: https://www.tricentis.com/
---
