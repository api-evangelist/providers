---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 29.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Attio Agentic Access
  operation_count: 45
  slug: attio-agentic-access
  summary_line: 45 operations · 23 acting
api_count: 16
apis:
- description: The Attributes API from Attio — 2 operation(s) for attributes.
  name: Attio Attributes API
  slug: attio-attributes-api
- description: The Call Recordings API from Attio — 1 operation(s) for call recordings.
  name: Attio Call Recordings API
  slug: attio-call-recordings-api
- description: The Comments API from Attio — 2 operation(s) for comments.
  name: Attio Comments API
  slug: attio-comments-api
- description: The Entries API from Attio — 1 operation(s) for entries.
  name: Attio Entries API
  slug: attio-entries-api
- description: The Files API from Attio — 1 operation(s) for files.
  name: Attio Files API
  slug: attio-files-api
- description: The Lists API from Attio — 2 operation(s) for lists.
  name: Attio Lists API
  slug: attio-lists-api
- description: The Meetings API from Attio — 2 operation(s) for meetings.
  name: Attio Meetings API
  slug: attio-meetings-api
- description: The Meta API from Attio — 1 operation(s) for meta.
  name: Attio Meta API
  slug: attio-meta-api
- description: The Notes API from Attio — 1 operation(s) for notes.
  name: Attio Notes API
  slug: attio-notes-api
- description: The OAuth API from Attio — 2 operation(s) for oauth.
  name: Attio OAuth API
  slug: attio-oauth-api
- description: The Objects API from Attio — 2 operation(s) for objects.
  name: Attio Objects API
  slug: attio-objects-api
- description: The Records API from Attio — 3 operation(s) for records.
  name: Attio Records API
  slug: attio-records-api
- description: The Tasks API from Attio — 1 operation(s) for tasks.
  name: Attio Tasks API
  slug: attio-tasks-api
- description: The Threads API from Attio — 1 operation(s) for threads.
  name: Attio Threads API
  slug: attio-threads-api
- description: The Webhooks API from Attio — 2 operation(s) for webhooks.
  name: Attio Webhooks API
  slug: attio-webhooks-api
- description: The Workspace Members API from Attio — 2 operation(s) for workspace members.
  name: Attio Workspace Members API
  slug: attio-workspace-members-api
artifact_total: 21
collections:
- collection_type: open
  name: Attio REST API
  slug: open-attio
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/attio-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/attio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/attio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/attio-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/attio
- group: company
  title: ''
  type: Website
  url: https://attio.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.attio.com
- group: commercial
  title: ''
  type: Pricing
  url: https://attio.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.attio.com/welcome/sign-in
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.attio.com/llms.txt
created: '2026-05-11'
description: Attio is a modern, flexible, and data-driven customer relationship management (CRM) platform that lets revenue teams build a CRM around their unique data model with customizable objects, attributes, lists, and workflows. Attio syncs contacts and companies from email and calendar, enriches them with data, and powers reporting, sequences, and automations. The Attio REST API exposes full CRUD access to records, lists, objects, attributes, tasks, notes, threads, comments, and webhooks using Bearer token authentication and a public OpenAPI specification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-11'
name: Attio
nav: Providers
network: true
overview: 'Attio publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Call Recordings API, Comments API, and 13 more. Tagged areas include CRM, Customer Relationship Management, Sales, Contacts, and Companies.


  Attio''s developer surface includes authentication, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 93
scopes:
- name: Attio Scopes
  scope_count: 7
  slug: attio-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 28.5
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 57.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/attio/refs/heads/main/screenshots/attio-2026-06-20T172546.png
security:
- kind: authentication
  name: Attio Authentication
  slug: attio-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Attio Domain Security
  slug: attio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: attio
tags:
- CRM
- Customer Relationship Management
- Sales
- Contacts
- Companies
- Pipeline
- Workflows
website: https://attio.com
---
