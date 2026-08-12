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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Nodeping Agentic Access
  operation_count: 25
  slug: nodeping-agentic-access
  summary_line: 25 operations · 14 acting
api_count: 8
apis:
- description: The Accounts API from NodePing — 1 operation(s) for accounts.
  name: NodePing Accounts API
  slug: nodeping-accounts-api
- description: The Checks API from NodePing — 2 operation(s) for checks.
  name: NodePing Checks API
  slug: nodeping-checks-api
- description: The Contactgroups API from NodePing — 1 operation(s) for contactgroups.
  name: NodePing Contactgroups API
  slug: nodeping-contactgroups-api
- description: The Contacts API from NodePing — 1 operation(s) for contacts.
  name: NodePing Contacts API
  slug: nodeping-contacts-api
- description: The Info API from NodePing — 1 operation(s) for info.
  name: NodePing Info API
  slug: nodeping-info-api
- description: The Notifications API from NodePing — 1 operation(s) for notifications.
  name: NodePing Notifications API
  slug: nodeping-notifications-api
- description: The Results API from NodePing — 3 operation(s) for results.
  name: NodePing Results API
  slug: nodeping-results-api
- description: The Schedules API from NodePing — 1 operation(s) for schedules.
  name: NodePing Schedules API
  slug: nodeping-schedules-api
artifact_total: 18
collections:
- collection_type: open
  name: NodePing API
  slug: open-nodeping
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nodeping-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nodeping-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nodeping-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NodePing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nodeping
- group: company
  title: ''
  type: Website
  url: https://nodeping.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nodeping.com/docs-api.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/openapi/nodeping-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/json-schema/nodeping-check-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/json-ld/nodeping-context.jsonld
created: '2025-02-12'
description: NodePing provides uptime monitoring for websites and services with flat-rate plans that include unlimited international SMS notifications and unlimited users. The REST API exposes accounts, contacts, contact groups, schedules, checks, results, notifications, and probe info.
finops:
- name: Nodeping Finops
  service_category: API
  slug: nodeping-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nodeping.png
json_schemas:
- name: NodePing Check
  property_count: 21
  slug: nodeping-check
jsonld:
- class_count: 13
  name: Nodeping Context
  property_count: 0
  slug: nodeping-context
layout: provider
modified: '2026-05-19'
name: NodePing
nav: Providers
network: true
overview: 'NodePing publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Checks API, Contactgroups API, and 5 more. Tagged areas include Monitoring, Uptime, Notifications, and SaaS.


  The NodePing catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NodePing''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Nodeping Plans Pricing
  plan_count: 3
  slug: nodeping-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Nodeping Rate Limits
  slug: nodeping-rate-limits
rules:
- name: NodePing API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nodeping-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.1
  delta: -8.5
  facets:
    commercial_clarity: 15.8
    contract_quality: 63.4
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/nodeping/refs/heads/main/screenshots/nodeping-2026-06-20T190350.png
security:
- kind: authentication
  name: Nodeping Authentication
  slug: nodeping-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nodeping Domain Security
  slug: nodeping-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nodeping
tags:
- Monitoring
- Uptime
- Notifications
- SaaS
website: https://nodeping.com/
---
