---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Provider-centric and backend/bulk FHIR APIs for integrating with eClinicalWorks EHR. Supports SMART on FHIR EHR Launch, Standalone Launch, Backend Services, and CDS Hooks. Enables access to clinical d
  name: eClinicalWorks FHIR API
  slug: eclinicalworks-fhir-api
- description: Patient-facing FHIR APIs accessible via the healow developer portal. Enables third-party applications to connect with the healow network for clinical data, scheduling, and remote patient monitoring in
  name: healow Patient-Centric FHIR API
  slug: healow-fhir-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eclinicalworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eclinicalworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://fhir.eclinicalworks.com/ecwopendev/documentation/getting-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/eclinicalworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eclinicalworks
- group: company
  title: ''
  type: Blog
  url: https://blog.eclinicalworks.com
- group: company
  title: ''
  type: BlogTopic
  url: https://blog.eclinicalworks.com/topic/apis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eclinicalworks.com/products-services/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://instatus.com/now/en/eclinicalworks.com
- group: other
  title: ''
  type: X
  url: https://x.com/eClinicalWorks
- group: commercial
  title: ''
  type: Plans
  url: plans/eclinicalworks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eclinicalworks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eclinicalworks-finops.yml
created: '2026-06-13'
description: eClinicalWorks is a cloud-based EHR and practice management platform serving more than 180,000 physicians and 850,000 medical professionals. It provides REST and FHIR-compliant APIs for accessing patient data, appointments, clinical notes, billing, and health information exchange. Third-party developers can build patient-facing apps via the healow developer portal and provider-facing or backend service apps via the eClinicalWorks FHIR developer portal, using SMART on FHIR and OAuth 2.0 authentication.
finops:
- name: Eclinicalworks Finops
  service_category: ''
  slug: eclinicalworks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eclinicalworks.png
jsonld:
- class_count: 21
  name: Eclinicalworks Context
  property_count: 8
  slug: eclinicalworks-context
layout: provider
modified: '2026-06-13'
name: eClinicalWorks
nav: Providers
network: true
overview: 'eClinicalWorks publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EHR, FHIR, Healthcare, Electronic Health Records, and Practice Management.


  The eClinicalWorks catalog on APIs.io includes 1 JSON-LD context.


  eClinicalWorks'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Eclinicalworks Plans Pricing
  plan_count: 4
  slug: eclinicalworks-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 0
  name: Eclinicalworks Rate Limits
  slug: eclinicalworks-rate-limits
score:
  band: emerging
  composite: 23.3
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eclinicalworks/refs/heads/main/screenshots/eclinicalworks-2026-06-20T180425.png
security:
- kind: domain-security
  name: Eclinicalworks Domain Security
  slug: eclinicalworks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eclinicalworks
tags:
- EHR
- FHIR
- Healthcare
- Electronic Health Records
- Practice Management
- Clinical Data
- Health Information Exchange
- Patient Data
- Appointments
- Billing
- SMART on FHIR
website: https://www.eclinicalworks.com
---
