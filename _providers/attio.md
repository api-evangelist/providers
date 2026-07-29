---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 29.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Attio Agentic Access
  operation_count: 45
  slug: attio-agentic-access
  summary_line: 45 operations · 23 acting
api_count: 1
apis:
- description: 'Public REST API for the Attio CRM platform with full CRUD access to records, objects, attributes, lists, entries, tasks, notes, threads, comments, workspace members, and webhooks. Authentication uses '
  name: Attio REST API
  slug: rest-api
artifact_total: 6
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
overview: 'Attio publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include CRM, Customer Relationship Management, Sales, Contacts, and Companies.


  Attio''s developer surface includes authentication, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 71
scopes:
- name: Attio Scopes
  scope_count: 7
  slug: attio-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 23.6
  delta: -5.9
  facets:
    commercial_clarity: 10.5
    contract_quality: 40.3
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
