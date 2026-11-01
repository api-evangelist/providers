---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
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
    agentic_access: true
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Photon Agentic Access
  operation_count: 0
  slug: photon-agentic-access
  summary_line: 0 operations
api_count: 1
apis:
- description: Photon's native GraphQL Clinical API for managing patients, prescriptions, orders, pharmacies, the treatment/medication catalog, drug-drug and drug-allergy interaction screening, webhooks, and organiz
  name: Photon Clinical API
  slug: photon-clinical-api
- description: 'Photon''s GraphQL Patient Benefits API for managing patient benefits and enabling pharmacy benefit checks (coverage options, copay, and formulary) during the prescribing workflow. Served over the same '
  name: Photon Patient Benefits API
  slug: photon-patient-benefits-api
- baseURL: https://clinical-api.photon.health/graphql
  baseurl_source: declared
  description: Machine-readable discovery resources for agents and integrations.
  name: Photon Agent discovery API
  slug: photon-agent-discovery-api
- baseURL: https://clinical-api.photon.health/graphql
  baseurl_source: declared
  description: First-party endpoint for adding newsletter signups to Ghost Members.
  name: Photon Newsletter API
  slug: photon-newsletter-api
- baseURL: https://clinical-api.photon.health/graphql
  baseurl_source: declared
  description: First-party onboarding endpoints for prescriber, developer, clinic, enterprise, platform, and other paths.
  name: Photon Onboarding API
  slug: photon-onboarding-api
artifact_total: 19
asyncapis:
- description: ''
  name: Photon Order Events Webhooks
  slug: photon-order-events-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/photon/skills/photon-developer-sandbox-onboarding.md
  title: ''
  type: AgentSkill
  url: skills/photon-developer-sandbox-onboarding.md
- group: auth
  href: https://artifacts.apis.io/photon/security/photon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/photon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://photonhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.photon.health/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.photon.health/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.photon.health/reference/clinical-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.photon.health/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.photon.health/docs/authentication
- group: start
  title: ''
  type: SignUp
  url: https://photonhealth.com/onboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Photon-Health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/photonhealth
- group: operate
  title: ''
  type: StatusPage
  url: https://status.photon.health
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.photon.health
- group: company
  title: ''
  type: Blog
  url: https://photonhealth.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://photonhealth.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://photonhealth.com/terms
- group: auth
  href: https://artifacts.apis.io/photon/authentication/photon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/photon-authentication.yml
- group: auth
  href: https://artifacts.apis.io/photon/scopes/photon-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/photon-scopes.yml
- group: build
  href: https://artifacts.apis.io/photon/packages/photon-packages.yml
  title: ''
  type: Packages
  url: packages/photon-packages.yml
- group: build
  href: https://artifacts.apis.io/photon/packages/photon-packages.yml
  title: ''
  type: SDKs
  url: packages/photon-packages.yml
- group: agent
  href: https://artifacts.apis.io/photon/well-known/photon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/photon-well-known.yml
- group: agent
  href: https://artifacts.apis.io/photon/mcp/photon-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/photon-mcp.yml
- group: agent
  href: https://artifacts.apis.io/photon/llms/photon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/photon-llms.txt
- group: design
  href: https://artifacts.apis.io/photon/conformance/photon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/photon-conformance.yml
- group: design
  href: https://artifacts.apis.io/photon/errors/photon-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/photon-error-codes.yml
- group: design
  href: https://artifacts.apis.io/photon/lifecycle/photon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/photon-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/photon/sandbox/photon-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/photon-sandbox.yml
- group: design
  href: https://artifacts.apis.io/photon/conventions/photon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/photon-conventions.yml
- group: design
  href: https://artifacts.apis.io/photon/components/photon-components.yml
  title: ''
  type: Components
  url: components/photon-components.yml
- group: design
  href: https://artifacts.apis.io/photon/data-model/photon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/photon-data-model.yml
- group: design
  href: https://artifacts.apis.io/photon/asyncapi/photon-order-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/photon-order-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/photon/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/photon/openapi/_original/photon-website-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/photon-website-api-openapi.json
- group: other
  href: https://artifacts.apis.io/photon/overlays/photon-website-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/photon-website-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/photon/well-known/photon-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/photon-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/photon/agentic-access/photon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/photon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/photon/security/photon-trust-center.yml
  title: ''
  type: Compliance
  url: security/photon-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/photon/plans/photon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/photon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/photon/rate-limits/photon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/photon-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@photon.health
- group: start
  title: ''
  type: Login
  url: https://app.photon.health/login
- group: operate
  title: ''
  type: FAQ
  url: https://photonhealth.com/faq
- group: agent
  href: https://artifacts.apis.io/photon/llms/photon-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/photon-docs-llms.txt
created: '2026-07-24'
description: Photon Health is a United States prescription-infrastructure and e-prescribing (eRx) platform that lets digital-health companies embed prescribing, pharmacy selection, prescription routing, and fulfillment tracking into their clinical applications. Rather than an HL7 FHIR interface, Photon exposes a native GraphQL Clinical API - a single POST /graphql endpoint covering patients, prescriptions, orders, pharmacies, the medication/treatment catalog, drug-drug and drug-allergy screening, webhooks, and organization/user administration - plus a Patient Benefits API for pharmacy benefit checks and coverage. It also ships Photon Elements, prebuilt WebComponent UI for prescribing. The API is secured with OAuth2 client-credentials (Auth0) using machine-to-machine and user access tokens and prescription/order scopes; a sandbox runs on neutron.health. Photon serves prescribers and pharmacy-innovation partners including Amazon Pharmacy, Sesame, WeightWatchers, and Found.
finops:
- has_sources: true
  method: derived
  name: Photon Finops
  primary_unit: orders
  service_category: ''
  slug: photon-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-09-16'
name: Photon
nav: Providers
network: true
overview: 'Photon publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent discovery API, Newsletter API, Onboarding API, and 2 more. Tagged areas include Healthcare, United States, e-Prescribing, Pharmacy, and Prescription Routing.


  The Photon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Photon''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, engineering blog, sandbox, and 36 more developer resources.'
plans:
- name: Photon Plans Pricing
  plan_count: 5
  slug: photon-plans-pricing
- name: Photon Price Estimates
  plan_count: 0
  slug: photon-price-estimates
random_paper: 16
rate_limits:
- limit_count: 0
  name: Photon Rate Limits
  slug: photon-rate-limits
scopes:
- name: Photon Scopes
  scope_count: 6
  slug: photon-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 65.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 57.1
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
    score: 47.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/photon/photon-2026-08-17T081212.png
security:
- kind: authentication
  name: Photon Authentication
  slug: photon-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Photon Domain Security
  slug: photon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Photon Trust Center
  slug: photon-trust-center
  summary_line: SOC 2, HIPAA
skill_count: 4
skills:
- name: Run a patient benefit check
  slug: photon-benefit-check
- name: Onboard to the Photon developer sandbox
  slug: photon-developer-sandbox-onboarding
- name: Subscribe to Photon order events
  slug: photon-order-events-webhooks
- name: Sync a patient into Photon
  slug: photon-sync-patient
slug: photon
tags:
- Healthcare
- United States
- e-Prescribing
- Pharmacy
- Prescription Routing
- GraphQL
- Clinical API
- Digital Health
- Benefit Check
- Authentication
website: https://photonhealth.com/
---
