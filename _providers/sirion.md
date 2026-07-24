---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sirion Agentic Access
  operation_count: 15
  slug: sirion-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 6
apis:
- description: Contract Requests (CDRs) that drive intake and authoring (MODELED).
  name: Sirion Contract Requests API
  slug: sirion-contract-requests-api
- description: Executed contracts / agreements in the SirionOne repository (MODELED).
  name: Sirion Contracts API
  slug: sirion-contracts-api
- description: Contract metadata fields and AI-extracted clauses (MODELED).
  name: Sirion Metadata & Clauses API
  slug: sirion-metadata-clauses-api
- description: Contractual obligations and performance tracking (MODELED).
  name: Sirion Obligations API
  slug: sirion-obligations-api
- description: Suppliers and counterparties linked to contracts (MODELED).
  name: Sirion Suppliers API
  slug: sirion-suppliers-api
- description: Outbound webhook subscriptions for event notifications (MODELED).
  name: Sirion Webhooks API
  slug: sirion-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: Sirion CLM API (Modeled)
  slug: open-sirion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sirion-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sirion-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.sirion.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sirion.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/sirion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sirion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sirion-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sirion-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sirionlabs
created: '2026-07-12'
description: Sirion (SirionLabs) is an AI-native enterprise Contract Lifecycle Management (CLM) platform. SirionOne manages the full agreement lifecycle - authoring, negotiation, e-signature, a searchable contract repository, metadata and clause extraction, obligation and performance management, and supplier / counterparty governance. The platform exposes REST "Business API & Integrations" capabilities plus pre-built connectors (Salesforce, SAP Ariba, SAP S/4HANA, DocuSign, iPaaS) and configurable webhooks, secured with OAuth 2.0 client credentials. API access is enterprise / contract-gated - credentials are provisioned per tenant and the API reference is available to authenticated Sirion users. Endpoint paths and schemas in this entry are MODELED from public product references, not copied from a public reference document.
finops:
- name: Sirion Finops
  service_category: Contract Lifecycle Management
  slug: sirion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sirion.png
layout: provider
modified: '2026-07-12'
name: Sirion
nav: Providers
network: true
overview: 'Sirion publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contract Requests API, Contracts API, Metadata & Clauses API, and 3 more. Tagged areas include Contract Management, Contract Lifecycle Management, CLM, Contracts, and AI.


  Sirion''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Sirion Plans Pricing
  plan_count: 1
  slug: sirion-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 3
  name: Sirion Rate Limits
  slug: sirion-rate-limits
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sirion Authentication
  slug: sirion-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sirion Domain Security
  slug: sirion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sirion
tags:
- Contract Management
- Contract Lifecycle Management
- CLM
- Contracts
- AI
- Enterprise
- Legal
- Agreements
- Supplier Management
- Obligations
website: https://www.sirion.ai
---
