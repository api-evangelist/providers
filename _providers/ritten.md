---
access_model:
  confidence: high
  label: Public spec, gated credentials
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://docs.ritten.io/
  - https://docs.ritten.io/swagger/openapi.yaml
  - https://www.ritten.io/
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: The calendar API from Ritten — 2 operation(s) for calendar.
  name: Ritten Calendar API
  slug: ritten-calendar-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Endpoints for accessing CRM cases (admissions pipeline).
  name: Ritten Cases API
  slug: ritten-cases-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: The contacts API from Ritten — 3 operation(s) for contacts.
  name: Ritten Contacts API
  slug: ritten-contacts-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Endpoints for creating clinical encounters (visits) and discovering the encounter types they are created from.
  name: Ritten Encounters API
  slug: ritten-encounters-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Endpoints for accessing clinic facilities (service locations).
  name: Ritten Facilities API
  slug: ritten-facilities-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Endpoints for accessing form definitions and form-related data.
  name: Ritten Forms API
  slug: ritten-forms-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Ritten provides insights and reporting endpoints for analytics and data export. These endpoints return various reports about admissions, discharges, census, billing, and CRM data. Most endpoints suppo
  name: Ritten Insights API
  slug: ritten-insights-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: The insurance API from Ritten — 2 operation(s) for insurance.
  name: Ritten Insurance API
  slug: ritten-insurance-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: OAuth 2.0 token endpoint for obtaining access tokens. This is the recommended way to authenticate with the Ritten External API.
  name: Ritten OAUTH API
  slug: ritten-oauth-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Endpoints for accessing CRM organizations and organization members. Requires CRM to be available for the target clinic (`X-Ritten-Tenant`). Integrations must be explicitly provisioned by Ritten for or
  name: Ritten Organizations API
  slug: ritten-organizations-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: The patients API from Ritten — 8 operation(s) for patients.
  name: Ritten Patients API
  slug: ritten-patients-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Endpoints for creating, accessing, and managing clinic programs.
  name: Ritten Programs API
  slug: ritten-programs-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: Endpoints for accessing clinic tasks. Tasks linked to a client are only returned when the integration is authorized to read that client.
  name: Ritten Tasks API
  slug: ritten-tasks-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: The users API from Ritten — 6 operation(s) for users.
  name: Ritten Users API
  slug: ritten-users-api
- baseURL: https://api.ritten.io/v1
  baseurl_source: declared
  description: 'Ritten provides webhooks for various events that occur in the system. Integrating partners can subscribe to these events to receive real-time updates. Webhooks sent from Ritten are POST requests with '
  name: Ritten Webhooks API
  slug: ritten-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Ritten Webhooks
  slug: ritten-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ritten-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://ritten.io
- group: company
  title: ''
  type: Blog
  url: https://www.ritten.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ritten.io/support
- group: start
  title: ''
  type: Login
  url: https://secure.ritten.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ritten.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ritten.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.ritten.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/ritten-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ritten-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ritten.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ritten.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ritten.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rittenlabs
- group: auth
  title: ''
  type: Authentication
  url: authentication/ritten-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ritten-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ritten-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ritten-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ritten-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ritten-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ritten-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ritten-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ritten-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ritten-external-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ritten-llms.txt
created: '2026-07-17'
description: Ritten is a cloud-based electronic medical record (EMR), CRM and revenue-cycle platform built specifically for behavioral health and substance-use treatment organizations - detox, residential, PHP/IOP, and outpatient providers. Its browser-based product covers clinical documentation (group and individual notes, AI-assisted charting), scheduling, revenue-cycle management (claims, billing, authorizations), a HIPAA-compliant patient portal, treatment planning, compliance tooling (audit trails, signature routing), and outcomes reporting. Ritten publishes a public REST contract for integrating partners - the Ritten External API - documented with an OpenAPI 3.1.0 definition covering 56 paths, 71 operations and 93 schemas across patients, contacts, CRM cases, programs, facilities, organizations, tasks, encounters, forms, insurance payers, users and a 17-operation insights and reporting family, plus six webhook events. Authentication is OAuth 2.0 client_credentials with a required X-Ritten-Tenant
  header selecting the clinic instance; credentials are provisioned by Ritten to partners rather than self-service. Ritten is built for HIPAA-regulated and 42 CFR Part 2 confidentiality requirements with role-based access controls and audit logs, and supports operational integrations for e-prescribing, labs, eligibility/billing clearinghouses, and telehealth. Backed by 8VC and Threshold Ventures; based in Philadelphia, PA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ritten.png
layout: provider
modified: '2026-08-15'
name: Ritten
nav: Providers
network: true
overview: 'Ritten publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Cases API, Contacts API, and 12 more. Tagged areas include Company, Behavioral Health, EMR, EHR, and Healthcare.


  The Ritten catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ritten''s developer surface includes engineering blog, support, documentation, API reference, authentication, sandbox, and 20 more developer resources.'
plans:
- name: Ritten Plans Pricing
  plan_count: 0
  slug: ritten-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Ritten Rate Limits
  slug: ritten-rate-limits
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 56.8
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 50.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
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
    score: 37.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ritten/refs/heads/main/screenshots/ritten-2026-08-17T081615.png
security:
- kind: authentication
  name: Ritten Authentication
  slug: ritten-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Ritten Domain Security
  slug: ritten-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ritten
tags:
- Company
- Behavioral Health
- EMR
- EHR
- Healthcare
- Practice Management
- HIPAA
- Revenue Cycle Management
- Clinical Documentation
- Telehealth
- OpenAPI
- Webhook
- Behavioral Health API
- Substance Use Treatment
- 42 CFR Part 2
- Electronic Health Records
website: https://ritten.io
---
