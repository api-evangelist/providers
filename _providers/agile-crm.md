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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
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
artifact_total: 15
collections:
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
created: '2026-05-11'
description: Agile CRM is an all-in-one customer relationship management platform aimed at small and mid-sized businesses, unifying contact management, sales pipeline tracking, marketing automation, helpdesk ticketing, and telephony in a single application. The platform offers visual workflow builders, email campaigns, landing pages, and web-to-lead forms with built-in reporting. The Agile CRM REST API exposes contacts, deals, campaigns, tasks, and tickets using HTTP Basic authentication with an email and API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agile-crm.png
layout: provider
modified: '2026-05-11'
name: Agile CRM
nav: Providers
network: true
overview: 'Agile CRM publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Companies API, Contacts API, and 7 more. Tagged areas include CRM, Sales Automation, Marketing Automation, Helpdesk, and Small Business.


  Agile CRM''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 4 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 26.4
  delta: -2.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
