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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Hibob Agentic Access
  operation_count: 28
  slug: hibob-agentic-access
  summary_line: 28 operations · 23 acting
api_count: 10
apis:
- description: REST API for managing employee data, time off, tasks, documents, and lifecycle events in HiBob. Authentication uses HTTP Basic with an API service user ID and token (Base64-encoded).
  name: Bob Public API
  slug: public-api
- description: Webhooks for receiving real-time notifications of employee lifecycle and data change events from HiBob to drive downstream automation.
  name: Bob Webhooks
  slug: webhooks
- description: The Attendance API from HiBob — 4 operation(s) for attendance.
  name: HiBob Attendance API
  slug: hibob-attendance-api
- description: The Documents API from HiBob — 3 operation(s) for documents.
  name: HiBob Documents API
  slug: hibob-documents-api
- description: The Employee Tables API from HiBob — 4 operation(s) for employee tables.
  name: HiBob Employee Tables API
  slug: hibob-employee-tables-api
- description: The Goals API from HiBob — 3 operation(s) for goals.
  name: HiBob Goals API
  slug: hibob-goals-api
- description: The Hiring API from HiBob — 4 operation(s) for hiring.
  name: HiBob Hiring API
  slug: hibob-hiring-api
- description: The Learning API from HiBob — 2 operation(s) for learning.
  name: HiBob Learning API
  slug: hibob-learning-api
- description: The People API from HiBob — 4 operation(s) for people.
  name: HiBob People API
  slug: hibob-people-api
- description: The Projects API from HiBob — 3 operation(s) for projects.
  name: HiBob Projects API
  slug: hibob-projects-api
artifact_total: 14
collections:
- collection_type: open
  name: Bob (HiBob) Public API
  slug: open-hibob
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hibob-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hibob-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hibob-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hibob
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hibob
- group: company
  title: ''
  type: Website
  url: https://www.hibob.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.hibob.com/
- group: operate
  title: ''
  type: Support
  url: https://help.hibob.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hibob.com/pricing/
- group: agent
  title: ''
  type: LlmsText
  url: https://api.hibob.com/llms.txt
created: '2026-05-11'
description: HiBob (Bob) is a modern HR platform for growing companies, providing core HRIS, employee data management, time off, performance, compensation, workflows, surveys, and people analytics. The Bob Public API enables programmatic access to employee data, time off, tasks, documents, and events via webhooks for HRIS integrations and people-data automation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hibob.png
layout: provider
modified: '2026-05-11'
name: HiBob
nav: Providers
network: true
overview: 'HiBob publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Attendance API, Documents API, Employee Tables API, and 5 more. Tagged areas include HR, HRIS, People Operations, Employee Data, and Time Off.


  HiBob''s developer surface includes authentication, documentation, support, pricing, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 26.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 47.8
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hibob/refs/heads/main/screenshots/hibob-2026-06-20T182725.png
security:
- kind: authentication
  name: Hibob Authentication
  slug: hibob-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hibob Domain Security
  slug: hibob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hibob
tags:
- HR
- HRIS
- People Operations
- Employee Data
- Time Off
- HR Tech
website: https://www.hibob.com
---
