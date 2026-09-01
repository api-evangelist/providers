---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Tray Ai Agentic Access
  operation_count: 35
  slug: tray-ai-agentic-access
  summary_line: 35 operations · 25 acting
api_count: 2
apis:
- description: Generate and manage user tokens for authenticating API calls. The authorize mutation generates a user token from a master token.
  name: Tray.ai Authentication API
  slug: tray-ai-authentication-api
- description: Create, retrieve, and delete third-party service authentications that power Tray connectors (e.g., Salesforce, Slack).
  name: Tray.ai Authentications API
  slug: tray-ai-authentications-api
- description: Call any Tray connector operation to pull data from a particular service and display it in your application.
  name: Tray.ai Call Connector API
  slug: tray-ai-call-connector-api
- description: List available connectors and their operations, and call connector operations to interact with third-party services programmatically.
  name: Tray.ai Connectors API
  slug: tray-ai-connectors-api
- description: Deploy CDK (Connector Development Kit) connectors to the Tray platform.
  name: Tray.ai Deployments API
  slug: tray-ai-deployments-api
- description: Manage projects and solutions for environment promotion, including creating, exporting, and importing project versions.
  name: Tray.ai Projects API
  slug: tray-ai-projects-api
- description: Create, update, enable, disable, and delete solution instances for end users. Requires a user token for most operations.
  name: Tray.ai Solution Instances API
  slug: tray-ai-solution-instances-api
- description: Retrieve solutions (integrations) that have been built and published on the Tray platform.
  name: Tray.ai Solutions API
  slug: tray-ai-solutions-api
- description: List available triggers and manage trigger subscriptions to receive real-time data from third-party services.
  name: Tray.ai Triggers API
  slug: tray-ai-triggers-api
- description: Manage external users of your embedded application. Requires a master token for most operations.
  name: Tray.ai Users API
  slug: tray-ai-users-api
- description: Import and export Tray workflows between embedded accounts, useful for promoting workflows from staging to production.
  name: Tray.ai Workflows API
  slug: tray-ai-workflows-api
- description: Manage workspaces and workspace users. Workspaces divide your organization into sub-categories such as departments or dev/prod environments.
  name: Tray.ai Workspaces API
  slug: tray-ai-workspaces-api
artifact_total: 102
collections:
- collection_type: postman
  name: Tray.ai Embedded Authentication API
  slug: postman-tray-ai-authentication-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Authentications API
  slug: postman-tray-ai-authentications-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Call Connector API
  slug: postman-tray-ai-call-connector-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Connectors API
  slug: postman-tray-ai-connectors-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Deployments API
  slug: postman-tray-ai-deployments-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Projects API
  slug: postman-tray-ai-projects-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Solution Instances API
  slug: postman-tray-ai-solution-instances-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Solutions API
  slug: postman-tray-ai-solutions-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Triggers API
  slug: postman-tray-ai-triggers-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Users API
  slug: postman-tray-ai-users-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Workflows API
  slug: postman-tray-ai-workflows-api
- collection_type: postman
  name: Tray.ai Embedded Authentication Workspaces API
  slug: postman-tray-ai-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tray.ai Embedded Authentication API
  slug: open-tray-ai-authentication-api
- collection_type: open
  name: Tray.ai Embedded Authentication Authentications API
  slug: open-tray-ai-authentications-api
- collection_type: open
  name: Tray.ai Embedded Authentication Call Connector API
  slug: open-tray-ai-call-connector-api
- collection_type: open
  name: Tray.ai Embedded Authentication Connectors API
  slug: open-tray-ai-connectors-api
- collection_type: open
  name: Tray.ai Embedded Authentication Deployments API
  slug: open-tray-ai-deployments-api
- collection_type: open
  name: Tray.ai Embedded API
  slug: open-tray-ai-embedded-api
- collection_type: open
  name: Tray.ai Platform API
  slug: open-tray-ai-platform-api
- collection_type: open
  name: Tray.ai Embedded Authentication Projects API
  slug: open-tray-ai-projects-api
- collection_type: open
  name: Tray.ai Embedded Authentication Solution Instances API
  slug: open-tray-ai-solution-instances-api
- collection_type: open
  name: Tray.ai Embedded Authentication Solutions API
  slug: open-tray-ai-solutions-api
- collection_type: open
  name: Tray.ai Embedded Authentication Triggers API
  slug: open-tray-ai-triggers-api
- collection_type: open
  name: Tray.ai Embedded Authentication Users API
  slug: open-tray-ai-users-api
- collection_type: open
  name: Tray.ai Embedded Authentication Workflows API
  slug: open-tray-ai-workflows-api
- collection_type: open
  name: Tray.ai Embedded Authentication Workspaces API
  slug: open-tray-ai-workspaces-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/trayai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tray-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tray-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tray-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tray-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trayio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tray-ai
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tray-ai-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: https://tray.ai/packages
- group: commercial
  title: ''
  type: PlansSpec
  url: plans/tray-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tray-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tray-ai-finops.yml
- group: start
  title: ''
  type: Login
  url: https://app.tray.io/login
- group: company
  title: ''
  type: Blog
  url: https://tray.ai/blog
- group: other
  title: ''
  type: CaseStudies
  url: https://tray.ai/customers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tray.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tray.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tray.ai/
- group: other
  title: ''
  type: AtomFeed
  url: https://status.tray.ai/history.atom
- group: other
  title: ''
  type: RSSFeed
  url: https://status.tray.ai/history.rss
- group: company
  title: ''
  type: Website
  url: https://tray.ai/
