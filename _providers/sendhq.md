---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Session-authenticated workspace administration.
  name: SendHQ Account and billing API
  slug: sendhq-account-and-billing-api
- description: Inspect events, reputation outcomes, and blocked recipients.
  name: SendHQ Deliverability API
  slug: sendhq-deliverability-api
- description: Provision sender identities and understand DNS verification state.
  name: SendHQ Domains API
  slug: sendhq-domains-api
- description: Build composer flows with private attachment storage.
  name: SendHQ Drafts and attachments API
  slug: sendhq-drafts-and-attachments-api
- description: Send, retrieve, search, reply, and inspect delivery events.
  name: SendHQ Emails and threads API
  slug: sendhq-emails-and-threads-api
- description: Draft, render, test, version, publish, and send reusable content.
  name: SendHQ Hosted templates API
  slug: sendhq-hosted-templates-api
- description: Create addresses and work with received conversations.
  name: SendHQ Inbound email API
  slug: sendhq-inbound-email-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendhq-llms.txt
- group: company
  title: ''
  type: Website
  url: https://sendhq.cc/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sendhq.cc/docs
- group: start
  title: ''
  type: Console
  url: https://app.sendhq.cc/
- group: build
  title: ''
  type: Tools
  url: https://sendhq.cc/tools
- group: other
  title: ''
  type: Templates
  url: https://sendhq.cc/templates
- group: other
  title: ''
  type: Glossary
  url: https://sendhq.cc/glossary
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendhq.cc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendhq.cc/privacy
- group: operate
  title: ''
  type: Support
  url: https://sendhq.cc/contact
created: '2026-08-24'
description: SendHQ is a transactional email API for product teams and AI agents — verified-domain sending, inbound email, hosted templates, drafts and attachments, delivery events, suppressions and workspace-scoped API keys, with a web dashboard at app.sendhq.cc. The public contract is an OpenAPI 3.1 document of 32 paths and 47 operations served from sendhq.cc/api/v1, authenticated with a bearer token or a session cookie. The largest operation groups are hosted templates, drafts and attachments, emails and threads, account and billing, domains, inbound email and deliverability. The company markets the product explicitly at coding agents.
layout: provider
modified: '2026-08-24'
name: SendHQ
nav: Providers
network: true
overview: 'SendHQ publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account and billing API, Deliverability API, Domains API, and 4 more. Tagged areas include email api, Transactional Email, Inbound Email, and deliverability.


  SendHQ''s developer surface includes developer console, tooling, support, and 7 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 42.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: sendhq
tags:
- email api
- Transactional Email
- Inbound Email
- deliverability
website: https://sendhq.cc/
---
