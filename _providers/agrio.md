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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agrio Agentic Access
  operation_count: 3
  slug: agrio-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 5
apis:
- description: Account credit balance and usage monitoring.
  name: agrio Balance API
  slug: agrio-balance-api
- description: Credit management for API usage.
  name: agrio Credit API
  slug: agrio-credit-api
- description: Supported agricultural crop types.
  name: agrio Crops API
  slug: agrio-crops-api
- description: Plant disease and pest diagnosis from images.
  name: agrio Diagnose API
  slug: agrio-diagnose-api
- description: Diagnosis results and disease identification data.
  name: agrio Diagnosis API
  slug: agrio-diagnosis-api
artifact_total: 48
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agrio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agrio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agrio-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://agrio.app/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agrio-app
- group: company
  title: ''
  type: Website
  url: https://agrio.app
- group: start
  title: ''
  type: Portal
  url: https://pro.agrio.app/image-diagnosis-api
- group: operate
  title: ''
  type: Support
  url: mailto:info@saillog.co
- group: design
  title: ''
  type: SpectralRules
  url: rules/agrio-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agrio-vocabulary.yaml
description: Agrio is a precision plant protection solution that helps growers and crop advisors forecast, identify, and treat plant diseases, pests, and nutrient deficiencies. With Agrio APIs, developers can access AI-powered plant disease diagnosis from images, crop advisory data, weather pattern analysis, pest and disease predictions, and satellite vegetation monitoring to build accurate crop advisory tools.
examples:
- key_count: 3
  name: Agrio Credit Balance Example
  slug: agrio-credit-balance-example
- key_count: 3
  name: Agrio Crop Example
  slug: agrio-crop-example
- key_count: 2
  name: Agrio Diagnose Request Example
  slug: agrio-diagnose-request-example
- key_count: 3
  name: Agrio Diagnosis Example
  slug: agrio-diagnosis-example
- key_count: 4
  name: Agrio Diagnosis Result Example
  slug: agrio-diagnosis-result-example
- key_count: 3
  name: Agrio Error Response Example
  slug: agrio-error-response-example
- key_count: 1
  name: Agrio Supported Crops Response Example
  slug: agrio-supported-crops-response-example
features:
- description: Computer vision algorithms identify plant diseases, pests, and nutrient deficiencies from uploaded photos with confidence scores.
  name: AI Image Diagnosis
- description: Predictive algorithms forecast disease pressure before or between scouting events to enable proactive intervention.
  name: AgrioShield Pest Prediction
- description: Remote sensing AI detects vegetation issues from satellite data, enabling early detection before visible symptoms appear.
  name: Satellite Imagery Alerts
- description: Returns multiple ranked diagnoses with confidence scores, common names, and scientific names for disambiguation.
  name: Ranked Diagnoses
- description: API usage is metered using a credit system; one credit is consumed per diagnosis request.
  name: Credit-Based Usage
- description: Discoverable catalog of supported crop types for building targeted diagnosis workflows.
  name: Supported Crop Catalog
finops:
- name: Agrio Finops
  service_category: API
  slug: agrio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agrio.png
integrations:
- description: Agrio APIs integrate weather pattern data to enhance pest and disease prediction models.
  name: Weather Data Systems
- description: Remote sensing data from satellite providers is used for vegetation monitoring and anomaly detection.
  name: Satellite Imagery Providers
json_schemas:
- name: Credit Balance
  property_count: 3
  slug: agrio-credit-balance
- name: Crop
  property_count: 3
  slug: agrio-crop
- name: Diagnose Request
  property_count: 2
  slug: agrio-diagnose-request
- name: Diagnosis Result
  property_count: 4
  slug: agrio-diagnosis-result
- name: Diagnosis
  property_count: 3
  slug: agrio-diagnosis
- name: Error Response
  property_count: 3
  slug: agrio-error-response
- name: Supported Crops Response
  property_count: 1
  slug: agrio-supported-crops-response
json_structures:
- name: Agrio Credit Balance Structure
  property_count: 3
  slug: agrio-credit-balance-structure
- name: Agrio Crop Structure
  property_count: 3
  slug: agrio-crop-structure
- name: Agrio Diagnose Request Structure
  property_count: 2
  slug: agrio-diagnose-request-structure
- name: Agrio Diagnosis Result Structure
  property_count: 4
  slug: agrio-diagnosis-result-structure
- name: Agrio Diagnosis Structure
  property_count: 3
  slug: agrio-diagnosis-structure
- name: Agrio Error Response Structure
  property_count: 3
  slug: agrio-error-response-structure
- name: Agrio Supported Crops Response Structure
  property_count: 1
  slug: agrio-supported-crops-response-structure
jsonld:
- class_count: 7
  name: Agrio Context
  property_count: 16
  slug: agrio-context
layout: provider
modified: '2026-05-19'
name: agrio
nav: Providers
network: true
overview: 'agrio publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Credit API, Crops API, and 2 more. Tagged areas include Agriculture, Plant Disease, Pest Detection, AI, and Crop Advisory.


  The agrio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  agrio''s developer surface includes authentication, engineering blog, developer portal, support, and 6 more developer resources.'
plans:
- name: Agrio Plans Pricing
  plan_count: 3
  slug: agrio-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Agrio Rate Limits
  slug: agrio-rate-limits
rules:
- name: agrio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agrio-jsonschema-spectral-rules
- name: agrio API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 15
  slug: agrio-spectral-rules
score:
  band: developing
  composite: 54.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 84.5
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agrio/refs/heads/main/screenshots/agrio-2026-06-20T170436.png
security:
- kind: authentication
  name: Agrio Authentication
  slug: agrio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agrio Domain Security
  slug: agrio-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: agrio
tags:
- Agriculture
- Plant Disease
- Pest Detection
- AI
- Crop Advisory
use_cases:
- description: Embed AI plant disease diagnosis into existing crop advisory and farm management applications.
  name: Crop Advisory Tool Integration
- description: Enable agronomists and farmers to photograph plant symptoms and receive immediate AI-powered diagnosis.
  name: In-Field Disease Identification
- description: Use AgrioShield alerts to notify growers when disease or pest conditions become favorable before visible symptoms appear.
  name: Early Warning Systems
- description: Integrate Agrio diagnosis into precision agriculture platforms for targeted treatment recommendations.
  name: Precision Agriculture Platforms
- description: Access Agrio plant disease data for agricultural research and development of new advisory models.
  name: Research and Development
website: https://agrio.app
---
