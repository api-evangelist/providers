---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Folk Agentic Access
  operation_count: 39
  slug: folk-agentic-access
  summary_line: 39 operations · 22 acting
api_count: 1
apis:
- description: Operations related to companies.
  name: Folk Companies API
  slug: folk-companies-api
- description: Operations related to deals.
  name: Folk Deals API
  slug: folk-deals-api
- description: Operations related to groups.
  name: Folk Groups API
  slug: folk-groups-api
- description: Operations related to interactions.
  name: Folk Interactions API
  slug: folk-interactions-api
- description: Operations related to notes.
  name: Folk Notes API
  slug: folk-notes-api
- description: Operations related to people.
  name: Folk People API
  slug: folk-people-api
- description: Operations related to reminders.
  name: Folk Reminders API
  slug: folk-reminders-api
- description: Operations related to users.
  name: Folk Users API
  slug: folk-users-api
- description: Operations related to webhooks.
  name: Folk Webhooks API
  slug: folk-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Folk External API
  slug: open-folk-app
- collection_type: open
  name: Folk External Companies API
  slug: open-folk-companies-api
- collection_type: open
  name: Folk External Companies Deals API
  slug: open-folk-deals-api
- collection_type: open
  name: Folk External Companies Groups API
  slug: open-folk-groups-api
- collection_type: open
  name: Folk External Companies Interactions API
  slug: open-folk-interactions-api
- collection_type: open
  name: Folk External Companies Notes API
  slug: open-folk-notes-api
- collection_type: open
  name: Folk External Companies People API
  slug: open-folk-people-api
- collection_type: open
  name: Folk External Companies Reminders API
  slug: open-folk-reminders-api
- collection_type: open
  name: Folk External Companies Users API
  slug: open-folk-users-api
- collection_type: open
  name: Folk External Companies Webhooks API
  slug: open-folk-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/folk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/folk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/folk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.folk.app/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.folk.app/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/folk-js
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/folkhq/
- group: company
  title: ''
  type: Blog
  url: https://www.folk.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.folk.app/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.folk.app/
- group: other
  title: ''
  type: X
  url: https://twitter.com/FolkHQ
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/folk-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/folk-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/folk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/folk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/folk-finops.yml
created: '2026-06-12'
description: Folk is a collaborative CRM platform designed for agencies, investors, and sales teams who need to manage relationships at scale. It provides a REST API organized around predictable resource-oriented URLs, accepting and returning JSON-encoded payloads with standard HTTP response codes. The API enables developers to manage contacts (people and companies), pipelines and deals, notes, reminders, interactions, and custom fields programmatically. Webhooks are supported for real-time event notifications, and the platform integrates with 5,000+ tools including Gmail, Outlook, LinkedIn, WhatsApp, and Zapier. API access is available on the Premium and Enterprise plans.
examples:
- key_count: 1
  name: Folk Examples
  slug: folk-examples
finops:
- name: Folk Finops
  service_category: CRM / Contact Management
  slug: folk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/folk.png
json_schemas:
- name: Folk API Schemas
  property_count: 0
  slug: folk-schemas
jsonld:
- class_count: 28
  name: Folk Context
  property_count: 26
  slug: folk-context
layout: provider
modified: '2026-06-12'
name: Folk
nav: Providers
network: true
overview: 'Folk publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Deals API, Groups API, and 6 more. Tagged areas include CRM, Contacts, Pipelines, Sales, and Relationships.


  The Folk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Folk''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Folk Plans Pricing
  plan_count: 3
  slug: folk-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Folk Rate Limits
  slug: folk-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Folk API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: folk-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 29.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 76.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 42.1
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/folk/refs/heads/main/screenshots/folk-2026-07-25T214908.png
security:
- kind: authentication
  name: Folk Authentication
  slug: folk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Folk Domain Security
  slug: folk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: folk
tags:
- CRM
- Contacts
- Pipelines
- Sales
- Relationships
- Notes
- Deals
- Webhook
website: https://www.folk.app/
---
