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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Signaturely Agentic Access
  operation_count: 27
  slug: signaturely-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 7
apis:
- description: List, download, share, remind on, and manage documents.
  name: Signaturely Documents API
  slug: signaturely-documents-api
- description: Organize documents and folders.
  name: Signaturely Folders API
  slug: signaturely-folders-api
- description: Create signature requests from templates and bulk-send from CSV data.
  name: Signaturely Signature Requests API
  slug: signaturely-signature-requests-api
- description: Manage team members and roles.
  name: Signaturely Team API
  slug: signaturely-team-api
- description: Work with reusable templates.
  name: Signaturely Templates API
  slug: signaturely-templates-api
- description: Account information for the authenticated API key.
  name: Signaturely User API
  slug: signaturely-user-api
- description: Subscribe to document lifecycle events.
  name: Signaturely Webhooks API
  slug: signaturely-webhooks-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signaturely-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signaturely-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signaturely-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signaturely
- group: company
  title: ''
  type: Website
  url: https://signaturely.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signaturely.com/
- group: other
  title: ''
  type: APIOverview
  url: https://signaturely.com/api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.signaturely.com/category/53-api
- group: commercial
  title: ''
  type: Plans
  url: plans/signaturely-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signaturely-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/signaturely-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://signaturely.com/feed/
created: '2026-07-03'
description: 'Signaturely is simple electronic signature software for sending, signing, and managing legally binding documents online. Beyond the web app, Signaturely offers a documented public REST API (base https://api.signaturely.com/api/v1) gated behind separately billed API plans (Gold, Platinum, Titanium). The API is authenticated with an API key ("Authorization: Api-Key {API_KEY}") issued from the account API settings, with OAuth, embedded signing, and embedded requesting available on higher tiers. It lets developers send signature requests from templates, bulk-send from CSV data, manage documents (list, download, share, send reminders, revert, activity), manage templates and folders, manage team members, and subscribe to webhooks for document events. There is no separate "contacts" resource; signers are supplied inline on each signature request.'
finops:
- name: Signaturely Finops
  service_category: E-Signature and Document Automation
  slug: signaturely-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signaturely.png
layout: provider
modified: '2026-07-03'
name: Signaturely
nav: Providers
network: true
overview: 'Signaturely publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Folders API, Signature Requests API, and 4 more. Tagged areas include Electronic Signature, eSignature, Document Signing, E-Signature API, and Contracts.


  Signaturely''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Signaturely Plans Pricing
  plan_count: 4
  slug: signaturely-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Signaturely Rate Limits
  slug: signaturely-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.0
    developer_ergonomics: 26.1
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Signaturely Authentication
  slug: signaturely-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Signaturely Domain Security
  slug: signaturely-domain-security
  summary_line: TLSv1.3 · DMARC
slug: signaturely
tags:
- Electronic Signature
- eSignature
- Document Signing
- E-Signature API
- Contracts
- Signature Requests
- SaaS
website: https://signaturely.com
---
