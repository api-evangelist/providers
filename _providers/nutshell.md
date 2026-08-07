---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nutshell Agentic Access
  operation_count: 5
  slug: nutshell-agentic-access
  summary_line: 5 operations
api_count: 7
apis:
- description: Resource-based REST API for managing contacts, leads, accounts, activities, pipelines, and tasks in Nutshell CRM. Authentication uses an API key generated from the Nutshell account settings.
  name: Nutshell REST API
  slug: rest-api
- description: Legacy JSON-RPC API for accessing Nutshell CRM data, retained for backward compatibility with existing integrations.
  name: Nutshell Legacy JSON-RPC API
  slug: json-rpc
- description: The Accounts API from Nutshell — 1 operation(s) for accounts.
  name: Nutshell Accounts API
  slug: nutshell-accounts-api
- description: The Activities API from Nutshell — 1 operation(s) for activities.
  name: Nutshell Activities API
  slug: nutshell-activities-api
- description: The Contacts API from Nutshell — 1 operation(s) for contacts.
  name: Nutshell Contacts API
  slug: nutshell-contacts-api
- description: The Leads API from Nutshell — 1 operation(s) for leads.
  name: Nutshell Leads API
  slug: nutshell-leads-api
- description: The Pipelines API from Nutshell — 1 operation(s) for pipelines.
  name: Nutshell Pipelines API
  slug: nutshell-pipelines-api
artifact_total: 12
collections:
- collection_type: open
  name: Nutshell REST API
  slug: open-nutshell
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nutshell-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nutshell-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutshell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nutshell-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nutshell-llc
- group: company
  title: ''
  type: Website
  url: https://www.nutshell.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.nutshell.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nutshell.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.nutshell.com/start-your-free-trial
- group: operate
  title: ''
  type: Support
  url: https://support.nutshell.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nutshellcrm
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.nutshell.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.nutshell.com/feed
created: '2026-05-11'
description: Nutshell is a CRM and email marketing platform for small to mid-sized B2B sales teams, providing pipeline management, contact and company records, reporting, automation, and built-in email campaigns. The product unifies sales pipelines, activity tracking, and outbound communications in one workspace with mobile and desktop clients. Nutshell exposes a REST API for contacts, leads, accounts, activities, and pipelines, plus a legacy JSON-RPC API, both authenticated with an API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutshell.png
layout: provider
modified: '2026-05-11'
name: Nutshell
nav: Providers
network: true
overview: 'Nutshell publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Contacts API, and 2 more. Tagged areas include CRM, Sales, Pipeline Management, Email Marketing, and Contact Management.


  Nutshell''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 88
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 54.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutshell/refs/heads/main/screenshots/nutshell-2026-06-20T190536.png
security:
- kind: authentication
  name: Nutshell Authentication
  slug: nutshell-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nutshell Domain Security
  slug: nutshell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nutshell Trust Center
  slug: nutshell-trust-center
  summary_line: SOC 2, GDPR
slug: nutshell
tags:
- CRM
- Sales
- Pipeline Management
- Email Marketing
- Contact Management
- Sales Automation
website: https://www.nutshell.com
---
