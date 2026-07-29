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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Capsule Crm Agentic Access
  operation_count: 27
  slug: capsule-crm-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 6
apis:
- description: REST API for managing Capsule parties (contacts and organisations), opportunities, projects (cases), tasks, users, tags, and custom fields. Each request must include an Authorization Bearer token obta
  name: Capsule CRM API v2
  slug: v2-api
- description: The Entries API from Capsule CRM — 2 operation(s) for entries.
  name: Capsule CRM Entries API
  slug: capsule-crm-entries-api
- description: The Opportunities API from Capsule CRM — 3 operation(s) for opportunities.
  name: Capsule CRM Opportunities API
  slug: capsule-crm-opportunities-api
- description: The Parties API from Capsule CRM — 4 operation(s) for parties.
  name: Capsule CRM Parties API
  slug: capsule-crm-parties-api
- description: The Projects API from Capsule CRM — 2 operation(s) for projects.
  name: Capsule CRM Projects API
  slug: capsule-crm-projects-api
- description: The Tasks API from Capsule CRM — 2 operation(s) for tasks.
  name: Capsule CRM Tasks API
  slug: capsule-crm-tasks-api
artifact_total: 11
collections:
- collection_type: open
  name: Capsule CRM API v2
  slug: open-capsule-crm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capsule-crm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capsule-crm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capsule-crm-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://capsulecrm.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.capsulecrm.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.capsulecrm.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://capsulecrm.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://capsulecrm.com/signup/
- group: operate
  title: ''
  type: Support
  url: https://support.capsulecrm.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capsule-crm
- group: company
  title: ''
  type: Blog
  url: https://capsulecrm.com/blog/
- group: agent
  title: ''
  type: MCPServer
  url: https://capsulecrm.com/blog/what-if-you-could-just-ask-your-crm-introducing-capsule-mcp/
created: '2026-05-11'
description: Capsule is a simple online CRM for small and midsize businesses that manages contacts, sales pipelines, tasks, projects, and email integration with a focus on ease of use. The Capsule API v2 is a REST/JSON service exposing parties (people and organisations), opportunities, projects, tasks, cases, users, and custom fields for integration with marketing, finance, and productivity tools. Authentication uses a Bearer token (personal access token or OAuth 2 access token) against the base URL https://api.capsulecrm.com/api/v2/.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capsule-crm.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-07-12'
name: Capsule CRM
nav: Providers
network: true
overview: 'Capsule CRM publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Entries API, Opportunities API, Parties API, and 2 more. Tagged areas include CRM, Sales, Contacts, Pipeline Management, and Tasks.


  Capsule CRM''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 31.6
  delta: -2.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 53.4
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 33.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/capsule-crm/refs/heads/main/screenshots/capsule-crm-2026-06-20T173943.png
security:
- kind: authentication
  name: Capsule Crm Authentication
  slug: capsule-crm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capsule Crm Domain Security
  slug: capsule-crm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capsule-crm
tags:
- CRM
- Sales
- Contacts
- Pipeline Management
- Tasks
- Projects
- SMB
website: https://capsulecrm.com
---
