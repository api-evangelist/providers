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
- acting_count: 9
  human_in_the_loop: 0
  name: Contractbook Agentic Access
  operation_count: 16
  slug: contractbook-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 7
apis:
- description: Contractbook's document life-cycle notification (webhook) mechanism. When a document is created, updated, or signed, Contractbook sends an HTTP request to a client-configured callback URL, letting int
  name: Contractbook Document Webhooks
  slug: contractbook-document-webhooks
- description: The Attachments API from Contractbook — 1 operation(s) for attachments.
  name: Contractbook Attachments API
  slug: contractbook-attachments-api
- description: The Automations API from Contractbook — 2 operation(s) for automations.
  name: Contractbook Automations API
  slug: contractbook-automations-api
- description: The Document sharing API from Contractbook — 1 operation(s) for document sharing.
  name: Contractbook Document sharing API
  slug: contractbook-document-sharing-api
- description: The Documents API from Contractbook — 5 operation(s) for documents.
  name: Contractbook Documents API
  slug: contractbook-documents-api
- description: The Spaces API from Contractbook — 2 operation(s) for spaces.
  name: Contractbook Spaces API
  slug: contractbook-spaces-api
- description: The Templates API from Contractbook — 2 operation(s) for templates.
  name: Contractbook Templates API
  slug: contractbook-templates-api
artifact_total: 13
collections:
- collection_type: open
  name: Contractbook API v3
  slug: open-contractbook
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contractbook-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contractbook-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contractbook
- group: company
  title: ''
  type: Website
  url: https://contractbook.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.contractbook.com/v3/docs
- group: operate
  title: ''
  type: SupportCenter
  url: https://support.contractbook.com
- group: commercial
  title: ''
  type: Plans
  url: plans/contractbook-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/contractbook-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/contractbook-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://contractbook.com/blog
created: '2026-07-11'
description: Contractbook is a contract lifecycle management (CLM) platform that turns static contracts into structured, automatable data. Its Public API v3 (base https://api.contractbook.com/v3, Bearer API-key auth) lets teams generate pre-filled contract drafts from any data source, send documents for electronic signature, manage templates, organize documents into spaces, run automations, upload attachments, and receive webhook notifications on document life-cycle events. Contractbook covers the full contract lifecycle - drafting, negotiation, signing, storage, and post-signature management - for legal, sales, HR, and procurement teams.
finops:
- name: Contractbook Finops
  service_category: Contract Lifecycle Management
  slug: contractbook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contractbook.png
layout: provider
modified: '2026-07-11'
name: Contractbook
nav: Providers
network: true
overview: 'Contractbook publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Automations API, Document sharing API, and 3 more. Tagged areas include Contract Management, CLM, Contract Lifecycle, Legal, and eSignature.


  Contractbook''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Contractbook Plans Pricing
  plan_count: 4
  slug: contractbook-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 4
  name: Contractbook Rate Limits
  slug: contractbook-rate-limits
score:
  band: thin
  composite: 35.8
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contractbook/refs/heads/main/screenshots/contractbook-2026-07-25T210337.png
security:
- kind: authentication
  name: Contractbook Authentication
  slug: contractbook-authentication
  summary_line: http · 1 scheme
slug: contractbook
tags:
- Contract Management
- CLM
- Contract Lifecycle
- Legal
- eSignature
- Contracts
- Document Automation
- LegalTech
website: https://contractbook.com
---
