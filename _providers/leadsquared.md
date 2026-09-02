---
access_model:
  confidence: high
  label: Sales-gated onboarding, list pricing published
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.leadsquared.com/sales-crm-pricing/
  - https://www.leadsquared.com/marketing-automation-pricing/
  - https://www.leadsquared.com/free-trial/
  trial: false
  try_now: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Leadsquared Agentic Access
  operation_count: 4
  slug: leadsquared-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: REST API for managing leads, opportunities, activities, tasks, users, campaigns, and other CRM resources in LeadSquared. Includes Sales CRM, Service CRM, Async, and Portal APIs along with Lapps, Batch
  name: LeadSquared REST API
  slug: rest-api
- description: Queued, retrying variants of the highest-volume LeadSquared write operations — Capture Leads, Update a Lead, Post an Activity on a Lead, Create a Lead and Activity, Capture Opportunities, Update an Op
  name: LeadSquared Async API
  slug: async-api
- description: Activity events on leads
  name: LeadSquared Activities API
  slug: leadsquared-activities-api
- description: Lead create, get, and search
  name: LeadSquared Leads API
  slug: leadsquared-leads-api
artifact_total: 17
asyncapis:
- description: ''
  name: Leadsquared Webhooks
  slug: leadsquared-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LeadSquared REST Activities API
  slug: open-leadsquared-activities-api
- collection_type: open
  name: LeadSquared REST Activities Leads API
  slug: open-leadsquared-leads-api
- collection_type: open
  name: LeadSquared REST API
  slug: open-leadsquared
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leadsquared-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leadsquared-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leadsquared-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadsquared
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leadsquared
- group: company
  title: ''
  type: Website
  url: https://www.leadsquared.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.leadsquared.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leadsquared.com/marketing-automation-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.leadsquared.com/book-demo/
- group: start
  title: ''
  type: Login
  url: https://login.leadsquared.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.leadsquared.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.leadsquared.com/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.leadsquared.com/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.leadsquared.com/
- group: company
  title: ''
  type: Blog
  url: https://www.leadsquared.com/learn/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/leadsquaredapi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leadsquared.com/leadsquared-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leadsquared.com/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/leadsquared-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leadsquared-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/leadsquared-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leadsquared-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leadsquared-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leadsquared-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leadsquared-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leadsquared-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leadsquared-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leadsquared-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leadsquared-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leadsquared-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leadsquared.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leadsquared-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leadsquared-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.leadsquared.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/leadsquared-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadsquared-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.leadsquared.com/security/
created: '2026-05-11'
description: LeadSquared is a marketing automation and CRM platform that helps businesses capture, manage, nurture, and convert leads across sales, marketing, and service workflows. It offers Sales CRM, Service CRM, marketing automation, field force automation, and a no-code/low-code platform for building industry-specific customer experiences. The LeadSquared REST API provides access to core platform resources like leads, opportunities, activities, tasks, and users using API key authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadsquared.png
layout: provider
mcp_servers:
- description: ''
  name: LeadSquared MCP Server
  slug: leadsquared-mcp-server
modified: '2026-08-13'
name: LeadSquared
nav: Providers
network: true
overview: 'LeadSquared publishes 3 APIs on the [APIs.io](https://apis.io/) network: REST API, Activities API, and Leads API. Tagged areas include Marketing Automation, CRM, Sales Automation, Lead Management, and Customer Engagement.


  The LeadSquared catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LeadSquared''s developer surface includes authentication, documentation, pricing, signup flow, API reference, getting-started guide, support, and 31 more developer resources.'
plans:
- name: Leadsquared Plans Pricing
  plan_count: 4
  slug: leadsquared-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 10
  name: Leadsquared Rate Limits
  slug: leadsquared-rate-limits
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 24
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 4.5
    contract_quality: 55.5
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leadsquared/refs/heads/main/screenshots/leadsquared-2026-06-20T184350.png
security:
- kind: authentication
  name: Leadsquared Authentication
  slug: leadsquared-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Leadsquared Domain Security
  slug: leadsquared-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Leadsquared Vulnerability Disclosure
  slug: leadsquared-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Leadsquared Trust Center
  slug: leadsquared-trust-center
  summary_line: ISO 27001:2022, GDPR
slug: leadsquared
tags:
- Marketing Automation
- CRM
- Sales Automation
- Lead Management
- Customer Engagement
- Field Force Automation
website: https://www.leadsquared.com
---
