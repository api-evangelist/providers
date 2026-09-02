---
agent_readiness:
  band: agent-aware
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Autoderm Ai Dermatology Api Agentic Access
  operation_count: 17
  slug: autoderm-ai-dermatology-api-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 2
apis:
- description: The device API from Autoderm – AI Dermatology API — 1 operation(s) for device.
  name: Autoderm – AI Dermatology API Device API
  slug: autoderm-ai-dermatology-api-device-api
- description: The inference API from Autoderm – AI Dermatology API — 5 operation(s) for inference.
  name: Autoderm – AI Dermatology API Inference API
  slug: autoderm-ai-dermatology-api-inference-api
- description: The system API from Autoderm – AI Dermatology API — 6 operation(s) for system.
  name: Autoderm – AI Dermatology API System API
  slug: autoderm-ai-dermatology-api-system-api
- description: The utils API from Autoderm – AI Dermatology API — 1 operation(s) for utils.
  name: Autoderm – AI Dermatology API Utils API
  slug: autoderm-ai-dermatology-api-utils-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Autoderm Device API
  slug: open-autoderm-ai-dermatology-api-device-api
- collection_type: open
  name: Autoderm Inference API
  slug: open-autoderm-ai-dermatology-api-inference-api
- collection_type: open
  name: Autoderm System API
  slug: open-autoderm-ai-dermatology-api-system-api
- collection_type: open
  name: Autoderm Utils API
  slug: open-autoderm-ai-dermatology-api-utils-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/autoderm-ai-dermatology-api-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://autoderm.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.autoderm.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.autoderm.ai/en
- group: docs
  title: ''
  type: APIReference
  url: https://docs.autoderm.ai/en/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.autoderm.ai/en/getting-started/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.autoderm.ai/en/support/support-contact
- group: company
  title: ''
  type: Blog
  url: https://autoderm.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autodermai
- group: commercial
  title: ''
  type: Pricing
  url: https://autoderm.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.autoderm.ai/en/auth/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.autoderm.ai/en/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autoderm.ai/terms-of-service-autoderm/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autoderm.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://autoderm.ai/regulatory/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.autoderm.ai/en/support/api-versioning
- group: design
  title: ''
  type: Versioning
  url: https://docs.autoderm.ai/en/support/api-versioning
- group: auth
  title: ''
  type: Authentication
  url: authentication/autoderm-ai-dermatology-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/autoderm-ai-dermatology-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/autoderm-ai-dermatology-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autoderm-ai-dermatology-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autoderm-ai-dermatology-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/autoderm-ai-dermatology-api-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/autoderm-ai-dermatology-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/autoderm-ai-dermatology-api-plans.yml
- group: build
  title: ''
  type: Packages
  url: packages/autoderm-ai-dermatology-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/autoderm-ai-dermatology-api-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: other
  title: ''
  type: Overlay
  url: overlays/autoderm-ai-dermatology-api-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autoderm-ai-dermatology-api-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/autoderm-ai-dermatology-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autoderm-ai-dermatology-api-domain-security.yml
created: '2026-08-07'
description: Autoderm is a white-label REST API for AI-assisted analysis of dermatological images, operated as a regulated medical device. A client POSTs a single skin photograph as multipart/form-data and receives the top five most probable conditions, each with a confidence score between 0 and 1, an ICD-10 code and an English name; a companion static catalog maps every ICD-10 code to localized and layman's names plus read-more links in seven languages. Alongside disease detection the API exposes Fitzpatrick skin-type classification, a blur/image-quality screen, a genitalia content-safety classifier, an age estimator, and — unusually — the regulatory device label itself as a live anonymous endpoint. Autoderm is CE-marked under EU MDD 93/42/EEC as a legacy Class I device, is transitioning to MDR Class IIa under EU MDR 2017/745, and holds FDA Breakthrough Device Designation. It is sold into telemedicine, pharmacy, and digital health platforms as a decision-support and triage tool, and is
  explicitly not intended as a means of diagnosis.
examples:
- key_count: 1
  name: Autoderm Ai Dermatology Api Get Disease Catalog 401
  slug: autoderm-ai-dermatology-api-get-disease-catalog-401
- key_count: 1
  name: Autoderm Ai Dermatology Api Get Health 200
  slug: autoderm-ai-dermatology-api-get-health-200
- key_count: 11
  name: Autoderm Ai Dermatology Api Get Label 200
  slug: autoderm-ai-dermatology-api-get-label-200
- key_count: 2
  name: Autoderm Ai Dermatology Api Get Version 200
  slug: autoderm-ai-dermatology-api-get-version-200
