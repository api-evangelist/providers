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
- acting_count: 17
  human_in_the_loop: 0
  name: Budibase Agentic Access
  operation_count: 26
  slug: budibase-agentic-access
  summary_line: 26 operations · 17 acting
api_count: 5
apis:
- description: Manage Budibase applications.
  name: Budibase Applications API
  slug: budibase-applications-api
- description: Execute and search queries.
  name: Budibase Queries API
  slug: budibase-queries-api
- description: Manage rows inside a table.
  name: Budibase Rows API
  slug: budibase-rows-api
- description: Manage data tables inside an application.
  name: Budibase Tables API
  slug: budibase-tables-api
- description: Manage Budibase users.
  name: Budibase Users API
  slug: budibase-users-api
artifact_total: 21
collections:
- collection_type: open
  name: Budibase Public API
  slug: open-budibase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/budibase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/budibase-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/budibase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/budibase-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/budibase
- group: company
  title: ''
  type: Website
  url: https://budibase.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.budibase.com
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/budibase/budibase
- group: company
  title: ''
  type: Blog
  url: https://budibase.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://budibase.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://budibase.com/changelog
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/budibase-733030666647765003
- group: start
  title: ''
  type: Signup
  url: https://account.budibase.app/register
- group: start
  title: ''
  type: Login
  url: https://account.budibase.app/auth/login
- group: operate
  title: ''
  type: Support
  url: https://budibase.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://budibase.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://budibase.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.budibase.com/llms.txt
created: '2026-03-27'
description: Budibase is an open source low-code platform for building AI agents, internal tools, and workflow automations. It enables teams to connect databases, spreadsheets, and business systems, then build applications and automations on top without extensive coding. Used by over 300,000 teams ranging from SMEs to government organizations, Budibase accelerates the delivery of internal business applications and process automation.
features:
- features:
  - PostgreSQL
  - MySQL
  - MongoDB
  - REST APIs
  - Google Sheets
  - Airtable
  - S3
  - Redis
  - CouchDB
  - Oracle
  - Microsoft SQL Server
  name: Data Sources
  url: https://budibase.com/product/connections
- features:
  - Drag-and-Drop UI Builder
  - Pre-Built Components
  - Custom JavaScript
  - Responsive Layouts
  - Multi-Page Apps
  - Screen Templates
  - Role-Based Permissions
  name: App Building
  url: https://budibase.com/product/apps
- features:
  - Visual API Explorer
  - REST Endpoint Creation
  - Query Builder
  - Response Mapping
  - Authentication Configuration
  name: API Builder
  url: https://budibase.com/product/apis
- features:
  - Docker Deployment
  - Kubernetes Support
  - DigitalOcean App Platform
  - AWS Deployment
  - On-Premises Support
  - Air-Gapped Deployments
  name: Self-Hosting
  url: https://docs.budibase.com/docs/self-hosting
finops:
- name: Budibase Finops
  service_category: API
  slug: budibase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/budibase.png
layout: provider
modified: '2026-04-21'
name: Budibase
nav: Providers
network: true
overview: 'Budibase publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Queries API, Rows API, and 2 more. Tagged areas include AI Agents, Automation, Internal Tools, Low-Code, and Open Source.


  Budibase''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, signup flow, support, and 11 more developer resources.'
plans:
- name: Budibase Plans Pricing
  plan_count: 3
  slug: budibase-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Budibase Rate Limits
  slug: budibase-rate-limits
score:
  band: developing
  composite: 49.6
  delta: -1.8
  facets:
    commercial_clarity: 92.1
    contract_quality: 53.4
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/budibase/refs/heads/main/screenshots/budibase-2026-06-20T173737.png
security:
- kind: authentication
  name: Budibase Authentication
  slug: budibase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Budibase Domain Security
  slug: budibase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Budibase Trust Center
  slug: budibase-trust-center
  summary_line: ISO 27001, GDPR
slug: budibase
tags:
- AI Agents
- Automation
- Internal Tools
- Low-Code
- Open Source
- Workflow Automation
use_cases:
- features:
  - Database-Connected Apps
  - CRUD Interfaces
  - Role-Based Access Control
  - Multi-Step Forms
  - Admin Panels
  - Approval Workflows
  name: Internal App Building
  url: https://budibase.com/product/apps
- features:
  - Employee Request Handling
  - Question Answering Across Channels
  - Support Ticket Triage
  - Automated Routing
  - Process Automation
  name: AI Agents
  url: https://budibase.com/product/agents
- features:
  - Approval Workflows
  - Notification Routing
  - Scheduled Automations
  - Trigger-Based Actions
  - Webhook Integrations
  - Multi-Step Pipelines
  name: Workflow Automation
  url: https://budibase.com/product/automations
- features:
  - Database Connections
  - Spreadsheet Import
  - REST API Integration
  - Data Tables
  - Schema Management
  - Data Transformations
  name: Data Management
  url: https://budibase.com/product/data
website: https://budibase.com
---
