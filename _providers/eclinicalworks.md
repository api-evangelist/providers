---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
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
artifact_total: 17
asyncapis:
- description: ''
  name: Eclinicalworks Healow Rpm Webhooks
  slug: eclinicalworks-healow-rpm-webhooks
common:
- group: design
  href: https://artifacts.apis.io/eclinicalworks/json-ld/eclinicalworks-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eclinicalworks-context.jsonld
- group: other
  href: https://artifacts.apis.io/eclinicalworks/hosts/eclinicalworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eclinicalworks-hosts.yml
- group: auth
  href: https://artifacts.apis.io/eclinicalworks/security/eclinicalworks-domain-security.yml
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
  href: https://artifacts.apis.io/eclinicalworks/plans/eclinicalworks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eclinicalworks-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/eclinicalworks/rate-limits/eclinicalworks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eclinicalworks-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/eclinicalworks/finops/eclinicalworks-finops.yml
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
  href: https://artifacts.apis.io/eclinicalworks/authentication/eclinicalworks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eclinicalworks-authentication.yml
- group: auth
  href: https://artifacts.apis.io/eclinicalworks/scopes/eclinicalworks-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/eclinicalworks-scopes.yml
- group: agent
  href: https://artifacts.apis.io/eclinicalworks/well-known/eclinicalworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eclinicalworks-well-known.yml
- group: design
  href: https://artifacts.apis.io/eclinicalworks/conformance/eclinicalworks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eclinicalworks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.eclinicalworks.com/products-services/the-eclinicalworks-cloud/
- group: design
  href: https://artifacts.apis.io/eclinicalworks/errors/eclinicalworks-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/eclinicalworks-error-codes.yml
- group: design
  href: https://artifacts.apis.io/eclinicalworks/lifecycle/eclinicalworks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/eclinicalworks-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/eclinicalworks/conventions/eclinicalworks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eclinicalworks-conventions.yml
- group: design
  href: https://artifacts.apis.io/eclinicalworks/data-model/eclinicalworks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eclinicalworks-data-model.yml
- group: start
  href: https://artifacts.apis.io/eclinicalworks/sandbox/eclinicalworks-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/eclinicalworks-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/eclinicalworks/mcp/eclinicalworks-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/eclinicalworks-mcp.yml
- group: auth
  href: https://artifacts.apis.io/eclinicalworks/security/eclinicalworks-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/eclinicalworks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.eclinicalworks.com/responsible-disclosure-policy/
- group: design
  href: https://artifacts.apis.io/eclinicalworks/asyncapi/eclinicalworks-healow-rpm-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/eclinicalworks-healow-rpm-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/eclinicalworks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/eclinicalworks/conformance/eclinicalworks-fhir-capabilitystatement.json
  title: ''
  type: CapabilityStatement
  url: conformance/eclinicalworks-fhir-capabilitystatement.json
created: '2026-06-13'
description: 'eClinicalWorks is a cloud-based EHR and practice-management platform serving more than 180,000 physicians and 850,000 medical professionals. Its API surface is standards-based rather than proprietary: FHIR R4 served by the eCW FHIR Facade behind SMART on FHIR and OAuth 2.0, split across a provider-facing facade (fhir4.eclinicalworks.com) and a patient-facing healow facade (fhir4.healow.com), each tenant-scoped by a six-character practice code. eClinicalWorks publishes no OpenAPI; the machine-readable contract is the FHIR CapabilityStatement at each tenant''s /metadata plus the SMART configuration at /.well-known/smart-configuration, which advertises 486 scopes. Capabilities include SMART EHR Launch and Standalone Launch, Backend Services with Group/$export bulk data, CDS Hooks, a documented writeback catalogue, patient-facing healow Clinical and Scheduling APIs, and a bidirectional healow RPM Vendor (Tracker) API for remote-monitoring device orders and observations. APIs are
  certified to the ONC 45 CFR 170.315(g)(10) Standardized API for Patient and Population Services criterion.'
finops:
- has_sources: true
  method: derived
  name: Eclinicalworks Finops
  primary_unit: provider/month
  service_category: ''
  slug: eclinicalworks-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eclinicalworks.png
jsonld:
- class_count: 21
  name: Eclinicalworks Context
  property_count: 8
  slug: eclinicalworks-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.eclinicalworks.com requiring OAuth.
  name: eClinicalWorks MCP Server
  slug: eclinicalworks-mcp-yml
modified: '2026-10-12'
name: eClinicalWorks
nav: Providers
network: true
overview: 'eClinicalWorks is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electronic Health Records, FHIR, Healthcare, Practice Management, and Clinical Data.


  The eClinicalWorks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  eClinicalWorks'' developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, signup flow, and 31 more developer resources.'
plans:
- name: Eclinicalworks Plans Pricing
  plan_count: 4
  slug: eclinicalworks-plans-pricing
- name: Eclinicalworks Price Estimates
  plan_count: 0
  slug: eclinicalworks-price-estimates
random_paper: 10
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
  composite: 69.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 71.0
    catalog_earned_first_party: 20.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 66.1
    discoverability: 73.3
    operational_transparency: 55.3
  previous_composite: 69.1
  provenance:
    conformance: first-party
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/eclinicalworks/eclinicalworks-2026-06-20T180425.png
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
skill_count: 3
skills:
- name: eclinicalworks-bulk-group-export
  slug: eclinicalworks-bulk-group-export
- name: eclinicalworks-healow-rpm-vendor-integration
  slug: eclinicalworks-healow-rpm-vendor-integration
- name: eclinicalworks-smart-standalone-patient-read
  slug: eclinicalworks-smart-standalone-patient-read
slug: eclinicalworks
tags:
- Electronic Health Records
- FHIR
- Healthcare
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
