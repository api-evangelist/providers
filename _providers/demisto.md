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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 63
  human_in_the_loop: 2
  name: Demisto Agentic Access
  operation_count: 75
  slug: demisto-agentic-access
  summary_line: 75 operations · 63 acting · 2 human-in-the-loop
api_count: 24
apis:
- description: The Apikeys API from Demisto — 1 operation(s) for apikeys.
  name: Demisto Apikeys API
  slug: demisto-apikeys-api
- description: The Automation API from Demisto — 5 operation(s) for automation.
  name: Demisto Automation API
  slug: demisto-automation-api
- description: The Classifier API from Demisto — 1 operation(s) for classifier.
  name: Demisto Classifier API
  slug: demisto-classifier-api
- description: The Contentpacks API from Demisto — 1 operation(s) for contentpacks.
  name: Demisto Contentpacks API
  slug: demisto-contentpacks-api
- description: The Dashboards API from Demisto — 1 operation(s) for dashboards.
  name: Demisto Dashboards API
  slug: demisto-dashboards-api
- description: The Entry API from Demisto — 8 operation(s) for entry.
  name: Demisto Entry API
  slug: demisto-entry-api
- description: The Evidence API from Demisto — 3 operation(s) for evidence.
  name: Demisto Evidence API
  slug: demisto-evidence-api
- description: The Incident API from Demisto — 8 operation(s) for incident.
  name: Demisto Incident API
  slug: demisto-incident-api
- description: The Incidentfields API from Demisto — 2 operation(s) for incidentfields.
  name: Demisto Incidentfields API
  slug: demisto-incidentfields-api
- description: The Incidents API from Demisto — 1 operation(s) for incidents.
  name: Demisto Incidents API
  slug: demisto-incidents-api
- description: The Incidenttype API from Demisto — 1 operation(s) for incidenttype.
  name: Demisto Incidenttype API
  slug: demisto-incidenttype-api
- description: The Incidenttypes API from Demisto — 1 operation(s) for incidenttypes.
  name: Demisto Incidenttypes API
  slug: demisto-incidenttypes-api
- description: The Indicator API from Demisto — 3 operation(s) for indicator.
  name: Demisto Indicator API
  slug: demisto-indicator-api
- description: The Indicators API from Demisto — 8 operation(s) for indicators.
  name: Demisto Indicators API
  slug: demisto-indicators-api
- description: The Inv Playbook API from Demisto — 11 operation(s) for inv playbook.
  name: Demisto Inv Playbook API
  slug: demisto-inv-playbook-api
- description: The Investigations API from Demisto — 1 operation(s) for investigations.
  name: Demisto Investigations API
  slug: demisto-investigations-api
- description: The Layouts API from Demisto — 1 operation(s) for layouts.
  name: Demisto Layouts API
  slug: demisto-layouts-api
- description: The Playbook API from Demisto — 1 operation(s) for playbook.
  name: Demisto Playbook API
  slug: demisto-playbook-api
- description: The Report API from Demisto — 1 operation(s) for report.
  name: Demisto Report API
  slug: demisto-report-api
- description: The Reports API from Demisto — 4 operation(s) for reports.
  name: Demisto Reports API
  slug: demisto-reports-api
- description: The Reputation API from Demisto — 1 operation(s) for reputation.
  name: Demisto Reputation API
  slug: demisto-reputation-api
- description: The Settings API from Demisto — 3 operation(s) for settings.
  name: Demisto Settings API
  slug: demisto-settings-api
- description: The Statistics API from Demisto — 2 operation(s) for statistics.
  name: Demisto Statistics API
  slug: demisto-statistics-api
- description: The Widgets API from Demisto — 3 operation(s) for widgets.
  name: Demisto Widgets API
  slug: demisto-widgets-api
artifact_total: 28
common:
- group: company
  title: ''
  type: Website
  url: https://www.demisto.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://xsoar.pan.dev
- group: docs
  title: ''
  type: Documentation
  url: https://xsoar.pan.dev/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://xsoar.pan.dev/docs/reference/api/demisto-class
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Get-Started-with-APIs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demisto
- group: auth
  title: ''
  type: Authentication
  url: authentication/demisto-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/demisto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demisto-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/demisto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/demisto-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/demisto-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/demisto-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/demisto-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/demisto-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/demisto-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/demisto-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demisto-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paloaltonetworks.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://xsoar.pan.dev/docs/reference/integrations/demisto-rest-api
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/demisto-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demisto-llms.txt
created: '2026-07-17'
description: Demisto is a Security Orchestration, Automation, and Response (SOAR) platform that unifies incident case management, playbook-driven automation, real-time analyst collaboration (the "War Room"), and threat-intelligence management. Founded as an independent security startup backed by Accel and Greylock, Demisto was acquired by Palo Alto Networks in 2019 for roughly $560M and rebranded as Cortex XSOAR; the demisto.com domain now redirects to the Cortex XSOAR product. The Demisto REST API exposes incidents, war-room entries, evidence, threat indicators, and automation scripts programmatically, with a Swagger 2.0 specification, an official Python client (demisto-py), and a content-development SDK/CLI (demisto-sdk). This API Evangelist profile was enriched from the provider's public developer surface (xsoar.pan.dev, docs-cortex.paloaltonetworks.com, and the github.com/demisto organization).
image: https://avatars.githubusercontent.com/u/11011767?v=4
layout: provider
mcp_servers:
- description: ''
  name: demisto-mcp.yml
  slug: demisto-mcpyml
modified: '2026-07-18'
name: Demisto
nav: Providers
network: true
overview: 'Demisto publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Apikeys API, Automation API, Classifier API, and 21 more. Tagged areas include Company, Security, SOAR, Incident Response, and Threat Intelligence.


  Demisto''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, and 17 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 40.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.7
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 40.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demisto/refs/heads/main/screenshots/demisto-2026-07-25T211711.png
security:
- kind: authentication
  name: Demisto Authentication
  slug: demisto-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Demisto Domain Security
  slug: demisto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: demisto
tags:
- Company
- Security
- SOAR
- Incident Response
- Threat Intelligence
- Security Automation
website: https://www.demisto.com
---
