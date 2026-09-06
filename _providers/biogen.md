---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Biogen Agentic Access
  operation_count: 3
  slug: biogen-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://developer.biogen.com
  baseurl_source: declared
  description: API key management and usage
  name: Biogen Keys API
  slug: biogen-keys-api
- baseURL: https://developer.biogen.com
  baseurl_source: declared
  description: Available Biogen API services
  name: Biogen Services API
  slug: biogen-services-api
- baseURL: https://dev1.api.biogen.com
  baseurl_source: declared
  description: 'Service and package export lookups on Biogen''s non-production API gateway. This is the only Biogen API whose machine-readable definition is published anonymously — Biogen serves it as a Mashery/Boomi '
  name: Biogen CDP Export API (Non-Production)
  slug: biogen-cdp-export-api
artifact_total: 44
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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/biogen-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/biogen-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/biogen-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/biogen-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/biogen-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/biogen-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/biogen-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/biogen-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/biogen-mcp.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/biogen-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/biogen-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biogen.com/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biogen.com/privacy-center.html
- group: operate
  title: ''
  type: Support
  url: https://www.biogen.com/company/contact-us.html
- group: company
  title: ''
  type: Blog
  url: https://www.biogen.com/stories.html
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
modified: '2026-09-04'
name: Biogen
nav: Providers
network: true
overview: 'Biogen publishes 3 APIs on the [APIs.io](https://apis.io/) network: Keys API, Services API, and CDP Export API (Non-Production). Tagged areas include Biotechnology, Healthcare, Life Sciences, Pharmaceuticals, and Neurology.


  The Biogen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Biogen''s developer surface includes authentication, developer portal, documentation, sandbox, support, engineering blog, and 20 more developer resources.'
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
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 73.5
    catalog_earned_first_party: 16.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 33.3
    contract_quality: 20.4
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 23.7
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 48.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Biogen Authentication
  slug: biogen-authentication
  summary_line: apiKey · 2 schemes
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
