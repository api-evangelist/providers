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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Logic Apps Agentic Access
  operation_count: 13
  slug: logic-apps-agentic-access
  summary_line: 13 operations · 6 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Inspect and cancel workflow runs.
  name: Azure Logic Apps WorkflowRuns API
  slug: logic-apps-workflowruns-api
- description: Manage Logic Apps workflows.
  name: Azure Logic Apps Workflows API
  slug: logic-apps-workflows-api
- description: Manage workflow triggers and their histories.
  name: Azure Logic Apps WorkflowTriggers API
  slug: logic-apps-workflowtriggers-api
- description: Manage versions of workflow definitions.
  name: Azure Logic Apps WorkflowVersions API
  slug: logic-apps-workflowversions-api
artifact_total: 13
collections:
- collection_type: open
  name: Azure Logic Apps Management API
  slug: open-logic-apps-management-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/logic-apps-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/logic-apps-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logic-apps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/logic-apps-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/logic-apps-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/logic-apps
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/logic-apps/
- group: docs
  title: ''
  type: Reference
  url: https://learn.microsoft.com/en-us/rest/api/logic/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/logic-apps/
created: '2026-03-27'
description: Azure Logic Apps is a cloud-based workflow automation service for integrating apps, data, and services across organizations. It provides a managed iPaaS platform with hundreds of connectors, a visual workflow designer, and a fully documented Azure Resource Manager REST API for managing workflows, runs, triggers and versions.
finops:
- name: Logic Apps Finops
  service_category: API
  slug: logic-apps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logic-apps.png
layout: provider
modified: '2026-05-19'
name: Azure Logic Apps
nav: Providers
network: true
overview: 'Azure Logic Apps publishes 4 APIs on the [APIs.io](https://apis.io/) network, including WorkflowRuns API, Workflows API, WorkflowTriggers API, and 1 more. Tagged areas include Azure, Enterprise, iPaaS, Integration, and Microsoft.


  Azure Logic Apps'' developer surface includes authentication, documentation, pricing, and 6 more developer resources.'
plans:
- name: Logic Apps Plans Pricing
  plan_count: 3
  slug: logic-apps-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Logic Apps Rate Limits
  slug: logic-apps-rate-limits
scopes:
- name: Logic Apps Scopes
  scope_count: 1
  slug: logic-apps-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 38.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.3
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logic-apps/refs/heads/main/screenshots/logic-apps-2026-06-20T184652.png
security:
- kind: authentication
  name: Logic Apps Authentication
  slug: logic-apps-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Logic Apps Domain Security
  slug: logic-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Logic Apps Vulnerability Disclosure
  slug: logic-apps-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: logic-apps
tags:
- Azure
- Enterprise
- iPaaS
- Integration
- Microsoft
- Workflow Automation
website: https://azure.microsoft.com/en-us/products/logic-apps
---
