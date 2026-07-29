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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Thriva Agentic Access
  operation_count: 29
  slug: thriva-agentic-access
  summary_line: 29 operations · 11 acting
api_count: 10
apis:
- description: The Appointments API API from Thriva — 2 operation(s) for appointments api.
  name: Thriva Appointments API API
  slug: thriva-appointments-api-api
- description: The Auth API API from Thriva — 1 operation(s) for auth api.
  name: Thriva Auth API API
  slug: thriva-auth-api-api
- description: The Biomarkers API API from Thriva — 1 operation(s) for biomarkers api.
  name: Thriva Biomarkers API API
  slug: thriva-biomarkers-api-api
- description: The Bulk Orders API API from Thriva — 4 operation(s) for bulk orders api.
  name: Thriva Bulk Orders API API
  slug: thriva-bulk-orders-api-api
- description: The Escalations API API from Thriva — 1 operation(s) for escalations api.
  name: Thriva Escalations API API
  slug: thriva-escalations-api-api
- description: The Orders API API from Thriva — 7 operation(s) for orders api.
  name: Thriva Orders API API
  slug: thriva-orders-api-api
- description: The Result attachments API API from Thriva — 2 operation(s) for result attachments api.
  name: Thriva Result attachments API API
  slug: thriva-result-attachments-api-api
- description: The Results API API from Thriva — 2 operation(s) for results api.
  name: Thriva Results API API
  slug: thriva-results-api-api
- description: The Tracking API API from Thriva — 1 operation(s) for tracking api.
  name: Thriva Tracking API API
  slug: thriva-tracking-api-api
- description: The Users API API from Thriva — 3 operation(s) for users api.
  name: Thriva Users API API
  slug: thriva-users-api-api
artifact_total: 16
asyncapis:
- description: ''
  name: Thriva Webhooks
  slug: thriva-webhooks
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: thriva-mcp.yml
  slug: thriva-mcpyml
modified: '2026-07-21'
name: Thriva
nav: Providers
network: true
overview: 'Thriva publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Appointments API API, Auth API API, Biomarkers API API, and 7 more. Tagged areas include Company, Healthcare, Diagnostics, Blood Testing, and At-Home Testing.


  The Thriva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Thriva''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 20 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 45.9
  delta: -3.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.0
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 49.0
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Webhooks
- United Kingdom
website: https://thriva.co
---
