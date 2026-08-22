---
access_model:
  confidence: high
  label: Enterprise contract; API credentials provisioned per health system
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/dexcare-plans-pricing.yml
  - https://developers.dexcarehealth.com/api/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 40.8
  scored_at: '2026-08-19'
api_count: 7
apis:
- description: RESTful service for accessing business information and performing actions against DexCare-managed healthcare environments. The umbrella reference covering the Patient and Reporting surfaces, which are
  name: DexCare REST API
  slug: dexcare-rest-api
- description: Create and follow on-demand virtual visits, and read regional virtual-care availability and estimated wait times. Declares two distinct bearer schemes, PatientJWT and StaffJWT, bound to different oper
  name: DexCare Visit Service API
  slug: dexcare-visit-service-api
- description: Aggregated in-person and virtual appointment discovery across a health system, returning available providers and timeslots filtered by location, specialty, visit type and date range. OpenAPI 3.0.3, ve
  name: DexCare Care Options API
  slug: dexcare-care-options-api
- description: Provider- and department-level appointment slot search, addressed by National Provider Identifier, plus the slot-taken and slot-released notifications a health system sends DexCare when its own schedu
  name: DexCare Slots Availability API
  slug: dexcare-slots-availability-api
- description: Books an in-person appointment for a queued guest visit once a timeslot has been selected. OpenAPI 3.0.3, version 1.2.0, 1 operation.
  name: DexCare Visit Booking API
  slug: dexcare-visit-booking-api
- description: 'Natural-language care search across a health system''s clinicians and clinics. Rules-based NLP tokenizes and stems the query, expands clinical synonyms, tolerates spelling errors and infers intent and '
  name: DexCare Omni Search API
  slug: dexcare-omni-search-api
- description: Schema-driven query and export of the provider, department, location and business-line golden record held in DexCare PDM+. The JSON Schema for any entity type is itself retrievable at runtime, and bat
  name: DexCare Provider Data Management API
  slug: dexcare-provider-data-management-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://dexcare.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dexcarehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dexcarehealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dexcarehealth.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dexcarehealth.com/jssdk/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DexCare
- group: company
  title: ''
  type: Blog
  url: https://dexcare.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dexcare.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dexcare.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://developers.dexcarehealth.com/home/support
- group: build
  title: ''
  type: Packages
  url: packages/dexcare-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dexcare-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dexcare-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dexcare-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dexcare-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dexcare-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.dexcarehealth.com/home/support
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dexcare-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dexcare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dexcare.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dexcare-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dexcare-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dexcare-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dexcare-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dexcare-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dexcare-plans-pricing.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dexcare-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'DexCare is a healthcare navigation and care-orchestration platform, launched from within Providence Health, that connects patients to available care across fragmented health systems while helping providers fill capacity and reduce wait times. Its products span Search & Schedule, Virtual On Demand, Provider Data Management (PDM+), Optimize AI, and Acquire. DexCare publishes six OpenAPI definitions on its own developer portal covering 27 operations across the Visit Service, Visit Booking, Care Options, Slots Availability, Omni Search and Provider Data Management services, alongside prose references for the Patient and Reporting APIs and native iOS, Android and JavaScript SDKs. There is no shared base URL: every health system is provisioned its own UAT and production hosts, and the published specifications use templated or per-tenant servers. Public directory, availability and search endpoints are open, while PHI/PII endpoints require an OAuth 2.0-issued JWT bearer token and server-to-server
  services require a DexCare-issued x-api-key. DexCare operates as a HIPAA business associate. This profile was enriched from DexCare''s public developer surface as part of the API Evangelist network (originally surfaced as an ICONIQ Capital portfolio lead).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dexcare.png
layout: provider
mcp_servers:
- description: ''
  name: dexcare-mcp.yml
  slug: dexcare-mcpyml
modified: '2026-08-15'
name: DexCare
nav: Providers
network: true
overview: 'DexCare publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Visit Service API, Care Options API, Slots Availability API, and 3 more. Tagged areas include Company, Healthcare, Health IT, Patient Access, and Scheduling.


  DexCare''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 21 more developer resources.'
plans:
- name: Dexcare Plans Pricing
  plan_count: 0
  slug: dexcare-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Dexcare Rate Limits
  slug: dexcare-rate-limits
score:
  band: developing
  composite: 52.5
  delta: 4.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 56.2
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 48.4
  provenance:
    conformance: first-party
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/screenshots/dexcare-2026-07-25T211834.png
security:
- kind: authentication
  name: Dexcare Authentication
  slug: dexcare-authentication
  summary_line: oauth2/http/apiKey/none · 7 schemes
- kind: domain-security
  name: Dexcare Domain Security
  slug: dexcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dexcare
tags:
- Company
- Healthcare
- Health IT
- Patient Access
- Scheduling
- Virtual Care
- Telehealth
- Care Navigation
- Provider Data
- Search
- SDK
website: https://dexcare.com/
---