- group: start
  title: ''
  type: Portal
  url: https://tray.ai/documentation/developer/
- group: other
  title: ''
  type: Product
  url: https://tray.ai/documentation/agent-builder/
- group: other
  title: ''
  type: Product
  url: https://tray.ai/documentation/agent-hub/
- group: other
  title: ''
  type: Product
  url: https://tray.ai/
- group: other
  title: ''
  type: Product
  url: https://tray.ai/
- group: other
  title: ''
  type: Product
  url: https://tray.ai/products/embedded
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trayio/falafel
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trayio/threadneedle
- group: build
  title: ''
  type: Examples
  url: https://github.com/trayio/CDK-examples-public
- group: build
  title: ''
  type: Examples
  url: https://github.com/trayio/embedded-edition-sample-app
- group: build
  title: ''
  type: Tools
  url: https://github.com/trayio/connector-tester-public
- group: build
  title: ''
  type: Tools
  url: https://github.com/trayio/script-connector-tester
- group: build
  title: ''
  type: Tools
  url: https://github.com/trayio/embedded-customjs-public
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/tray-docs/tray-io-s-public-workspace
- group: commercial
  title: ''
  type: PlanTiers
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://tray.ai/llms.txt
created: '2025-06-05'
description: Tray.ai (formerly Tray.io) is an AI-ready enterprise orchestration platform for data and AI, combining a Merlin Agent Builder for no-code AI agent creation, an Agent Gateway for governed MCP server management, and an intelligent iPaaS with 700+ pre-built connectors. It exposes a REST Platform API (Connectivity API) and a GraphQL Embedded API for building, embedding, and operating AI agents and integration automations at enterprise scale.
examples:
- key_count: 2
  name: Tray Ai Call Connector Example
  slug: tray-ai-call-connector-example
- key_count: 2
  name: Tray Ai Create Authentication Example
  slug: tray-ai-create-authentication-example
- key_count: 2
  name: Tray Ai Create Solution Instance Example
  slug: tray-ai-create-solution-instance-example
- key_count: 2
  name: Tray Ai List Connectors Example
  slug: tray-ai-list-connectors-example
features:
- name: 700+ Connectors
- name: Merlin Agent Builder
- name: Agent Gateway for MCP
- name: Agent Hub
- name: Universal Automation Cloud
- name: Connectivity API
- name: Embedded Bundle
- name: Connector Development Kit (CDK)
- name: Connector Builder
- name: Composable Templates
- name: Auth API
- name: Auth Collector
- name: Management API
- name: Trigger API
- name: Workflows
- name: Workspaces
- name: Insights
- name: Intelligent Document Processing
- name: Log Streaming
- name: Log Retention
- name: Account Audit Log Streaming
- name: Advanced On-Prem
- name: Static IP for On-Prem
- name: HIPAA
- name: Multi-Factor Authentication
- name: Role-Based Access Control
- name: SSO
- name: Regional Hosting (US, EU, APAC)
- name: Tray Academy
- name: Tray Community
- name: In-App Support
- name: Dedicated Slack Channel
finops:
- name: Tray Ai Finops
  service_category: API
  slug: tray-ai-finops
graphqls:
- description: The Tray.ai Embedded API is a GraphQL-based API that allows partners and customers to present in-app embedded integration experiences. It provides programmatic access to manage users, solutions, solut
  name: Tray.ai GraphQL API
  slug: tray-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tray-ai.png
json_schemas:
- name: Tray.ai Authentication
  property_count: 7
  slug: authentication
- name: Tray.ai Connector
  property_count: 5
  slug: connector
- name: Tray.ai Solution Instance
  property_count: 10
  slug: solution-instance
- name: Tray.ai Solution
  property_count: 6
  slug: solution
- name: Tray.ai Trigger Subscription
  property_count: 8
  slug: subscription
- name: Tray.ai User
  property_count: 7
  slug: user
- name: Tray.ai Workspace
  property_count: 4
  slug: workspace
json_structures:
- name: Tray Ai Connector Structure
  property_count: 0
  slug: tray-ai-connector-structure
- name: Tray Ai Solution Instance Structure
  property_count: 0
  slug: tray-ai-solution-instance-structure
jsonld:
- class_count: 51
  name: Tray Ai Context
  property_count: 0
  slug: tray-ai-context
layout: provider
modified: '2026-05-22'
name: Tray.ai
nav: Providers
network: true
overview: 'Tray.ai publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Authentications API, Call Connector API, and 9 more. Tagged areas include Automation, Integration, iPaaS, AI Agents, and MCP.


  The Tray.ai catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tray.ai''s developer surface includes authentication, engineering blog, developer portal, code examples, tooling, and 31 more developer resources.'
plans:
- name: Tray Ai Plans Pricing
  plan_count: 3
  slug: tray-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 7
  name: Tray Ai Rate Limits
  slug: tray-ai-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tray.ai API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tray-ai-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Tray.ai API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: tray-ai-rules
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 41.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 28.8
    contract_quality: 73.7
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tray-ai/refs/heads/main/screenshots/tray-ai-2026-06-20T195639.png
security:
- kind: authentication
  name: Tray Ai Authentication
  slug: tray-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tray Ai Domain Security
  slug: tray-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tray Ai Trust Center
  slug: tray-ai-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: tray-ai
tags:
- Automation
- Integration
- iPaaS
- AI Agents
- MCP
use_cases:
- name: AI Agent Orchestration
- name: MCP Governance
- name: E-commerce
- name: Embedded integrations
- name: IT Onboarding
- name: Lead lifecycle
- name: Order-to-cash
website: https://tray.ai/
---
