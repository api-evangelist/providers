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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Zendesk Sell Agentic Access
  operation_count: 18
  slug: zendesk-sell-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 4
apis:
- description: OAuth 2.0-authenticated REST API for managing leads, contacts, deals, accounts, notes, tasks, calls, sources, stages, pipelines, and custom fields in Zendesk Sell. Bearer access tokens are passed in t
  name: Zendesk Sell (Sales CRM) API
  slug: sales-crm-api
- description: Individual people and organizations.
  name: Zendesk Sell Contacts API
  slug: zendesk-sell-contacts-api
- description: Sales opportunities moving through pipeline stages.
  name: Zendesk Sell Deals API
  slug: zendesk-sell-deals-api
- description: Pre-qualified sales prospects.
  name: Zendesk Sell Leads API
  slug: zendesk-sell-leads-api
artifact_total: 11
collections:
- collection_type: open
  name: Zendesk Sell (Sales CRM) API
  slug: open-zendesk-sell
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zendesk-sell-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zendesk-sell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zendesk-sell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zendesk-sell-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zendesk-sell-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zendesk.com/sell/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/api-reference/sales-crm/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.zendesk.com/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zendesk.com/sell/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.zendesk.com/register/
- group: start
  title: ''
  type: Login
  url: https://www.zendesk.com/login/
- group: operate
  title: ''
  type: Support
  url: https://support.zendesk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zendesk
created: '2026-05-11'
description: Zendesk Sell (formerly Base CRM) is a sales CRM platform that helps sales teams manage leads, contacts, deals, and pipelines while integrating with the broader Zendesk customer experience suite. The platform offers pipeline analytics, email and call tracking, mobile apps, and territory management for high-velocity sales organizations. The Sell API is a RESTful API authenticated via OAuth 2.0 (authorization code, implicit, password, and refresh token grants) at the api.getbase.com host that provides full CRUD access to leads, contacts, deals, accounts, notes, tasks, calls, and custom fields.
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Zendesk Sell (formerly Base CRM) Sales CRM API. The schema is derived from the [Zendesk Sell REST API reference](https://developer.zendesk.c
  name: Zendesk Sell GraphQL Schema
  slug: zendesk-sell-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zendesk-sell.png
layout: provider
modified: '2026-05-11'
name: Zendesk Sell
nav: Providers
network: true
overview: 'Zendesk Sell publishes 3 APIs on the [APIs.io](https://apis.io/) network: Contacts API, Deals API, and Leads API. Tagged areas include CRM, Sales, Sales Automation, Leads, and Deals.


  Zendesk Sell''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 7 more developer resources.'
random_paper: 73
scopes:
- name: Zendesk Sell Scopes
  scope_count: 2
  slug: zendesk-sell-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 62.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zendesk-sell/refs/heads/main/screenshots/zendesk-sell-2026-06-20T201812.png
security:
- kind: authentication
  name: Zendesk Sell Authentication
  slug: zendesk-sell-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zendesk Sell Domain Security
  slug: zendesk-sell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zendesk Sell Vulnerability Disclosure
  slug: zendesk-sell-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: zendesk-sell
tags:
- CRM
- Sales
- Sales Automation
- Leads
- Deals
- Pipeline
- Customer Experience
website: https://www.zendesk.com/sell/
---
