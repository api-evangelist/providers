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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Budibase Agentic Access
  operation_count: 26
  slug: budibase-agentic-access
  summary_line: 26 operations · 17 acting
api_count: 1
apis:
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: spec
  description: Manage Budibase applications.
  name: Budibase Applications API
  slug: budibase-applications-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: spec
  description: Execute and search queries.
  name: Budibase Queries API
  slug: budibase-queries-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: spec
  description: Manage rows inside a table.
  name: Budibase Rows API
  slug: budibase-rows-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: spec
  description: Manage data tables inside an application.
  name: Budibase Tables API
  slug: budibase-tables-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: spec
  description: Manage Budibase users.
  name: Budibase Users API
  slug: budibase-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Budibase Public Applications API
  slug: open-budibase-applications-api
- collection_type: open
  name: Budibase Public Applications Queries API
  slug: open-budibase-queries-api
- collection_type: open
  name: Budibase Public Applications Rows API
  slug: open-budibase-rows-api
- collection_type: open
  name: Budibase Public Applications Tables API
  slug: open-budibase-tables-api
- collection_type: open
  name: Budibase Public Applications Users API
  slug: open-budibase-users-api
- collection_type: open
  name: Budibase Public API
  slug: open-budibase
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/budibase/budibase/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/budibase/budibase/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Budibase/budibase/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Budibase/budibase/blob/master/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Budibase/budibase/blob/master/.github/CONTRIBUTING.md
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
overview: 'Budibase publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Queries API, Rows API, and 2 more. Tagged areas include AI Agents, Automation, Internal Tools, Low-Code, and Open-Source.


  Budibase''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, signup flow, support, and 16 more developer resources.'
plans:
- name: Budibase Plans Pricing
  plan_count: 3
  slug: budibase-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Budibase Rate Limits
  slug: budibase-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -5.9
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 17.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: falling
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
- Open-Source
- Workflow-Automation
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
