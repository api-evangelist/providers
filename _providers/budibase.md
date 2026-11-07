---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Budibase Agentic Access
  operation_count: 67
  slug: budibase-agentic-access
  summary_line: 67 operations · 43 acting
api_count: 1
apis:
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: Manage Budibase applications.
  name: Budibase Applications API
  slug: budibase-applications-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: Execute and search queries.
  name: Budibase Queries API
  slug: budibase-queries-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: Manage rows inside a table.
  name: Budibase Rows API
  slug: budibase-rows-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: Manage data tables inside an application.
  name: Budibase Tables API
  slug: budibase-tables-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: Manage Budibase users.
  name: Budibase Users API
  slug: budibase-users-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: The metrics API from Budibase — 1 operation(s) for metrics.
  name: Budibase Metrics API
  slug: budibase-metrics-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: The roles API from Budibase — 2 operation(s) for roles.
  name: Budibase Roles API
  slug: budibase-roles-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: The views API from Budibase — 3 operation(s) for views.
  name: Budibase Views API
  slug: budibase-views-api
- baseURL: https://budibase.app/api/public/v1
  baseurl_source: declared
  description: The workspaces API from Budibase — 7 operation(s) for workspaces.
  name: Budibase Workspaces API
  slug: budibase-workspaces-api
artifact_total: 37
asyncapis:
- description: ''
  name: Budibase Webhooks
  slug: budibase-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/budibase/finops/budibase-finops.yml
  title: ''
  type: FinOps
  url: finops/budibase-finops.yml
- group: other
  href: https://artifacts.apis.io/budibase/capabilities/budibase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/budibase-capability-edges.yml
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
  href: https://artifacts.apis.io/budibase/agentic-access/budibase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/budibase-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/budibase/security/budibase-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/budibase-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/budibase/security/budibase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/budibase-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/budibase/authentication/budibase-authentication.yml
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
- group: build
  href: https://artifacts.apis.io/budibase/packages/budibase-packages.yml
  title: ''
  type: Packages
  url: packages/budibase-packages.yml
- group: build
  href: https://artifacts.apis.io/budibase/packages/budibase-packages.yml
  title: ''
  type: SDKs
  url: packages/budibase-packages.yml
- group: build
  href: https://artifacts.apis.io/budibase/cli/budibase-cli.yml
  title: ''
  type: CLI
  url: cli/budibase-cli.yml
- group: design
  href: https://artifacts.apis.io/budibase/components/budibase-components.yml
  title: ''
  type: Components
  url: components/budibase-components.yml
- group: design
  href: https://artifacts.apis.io/budibase/conventions/budibase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/budibase-conventions.yml
- group: design
  href: https://artifacts.apis.io/budibase/errors/budibase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/budibase-problem-types.yml
- group: design
  href: https://artifacts.apis.io/budibase/data-model/budibase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/budibase-data-model.yml
- group: operate
  href: https://artifacts.apis.io/budibase/rate-limits/budibase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/budibase-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/budibase/plans/budibase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/budibase-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/budibase/lifecycle/budibase-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/budibase-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.budibase.com
- group: operate
  href: https://artifacts.apis.io/budibase/changelog/budibase-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/budibase-changelog.yml
- group: design
  href: https://artifacts.apis.io/budibase/conformance/budibase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/budibase-conformance.yml
- group: auth
  href: https://artifacts.apis.io/budibase/conformance/budibase-conformance.yml
  title: ''
  type: Compliance
  url: conformance/budibase-conformance.yml
- group: auth
  href: https://artifacts.apis.io/budibase/security/budibase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/budibase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Budibase/budibase/security/advisories/new
- group: design
  href: https://artifacts.apis.io/budibase/asyncapi/budibase-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/budibase-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/budibase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/budibase/mcp/budibase-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/budibase-mcp.yml
- group: other
  href: https://artifacts.apis.io/budibase/overlays/budibase-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/budibase-public-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/budibase/llms/budibase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/budibase-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.budibase.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.budibase.com/docs/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.budibase.com/docs/public-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Budibase
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
  url: https://docs.budibase.com/docs/hosting-methods
finops:
- has_sources: true
  method: derived
  name: Budibase Finops
  primary_unit: subscription
  service_category: ''
  slug: budibase-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/budibase.png
layout: provider
modified: '2026-09-04'
name: Budibase
nav: Providers
network: true
overview: 'Budibase publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Queries API, Rows API, and 6 more. Tagged areas include AI Agents, Automation, Internal Tools, Low-Code, and Open Source.


  The Budibase catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Budibase''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, signup flow, support, and 43 more developer resources.'
plans:
- name: Budibase Plans Pricing
  plan_count: 6
  slug: budibase-plans-pricing
- name: Budibase Price Estimates
  plan_count: 0
  slug: budibase-price-estimates
random_paper: 15
rate_limits:
- limit_count: 1
  name: Budibase Rate Limits
  slug: budibase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Budibase API Rules
  rule_count: 48
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 5
  slug: budibase-rules
score:
  band: strong
  composite: 65.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 57.5
    developer_ergonomics: 57.7
    discoverability: 73.2
    operational_transparency: 65.8
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/budibase/budibase-2026-06-20T173737.png
security:
- kind: authentication
  name: Budibase Authentication
  slug: budibase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Budibase Domain Security
  slug: budibase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Budibase Vulnerability Disclosure
  slug: budibase-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Budibase Trust Center
  slug: budibase-trust-center
  summary_line: ISO 27001, GDPR, SOC 1 / SOC 2
skill_count: 3
skills:
- name: budibase-manage-users-and-roles
  slug: budibase-manage-users-and-roles
- name: budibase-provision-workspace-app
  slug: budibase-provision-workspace-app
- name: budibase-read-and-write-rows
  slug: budibase-read-and-write-rows
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
