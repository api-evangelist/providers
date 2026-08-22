---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: Appfire Agentic Access
  operation_count: 41
  slug: appfire-agentic-access
  summary_line: 41 operations · 27 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: Public REST API for BigPicture, BigGantt and BigTemplate on Atlassian Cloud (Appfire's portfolio and project-management suite). Exposes boxes, box types, tasks, teams, team memberships, resources, ski
  name: BigPicture Cloud Public API
  slug: bigpicture-cloud-public-api
- description: 'Retrieve objectives, key results, updates, and comments. Use **expand** to include related entities (teams, periods, labels, etc.) instead of IDs only. Authenticate with the **API-Token** header. For '
  name: Appfire API query methods API
  slug: appfire-api-query-methods-api
- description: '**POST** with a JSON body. Send **Content-Type: application/json** and the **API-Token** header. Creates update records that set current status (and key-result progress where applicable).'
  name: Appfire API update methods API
  slug: appfire-api-update-methods-api
- description: The Settings API from Appfire — 16 operation(s) for settings.
  name: Appfire Settings API
  slug: appfire-settings-api
- description: The Worklogs API from Appfire — 10 operation(s) for worklogs.
  name: Appfire Worklogs API
  slug: appfire-worklogs-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OKR API query methods API
  slug: open-appfire-api-query-methods-api
- collection_type: open
  name: OKR API update methods API
  slug: open-appfire-api-update-methods-api
- collection_type: open
  name: Appfire Settings API
  slug: open-appfire-settings-api
- collection_type: open
  name: Appfire Worklogs API
  slug: open-appfire-worklogs-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appfire-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appfire-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/appfire-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appfire-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appfire-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://appfire.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bigpicture.one/
- group: docs
  title: ''
  type: Documentation
  url: https://appfire.atlassian.net/wiki/spaces/APPFIRE/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bigpicture.one/reference/whatisbigpicture
- group: operate
  title: ''
  type: Support
  url: https://support.appfire.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appfire.com/
- group: company
  title: ''
  type: Blog
  url: https://appfire.com/resources/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appfire.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appfire.com/eula
- group: auth
  title: ''
  type: Compliance
  url: https://trust.appfire.com/
- group: build
  title: ''
  type: Packages
  url: packages/appfire-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appfire-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/appfire-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appfire-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appfire-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appfire-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appfire-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appfire-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appfire-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appfire-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/appfire-okr-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appfire-7pace-timetracker-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/appfire-7pace-timetracker-v1-overlay.yaml
created: '2026-08-06'
description: 'Appfire is a global software company that builds, acquires, and operates a large portfolio of apps that enhance, extend, and connect the platforms enterprise teams already run on — principally Atlassian Jira, Confluence and Jira Service Management (Cloud and Data Center), plus Microsoft Azure DevOps, monday.com and Salesforce. Its product families cover portfolio and project management (BigPicture, BigGantt, BigTemplate), goal setting (OKR for Jira), time tracking (7pace Timetracker for Jira and for Azure DevOps), document workflow and approvals (Comala Document Management), workflow automation and scripting (Jira Misc Workflow Extensions, Power Scripts), and administration tooling (the Appfire/Atlassian Command Line Interface). Public, machine-readable API surface is per-product rather than company-wide: 7pace Timetracker for Jira publishes OpenAPI 3.0 for its v1 and v2 REST APIs, the OKR app serves an OpenAPI 3.1 document for its public export/update API, and BigPicture publishes
  a hosted API reference for its Cloud and Data Center REST APIs.'
layout: provider
mcp_servers:
- description: ''
  name: appfire-mcp.yml
  slug: appfire-mcpyml
modified: '2026-08-06'
name: Appfire
nav: Providers
network: true
overview: 'Appfire publishes 4 APIs on the [APIs.io](https://apis.io/) network, including API query methods API, API update methods API, Settings API, and 1 more. Tagged areas include atlassian, jira, confluence, project-portfolio-management, and work-management.


  Appfire''s developer surface includes authentication, documentation, API reference, support, engineering blog, CLI, changelog, and 22 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 45.3
  delta: -3.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 16.7
    contract_quality: 60.7
    developer_ergonomics: 49.4
    discoverability: 88.9
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appfire/refs/heads/main/screenshots/appfire-2026-08-07T161502.png
security:
- kind: authentication
  name: Appfire Authentication
  slug: appfire-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Appfire Domain Security
  slug: appfire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Appfire Trust Center
  slug: appfire-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, HIPAA, GDPR
slug: appfire
tags:
- atlassian
- jira
- confluence
- project-portfolio-management
- work-management
- time-tracking
- okr
- workflow-automation
- azure-devops
- marketplace-apps
- document-workflow
- enterprise-software
website: https://appfire.com
---
