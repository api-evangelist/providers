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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Microsoft Power Automate Agentic Access
  operation_count: 18
  slug: microsoft-power-automate-agentic-access
  summary_line: 18 operations · 9 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.flow.microsoft.com
  baseurl_source: declared
  description: Operations for managing connections
  name: Microsoft Power Automate Connections API
  slug: microsoft-power-automate-connections-api
- baseURL: https://api.flow.microsoft.com
  baseurl_source: declared
  description: Operations for managing connectors
  name: Microsoft Power Automate Connectors API
  slug: microsoft-power-automate-connectors-api
- baseURL: https://api.flow.microsoft.com
  baseurl_source: declared
  description: Operations for managing Power Automate environments
  name: Microsoft Power Automate Environments API
  slug: microsoft-power-automate-environments-api
- baseURL: https://api.flow.microsoft.com
  baseurl_source: declared
  description: Operations for managing flow sharing and ownership
  name: Microsoft Power Automate Flow Permissions API
  slug: microsoft-power-automate-flow-permissions-api
- baseURL: https://api.flow.microsoft.com
  baseurl_source: declared
  description: Operations for managing flow run history
  name: Microsoft Power Automate Flow Runs API
  slug: microsoft-power-automate-flow-runs-api
- baseURL: https://api.flow.microsoft.com
  baseurl_source: declared
  description: Operations for managing cloud flows
  name: Microsoft Power Automate Flows API
  slug: microsoft-power-automate-flows-api
arazzos:
- description: Find a run that is still executing, confirm it is live, and cancel it.
  name: Microsoft Power Automate Cancel an In-Flight Run
  slug: microsoft-power-automate-cancel-running-run-workflow
- description: Resolve the connectors and connections a single flow depends on.
  name: Microsoft Power Automate Audit a Flow's Connector Dependencies
  slug: microsoft-power-automate-connector-dependency-audit-workflow
- description: Walk every environment and inventory its flows, connections, and connectors.
  name: Microsoft Power Automate Environment Inventory
  slug: microsoft-power-automate-environment-inventory-workflow
- description: Confirm a flow is request-triggered, fetch its callback URL, and observe the resulting run.
  name: Microsoft Power Automate Retrieve a Flow Trigger Callback URL
  slug: microsoft-power-automate-flow-callback-url-workflow
- description: Read a flow's current owners, add or remove owners, and verify the new roster.
  name: Microsoft Power Automate Manage Flow Owners
  slug: microsoft-power-automate-manage-flow-owners-workflow
- description: Create a new cloud flow in an environment, turn it on, and read back its state.
  name: Microsoft Power Automate Provision and Activate a Flow
  slug: microsoft-power-automate-provision-flow-workflow
- description: Check a flow for in-flight runs, deactivate it, and then delete it.
  name: Microsoft Power Automate Retire a Flow Safely
  slug: microsoft-power-automate-retire-flow-workflow
- description: Stop a running flow, update its definition, restart it, and verify the result.
  name: Microsoft Power Automate Safely Update a Live Flow
  slug: microsoft-power-automate-safe-update-flow-workflow
- description: Find a failed run in a flow's history, inspect it, and resubmit its trigger.
  name: Microsoft Power Automate Triage and Resubmit a Failed Run
  slug: microsoft-power-automate-triage-failed-run-workflow
artifact_total: 77
collections:
- collection_type: postman
  name: Microsoft Power Automate Management Connections API
  slug: postman-microsoft-power-automate-connections-api
- collection_type: postman
  name: Microsoft Power Automate Management Connections Connectors API
  slug: postman-microsoft-power-automate-connectors-api
- collection_type: postman
  name: Microsoft Power Automate Management Connections Environments API
  slug: postman-microsoft-power-automate-environments-api
- collection_type: postman
  name: Microsoft Power Automate Management Connections Flow Permissions API
  slug: postman-microsoft-power-automate-flow-permissions-api
- collection_type: postman
  name: Microsoft Power Automate Management Connections Flow Runs API
  slug: postman-microsoft-power-automate-flow-runs-api
