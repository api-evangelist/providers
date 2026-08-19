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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Azure Document Intelligence Agentic Access
  operation_count: 27
  slug: azure-document-intelligence-agentic-access
  summary_line: 27 operations · 14 acting
api_count: 9
apis:
- description: The DocumentClassifiers API from Azure AI Document Intelligence — 5 operation(s) for documentclassifiers.
  name: Azure AI Document Intelligence DocumentClassifiers API
  slug: azure-document-intelligence-documentclassifiers-api
- description: The DocumentClassifiers:authorizeCopy API from Azure AI Document Intelligence — 1 operation(s) for documentclassifiers:authorizecopy.
  name: Azure AI Document Intelligence DocumentClassifiers:authorizeCopy API
  slug: azure-document-intelligence-documentclassifiers-authorizecopy-api
- description: The DocumentClassifiers:build API from Azure AI Document Intelligence — 1 operation(s) for documentclassifiers:build.
  name: Azure AI Document Intelligence DocumentClassifiers:build API
  slug: azure-document-intelligence-documentclassifiers-build-api
- description: The DocumentModels API from Azure AI Document Intelligence — 10 operation(s) for documentmodels.
  name: Azure AI Document Intelligence DocumentModels API
  slug: azure-document-intelligence-documentmodels-api
- description: The DocumentModels:authorizeCopy API from Azure AI Document Intelligence — 1 operation(s) for documentmodels:authorizecopy.
  name: Azure AI Document Intelligence DocumentModels:authorizeCopy API
  slug: azure-document-intelligence-documentmodels-authorizecopy-api
- description: The DocumentModels:build API from Azure AI Document Intelligence — 1 operation(s) for documentmodels:build.
  name: Azure AI Document Intelligence DocumentModels:build API
  slug: azure-document-intelligence-documentmodels-build-api
- description: The DocumentModels:compose API from Azure AI Document Intelligence — 1 operation(s) for documentmodels:compose.
  name: Azure AI Document Intelligence DocumentModels:compose API
  slug: azure-document-intelligence-documentmodels-compose-api
- description: The Info API from Azure AI Document Intelligence — 1 operation(s) for info.
  name: Azure AI Document Intelligence Info API
  slug: azure-document-intelligence-info-api
- description: The Operations API from Azure AI Document Intelligence — 2 operation(s) for operations.
  name: Azure AI Document Intelligence Operations API
  slug: azure-document-intelligence-operations-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers API
  slug: open-azure-document-intelligence-documentclassifiers-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers DocumentClassifiers:authorizeCopy API
  slug: open-azure-document-intelligence-documentclassifiers-authorizecopy-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers DocumentClassifiers:build API
  slug: open-azure-document-intelligence-documentclassifiers-build-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers DocumentModels API
  slug: open-azure-document-intelligence-documentmodels-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers DocumentModels:authorizeCopy API
  slug: open-azure-document-intelligence-documentmodels-authorizecopy-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers DocumentModels:build API
  slug: open-azure-document-intelligence-documentmodels-build-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers DocumentModels:compose API
  slug: open-azure-document-intelligence-documentmodels-compose-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers Info API
  slug: open-azure-document-intelligence-info-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer) DocumentClassifiers Operations API
  slug: open-azure-document-intelligence-operations-api
- collection_type: open
  name: Document Intelligence (formerly Form Recognizer)
  slug: open-azure-document-intelligence
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-document-intelligence-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-document-intelligence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-document-intelligence-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-document-intelligence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-document-intelligence-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/document-intelligence/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/ai/data-plane/DocumentIntelligence
- group: start
  title: ''
  type: AzurePortal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/azure-document-intelligence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/azure-document-intelligence-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/azure-document-intelligence-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-05-08'
description: Azure AI Document Intelligence (formerly Form Recognizer) is Microsoft's cloud document understanding service. It exposes prebuilt models for invoices, receipts, IDs, business cards, tax forms and contracts, plus a layout/OCR Read model and a Custom-model framework for fine-tuned extraction. The 2024- 11-30 GA REST API is the current stable surface; preview APIs add Custom Generative Extraction.
finops:
- name: Azure Document Intelligence Finops
  service_category: AI / IDP
  slug: azure-document-intelligence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-document-intelligence.png
layout: provider
modified: '2026-05-19'
name: Azure AI Document Intelligence
nav: Providers
network: true
overview: 'Azure AI Document Intelligence publishes 9 APIs on the [APIs.io](https://apis.io/) network, including DocumentClassifiers API, DocumentClassifiers:authorizeCopy API, DocumentClassifiers:build API, and 6 more. Tagged areas include AI, Document AI, Azure, IDP, and OCR.


  Azure AI Document Intelligence''s developer surface includes authentication, documentation, pricing, GitHub presence, and 10 more developer resources.'
plans:
- name: Azure Document Intelligence Plans Pricing
  plan_count: 5
  slug: azure-document-intelligence-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 4
  name: Azure Document Intelligence Rate Limits
  slug: azure-document-intelligence-rate-limits
scopes:
- name: Azure Document Intelligence Scopes
  scope_count: 1
  slug: azure-document-intelligence-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 29.2
  delta: -0.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 42.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 29.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-document-intelligence/refs/heads/main/screenshots/azure-document-intelligence-2026-06-20T172854.png
security:
- kind: authentication
  name: Azure Document Intelligence Authentication
  slug: azure-document-intelligence-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Azure Document Intelligence Domain Security
  slug: azure-document-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Document Intelligence Vulnerability Disclosure
  slug: azure-document-intelligence-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-document-intelligence
tags:
- AI
- Document AI
- Azure
- IDP
- OCR
- Microsoft
- REST
website: https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence
---
