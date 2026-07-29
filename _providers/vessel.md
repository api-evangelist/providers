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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Vessel Agentic Access
  operation_count: 28
  slug: vessel-agentic-access
  summary_line: 28 operations · 21 acting
api_count: 15
apis:
- description: The Vessel Actions API provides pre-built, validated actions for common integration operations across CRM, sales engagement, marketing automation, chat, and dialer systems. Actions validate API respon
  name: Vessel Actions API
  slug: actions-api
- description: The Vessel Unified API provides a standardized interface across integrations, abstracting away the differences between third-party APIs to provide a consistent developer experience. Supports CRM, sale
  name: Vessel Unified API
  slug: unified-api
- description: The Accounts API from Vessel — 2 operation(s) for accounts.
  name: Vessel Accounts API
  slug: vessel-accounts-api
- description: The Authentication API from Vessel — 4 operation(s) for authentication.
  name: Vessel Authentication API
  slug: vessel-authentication-api
- description: The Connections API from Vessel — 4 operation(s) for connections.
  name: Vessel Connections API
  slug: vessel-connections-api
- description: The Contacts API from Vessel — 3 operation(s) for contacts.
  name: Vessel Contacts API
  slug: vessel-contacts-api
- description: The Deals API from Vessel — 3 operation(s) for deals.
  name: Vessel Deals API
  slug: vessel-deals-api
- description: The Engagement Unifications API from Vessel — 1 operation(s) for engagement unifications.
  name: Vessel Engagement Unifications API
  slug: vessel-engagement-unifications-api
- description: The Integrations API from Vessel — 1 operation(s) for integrations.
  name: Vessel Integrations API
  slug: vessel-integrations-api
- description: The Leads API from Vessel — 2 operation(s) for leads.
  name: Vessel Leads API
  slug: vessel-leads-api
- description: The Notes API from Vessel — 2 operation(s) for notes.
  name: Vessel Notes API
  slug: vessel-notes-api
- description: The Passthrough API from Vessel — 1 operation(s) for passthrough.
  name: Vessel Passthrough API
  slug: vessel-passthrough-api
- description: The Tasks API from Vessel — 1 operation(s) for tasks.
  name: Vessel Tasks API
  slug: vessel-tasks-api
- description: The Users API from Vessel — 1 operation(s) for users.
  name: Vessel Users API
  slug: vessel-users-api
- description: The Webhooks API from Vessel — 3 operation(s) for webhooks.
  name: Vessel Webhooks API
  slug: vessel-webhooks-api
artifact_total: 32
collections:
- collection_type: open
  name: Vessel CRM API
  slug: open-vessel-crm
- collection_type: open
  name: Vessel Platform API
  slug: open-vessel-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vessel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vessel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vessel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vesselapi
- group: company
  title: ''
  type: Website
  url: https://www.vessel.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vessel.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vesselapi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vesselapi/integrations
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vesselapi/client-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@vesselapi/sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@vesselapi/react-vessel-link
- group: company
  title: ''
  type: Blog
  url: https://www.vessel.dev/blog
created: '2026-05-03'
description: 'Vessel is a developer-first embedded integrations platform that enables product teams to add native integrations to their applications. It provides unified API abstractions, actions APIs, and passthrough APIs to connect with CRM, sales engagement, marketing automation, chat, and dialer tools while managing authentication, rate limits, and data normalization. The platform supports OAuth and API-key authentication via a drop-in React UI component (Vessel Link), with two API surfaces: api.vessel.dev for the newer GTM integrations platform and api.vessel.land for the CRM-focused platform.'
examples:
- key_count: 2
  name: Vessel Create Session Token Example
  slug: vessel-create-session-token-example
- key_count: 2
  name: Vessel Get All Contacts Example
  slug: vessel-get-all-contacts-example
- key_count: 2
  name: Vessel List Integrations Example
  slug: vessel-list-integrations-example
finops:
- name: Vessel Finops
  service_category: Unified API / Integrations
  slug: vessel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vessel.png
json_schemas:
- name: Vessel CRM Contact
  property_count: 9
  slug: vessel-contact
- name: Vessel CRM Deal
  property_count: 9
  slug: vessel-deal
json_structures:
- name: Vessel Contact Structure
  property_count: 0
  slug: vessel-contact-structure
jsonld:
- class_count: 9
  name: Vessel Context
  property_count: 20
  slug: vessel-context
layout: provider
modified: '2026-05-19'
name: Vessel
nav: Providers
network: true
overview: 'Vessel publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Connections API, and 10 more. Tagged areas include CRM, Embedded Integrations, GTM, Integrations, and iPaaS.


  The Vessel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vessel''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Vessel Plans Pricing
  plan_count: 3
  slug: vessel-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 2
  name: Vessel Rate Limits
  slug: vessel-rate-limits
rules:
- name: Vessel API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 7
  slug: vessel-api-rules
- name: Vessel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vessel-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.7
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 55.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/screenshots/vessel-2026-06-20T200959.png
security:
- kind: authentication
  name: Vessel Authentication
  slug: vessel-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Vessel Domain Security
  slug: vessel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vessel
tags:
- CRM
- Embedded Integrations
- GTM
- Integrations
- iPaaS
- Sales Engagement
- Unified API
website: https://www.vessel.dev/
---
