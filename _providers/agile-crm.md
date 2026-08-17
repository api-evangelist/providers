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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Agile Crm Agentic Access
  operation_count: 71
  slug: agile-crm-agentic-access
  summary_line: 71 operations · 44 acting
api_count: 11
apis:
- description: HTTPS-only REST API for managing contacts, companies, deals, campaigns, tasks, notes, and tickets in Agile CRM. Authentication uses HTTP Basic auth with the account email as username and the REST clie
  name: Agile CRM REST API
  slug: rest-api
- description: The Campaigns API from Agile CRM — 2 operation(s) for campaigns.
  name: Agile CRM Campaigns API
  slug: agile-crm-campaigns-api
- description: The Companies API from Agile CRM — 1 operation(s) for companies.
  name: Agile CRM Companies API
  slug: agile-crm-companies-api
- description: The Contacts API from Agile CRM — 18 operation(s) for contacts.
  name: Agile CRM Contacts API
  slug: agile-crm-contacts-api
- description: The Deals API from Agile CRM — 11 operation(s) for deals.
  name: Agile CRM Deals API
  slug: agile-crm-deals-api
- description: The Documents API from Agile CRM — 2 operation(s) for documents.
  name: Agile CRM Documents API
  slug: agile-crm-documents-api
- description: The Events API from Agile CRM — 3 operation(s) for events.
  name: Agile CRM Events API
  slug: agile-crm-events-api
- description: The HelpDesk API from Agile CRM — 5 operation(s) for helpdesk.
  name: Agile CRM HelpDesk API
  slug: agile-crm-helpdesk-api
- description: The Notes API from Agile CRM — 7 operation(s) for notes.
  name: Agile CRM Notes API
  slug: agile-crm-notes-api
- description: The Tasks API from Agile CRM — 6 operation(s) for tasks.
  name: Agile CRM Tasks API
  slug: agile-crm-tasks-api
- description: The Tracks API from Agile CRM — 2 operation(s) for tracks.
  name: Agile CRM Tracks API
  slug: agile-crm-tracks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Agile Crm Webhooks
  slug: agile-crm-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agile CRM REST Campaigns API
  slug: open-agile-crm-campaigns-api
- collection_type: open
  name: Agile CRM REST Campaigns Companies API
  slug: open-agile-crm-companies-api
- collection_type: open
  name: Agile CRM REST Campaigns Contacts API
  slug: open-agile-crm-contacts-api
- collection_type: open
  name: Agile CRM REST Campaigns Deals API
  slug: open-agile-crm-deals-api
- collection_type: open
  name: Agile CRM REST Campaigns Documents API
  slug: open-agile-crm-documents-api
- collection_type: open
  name: Agile CRM REST Campaigns Events API
  slug: open-agile-crm-events-api
- collection_type: open
  name: Agile CRM REST Campaigns HelpDesk API
  slug: open-agile-crm-helpdesk-api
- collection_type: open
  name: Agile CRM REST Campaigns Notes API
  slug: open-agile-crm-notes-api
- collection_type: open
  name: Agile CRM REST Campaigns Tasks API
  slug: open-agile-crm-tasks-api
- collection_type: open
  name: Agile CRM REST Campaigns Tracks API
  slug: open-agile-crm-tracks-api
- collection_type: open
  name: Agile CRM REST API
  slug: open-agile-crm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agile-crm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agile-crm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agile-crm-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agile-crm
- group: company
  title: ''
  type: Website
  url: https://www.agilecrm.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.agilecrm.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agilecrm.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.agilecrm.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.agilecrm.com/blog/feed/
- group: build
  title: ''
  type: Packages
  url: packages/agile-crm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agile-crm-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agile-crm-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agile-crm-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agile-crm-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agile-crm-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agile-crm-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agile-crm-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agile-crm-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agile-crm-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/agile-crm-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agile-crm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agile-crm-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agilecrm.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/agilecrm/rest-api/blob/master/README.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agilecrm
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agilecrm.com/setup-guides
- group: operate
  title: ''
  type: Support
  url: https://www.agilecrm.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agilecrm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agilecrm.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.agilecrm.com/login
- group: company
  title: ''
  type: Partners
  url: https://www.agilecrm.com/partners
created: '2026-05-11'
description: Agile CRM is an all-in-one customer relationship management platform aimed at small and mid-sized businesses, unifying contact management, sales pipeline tracking, marketing automation, helpdesk ticketing, and telephony in a single application. The platform offers visual workflow builders, email campaigns, landing pages, and web-to-lead forms with built-in reporting. The Agile CRM REST API exposes contacts, deals, campaigns, tasks, and tickets using HTTP Basic authentication with an email and API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agile-crm.png
layout: provider
mcp_servers:
- description: ''
  name: agile-crm-mcp.yml
  slug: agile-crm-mcpyml
modified: '2026-08-13'
name: Agile CRM
nav: Providers
network: true
overview: 'Agile CRM publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Companies API, Contacts API, and 7 more. Tagged areas include CRM, Sales Automation, Marketing Automation, Helpdesk, and Small Business.


  The Agile CRM catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agile CRM''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, API reference, getting-started guide, and 25 more developer resources.'
plans:
- name: Agile Crm Plans Pricing
  plan_count: 4
  slug: agile-crm-plans-pricing
random_paper: 136
rate_limits:
- limit_count: 0
  name: Agile Crm Rate Limits
  slug: agile-crm-rate-limits
score:
  band: strong
  composite: 58.5
  delta: 29.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 64.2
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/agile-crm/refs/heads/main/screenshots/agile-crm-2026-06-20T170154.png
security:
- kind: authentication
  name: Agile Crm Authentication
  slug: agile-crm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agile Crm Domain Security
  slug: agile-crm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agile-crm
tags:
- CRM
- Sales Automation
- Marketing Automation
- Helpdesk
- Small Business
- Contact Management
website: https://www.agilecrm.com
---