- collection_type: postman
  name: Microsoft Power Automate Management Connections Flows API
  slug: postman-microsoft-power-automate-flows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Power Automate Management Connections API
  slug: open-microsoft-power-automate-connections-api
- collection_type: open
  name: Microsoft Power Automate Management Connections Connectors API
  slug: open-microsoft-power-automate-connectors-api
- collection_type: open
  name: Microsoft Power Automate Management Connections Environments API
  slug: open-microsoft-power-automate-environments-api
- collection_type: open
  name: Microsoft Power Automate Management Connections Flow Permissions API
  slug: open-microsoft-power-automate-flow-permissions-api
- collection_type: open
  name: Microsoft Power Automate Management Connections Flow Runs API
  slug: open-microsoft-power-automate-flow-runs-api
- collection_type: open
  name: Microsoft Power Automate Management Connections Flows API
  slug: open-microsoft-power-automate-flows-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-power-automate-management-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-power-automate/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-automate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-automate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-power-automate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-power-automate-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-power-automate-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-power-automate-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-power-automate-security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/microsoft-power-automate-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-power-automate-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-power-automate-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-power-automate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-power-automate-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-power-automate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-power-automate-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-power-automate-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-power-automate-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-power-automate-cli.yml
- group: design
  title: ''
  type: Components
  url: components/microsoft-power-automate-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-power-automate-data-model.yml
- group: start
  title: ''
  type: Portal
  url: https://make.powerautomate.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/power-automate/
- group: company
  title: ''
  type: Blog
  url: https://powerautomate.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://powerautomate.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powerplatform.microsoft.com/
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/powerplatform/power-automate
- group: commercial
  title: ''
  type: Pricing
  url: https://powerautomate.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/PowerApps-Samples
- group: design
  title: ''
  type: JSONLD
  url: json-ld/microsoft-power-automate-management-api-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-power-automate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-power-automate-vocabulary.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-environment-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-provision-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-safe-update-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-retire-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-triage-failed-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-cancel-running-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-manage-flow-owners-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-connector-dependency-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-power-automate-flow-callback-url-workflow.yml
created: '2024'
description: Microsoft Power Automate is a cloud-based service that helps you create automated workflows between your favorite apps and services to synchronize files, get notifications, collect data, and automate business processes. It supports automated, instant, and scheduled cloud flows, as well as desktop flows for robotic process automation.
examples:
- key_count: 2
  name: Power Automate Management Api Connector Example
  slug: power-automate-management-api-connector-example
- key_count: 3
  name: Power Automate Management Api Environment Example
  slug: power-automate-management-api-environment-example
- key_count: 4
  name: Power Automate Management Api Flow Example
  slug: power-automate-management-api-flow-example
- key_count: 4
  name: Power Automate Management Api Flow Run Example
  slug: power-automate-management-api-flow-run-example
features:
- description: Create event-triggered automations that run when specific events occur.
  name: Automated Cloud Flows
- description: Start automations on demand with the push of a button.
  name: Instant Cloud Flows
- description: Run automations on a recurring schedule.
  name: Scheduled Cloud Flows
- description: Automate desktop and legacy application tasks using robotic process automation.
  name: Desktop Flows (RPA)
- description: Create flows using natural language descriptions powered by AI.
  name: Copilot Integration
- description: Connect to over 1000 pre-built connectors for Microsoft and third-party services.
  name: 1000+ Connectors
- description: Build custom connectors using OpenAPI definitions.
  name: Custom Connectors
- description: Start from pre-built templates for common automation scenarios.
  name: Flow Templates
- description: Build approval workflows with built-in support for multi-stage approvals.
  name: Approval Workflows
- description: Configure error handling, retry policies, and notifications for flow failures.
  name: Error Handling
finops:
- name: Microsoft Power Automate Finops
  service_category: API
  slug: microsoft-power-automate-finops
image: https://powerautomate.microsoft.com/images/application-logos/svg/powerautomate.svg
integrations:
- description: Deep integration with SharePoint, Outlook, Teams, and other Microsoft 365 apps.
  name: Microsoft 365
