---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Logic Apps Agentic Access
  operation_count: 7
  slug: microsoft-azure-logic-apps-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure Logic Apps Operations API
  slug: microsoft-azure-logic-apps-operations-api
- description: Workflows operations
  name: Azure Logic Apps Workflows API
  slug: microsoft-azure-logic-apps-workflows-api
artifact_total: 25
collections:
- collection_type: open
  name: Azure Logic Apps REST API
  slug: open-microsoft-azure-logic-apps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-logic-apps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-logic-apps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-logic-apps-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-logic-apps-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/logic-apps/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/logic-apps/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Logic Apps is a cloud platform for creating and running automated workflows that integrate apps, data, services, and systems. It provides a visual designer and over 400 connectors to build event-driven, scheduled, and on-demand integrations.
features:
- description: Build workflows visually using a drag-and-drop designer in the Azure portal or Visual Studio Code.
  name: Visual Workflow Designer
- description: Connect to hundreds of SaaS apps, databases, file systems, and Azure services with prebuilt connectors.
  name: 400+ Connectors
- description: Start workflows from HTTP requests, scheduled timers, file changes, or events from connected services.
  name: Event-Driven Triggers
- description: Process EDI, AS2, X12, and EDIFACT messages with integration accounts for partner-to-partner workflows.
  name: B2B Integration
- description: Run long-running stateful workflows or short-lived stateless workflows for low-latency scenarios.
  name: Stateful and Stateless Workflows
- description: Connect to on-premises data sources using on-premises data gateways and integration service environments.
  name: Hybrid Connectivity
finops:
- name: Microsoft Azure Logic Apps Finops
  service_category: API
  slug: microsoft-azure-logic-apps-finops
image: https://azure.microsoft.com/svghandler/logic-apps/
integrations:
- description: Invoke Azure Functions from workflows for custom code execution.
  name: Azure Functions
- description: Send and receive messages through Azure Service Bus queues and topics.
  name: Azure Service Bus
- description: Integrate with Outlook, SharePoint, OneDrive, and Teams using Office 365 connectors.
  name: Office 365
- description: Connect to Salesforce CRM for record creation, updates, and event-driven workflows.
  name: Salesforce
- description: Expose and manage workflow endpoints through Azure API Management.
  name: Azure API Management
layout: provider
modified: '2026-05-19'
name: Azure Logic Apps
nav: Providers
network: true
overview: 'Azure Logic Apps publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Workflows API. Tagged areas include Automation, Azure, Integration, iPaaS, and Workflow.


  Azure Logic Apps'' developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Microsoft Azure Logic Apps Plans Pricing
  plan_count: 3
  slug: microsoft-azure-logic-apps-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Microsoft Azure Logic Apps Rate Limits
  slug: microsoft-azure-logic-apps-rate-limits
scopes:
- name: Microsoft Azure Logic Apps Scopes
  scope_count: 1
  slug: microsoft-azure-logic-apps-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 49.4
  delta: -1.1
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-logic-apps/refs/heads/main/screenshots/microsoft-azure-logic-apps-2026-06-20T185421.png
security:
- kind: authentication
  name: Microsoft Azure Logic Apps Authentication
  slug: microsoft-azure-logic-apps-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Logic Apps Domain Security
  slug: microsoft-azure-logic-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-logic-apps
tags:
- Automation
- Azure
- Integration
- iPaaS
- Workflow
use_cases:
- description: Connect SaaS apps, databases, and on-premises systems for end-to-end business process automation.
  name: Enterprise Application Integration
- description: Exchange business documents with partners using industry-standard EDI protocols.
  name: B2B and EDI Processing
- description: Trigger workflows based on events from Azure services, third-party APIs, or scheduled timers.
  name: Event-Driven Automation
- description: Transform and route data between systems using built-in mapping and conversion capabilities.
  name: Data Transformation
website: https://portal.azure.com/
---
