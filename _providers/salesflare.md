---
access_model:
  confidence: medium
  label: Paid (free trial) · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Salesflare Agentic Access
  operation_count: 72
  slug: salesflare-agentic-access
  summary_line: 72 operations · 37 acting · 1 human-in-the-loop
api_count: 20
apis:
- description: The Accounts API from Salesflare — 6 operation(s) for accounts.
  name: Salesflare Accounts API
  slug: salesflare-accounts-api
- description: The AI Message Feedbacks API from Salesflare — 2 operation(s) for ai message feedbacks.
  name: Salesflare AI Message Feedbacks API
  slug: salesflare-ai-message-feedbacks-api
- description: The AISetings API from Salesflare — 1 operation(s) for aisetings.
  name: Salesflare AISetings API
  slug: salesflare-aisetings-api
- description: The AISettings API from Salesflare — 1 operation(s) for aisettings.
  name: Salesflare AISettings API
  slug: salesflare-aisettings-api
- description: The Calls API from Salesflare — 2 operation(s) for calls.
  name: Salesflare Calls API
  slug: salesflare-calls-api
- description: The Contacts API from Salesflare — 2 operation(s) for contacts.
  name: Salesflare Contacts API
  slug: salesflare-contacts-api
- description: The Custom Fields API from Salesflare — 4 operation(s) for custom fields.
  name: Salesflare Custom Fields API
  slug: salesflare-custom-fields-api
- description: The Email Data Sources API from Salesflare — 2 operation(s) for email data sources.
  name: Salesflare Email Data Sources API
  slug: salesflare-email-data-sources-api
- description: The Filter Fields API from Salesflare — 1 operation(s) for filter fields.
  name: Salesflare Filter Fields API
  slug: salesflare-filter-fields-api
- description: The Groups API from Salesflare — 2 operation(s) for groups.
  name: Salesflare Groups API
  slug: salesflare-groups-api
- description: The Internal Notes API from Salesflare — 2 operation(s) for internal notes.
  name: Salesflare Internal Notes API
  slug: salesflare-internal-notes-api
- description: The Meetings API from Salesflare — 3 operation(s) for meetings.
  name: Salesflare Meetings API
  slug: salesflare-meetings-api
- description: The Opportunities API from Salesflare — 2 operation(s) for opportunities.
  name: Salesflare Opportunities API
  slug: salesflare-opportunities-api
- description: The Persons API from Salesflare — 1 operation(s) for persons.
  name: Salesflare Persons API
  slug: salesflare-persons-api
- description: The Pipelines API from Salesflare — 3 operation(s) for pipelines.
  name: Salesflare Pipelines API
  slug: salesflare-pipelines-api
- description: The Regional Settings API from Salesflare — 1 operation(s) for regional settings.
  name: Salesflare Regional Settings API
  slug: salesflare-regional-settings-api
- description: The Tags API from Salesflare — 3 operation(s) for tags.
  name: Salesflare Tags API
  slug: salesflare-tags-api
- description: The Tasks API from Salesflare — 2 operation(s) for tasks.
  name: Salesflare Tasks API
  slug: salesflare-tasks-api
- description: The Users API from Salesflare — 4 operation(s) for users.
  name: Salesflare Users API
  slug: salesflare-users-api
- description: The Workflows API from Salesflare — 4 operation(s) for workflows.
  name: Salesflare Workflows API
  slug: salesflare-workflows-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesflare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesflare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://salesflare.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.salesflare.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Salesflare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salesflare
- group: company
  title: ''
  type: Blog
  url: https://blog.salesflare.com
- group: commercial
  title: ''
  type: Pricing
  url: https://salesflare.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesflare.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/salesflare
- group: commercial
  title: ''
  type: Plans
  url: plans/salesflare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salesflare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/salesflare-finops.yml
created: '2026-06-12'
description: Salesflare is an intelligent CRM built for B2B startups and small businesses that automates data input by pulling contact and company information from emails, calendars, phone logs, and social profiles. The platform provides a REST API for programmatically managing accounts, contacts, opportunities, tasks, and email messages. Developers can use the API to integrate CRM data into their own applications, automate sales workflows, and synchronize data across systems. Salesflare supports bearer token authentication via API keys generated from the settings dashboard, with endpoints covering the full CRM object model including leads, pipelines, and enriched contact records.
examples:
- key_count: 13
  name: Salesflare Account Example
  slug: salesflare-account-example
- key_count: 13
  name: Salesflare Contact Example
  slug: salesflare-contact-example
- key_count: 14
  name: Salesflare Opportunity Example
  slug: salesflare-opportunity-example
- key_count: 10
  name: Salesflare Task Example
  slug: salesflare-task-example
finops:
- name: Salesflare Finops
  service_category: ''
  slug: salesflare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salesflare.png https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Salesflare API Schemas
  property_count: 0
  slug: salesflare-schemas
jsonld:
- class_count: 2
  name: Salesflare Context
  property_count: 49
  slug: salesflare-context
layout: provider
modified: '2026-06-12'
name: Salesflare
nav: Providers
network: true
overview: 'Salesflare publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AI Message Feedbacks API, AISetings API, and 17 more. Tagged areas include CRM, Sales, B2B, Contacts, and Accounts.


  The Salesflare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Salesflare''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Salesflare Plans Pricing
  plan_count: 3
  slug: salesflare-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: Salesflare Rate Limits
  slug: salesflare-rate-limits
rules:
- name: Salesflare API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: salesflare-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.6
  delta: -3.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesflare/refs/heads/main/screenshots/salesflare-2026-06-20T193340.png
security:
- kind: domain-security
  name: Salesflare Domain Security
  slug: salesflare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: salesflare
tags:
- CRM
- Sales
- B2B
- Contacts
- Accounts
- Opportunities
- Email
- Automation
- Lead Generation
website: https://salesflare.com
---
