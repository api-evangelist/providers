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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Revert Dev Agentic Access
  operation_count: 44
  slug: revert-dev-agentic-access
  summary_line: 44 operations · 22 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: The Connection API from Revert — 3 operation(s) for connection.
  name: Revert Connection API
  slug: revert-dev-connection-api
- description: The CRM Companies API from Revert — 3 operation(s) for crm companies.
  name: Revert CRM Companies API
  slug: revert-dev-crm-companies-api
- description: The CRM Contacts API from Revert — 3 operation(s) for crm contacts.
  name: Revert CRM Contacts API
  slug: revert-dev-crm-contacts-api
- description: The CRM Deals API from Revert — 3 operation(s) for crm deals.
  name: Revert CRM Deals API
  slug: revert-dev-crm-deals-api
- description: The CRM Events API from Revert — 2 operation(s) for crm events.
  name: Revert CRM Events API
  slug: revert-dev-crm-events-api
- description: The CRM Leads API from Revert — 3 operation(s) for crm leads.
  name: Revert CRM Leads API
  slug: revert-dev-crm-leads-api
- description: The CRM Notes API from Revert — 2 operation(s) for crm notes.
  name: Revert CRM Notes API
  slug: revert-dev-crm-notes-api
- description: The CRM Properties API from Revert — 1 operation(s) for crm properties.
  name: Revert CRM Properties API
  slug: revert-dev-crm-properties-api
- description: The CRM Proxy API from Revert — 1 operation(s) for crm proxy.
  name: Revert CRM Proxy API
  slug: revert-dev-crm-proxy-api
- description: The CRM Tasks API from Revert — 2 operation(s) for crm tasks.
  name: Revert CRM Tasks API
  slug: revert-dev-crm-tasks-api
- description: The CRM Users API from Revert — 2 operation(s) for crm users.
  name: Revert CRM Users API
  slug: revert-dev-crm-users-api
- description: The Metadata API from Revert — 1 operation(s) for metadata.
  name: Revert Metadata API
  slug: revert-dev-metadata-api
- description: The Webhook API from Revert — 1 operation(s) for webhook.
  name: Revert Webhook API
  slug: revert-dev-webhook-api
artifact_total: 19
collections:
- collection_type: open
  name: Revert Unified API
  slug: open-revert-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revert-dev-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revert-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revertinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revertdev
- group: company
  title: ''
  type: Website
  url: https://revert.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.revert.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/revert-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revert-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revert-dev-finops.yml
created: '2026-07-01'
description: Revert is an open-source unified API for building product integrations. A single normalized interface fronts many third-party SaaS providers across categories like CRM, with managed OAuth connections, a unified data model (contacts, leads, deals, companies, notes, tasks, events, users), a passthrough proxy for provider-specific calls, and webhooks. Revert is AGPL-3.0 licensed and self-hostable, with a hosted cloud offering.
finops:
- name: Revert Dev Finops
  service_category: Integration and Automation
  slug: revert-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revert-dev.png
layout: provider
modified: '2026-07-01'
name: Revert
nav: Providers
network: true
overview: 'Revert publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Connection API, CRM Companies API, CRM Contacts API, and 10 more. Tagged areas include Unified API, Integrations, CRM, iPaaS, and Open Source.


  Revert''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Revert Dev Plans Pricing
  plan_count: 3
  slug: revert-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Revert Dev Rate Limits
  slug: revert-dev-rate-limits
score:
  band: thin
  composite: 37.1
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Revert Dev Authentication
  slug: revert-dev-authentication
  summary_line: apiKey · 1 scheme
slug: revert-dev
tags:
- Unified API
- Integrations
- CRM
- iPaaS
- Open Source
- OAuth
website: https://revert.dev
---
