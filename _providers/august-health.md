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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: RESTful v1 API for the August Health EHR platform covering organizations, facilities, rooms, census, residents, contacts, assessments, incidents & notes, medications (orders and administrations), vita
  name: August Health API
  slug: august-health-api
artifact_total: 7
asyncapis:
- description: Event surface for the August Health EHR platform. Consumers subscribe via the webhooks application portal and receive HTTP POST callbacks. Each delivery carries the envelope { eventType, eventId, even
  name: August Health Webhooks
  slug: august-health-events-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://augusthealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.augusthealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.augusthealth.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.augusthealth.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.augusthealth.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.augusthealth.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@augusthealth.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/augusthealth
- group: start
  title: ''
  type: Login
  url: https://app.augusthealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.augusthealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.augusthealth.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.augusthealth.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.augusthealth.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.augusthealth.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/august-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/august-health-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/august-health-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/august-health-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/august-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/august-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/august-health-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/august-health-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/august-health-events-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/august-health-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/august-health-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/august-health-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/august-health-domain-security.yml
created: '2026-07-17'
description: August Health is an AI-enabled electronic health record (EHR) platform purpose-built for senior living and eldercare communities, spanning Move-Ins, EHR, eMAR, Care Track, Billing & Payments, and Insights. It publishes a RESTful v1 API and a developer portal (developer.augusthealth.com) that lets integration partners read and write resident, clinical, medication, billing, and census data, plus a webhook event surface for resident-lifecycle and billing events. Auth is bearer-JWT with named permissions; the platform is SOC 2 (AICPA) and HIPAA certified. August Health is backed by General Catalyst and Matrix Partners.
image: https://files.readme.io/1aa624066285820f9957c79e0fe44d8330186bc54681b372c14ed43fc2b25b60-small-AugustHealth_-_PrimaryLogoMark_-_RGB_-_FullColorAlt.png
layout: provider
mcp_servers:
- description: ''
  name: August Health MCP Server
  slug: august-health-mcp-server
modified: '2026-07-18'
name: August Health
nav: Providers
network: true
overview: 'August Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, EHR, Senior Living, and Elder Care.


  The August Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  August Health''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 22 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: August Health Rate Limits
  slug: august-health-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 41.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/august-health/refs/heads/main/screenshots/august-health-2026-07-25T201720.png
security:
- kind: authentication
  name: August Health Authentication
  slug: august-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: August Health Domain Security
  slug: august-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: August Health Trust Center
  slug: august-health-trust-center
  summary_line: SOC 2, HIPAA, AICPA
slug: august-health
tags:
- Company
- Healthcare
- EHR
- Senior Living
- Elder Care
- Electronic Health Records
- eMAR
- Billing
- Webhook
website: https://augusthealth.com
---
