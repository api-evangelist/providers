---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-09-03'
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
  name: Thriva Appointments API API
  slug: thriva-appointments-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Auth API API from Thriva — 1 operation(s) for auth api.
  name: Thriva Auth API API
  slug: thriva-auth-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Biomarkers API API from Thriva — 1 operation(s) for biomarkers api.
  name: Thriva Biomarkers API API
  slug: thriva-biomarkers-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Bulk Orders API API from Thriva — 4 operation(s) for bulk orders api.
  name: Thriva Bulk Orders API API
  slug: thriva-bulk-orders-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Escalations API API from Thriva — 1 operation(s) for escalations api.
  name: Thriva Escalations API API
  slug: thriva-escalations-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Orders API API from Thriva — 7 operation(s) for orders api.
  name: Thriva Orders API API
  slug: thriva-orders-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Result attachments API API from Thriva — 2 operation(s) for result attachments api.
  name: Thriva Result attachments API API
  slug: thriva-result-attachments-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Results API API from Thriva — 2 operation(s) for results api.
  name: Thriva Results API API
  slug: thriva-results-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Tracking API API from Thriva — 1 operation(s) for tracking api.
  name: Thriva Tracking API API
  slug: thriva-tracking-api-api
- baseURL: https://api.thriva.io
  baseurl_source: declared
  description: The Users API API from Thriva — 3 operation(s) for users api.
  name: Thriva Users API API
  slug: thriva-users-api-api
artifact_total: 26
asyncapis:
- description: ''
  name: Thriva Webhooks
  slug: thriva-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: CapabilityMap
  url: capabilities/thriva-capability-edges.yml
- group: other
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
  title: ''
  type: Authentication
  url: authentication/thriva-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/thriva-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/thriva-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thriva-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thriva-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thriva-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thriva-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/thriva-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thriva-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thriva-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thriva-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/thriva-packages.yml
- group: design
  title: ''
  type: Components
  url: components/thriva-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thriva-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thriva-agentic-access.yml
- group: auth
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
modified: '2026-07-21'
name: Thriva
nav: Providers
network: true
overview: 'Thriva publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Appointments API API, Auth API API, Biomarkers API API, and 7 more. Tagged areas include Company, Healthcare, Diagnostics, Blood Testing, and At-Home Testing.


  The Thriva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Thriva''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 22 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 56.9
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 42.8
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
    score: 37.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thriva/refs/heads/main/screenshots/thriva-2026-08-17T082348.png
security:
- kind: authentication
  name: Thriva Authentication
  slug: thriva-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Thriva Domain Security
  slug: thriva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
