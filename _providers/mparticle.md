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
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-10-31'
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
artifact_total: 28
asyncapis:
- description: ''
  name: Mparticle Webhooks
  slug: mparticle-webhooks
collections:
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
  href: https://artifacts.apis.io/mparticle/capabilities/mparticle-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mparticle-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/rokt/
- group: other
  href: https://artifacts.apis.io/mparticle/overlays/mparticle-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mparticle-events-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mparticle/overlays/mparticle-identity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mparticle-identity-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mparticle/overlays/mparticle-dataplanning-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mparticle-dataplanning-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mparticle/agentic-access/mparticle-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mparticle-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mparticle/security/mparticle-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mparticle-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mparticle/security/mparticle-vulnerability-disclosure.yml
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
  href: https://artifacts.apis.io/mparticle/security/mparticle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mparticle-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mparticle/authentication/mparticle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mparticle-authentication.yml
- group: design
  href: https://artifacts.apis.io/mparticle/conformance/mparticle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mparticle-conformance.yml
- group: design
  href: https://artifacts.apis.io/mparticle/conventions/mparticle-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mparticle-conventions.yml
- group: design
  href: https://artifacts.apis.io/mparticle/errors/mparticle-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mparticle-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mparticle/lifecycle/mparticle-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mparticle-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mparticle/changelog/mparticle-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mparticle-changelog.yml
- group: operate
  href: https://artifacts.apis.io/mparticle/rate-limits/mparticle-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mparticle-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mparticle/plans/mparticle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mparticle-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/mparticle/sandbox/mparticle-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mparticle-sandbox.yml
- group: design
  href: https://artifacts.apis.io/mparticle/data-model/mparticle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mparticle-data-model.yml
- group: build
  href: https://artifacts.apis.io/mparticle/packages/mparticle-packages.yml
  title: ''
  type: Packages
  url: packages/mparticle-packages.yml
- group: build
  href: https://artifacts.apis.io/mparticle/packages/mparticle-packages.yml
  title: ''
  type: SDKs
  url: packages/mparticle-packages.yml
- group: build
  href: https://artifacts.apis.io/mparticle/cli/mparticle-cli.yml
  title: ''
  type: CLI
  url: cli/mparticle-cli.yml
- group: design
  href: https://artifacts.apis.io/mparticle/components/mparticle-components.yml
  title: ''
  type: Components
  url: components/mparticle-components.yml
- group: design
  href: https://artifacts.apis.io/mparticle/asyncapi/mparticle-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mparticle-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/mparticle/mcp/mparticle-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mparticle-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mparticle/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/mparticle/well-known/mparticle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mparticle-well-known.yml
- group: auth
  href: https://artifacts.apis.io/mparticle/well-known/mparticle-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mparticle-security.txt
- group: docs
  href: https://artifacts.apis.io/mparticle/json-schema/mparticle-eventsapi-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/mparticle-eventsapi-schema.json
- group: agent
  href: https://artifacts.apis.io/mparticle/llms/mparticle-llms.txt
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
finops:
- has_sources: true
  method: derived
  name: Mparticle Finops
  primary_unit: ''
  service_category: ''
  slug: mparticle-finops
  template: true
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
overview: 'mParticle publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Plan API, Data Plan Version API, Events API, and 7 more. Tagged areas include Customer Data Platform, CDP, Analytics, Identity Resolution, and Audiences.


  The mParticle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  mParticle''s developer surface includes authentication, changelog, sandbox, CLI, documentation, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: Mparticle Plans Pricing
  plan_count: 0
  slug: mparticle-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 14
  name: Mparticle Rate Limits
  slug: mparticle-rate-limits
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.4
    catalog_earned_first_party: 12.0
    catalog_gap: 57.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 60.2
    developer_ergonomics: 80.4
    discoverability: 71.4
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 64.8
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mparticle/mparticle-2026-06-20T185839.png
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
skill_count: 3
skills:
- name: Govern mParticle data plans
  slug: mparticle-govern-data-plans
- name: Resolve a user identity with mParticle IDSync
  slug: mparticle-resolve-identity
- name: Send events to mParticle
  slug: mparticle-send-events
slug: mparticle
tags:
- Customer Data Platform
- CDP
- Analytics
- Identity Resolution
- Audiences
- Data Pipeline
- Marketing Data
- Event Streaming
- Data Governance
website: https://www.mparticle.com/
---
