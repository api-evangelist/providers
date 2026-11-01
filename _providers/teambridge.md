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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://open-api.teambridge.com
  baseurl_source: declared
  description: '**Powerful generic endpoints** for reading and writing any collection type. Works with all collections using field UUIDs. Query `/fields` first to discover the schema, then use these endpoints for fle'
  name: Teambridge Collections (Unified API) API
  slug: teambridge-collections-unified-api-api
- baseURL: https://open-api.teambridge.com
  baseurl_source: declared
  description: Endpoints for uploading and managing documents.
  name: Teambridge Documents API
  slug: teambridge-documents-api
- baseURL: https://open-api.teambridge.com
  baseurl_source: declared
  description: Endpoints for managing external system mappings. Mappings link Teambridge records to entities in external systems (like Bullhorn, ADP, etc.) by storing the external provider code, external ID, and obj
  name: Teambridge Mappings API
  slug: teambridge-mappings-api
- baseURL: https://open-api.teambridge.com
  baseurl_source: declared
  description: Utility endpoints for timezone information and other general-purpose data.
  name: Teambridge Utilities API
  slug: teambridge-utilities-api
- baseURL: https://open-api.teambridge.com
  baseurl_source: declared
  description: The Teambridge External API API from Teambridge — 0 operation(s) for teambridge external api.
  name: Teambridge External API
  slug: teambridge-teambridge-external-api-api
artifact_total: 17
asyncapis:
- description: ''
  name: Teambridge Webhooks
  slug: teambridge-webhooks
collections:
- collection_type: open
  name: Teambridge External Collections (Unified API) Collections (Unified API) Collections (Unified API) API
  slug: open-teambridge-collections-unified-api-api
- collection_type: open
  name: Teambridge External Collections (Unified API) Collections (Unified API) Documents API
  slug: open-teambridge-documents-api
- collection_type: open
  name: Teambridge External Collections (Unified API) Collections (Unified API) Mappings API
  slug: open-teambridge-mappings-api
- collection_type: open
  name: Teambridge External Collections (Unified API) Collections (Unified API) Utilities API
  slug: open-teambridge-utilities-api
common:
- group: company
  title: ''
  type: Website
  url: https://teambridge.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.teambridge.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teambridge.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.teambridge.com
- group: auth
  href: https://artifacts.apis.io/teambridge/authentication/teambridge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teambridge-authentication.yml
- group: auth
  href: https://artifacts.apis.io/teambridge/scopes/teambridge-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/teambridge-scopes.yml
- group: design
  href: https://artifacts.apis.io/teambridge/conventions/teambridge-conventions.yml
  title: ''
  type: Conventions
  url: conventions/teambridge-conventions.yml
- group: design
  href: https://artifacts.apis.io/teambridge/errors/teambridge-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/teambridge-problem-types.yml
- group: design
  href: https://artifacts.apis.io/teambridge/asyncapi/teambridge-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/teambridge-webhooks.yml
- group: design
  href: https://artifacts.apis.io/teambridge/lifecycle/teambridge-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/teambridge-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/teambridge/conformance/teambridge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teambridge-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.teambridge.com/
- group: design
  href: https://artifacts.apis.io/teambridge/data-model/teambridge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/teambridge-data-model.yml
- group: other
  href: https://artifacts.apis.io/teambridge/overlays/teambridge-external-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/teambridge-external-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/teambridge/mcp/teambridge-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/teambridge-mcp.yml
- group: agent
  href: https://artifacts.apis.io/teambridge/llms/teambridge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teambridge-llms.txt
- group: agent
  href: https://artifacts.apis.io/teambridge/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/teambridge/security/teambridge-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/teambridge-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/teambridge/security/teambridge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teambridge-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://teambridge.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://teambridge.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.teambridge.com
- group: start
  title: ''
  type: SignUp
  url: https://teambridge.com/book-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://teambridge.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://teambridge.com/privacy-policy
created: '2026-07-17'
description: Teambridge is an AI-native workforce-management platform for frontline and hourly teams, unifying scheduling, time tracking, instant pay, team communication, onboarding, compliance, and payroll behind autonomous AI agents. For integrators it publishes the Teambridge External API, a unified Collections API (OpenAPI 3.1.0) that reads and writes shifts, users, placements, locations, and custom collections, authenticated with OAuth 2.0 client credentials and complemented by HMAC-signed outbound webhooks for real-time change notification. Teambridge is backed by General Catalyst and Mayfield and reports SOC 2 Type II, ISO 27001, HIPAA, and GDPR compliance.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teambridge.png
layout: provider
modified: '2026-09-16'
name: Teambridge
nav: Providers
network: true
overview: 'Teambridge publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collections (Unified API) API, Documents API, Mappings API, and 2 more. Tagged areas include Company, Workforce Management, Scheduling, Time Tracking, and Payroll.


  The Teambridge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teambridge''s developer surface includes documentation, API reference, authentication, pricing, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 12
scopes:
- name: Teambridge Scopes
  scope_count: 1
  slug: teambridge-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 58.1
    developer_ergonomics: 42.3
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 48.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/teambridge/teambridge-2026-08-17T082257.png
security:
- kind: authentication
  name: Teambridge Authentication
  slug: teambridge-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Teambridge Domain Security
  slug: teambridge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Teambridge Trust Center
  slug: teambridge-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 3
skills:
- name: Consume and verify Teambridge webhooks
  slug: teambridge-consume-webhooks
- name: Read Teambridge collection records
  slug: teambridge-read-collection-records
- name: Create records and sync external mappings
  slug: teambridge-sync-external-mappings
slug: teambridge
tags:
- Company
- Workforce Management
- Scheduling
- Time Tracking
- Payroll
- Human Resources
- Frontline
- Webhook
website: https://teambridge.com
---
