---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Thriva Agentic Access
  operation_count: 29
  slug: thriva-agentic-access
  summary_line: 29 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Appointments API API from Thriva — 2 operation(s) for appointments api.
  name: Thriva Appointments API
  slug: thriva-appointments-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Auth API API from Thriva — 1 operation(s) for auth api.
  name: Thriva Auth API
  slug: thriva-auth-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Biomarkers API API from Thriva — 1 operation(s) for biomarkers api.
  name: Thriva Biomarkers API
  slug: thriva-biomarkers-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Bulk Orders API API from Thriva — 4 operation(s) for bulk orders api.
  name: Thriva Bulk Orders API
  slug: thriva-bulk-orders-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Escalations API API from Thriva — 1 operation(s) for escalations api.
  name: Thriva Escalations API
  slug: thriva-escalations-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Orders API API from Thriva — 7 operation(s) for orders api.
  name: Thriva Orders API
  slug: thriva-orders-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Result attachments API API from Thriva — 2 operation(s) for result attachments api.
  name: Thriva Result attachments API
  slug: thriva-result-attachments-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Results API API from Thriva — 2 operation(s) for results api.
  name: Thriva Results API
  slug: thriva-results-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Tracking API API from Thriva — 1 operation(s) for tracking api.
  name: Thriva Tracking API
  slug: thriva-tracking-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Users API API from Thriva — 3 operation(s) for users api.
  name: Thriva Users API
  slug: thriva-users-api-api
artifact_total: 29
asyncapis:
- description: ''
  name: Thriva Webhooks
  slug: thriva-webhooks
collections:
- collection_type: open
  name: Platform API V1 Appointments API API
  slug: open-thriva-appointments-api-api
- collection_type: open
  name: Platform API V1 Appointments API Auth API API
  slug: open-thriva-auth-api-api
- collection_type: open
  name: Platform API V1 Appointments API Biomarkers API API
  slug: open-thriva-biomarkers-api-api
- collection_type: open
  name: Platform API V1 Appointments API Bulk Orders API API
  slug: open-thriva-bulk-orders-api-api
- collection_type: open
  name: Platform API V1 Appointments API Escalations API API
  slug: open-thriva-escalations-api-api
- collection_type: open
  name: Platform API V1 Appointments API Orders API API
  slug: open-thriva-orders-api-api
- collection_type: open
  name: Platform API V1 Appointments API Result attachments API API
  slug: open-thriva-result-attachments-api-api
- collection_type: open
  name: Platform API V1 Appointments API Results API API
  slug: open-thriva-results-api-api
- collection_type: open
  name: Platform API V1 Appointments API Tracking API API
  slug: open-thriva-tracking-api-api
- collection_type: open
  name: Platform API V1 Appointments API Users API API
  slug: open-thriva-users-api-api
common:
- group: other
  href: https://artifacts.apis.io/thriva/capabilities/thriva-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thriva-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/thriva/overlays/thriva-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thriva-platform-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://thriva.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.thriva.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thriva.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thriva.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thriva.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/thrivahelpcenter/en/
- group: company
  title: ''
  type: Blog
  url: https://thriva.co/hub
- group: start
  title: ''
  type: Login
  url: https://thriva.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://s3-eu-west-1.amazonaws.com/thriva/legal/Website+Terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thriva.co/privacy-policy
- group: auth
  href: https://artifacts.apis.io/thriva/authentication/thriva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thriva-authentication.yml
- group: other
  href: https://artifacts.apis.io/thriva/well-known/thriva-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/thriva-openid-configuration.json
- group: design
  href: https://artifacts.apis.io/thriva/conventions/thriva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thriva-conventions.yml
- group: design
  href: https://artifacts.apis.io/thriva/conformance/thriva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thriva-conformance.yml
- group: design
  href: https://artifacts.apis.io/thriva/errors/thriva-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thriva-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thriva/lifecycle/thriva-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thriva-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/thriva/sandbox/thriva-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thriva-sandbox.yml
- group: design
  href: https://artifacts.apis.io/thriva/asyncapi/thriva-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thriva-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/thriva/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/thriva/mcp/thriva-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thriva-mcp.yml
- group: agent
  href: https://artifacts.apis.io/thriva/llms/thriva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thriva-llms.txt
- group: agent
  href: https://artifacts.apis.io/thriva/well-known/thriva-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thriva-well-known.yml
- group: build
  href: https://artifacts.apis.io/thriva/packages/thriva-packages.yml
  title: ''
  type: Packages
  url: packages/thriva-packages.yml
- group: design
  href: https://artifacts.apis.io/thriva/components/thriva-components.yml
  title: ''
  type: Components
  url: components/thriva-components.yml
- group: design
  href: https://artifacts.apis.io/thriva/data-model/thriva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thriva-data-model.yml
- group: agent
  href: https://artifacts.apis.io/thriva/agentic-access/thriva-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thriva-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/thriva/security/thriva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thriva-domain-security.yml
created: '2026-07-17'
description: Thriva is a UK digital-health company and the UK market leader in at-home consumer diagnostics, tracking 75+ blood biomarkers with doctor-reviewed insights. Alongside its direct-to-consumer service, the Thriva Platform offers partners a white-label at-home blood-testing infrastructure - kit logistics, lab processing, results and clinical escalations - through a RESTful JSON:API Platform API with OAuth2 client-credentials auth, Svix-signed webhooks and a full sandbox environment.
image: https://images.prismic.io/thriva/aXInFwIvOtkhB0T__WebisteBox_Wide_v5-1-.jpg
json_schemas:
- name: Thriva Platform API V1 - component schemas
  property_count: 0
  slug: thriva-platform-api-schemas
layout: provider
modified: '2026-09-16'
name: Thriva
nav: Providers
network: true
overview: 'Thriva publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointments API, Auth API, Biomarkers API, and 7 more. Tagged areas include Company, Healthcare, Diagnostics, Blood Testing, and At-Home Testing.


  The Thriva catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Thriva''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 22 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Thriva API Rules
  rule_count: 45
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 4
  slug: thriva-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 46.9
    catalog_earned_first_party: 0.0
    catalog_gap: 68.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 27.6
    contract_governance: 31.8
    contract_quality: 54.5
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thriva/thriva-2026-08-17T082348.png
security:
- kind: authentication
  name: Thriva Authentication
  slug: thriva-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Thriva Domain Security
  slug: thriva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Bulk-order kits and register samples
  slug: thriva-bulk-order-flow
- name: Handle clinical escalations
  slug: thriva-handle-clinical-escalations
- name: Order an at-home test and retrieve results
  slug: thriva-order-test-and-get-results
slug: thriva
tags:
- Company
- Healthcare
- Diagnostics
- Blood Testing
- At-Home Testing
- Digital Health
- Lab Testing
- Webhook
- United Kingdom
website: https://thriva.co
---