image: https://autoderm.ai/wp-content/uploads/2026/05/autoderm-logo.svg
json_schemas:
- name: AgeModelResponse
  property_count: 1
  slug: autoderm-ai-dermatology-api-AgeModelResponse
- name: Body_detect_blur_v1_utils_detect_blur_post
  property_count: 1
  slug: autoderm-ai-dermatology-api-Body_detect_blur_v1_utils_detect_blur_post
- name: Body_infer_age_v1_v1_infer_age_v1_post
  property_count: 1
  slug: autoderm-ai-dermatology-api-Body_infer_age_v1_v1_infer_age_v1_post
- name: Body_infer_diseases_v1_v1_infer_diseases_v1_post
  property_count: 1
  slug: autoderm-ai-dermatology-api-Body_infer_diseases_v1_v1_infer_diseases_v1_post
- name: Body_infer_genitals_v1_v1_infer_genitals_v1_post
  property_count: 1
  slug: autoderm-ai-dermatology-api-Body_infer_genitals_v1_v1_infer_genitals_v1_post
- name: Body_infer_skin_tone_v1_v1_infer_skin_tone_v1_post
  property_count: 1
  slug: autoderm-ai-dermatology-api-Body_infer_skin_tone_v1_v1_infer_skin_tone_v1_post
- name: BooleanAnalysis
  property_count: 2
  slug: autoderm-ai-dermatology-api-BooleanAnalysis
- name: DetectBlurResponse
  property_count: 2
  slug: autoderm-ai-dermatology-api-DetectBlurResponse
- name: DiseaseCatalogEntry
  property_count: 9
  slug: autoderm-ai-dermatology-api-DiseaseCatalogEntry
- name: DiseaseCatalogLocalizedEntry
  property_count: 3
  slug: autoderm-ai-dermatology-api-DiseaseCatalogLocalizedEntry
- name: DiseaseCategory
  property_count: 0
  slug: autoderm-ai-dermatology-api-DiseaseCategory
- name: DiseaseModelResponse
  property_count: 2
  slug: autoderm-ai-dermatology-api-DiseaseModelResponse
- name: DiseasePrediction
  property_count: 4
  slug: autoderm-ai-dermatology-api-DiseasePrediction
- name: HTTPValidationError
  property_count: 1
  slug: autoderm-ai-dermatology-api-HTTPValidationError
- name: MedicalDeviceLabel
  property_count: 11
  slug: autoderm-ai-dermatology-api-MedicalDeviceLabel
- name: SkinToneModelResponse
  property_count: 2
  slug: autoderm-ai-dermatology-api-SkinToneModelResponse
- name: ValidationError
  property_count: 5
  slug: autoderm-ai-dermatology-api-ValidationError
- name: Version
  property_count: 2
  slug: autoderm-ai-dermatology-api-Version
layout: provider
mcp_servers:
- description: Autoderm publishes NO hosted or remote MCP server. This manifest is a CANDIDATE tool surface derived one-to-one from the operations in Autoderm's own OpenAPI — it describes what an MCP server for this
  name: Autoderm – AI Dermatology API MCP Server
  slug: autoderm-ai-dermatology-api-mcp-server
modified: '2026-08-09'
name: Autoderm – AI Dermatology API
nav: Providers
network: true
overview: 'Autoderm – AI Dermatology API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Device API, Inference API, System API, and 1 more. Tagged areas include dermatology-api, ai-dermatology, Medical Imaging, Telemedicine, and skin-analysis.


  Autoderm – AI Dermatology API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Autoderm Ai Dermatology Api Plans
  plan_count: 3
  slug: autoderm-ai-dermatology-api-plans
random_paper: 19
rate_limits:
- limit_count: 3
  name: Autoderm Ai Dermatology Api Rate Limits
  slug: autoderm-ai-dermatology-api-rate-limits
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 24
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 56.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autoderm-ai-dermatology-api/refs/heads/main/screenshots/autoderm-ai-dermatology-api-2026-08-17T080622.png
security:
- kind: authentication
  name: Autoderm Ai Dermatology Api Authentication
  slug: autoderm-ai-dermatology-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Autoderm Ai Dermatology Api Domain Security
  slug: autoderm-ai-dermatology-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autoderm-ai-dermatology-api
tags:
- dermatology-api
- ai-dermatology
- Medical Imaging
- Telemedicine
- skin-analysis
- REST API
- OpenAPI
- llms-txt
- ce-marked
- White Label
- Healthcare
- Medical AI
- Computer-Vision
- Medical Device
- ICD-10
- image-classification
- Clinical Decision Support
- triage
website: https://autoderm.ai/
---
