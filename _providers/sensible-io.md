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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Sensible Io Agentic Access
  operation_count: 32
  slug: sensible-io-agentic-access
  summary_line: 32 operations · 20 acting
api_count: 9
apis:
- description: REST API for document extraction (sync/async, single-document or portfolio), classification, fill, generation and configuration management. Bearer-token auth.
  name: Sensible REST API
  slug: rest
- description: Account-related resources
  name: Sensible Account API
  slug: sensible-io-account-api
- description: Document type classification
  name: Sensible Classify API
  slug: sensible-io-classify-api
- description: Manage document type configs (SenseML)
  name: Sensible Configs API
  slug: sensible-io-configs-api
- description: Manage document types
  name: Sensible Document Types API
  slug: sensible-io-document-types-api
- description: Retrieve documents and extractions
  name: Sensible Documents API
  slug: sensible-io-documents-api
- description: Document data extraction
  name: Sensible Extract API
  slug: sensible-io-extract-api
- description: Manage reference documents per type
  name: Sensible Reference Documents API
  slug: sensible-io-reference-documents-api
- description: Generate upload URLs for documents
  name: Sensible Upload API
  slug: sensible-io-upload-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sensible REST Account API
  slug: open-sensible-io-account-api
- collection_type: open
  name: Sensible REST Account Classify API
  slug: open-sensible-io-classify-api
- collection_type: open
  name: Sensible REST Account Configs API
  slug: open-sensible-io-configs-api
- collection_type: open
  name: Sensible REST Account Document Types API
  slug: open-sensible-io-document-types-api
- collection_type: open
  name: Sensible REST Account Documents API
  slug: open-sensible-io-documents-api
- collection_type: open
  name: Sensible REST Account Extract API
  slug: open-sensible-io-extract-api
- collection_type: open
  name: Sensible REST Account Reference Documents API
  slug: open-sensible-io-reference-documents-api
- collection_type: open
  name: Sensible REST Account Upload API
  slug: open-sensible-io-upload-api
- collection_type: open
  name: Sensible REST API
  slug: open-sensible-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sensible-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sensible-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sensible-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensible-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sensible-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sensible-io
- group: company
  title: ''
  type: Website
  url: https://www.sensible.so/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensible.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sensible.so/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sensible-hq
- group: commercial
  title: ''
  type: Plans
  url: plans/sensible-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sensible-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sensible-io-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sensible.so/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.sensible.so/blog
created: '2026-05-08'
description: Sensible is a developer-focused document understanding platform that converts unstructured documents (PDFs, emails, images) into JSON. The core IP is SenseML — a document-specific query language combining LLM techniques with layout-based rules. The REST API exposes extract, classify, fill, generate and document-management endpoints, with SDKs for Node, Python and Go.
finops:
- name: Sensible Io Finops
  service_category: Document AI
  slug: sensible-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sensible-io.png
layout: provider
modified: '2026-05-08'
name: Sensible
nav: Providers
network: true
overview: 'Sensible publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Classify API, Configs API, and 5 more. Tagged areas include Artificial Intelligence, Document AI, IDP, Extraction, and LLM.


  Sensible''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Sensible Io Plans Pricing
  plan_count: 3
  slug: sensible-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Sensible Io Rate Limits
  slug: sensible-io-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sensible-io/refs/heads/main/screenshots/sensible-io-2026-06-20T193703.png
security:
- kind: authentication
  name: Sensible Io Authentication
  slug: sensible-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sensible Io Domain Security
  slug: sensible-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sensible Io Vulnerability Disclosure
  slug: sensible-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Sensible Io Trust Center
  slug: sensible-io-trust-center
  summary_line: SOC 2, HIPAA
slug: sensible-io
tags:
- Artificial Intelligence
- Document AI
- IDP
- Extraction
- LLM
- SenseML
- PDF
website: https://www.sensible.so/
---
