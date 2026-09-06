---
agent_readiness:
  band: agent-ready
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://sendhq.cc/api/v1
  baseurl_source: declared
  description: Session-authenticated workspace administration.
  name: SendHQ Account and billing API
  slug: sendhq-account-and-billing-api
- baseURL: https://sendhq.cc/api/v1
  baseurl_source: declared
  description: Inspect events, reputation outcomes, and blocked recipients.
  name: SendHQ Deliverability API
  slug: sendhq-deliverability-api
- baseURL: https://sendhq.cc/api/v1
  baseurl_source: declared
  description: Provision sender identities and understand DNS verification state.
  name: SendHQ Domains API
  slug: sendhq-domains-api
- baseURL: https://sendhq.cc/api/v1
  baseurl_source: declared
  description: Build composer flows with private attachment storage.
  name: SendHQ Drafts and attachments API
  slug: sendhq-drafts-and-attachments-api
- baseURL: https://sendhq.cc/api/v1
  baseurl_source: declared
  description: Send, retrieve, search, reply, and inspect delivery events.
  name: SendHQ Emails and threads API
  slug: sendhq-emails-and-threads-api
- baseURL: https://sendhq.cc/api/v1
  baseurl_source: declared
  description: Draft, render, test, version, publish, and send reusable content.
  name: SendHQ Hosted templates API
  slug: sendhq-hosted-templates-api
- baseURL: https://sendhq.cc/api/v1
  baseurl_source: declared
  description: Create addresses and work with received conversations.
  name: SendHQ Inbound email API
  slug: sendhq-inbound-email-api
- description: Resend-compatible REST API for transactional and inbound email, domains, templates, deliverability, and workspace administration. Base URL https://sendhq.cc/api/v1 with Bearer re_ API keys.
  name: SendHQ REST API
  slug: sendhq-rest-api
artifact_total: 8
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
overview: 'SendHQ publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account and billing API, Deliverability API, Domains API, and 5 more. Tagged areas include Email API, Transactional Email, inbound email, and Deliverability.


  SendHQ''s developer surface includes developer console, tooling, support, and 7 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 60.5
    developer_ergonomics: 42.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendhq/refs/heads/main/screenshots/sendhq-2026-09-02T154838.png
slug: sendhq
tags:
- Email API
- Transactional Email
- inbound email
- Deliverability
website: https://sendhq.cc/
---
