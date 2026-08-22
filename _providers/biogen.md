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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Biogen Agentic Access
  operation_count: 3
  slug: biogen-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: API key management and usage
  name: Biogen Keys API
  slug: biogen-keys-api
- description: Available Biogen API services
  name: Biogen Services API
  slug: biogen-services-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Biogen Developer API
  slug: open-biogen-developer-api
- collection_type: open
  name: Biogen Developer Keys API
  slug: open-biogen-keys-api
- collection_type: open
  name: Biogen Developer Keys Services API
  slug: open-biogen-services-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/biogen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biogen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/biogen-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Biogen-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biogen-
- group: start
  title: ''
  type: Portal
  url: https://developer.biogen.com/
- group: company
  title: ''
  type: Website
  url: https://www.biogen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.biogen.com/io-docs
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/rules/biogen-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/vocabulary/biogen-vocabulary.yaml
created: '2025-01-01'
description: Biogen is a global biotechnology company that discovers, develops, and delivers therapies for people living with serious neurological diseases including multiple sclerosis, Alzheimer's, and spinal muscular atrophy.
examples:
- key_count: 6
  name: Biogen Api Key Example
  slug: biogen-api-key-example
- key_count: 2
  name: Biogen Api Key Usage Example
  slug: biogen-api-key-usage-example
- key_count: 1
  name: Biogen Api Keys Response Example
  slug: biogen-api-keys-response-example
- key_count: 2
  name: Biogen Create Api Key Request Example
  slug: biogen-create-api-key-request-example
- key_count: 4
  name: Biogen Service Example
  slug: biogen-service-example
- key_count: 1
  name: Biogen Services Response Example
  slug: biogen-services-response-example
features:
- description: Programmatic access to Copaxone CRX pharmaceutical service.
  name: CCS-CRX API
- description: Self-service API key creation and usage monitoring via developer portal.
  name: API Key Management
- description: Interactive API documentation for testing endpoints directly in the browser.
  name: Interactive I/O Docs
- description: Monitor API request volumes and usage statistics per key.
  name: Usage Reporting
- description: REST-compliant API design following standard HTTP methods and response codes.
  name: REST Standards
finops:
- name: Biogen Finops
  service_category: Life Sciences / Pharmaceuticals
  slug: biogen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/biogen.png
integrations:
- description: Connect EHR and healthcare IT systems to Biogen pharmaceutical APIs.
  name: Healthcare IT Systems
- description: Integrate with Biogen patient support and copay assistance programs.
  name: Patient Support Programs
json_schemas:
- name: ApiKey
  property_count: 6
  slug: biogen-api-key
- name: ApiKeyUsage
  property_count: 2
  slug: biogen-api-key-usage
- name: ApiKeysResponse
  property_count: 1
  slug: biogen-api-keys-response
- name: CreateApiKeyRequest
  property_count: 2
  slug: biogen-create-api-key-request
- name: Service
  property_count: 4
  slug: biogen-service
- name: ServicesResponse
  property_count: 1
  slug: biogen-services-response
json_structures:
- name: Biogen Api Key Structure
  property_count: 6
  slug: biogen-api-key-structure
- name: Biogen Api Key Usage Structure
  property_count: 2
  slug: biogen-api-key-usage-structure
- name: Biogen Api Keys Response Structure
  property_count: 1
  slug: biogen-api-keys-response-structure
- name: Biogen Create Api Key Request Structure
  property_count: 2
  slug: biogen-create-api-key-request-structure
- name: Biogen Service Structure
  property_count: 4
  slug: biogen-service-structure
- name: Biogen Services Response Structure
  property_count: 1
  slug: biogen-services-response-structure
jsonld:
- class_count: 5
  name: Biogen Context
  property_count: 5
  slug: biogen-context
layout: provider
modified: '2026-04-21'
name: Biogen
nav: Providers
network: true
overview: 'Biogen publishes 2 APIs on the [APIs.io](https://apis.io/) network: Keys API and Services API. Tagged areas include Biotechnology, Healthcare, Life Sciences, Pharmaceuticals, and Neurology.


  The Biogen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Biogen''s developer surface includes authentication, developer portal, documentation, and 7 more developer resources.'
plans:
- name: Biogen Plans Pricing
  plan_count: 1
  slug: biogen-plans-pricing
press:
- date: '2026-05-25'
  title: Biogen Chooses Lexalytics® to Improve Customer Care ...
  url: https://www.lexalytics.com/news/biogen-chooses-lexalytics/
- date: '2026-05-25'
  title: Biogen and TheraPanacea Announce New Collaboration ...
  url: https://investors.biogen.com/news-releases/news-release-details/biogen-and-therapanacea-announce-new-collaboration-potential
- date: '2026-05-25'
  title: Biogen and City Therapeutics Announce Strategic ...
  url: https://investors.biogen.com/news-releases/news-release-details/biogen-and-city-therapeutics-announce-strategic-research
- date: '2026-05-25'
  title: Biogen's CIO is betting on a tech and AI overhaul to 'pave ...
  url: https://www.pharmavoice.com/news/biogen-cio-ai-tech-guy-hadari-growth-drug-pharma/808323/
- date: '2026-05-25'
  title: FINANCIAL RESULTS AND BUSINESS UPDATE
  url: https://investors.biogen.com/static-files/0612f509-be22-438f-b817-3acba3917b0b
random_paper: 19
rate_limits:
- limit_count: 1
  name: Biogen Rate Limits
  slug: biogen-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Biogen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: biogen-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Biogen API Rules
  rule_count: 28
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 21
  slug: biogen-spectral-rules
score:
  band: emerging
  composite: 25.3
  delta: -3.6
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 20.9
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Biogen Authentication
  slug: biogen-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Biogen Domain Security
  slug: biogen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biogen
tags:
- Biotechnology
- Healthcare
- Life Sciences
- Pharmaceuticals
- Neurology
- Fortune 500
use_cases:
- description: Integrate with Biogen pharmaceutical services like CCS-CRX programmatically.
  name: Pharmaceutical Service Integration
- description: Self-service API key registration and service access via developer portal.
  name: Developer Onboarding
- description: Connect healthcare systems to Biogen services for patient program support.
  name: Healthcare System Integration
website: https://www.biogen.com/
---
