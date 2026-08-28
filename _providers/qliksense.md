---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-26'
api_count: 13
apis:
- description: JSON-RPC WebSocket API for interacting with the Qlik Associative Engine, creating and manipulating apps, and building visualizations.
  name: Qlik Engine API
  slug: engine-api
- description: Manage Qlik Sense applications including creating, updating, publishing, and deleting apps in Qlik Cloud.
  name: Qlik Apps API
  slug: apps-api
- description: Manage users, groups, and authentication in Qlik Cloud tenants.
  name: Qlik Users API
  slug: users-api
- description: Manage shared and managed spaces for collaboration and content organization in Qlik Cloud.
  name: Qlik Spaces API
  slug: spaces-api
- description: Create and manage data connections to various data sources in Qlik Cloud.
  name: Qlik Data Connections API
  slug: data-connections-api
- description: Create and manage no-code automation workflows in Qlik Automate that connect applications together.
  name: Qlik Automations API
  slug: automations-api
- description: Trigger and manage data reload operations for Qlik Sense apps.
  name: Qlik Reload API
  slug: reloads-api
- description: Create and manage webhooks to provide other applications with real-time information from Qlik Cloud events.
  name: Qlik Webhooks API
  slug: webhooks-api
- description: Generate downloadable report assets from data with configurable templates and output formats.
  name: Qlik Reports API
  slug: reports-api
- description: Generate profile insights, create and manage ML experiments, deploy models, and run predictions in Qlik Cloud.
  name: Qlik Machine Learning API
  slug: ml-api
- description: Parse natural language queries with support for language configuration, visualization generation, and conversation context.
  name: Qlik Natural Language API
  slug: natural-language-api
- description: Configure and manage Qlik Cloud tenants including settings, licenses, and administrative operations.
  name: Qlik Tenants API
  slug: tenants-api
- description: Access events emitted upon each action taken in a tenant for detailed audit logging and compliance.
  name: Qlik Audits API
  slug: audits-api
artifact_total: 34
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qliksense-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://qlik.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: operate
  title: ''
  type: Support
  url: https://support.qlik.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog/
- group: build
  title: ''
  type: CLI
  url: https://qlik.dev/toolkits/qlik-cli/
- group: build
  title: ''
  type: SDKs
  url: https://qlik.dev/toolkits/qlik-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: learn
  title: ''
  type: Tutorials
  url: https://qlik.dev/tutorials/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlik.com/
- group: company
  title: ''
  type: Blog
  url: https://qlik.dev/changelog/tag/api/
created: '2024-01-15'
description: Collection of APIs for Qlik Sense, a business intelligence and visual analytics platform. Qlik provides REST APIs, WebSocket APIs, and developer tools for managing cloud tenants, applications, data connections, users, automations, and AI-powered analytics through the Qlik Cloud platform.
features:
- description: Qlik's unique Associative Engine enables dynamic data exploration without predefined queries or drill paths.
  name: Associative Engine
- description: Comprehensive REST API coverage for all Qlik Cloud resources including apps, data, users, and automation.
  name: 50+ REST APIs
- description: AutoML, natural language queries, and AI assistants for data-driven insights.
  name: AI-Powered Analytics
- description: Build automation workflows connecting Qlik with external applications without coding.
  name: No-Code Automation
- description: Event-driven architecture with webhooks for real-time notifications on platform events.
  name: Real-Time Webhooks
- description: Deploy Qlik Cloud across AWS, Azure, and GCP regions with global availability.
  name: Multi-Cloud Deployment
finops:
- name: Qliksense Finops
  service_category: API
  slug: qliksense-finops
image: /assets/icons/qliksense.png
integrations:
- description: Direct connectivity for analytics on Snowflake cloud data warehouse.
  name: Snowflake
- description: Integration with Databricks lakehouse for large-scale analytics workloads.
  name: Databricks
- description: Enterprise data connectivity for SAP ERP, BW, and HANA data sources.
  name: SAP
- description: CRM data integration for sales analytics and pipeline management.
  name: Salesforce
- description: Collaboration integration for sharing analytics insights and alerts in Slack.
  name: Slack
- description: Embed analytics and receive notifications within Microsoft Teams.
  name: Microsoft Teams
layout: provider
modified: '2026-04-18'
name: Qlik Sense APIs
nav: Providers
network: true
overview: 'Qlik Sense APIs publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Business Intelligence, Cloud, Data Visualization, and Enterprise.


  Qlik Sense APIs'' developer surface includes developer portal, getting-started guide, authentication, support, changelog, CLI, engineering blog, and 7 more developer resources.'
plans:
- name: Qliksense Plans Pricing
  plan_count: 3
  slug: qliksense-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Qliksense Rate Limits
  slug: qliksense-rate-limits
score:
  band: emerging
  composite: 24.5
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 22.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/screenshots/qliksense-2026-06-20T192343.png
security:
- kind: domain-security
  name: Qliksense Domain Security
  slug: qliksense-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: qliksense
tags:
- Analytics
- Business Intelligence
- Cloud
- Data Visualization
- Enterprise
use_cases:
- description: Embed interactive Qlik visualizations and dashboards in custom web applications.
  name: Embedded Analytics
- description: Automate data integration and transformation workflows using APIs and automation connectors.
  name: Data Pipeline Automation
- description: Enable business users to create and share analytics apps through the platform APIs.
  name: Self-Service BI
- description: Generate predictive analytics and natural language insights using ML and NLP APIs.
  name: AI-Powered Insights
- description: Manage multiple Qlik Cloud tenants programmatically for SaaS and enterprise deployments.
  name: Multi-Tenant Management
website: https://qlik.dev/
---