- description: Native integration with Dataverse for data storage and management.
  name: Microsoft Dataverse
- description: Connect to Azure Logic Apps, Functions, and other Azure services.
  name: Azure Services
- description: Automate business processes within Dynamics 365 CRM and ERP.
  name: Dynamics 365
- description: Connect to SAP systems for enterprise process automation.
  name: SAP
- description: Integrate with Salesforce for CRM automation workflows.
  name: Salesforce
json_schemas:
- name: Connector
  property_count: 2
  slug: power-automate-management-api-connector
- name: Environment
  property_count: 3
  slug: power-automate-management-api-environment
- name: FlowRun
  property_count: 4
  slug: power-automate-management-api-flow-run
- name: Flow
  property_count: 4
  slug: power-automate-management-api-flow
json_structures:
- name: Power Automate Management Api Connector Structure
  property_count: 2
  slug: power-automate-management-api-connector-structure
- name: Power Automate Management Api Environment Structure
  property_count: 3
  slug: power-automate-management-api-environment-structure
- name: Power Automate Management Api Flow Run Structure
  property_count: 4
  slug: power-automate-management-api-flow-run-structure
- name: Power Automate Management Api Flow Structure
  property_count: 4
  slug: power-automate-management-api-flow-structure
jsonld:
- class_count: 6
  name: Microsoft Power Automate Management Api Context
  property_count: 17
  slug: microsoft-power-automate-management-api-context
layout: provider
modified: '2026-06-20'
name: Microsoft Power Automate
nav: Providers
network: true
overview: 'Microsoft Power Automate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Connectors API, Environments API, and 3 more. Tagged areas include Automation, Business Process, Integration, Low-Code, and Microsoft.


  The Microsoft Power Automate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Power Automate''s developer surface includes authentication, changelog, CLI, developer portal, engineering blog, support, training material, and 36 more developer resources.'
plans:
- name: Microsoft Power Automate Plans Pricing
  plan_count: 3
  slug: microsoft-power-automate-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Microsoft Power Automate Rate Limits
  slug: microsoft-power-automate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Power Automate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-power-automate-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Microsoft Power Automate API Rules
  rule_count: 28
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 11
  slug: microsoft-power-automate-spectral-rules
scopes:
- name: Microsoft Power Automate Scopes
  scope_count: 1
  slug: microsoft-power-automate-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 32
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 33.3
    contract_quality: 31.7
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 36.8
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 71.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-power-automate/refs/heads/main/screenshots/microsoft-power-automate-2026-08-17T083607.png
security:
- kind: authentication
  name: Microsoft Power Automate Authentication
  slug: microsoft-power-automate-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Power Automate Domain Security
  slug: microsoft-power-automate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Power Automate Vulnerability Disclosure
  slug: microsoft-power-automate-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Power Automate Trust Center
  slug: microsoft-power-automate-trust-center
  summary_line: SOC 1, SOC 2 Type II, ISO 27001, ISO 27018, HIPAA, FedRAMP Moderate, FedRAMP High, PCI DSS, GDPR
slug: microsoft-power-automate
solutions:
- description: Premium plan with advanced connectors, AI Builder, and process mining.
  name: Power Automate Premium
- description: Per-process licensing for unattended RPA and hosted machines.
  name: Power Automate Process
- description: Hosted machine groups for scaling desktop automation.
  name: Power Automate Hosted
tags:
- Automation
- Business Process
- Integration
- Low-Code
- Microsoft
- Power Platform
- RPA
- Workflows
use_cases:
- description: Automatically process, route, and respond to emails based on content or sender.
  name: Email Automation
- description: Keep data synchronized across multiple systems and applications.
  name: Data Synchronization
- description: Automate business approval workflows across teams and departments.
  name: Approval Processes
- description: Automate document creation, routing, and archival workflows.
  name: Document Processing
- description: Automate IT helpdesk tickets, provisioning, and monitoring workflows.
  name: IT Process Automation
- description: Track brand mentions and automatically respond or alert teams.
  name: Social Media Monitoring
website: https://learn.microsoft.com/en-us/power-automate/
---
