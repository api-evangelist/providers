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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Provider-centric, backend and bulk FHIR R4 APIs for integrating with the eClinicalWorks EHR. Supports SMART on FHIR EHR Launch, Standalone Launch, Backend Services (private_key_jwt, RS384) and CDS Hoo
  name: eClinicalWorks FHIR API
  slug: eclinicalworks-fhir-api
- description: Patient-facing FHIR R4 APIs accessible through the healow developer portal, letting third-party applications connect to the healow network for clinical data and scheduling. Served by the same eCW FHIR
  name: healow Patient-Centric FHIR API
  slug: healow-fhir-api
- description: Bidirectional FHIR R4 API for remote-patient-monitoring device vendors. healow sends signed device orders to a vendor-hosted endpoint (POST create, DELETE cancel within a 60-minute window, authenticat
  name: healow RPM Vendor (Tracker) API
  slug: healow-rpm-vendor-api
artifact_total: 13
asyncapis:
- description: ''
  name: Eclinicalworks Healow Rpm Webhooks
  slug: eclinicalworks-healow-rpm-webhooks
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir.eclinicalworks.com/ecwopendev/
- group: docs
  title: ''
  type: APIReference
  url: https://fhir.eclinicalworks.com/ecwopendev/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://fhir.eclinicalworks.com/ecwopendev/documentation/getting-started
- group: operate
  title: ''
  type: Support
  url: https://fhir.eclinicalworks.com/ecwopendev/documentation/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://connect4.healow.com/apps/jsp/dev/signUp.jsp
- group: start
  title: ''
  type: Login
  url: https://fhir.eclinicalworks.com/ecwopendev/login-page
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eclinicalworks.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eclinicalworks.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/eclinicalworks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eclinicalworks-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eclinicalworks-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eclinicalworks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.eclinicalworks.com/products-services/the-eclinicalworks-cloud/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eclinicalworks-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eclinicalworks-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eclinicalworks-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eclinicalworks-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eclinicalworks-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/eclinicalworks-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eclinicalworks-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eclinicalworks-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eclinicalworks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.eclinicalworks.com/responsible-disclosure-policy/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eclinicalworks-healow-rpm-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: conformance/eclinicalworks-fhir-capabilitystatement.json
created: '2026-06-13'
description: 'eClinicalWorks is a cloud-based EHR and practice-management platform serving more than 180,000 physicians and 850,000 medical professionals. Its API surface is standards-based rather than proprietary: FHIR R4 served by the eCW FHIR Facade behind SMART on FHIR and OAuth 2.0, split across a provider-facing facade (fhir4.eclinicalworks.com) and a patient-facing healow facade (fhir4.healow.com), each tenant-scoped by a six-character practice code. eClinicalWorks publishes no OpenAPI; the machine-readable contract is the FHIR CapabilityStatement at each tenant''s /metadata plus the SMART configuration at /.well-known/smart-configuration, which advertises 486 scopes. Capabilities include SMART EHR Launch and Standalone Launch, Backend Services with Group/$export bulk data, CDS Hooks, a documented writeback catalogue, patient-facing healow Clinical and Scheduling APIs, and a bidirectional healow RPM Vendor (Tracker) API for remote-monitoring device orders and observations. APIs are
  certified to the ONC 45 CFR 170.315(g)(10) Standardized API for Patient and Population Services criterion.'
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
mcp_servers:
- description: ''
  name: eclinicalworks-mcp.yml
  slug: eclinicalworks-mcpyml
modified: '2026-08-14'
name: eClinicalWorks
nav: Providers
network: true
overview: 'eClinicalWorks publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EHR, FHIR, Healthcare, Electronic Health Records, and Practice Management.


  The eClinicalWorks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  eClinicalWorks'' developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, signup flow, and 31 more developer resources.'
plans:
- name: Eclinicalworks Plans Pricing
  plan_count: 4
  slug: eclinicalworks-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Eclinicalworks Rate Limits
  slug: eclinicalworks-rate-limits
scopes:
- name: Eclinicalworks Scopes
  scope_count: 486
  slug: eclinicalworks-scopes
  summary_line: 486 scopes
score:
  band: exemplar
  composite: 70.0
  delta: 46.7
  facets:
    commercial_clarity: 92.1
    contract_quality: 72.5
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 23.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 73.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/eclinicalworks/refs/heads/main/screenshots/eclinicalworks-2026-06-20T180425.png
security:
- kind: authentication
  name: Eclinicalworks Authentication
  slug: eclinicalworks-authentication
  summary_line: oauth2/openIdConnect/http · 7 schemes
- kind: domain-security
  name: Eclinicalworks Domain Security
  slug: eclinicalworks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eclinicalworks Vulnerability Disclosure
  slug: eclinicalworks-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
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
- US Core
- USCDI
- Bulk Data
- Remote Patient Monitoring
- Interoperability
- ONC Certified
- CDS Hooks
- healow
website: https://www.eclinicalworks.com
---
