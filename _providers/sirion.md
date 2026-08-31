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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sirion Agentic Access
  operation_count: 15
  slug: sirion-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sirion CLM API (Modeled) Contract Requests API
  slug: open-sirion-contract-requests-api
- collection_type: open
  name: Sirion CLM API (Modeled) Contract Requests Contracts API
  slug: open-sirion-contracts-api
- collection_type: open
  name: Sirion CLM API (Modeled) Contract Requests Metadata & Clauses API
  slug: open-sirion-metadata-clauses-api
- collection_type: open
  name: Sirion CLM API (Modeled) Contract Requests Obligations API
  slug: open-sirion-obligations-api
- collection_type: open
  name: Sirion CLM API (Modeled) Contract Requests Suppliers API
  slug: open-sirion-suppliers-api
- collection_type: open
  name: Sirion CLM API (Modeled) Contract Requests Webhooks API
  slug: open-sirion-webhooks-api
- collection_type: open
  name: Sirion CLM API (Modeled)
  slug: open-sirion
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sirion-capability-edges.yml
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
overview: 'Sirion publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contract Requests API, Contracts API, Metadata & Clauses API, and 3 more. Tagged areas include Contract Management, Contract Lifecycle Management, CLM, Contracts, and Artificial Intelligence.


  Sirion''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Sirion Plans Pricing
  plan_count: 1
  slug: sirion-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Sirion Rate Limits
  slug: sirion-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Artificial Intelligence
- Enterprise
- Legal
- Agreements
- Supplier Management
- Obligations
website: https://www.sirion.ai
---
