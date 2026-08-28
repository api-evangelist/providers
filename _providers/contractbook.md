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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-26'
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Contractbook Attachments API
  slug: open-contractbook-attachments-api
- collection_type: open
  name: Contractbook Attachments Automations API
  slug: open-contractbook-automations-api
- collection_type: open
  name: Contractbook Attachments Document sharing API
  slug: open-contractbook-document-sharing-api
- collection_type: open
  name: Contractbook Attachments Documents API
  slug: open-contractbook-documents-api
- collection_type: open
  name: Contractbook Attachments Spaces API
  slug: open-contractbook-spaces-api
- collection_type: open
  name: Contractbook Attachments Templates API
  slug: open-contractbook-templates-api
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
overview: 'Contractbook publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Automations API, Document sharing API, and 3 more. Tagged areas include Contract Management, CLM, Contract Lifecycle, Legal, and E-Signature.


  Contractbook''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Contractbook Plans Pricing
  plan_count: 4
  slug: contractbook-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Contractbook Rate Limits
  slug: contractbook-rate-limits
score:
  band: developing
  composite: 40.5
  delta: 3.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.8
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- E-Signature
- Contracts
- Document Automation
- Legal Tech
website: https://contractbook.com
---
