---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Nimble Agentic Access
  operation_count: 28
  slug: nimble-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 8
apis:
- description: REST API for managing contacts, companies, deals, activities, tasks, and notes in Nimble CRM. Authentication uses an API key passed as a Bearer token in the Authorization header.
  name: Nimble REST API
  slug: rest-api
- description: The Contacts API from Nimble — 4 operation(s) for contacts.
  name: Nimble Contacts API
  slug: nimble-contacts-api
- description: The Deals API from Nimble — 3 operation(s) for deals.
  name: Nimble Deals API
  slug: nimble-deals-api
- description: The Fields API from Nimble — 3 operation(s) for fields.
  name: Nimble Fields API
  slug: nimble-fields-api
- description: The Messages API from Nimble — 2 operation(s) for messages.
  name: Nimble Messages API
  slug: nimble-messages-api
- description: The Notes API from Nimble — 3 operation(s) for notes.
  name: Nimble Notes API
  slug: nimble-notes-api
- description: The Pipelines API from Nimble — 3 operation(s) for pipelines.
  name: Nimble Pipelines API
  slug: nimble-pipelines-api
- description: The Users API from Nimble — 1 operation(s) for users.
  name: Nimble Users API
  slug: nimble-users-api
artifact_total: 13
collections:
- collection_type: open
  name: Nimble CRM API
  slug: open-nimble
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nimble-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nimble-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nimble-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nimble-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nimble.com/blog/feed/
created: '2026-05-11'
description: Nimble is a relationship-focused CRM that unifies contacts, communications, social profiles, calendar, and email into a single workspace for small businesses and sales teams. The platform enriches contact records with social and business data, supports pipeline management, group messaging, and workflow automation across Microsoft 365 and Google Workspace. Nimble's REST API exposes contacts, deals, activities, and tasks via Bearer token authentication for building integrations and syncing CRM data.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nimble.png
layout: provider
modified: '2026-05-11'
name: Nimble
nav: Providers
network: true
overview: 'Nimble publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Deals API, Fields API, and 4 more. Tagged areas include CRM, Sales, Contact Management, Relationship Management, and Marketing Automation.


  Nimble''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
random_paper: 61
scopes:
- name: Nimble Scopes
  scope_count: 3
  slug: nimble-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.2
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Nimble Authentication
  slug: nimble-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nimble Domain Security
  slug: nimble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nimble
tags:
- CRM
- Sales
- Contact Management
- Relationship Management
- Marketing Automation
- Pipeline Management
---
