---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Azure Document Intelligence Agentic Access
  operation_count: 27
  slug: azure-document-intelligence-agentic-access
  summary_line: 27 operations · 14 acting
api_count: 1
apis:
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The DocumentClassifiers:authorizeCopy API from Azure AI Document Intelligence — 1 operation(s) for documentclassifiers:authorizecopy.
  name: Azure AI Document Intelligence DocumentClassifiers:authorizeCopy API
  slug: azure-document-intelligence-documentclassifiers-authorizecopy-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Info API from Azure AI Document Intelligence — 1 operation(s) for info.
  name: Azure AI Document Intelligence Info API
  slug: azure-document-intelligence-info-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Operations API from Azure AI Document Intelligence — 2 operation(s) for operations.
  name: Azure AI Document Intelligence Operations API
  slug: azure-document-intelligence-operations-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Document Classifiers API from Azure AI Document Intelligence — 5 operation(s) for document classifiers.
  name: Azure AI Document Intelligence Document Classifiers API
  slug: azure-document-intelligence-document-classifiers-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Document Classifiers:build API from Azure AI Document Intelligence — 1 operation(s) for document classifiers:build.
  name: Azure AI Document Intelligence Document Classifiers:build API
  slug: azure-document-intelligence-document-classifiers-build-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Document Models API from Azure AI Document Intelligence — 10 operation(s) for document models.
  name: Azure AI Document Intelligence Document Models API
  slug: azure-document-intelligence-document-models-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Document Models:authorize Copy API from Azure AI Document Intelligence — 1 operation(s) for document models:authorize copy.
  name: Azure AI Document Intelligence Document Models:authorize Copy API
  slug: azure-document-intelligence-document-models-authorize-copy-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Document Models:build API from Azure AI Document Intelligence — 1 operation(s) for document models:build.
  name: Azure AI Document Intelligence Document Models:build API
  slug: azure-document-intelligence-document-models-build-api
- baseURL: https://<your-resource>.cognitiveservices.azure.com
  baseurl_source: declared
  description: The Document Models:compose API from Azure AI Document Intelligence — 1 operation(s) for document models:compose.
  name: Azure AI Document Intelligence Document Models:compose API
  slug: azure-document-intelligence-document-models-compose-api
artifact_total: 28
collections:
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
- group: other
  href: https://artifacts.apis.io/azure-document-intelligence/capabilities/azure-document-intelligence-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/azure-document-intelligence-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/azure-document-intelligence/agentic-access/azure-document-intelligence-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-document-intelligence-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/azure-document-intelligence/security/azure-document-intelligence-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-document-intelligence-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/azure-document-intelligence/security/azure-document-intelligence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azure-document-intelligence-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/azure-document-intelligence/authentication/azure-document-intelligence-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azure-document-intelligence-authentication.yml
- group: auth
  href: https://artifacts.apis.io/azure-document-intelligence/scopes/azure-document-intelligence-scopes.yml
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
  href: https://artifacts.apis.io/azure-document-intelligence/plans/azure-document-intelligence-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azure-document-intelligence-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/azure-document-intelligence/rate-limits/azure-document-intelligence-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/azure-document-intelligence-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/azure-document-intelligence/finops/azure-document-intelligence-finops.yml
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
- has_sources: true
  method: generated
  name: Azure Document Intelligence Finops
  primary_unit: 1K pages
  service_category: AI / IDP
  slug: azure-document-intelligence-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-document-intelligence.png
layout: provider
modified: '2026-05-19'
name: Azure AI Document Intelligence
nav: Providers
network: true
overview: 'Azure AI Document Intelligence publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including DocumentClassifiers:authorizeCopy API, Info API, Operations API, and 6 more. Tagged areas include Artificial Intelligence, Document AI, Microsoft Azure, Intelligent Document Processing, and OCR.


  The Azure AI Document Intelligence catalog on APIs.io includes 1 Spectral governance ruleset.


  Azure AI Document Intelligence''s developer surface includes authentication, documentation, pricing, GitHub presence, and 11 more developer resources.'
plans:
- name: Azure Document Intelligence Plans Pricing
  plan_count: 5
  slug: azure-document-intelligence-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Azure Document Intelligence Rate Limits
  slug: azure-document-intelligence-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Azure AI Document Intelligence API Rules
  rule_count: 55
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 4
  slug: azure-document-intelligence-rules
scopes:
- name: Azure Document Intelligence Scopes
  scope_count: 1
  slug: azure-document-intelligence-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 40.4
    developer_ergonomics: 35.7
    discoverability: 80.4
    operational_transparency: 23.7
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/azure-document-intelligence/azure-document-intelligence-2026-06-20T172854.png
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
- Artificial Intelligence
- Document AI
- Microsoft Azure
- Intelligent Document Processing
- OCR
- Microsoft
- REST
website: https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence
---
