---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Mparticle Agentic Access
  operation_count: 16
  slug: mparticle-agentic-access
  summary_line: 16 operations · 13 acting
api_count: 3
apis:
- description: REST API for retrieving unified user profiles, identities, attributes, and audience memberships at scale to personalize downstream applications.
  name: mParticle Profile API
  slug: profile-api
- description: Management REST API used to programmatically configure mParticle inputs, outputs, filters, audiences, data plans, and workspace settings as part of a fully versioned CDP-as-code workflow. Authenticate
  name: mParticle Platform API
  slug: platform-api
- description: REST API for building reverse-ETL pipelines that pull data out of a customer data warehouse (connections, data models, field transformations and pipelines) and load it into mParticle profiles and audi
  name: mParticle Warehouse Sync API
  slug: warehouse-sync-api
- baseURL: https://s2s.mparticle.com/v2
  baseurl_source: declared
  description: Endpoints for managing Data Plans
  name: mParticle Data Plan API
  slug: mparticle-data-plan-api
- baseURL: https://s2s.mparticle.com/v2
  baseurl_source: declared
  description: Endpoints for versioning Data Plans
  name: mParticle Data Plan Version API
  slug: mparticle-data-plan-version-api
- baseURL: https://s2s.mparticle.com/v2
  baseurl_source: declared
  description: Send your data to the mParticle platform.
  name: mParticle Events API
  slug: mparticle-events-api
- baseURL: https://s2s.mparticle.com/v2
  baseurl_source: declared
  description: The Identify API from mParticle — 1 operation(s) for identify.
  name: mParticle Identify API
  slug: mparticle-identify-api
- baseURL: https://s2s.mparticle.com/v2
  baseurl_source: declared
  description: The Login API from mParticle — 1 operation(s) for login.
  name: mParticle Login API
  slug: mparticle-login-api
- baseURL: https://s2s.mparticle.com/v2
  baseurl_source: declared
  description: The Logout API from mParticle — 1 operation(s) for logout.
  name: mParticle Logout API
  slug: mparticle-logout-api
- baseURL: https://s2s.mparticle.com/v2
  baseurl_source: declared
  description: The Modify API from mParticle — 1 operation(s) for modify.
  name: mParticle Modify API
  slug: mparticle-modify-api
artifact_total: 25
asyncapis:
- description: ''
  name: Mparticle Webhooks
  slug: mparticle-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: mParticle Events Bulkevents API
  slug: open-mparticle-bulkevents-api
- collection_type: open
  name: mParticle Bulkevents Events API
  slug: open-mparticle-events-api
- collection_type: open
  name: mParticle Events API
  slug: open-mparticle
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/rokt/
- group: other
  title: ''
  type: Overlay
  url: overlays/mparticle-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mparticle-identity-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mparticle-dataplanning-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mparticle-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mparticle-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mparticle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.rokt.com/vulnerability-disclosure/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mparticle.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mparticle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mparticle-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mparticle-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mparticle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mparticle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mparticle-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mparticle-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mparticle-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mparticle-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mparticle-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mparticle-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/mparticle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mparticle-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mparticle-cli.yml
- group: design
  title: ''
  type: Components
  url: components/mparticle-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mparticle-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mparticle-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mparticle-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mparticle-security.txt
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mparticle-eventsapi-schema.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mparticle-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mparticle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mparticle-inc-
- group: company
  title: ''
  type: Website
  url: https://www.mparticle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mparticle.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mparticle.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mparticle.com/developers/apis/http/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mparticle.com/guides/getting-started/
- group: build
  title: ''
  type: Postman
  url: https://docs.mparticle.com/downloads/dataplanning.postman_collection.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mparticle.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.mparticle.com/get-a-demo/
- group: start
  title: ''
  type: Login
  url: https://app.mparticle.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mparticle.com/legal/platform-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mparticle.com/privacypolicy/
- group: company
  title: ''
  type: Blog
  url: https://www.mparticle.com/blog/
created: '2026-05-11'
description: mParticle is a customer data platform (CDP) that helps brands collect, unify, and activate customer data across mobile, web, OTT, and server sources, then forward it in real time to hundreds of analytics, marketing, and warehouse destinations. The mParticle developer platform exposes server Events, IDSync, Profile, Warehouse Sync, Calculated Attributes, Data Planning and Platform APIs that let teams ingest events, resolve identity, manage configurations, and orchestrate audiences using HTTP Basic, an HMAC request digest, and OAuth 2.0 client-credentials bearer tokens. mParticle was acquired by Rokt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mparticle.png
json_schemas:
- name: Mparticle Eventsapi Bulk
  property_count: 0
  slug: mparticle-eventsapi-bulk
- name: Mparticle Eventsapi Sample
  property_count: 0
  slug: mparticle-eventsapi-sample
- name: Mparticle Eventsapi
  property_count: 25
  slug: mparticle-eventsapi
layout: provider
modified: '2026-08-13'
name: mParticle
nav: Providers
network: true
overview: 'mParticle publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Data Plan API, Data Plan Version API, Events API, and 4 more. Tagged areas include Customer Data Platform, CDP, Analytics, Identity Resolution, and Audience.


  The mParticle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  mParticle''s developer surface includes authentication, changelog, sandbox, CLI, documentation, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Mparticle Plans Pricing
  plan_count: 0
  slug: mparticle-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 14
  name: Mparticle Rate Limits
  slug: mparticle-rate-limits
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 58.0
    catalog_earned_first_party: 12.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 62.2
    developer_ergonomics: 42.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mparticle/refs/heads/main/screenshots/mparticle-2026-06-20T185839.png
security:
- kind: authentication
  name: Mparticle Authentication
  slug: mparticle-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Mparticle Domain Security
  slug: mparticle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mparticle Vulnerability Disclosure
  slug: mparticle-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mparticle Trust Center
  slug: mparticle-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: mparticle
tags:
- Customer Data Platform
- CDP
- Analytics
- Identity Resolution
- Audience
- Data Pipeline
- Marketing Data
- Event Streaming
- Data Governance
website: https://www.mparticle.com/
---
