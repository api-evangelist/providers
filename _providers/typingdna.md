---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-10-31'
api_count: 3
apis:
- baseURL: https://api.typingdna.com
  baseurl_source: declared
  description: Advanced routes for customisation
  name: TypingDNA Advanced API
  slug: typingdna-advanced-api
- baseURL: https://api.typingdna.com
  baseurl_source: declared
  description: Optional routes
  name: TypingDNA Optional API
  slug: typingdna-optional-api
- baseURL: https://api.typingdna.com
  baseurl_source: declared
  description: Main routes
  name: TypingDNA Standard API
  slug: typingdna-standard-api
artifact_total: 15
collections:
- collection_type: open
  name: TypingDNA - Authentication API Documentation advanced API
  slug: open-typingdna-advanced-api
- collection_type: open
  name: TypingDNA - Authentication API Documentation advanced optional API
  slug: open-typingdna-optional-api
- collection_type: open
  name: TypingDNA - Authentication API Documentation advanced standard API
  slug: open-typingdna-standard-api
common:
- group: commercial
  href: https://artifacts.apis.io/typingdna/plans/typingdna-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/typingdna-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/typingdna/capabilities/typingdna-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/typingdna-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/typingdna/overlays/typingdna-authentication-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/typingdna-authentication-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/typingdna/security/typingdna-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/typingdna-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/typingdna/security/typingdna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/typingdna-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/typingdna/authentication/typingdna-authentication.yml
  title: ''
  type: Authentication
  url: authentication/typingdna-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://typingdna.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.typingdna.com/clients/login
- group: docs
  title: ''
  type: Documentation
  url: https://api.typingdna.com/docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.typingdna.com/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.typingdna.com/docs/tutorials.html
- group: operate
  title: ''
  type: Support
  url: https://www.typingdna.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.typingdna.com
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.typingdna.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TypingDNA
- group: commercial
  title: ''
  type: Pricing
  url: https://www.typingdna.com/pricing/auth-api
- group: start
  title: ''
  type: SignUp
  url: https://www.typingdna.com/clients/signup
- group: start
  title: ''
  type: Login
  url: https://www.typingdna.com/clients/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.typingdna.com/legal/authentication-API-standard-service-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.typingdna.com/legal/website-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.typingdna.com
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/collections/48c757074b638c64b350
- group: auth
  title: ''
  type: Compliance
  url: https://www.typingdna.com/pricing/auth-api
- group: build
  href: https://artifacts.apis.io/typingdna/packages/typingdna-packages.yml
  title: ''
  type: Packages
  url: packages/typingdna-packages.yml
- group: build
  href: https://artifacts.apis.io/typingdna/packages/typingdna-packages.yml
  title: ''
  type: SDKs
  url: packages/typingdna-packages.yml
- group: agent
  href: https://artifacts.apis.io/typingdna/well-known/typingdna-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/typingdna-well-known.yml
- group: other
  href: https://artifacts.apis.io/typingdna/well-known/typingdna-verify-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/typingdna-verify-openid-configuration.json
- group: agent
  href: https://artifacts.apis.io/typingdna/mcp/typingdna-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/typingdna-mcp.yml
- group: agent
  href: https://artifacts.apis.io/typingdna/llms/typingdna-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/typingdna-llms.txt
- group: design
  href: https://artifacts.apis.io/typingdna/conformance/typingdna-conformance.yml
  title: ''
  type: Conformance
  url: conformance/typingdna-conformance.yml
- group: design
  href: https://artifacts.apis.io/typingdna/errors/typingdna-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/typingdna-problem-types.yml
- group: design
  href: https://artifacts.apis.io/typingdna/lifecycle/typingdna-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/typingdna-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/typingdna/scopes/typingdna-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/typingdna-scopes.yml
- group: start
  href: https://artifacts.apis.io/typingdna/sandbox/typingdna-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/typingdna-sandbox.yml
- group: design
  href: https://artifacts.apis.io/typingdna/conventions/typingdna-conventions.yml
  title: ''
  type: Conventions
  url: conventions/typingdna-conventions.yml
- group: design
  href: https://artifacts.apis.io/typingdna/components/typingdna-components.yml
  title: ''
  type: Components
  url: components/typingdna-components.yml
- group: design
  href: https://artifacts.apis.io/typingdna/data-model/typingdna-data-model.yml
  title: ''
  type: DataModel
  url: data-model/typingdna-data-model.yml
- group: agent
  href: https://artifacts.apis.io/typingdna/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TypingDNA provides AI-based typing biometrics authentication, recognizing people by how they type on desktop and mobile keyboards. Its RESTful Authentication API enrolls and verifies typing patterns for fraud prevention, account-sharing detection and passwordless second factors, while Verify 2FA replaces SMS/email one-time codes with typing verification — standalone or as an OIDC authentication method for Okta, Ping Identity and Microsoft Entra ID. TypingDNA is certified for ISO 27001, ISO 27017 and ISO 27018.
finops:
- has_sources: true
  method: derived
  name: Typingdna Finops
  primary_unit: user
  service_category: ''
  slug: typingdna-finops
  template: false
image: https://www.typingdna.com/assets/images/default-meta-image.jpg
layout: provider
modified: '2026-07-21'
name: TypingDNA
nav: Providers
network: true
overview: 'TypingDNA publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Advanced API, Optional API, and Standard API. Tagged areas include Company, Authentication, Biometrics, Typing Biometrics, and Two-Factor Authentication.


  TypingDNA''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Typingdna Plans Pricing
  plan_count: 3
  slug: typingdna-plans-pricing
- name: Typingdna Price Estimates
  plan_count: 0
  slug: typingdna-price-estimates
random_paper: 14
scopes:
- name: Typingdna Scopes
  scope_count: 3
  slug: typingdna-scopes
  summary_line: 3 scopes · authorizationCode/refreshToken/deviceCode/jwtBearer
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 52.0
    developer_ergonomics: 78.0
    discoverability: 71.4
    operational_transparency: 21.1
  previous_composite: 55.7
  provenance:
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 37.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/typingdna/typingdna-2026-08-17T082510.png
security:
- kind: authentication
  name: Typingdna Authentication
  slug: typingdna-authentication
  summary_line: apiKey/http/openIdConnect · 4 schemes
- kind: domain-security
  name: Typingdna Domain Security
  slug: typingdna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Typingdna Trust Center
  slug: typingdna-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018
skill_count: 2
skills:
- name: Enroll a user and verify their typing pattern
  slug: typingdna-enroll-and-verify
- name: Add Verify 2FA typing verification to a login
  slug: typingdna-verify-2fa-flow
slug: typingdna
tags:
- Company
- Authentication
- Biometrics
- Typing Biometrics
- Two-Factor Authentication
- Identity
- Security
- Fraud Prevention
website: https://typingdna.com/
---
