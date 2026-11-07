---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Gridline Agentic Access
  operation_count: 32
  slug: gridline-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 6
apis:
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Deepfake API from Gridlines — 6 operation(s) for deepfake.
  name: Gridlines Deepfake API
  slug: gridline-deepfake-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Digilocker API from Gridlines — 6 operation(s) for digilocker.
  name: Gridlines Digilocker API
  slug: gridline-digilocker-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The E-Sign API from Gridlines — 4 operation(s) for e-sign.
  name: Gridlines E Sign API
  slug: gridline-e-sign-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Face Api API from Gridlines — 1 operation(s) for face api.
  name: Gridlines Face API
  slug: gridline-face-api-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Individual API from Gridlines — 1 operation(s) for individual.
  name: Gridlines Individual API
  slug: gridline-individual-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Liveness API from Gridlines — 1 operation(s) for liveness.
  name: Gridlines Liveness API
  slug: gridline-liveness-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Pull Education Documents API from Gridlines — 2 operation(s) for pull education documents.
  name: Gridlines Pull Education Documents API
  slug: gridline-pull-education-documents-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The UIDAI OVSE API from Gridlines — 2 operation(s) for uidai ovse.
  name: Gridlines UIDAI OVSE API
  slug: gridline-uidai-ovse-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Utility API from Gridlines — 6 operation(s) for utility.
  name: Gridlines Utility API
  slug: gridline-utility-api
- baseURL: https://api.gridlines.io
  baseurl_source: declared
  description: The Workflow Mgmt API from Gridlines — 3 operation(s) for workflow mgmt.
  name: Gridlines Workflow Mgmt API
  slug: gridline-workflow-mgmt-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/gridline/agentic-access/gridline-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gridline-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/gridline/rate-limits/gridline-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gridline-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/gridline/rules/gridline-rules.yml
  title: ''
  type: Spectral
  url: rules/gridline-rules.yml
- group: design
  href: https://artifacts.apis.io/gridline/json-ld/gridline-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gridline-context.jsonld
- group: design
  href: https://artifacts.apis.io/gridline/vocabulary/gridline-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gridline-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gridline/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gridline/data-model/gridline-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gridline-data-model.yml
- group: design
  href: https://artifacts.apis.io/gridline/conventions/gridline-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gridline-conventions.yml
- group: design
  href: https://artifacts.apis.io/gridline/conventions/gridline-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gridline-conventions.yml
- group: start
  href: https://artifacts.apis.io/gridline/sandbox/gridline-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gridline-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/gridline/lifecycle/gridline-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gridline-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gridline/lifecycle/gridline-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gridline-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gridline/conformance/gridline-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gridline-conformance.yml
- group: other
  href: https://artifacts.apis.io/gridline/overlays/gridline-aadhaar-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gridline-aadhaar-overlay.yaml
- group: build
  href: https://artifacts.apis.io/gridline/integrations/gridline-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/gridline-integration-edges.yml
- group: design
  href: https://artifacts.apis.io/gridline/components/gridline-components.yml
  title: ''
  type: Components
  url: components/gridline-components.yml
- group: auth
  href: https://artifacts.apis.io/gridline/authentication/gridline-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gridline-authentication.yml
- group: design
  href: https://artifacts.apis.io/gridline/errors/gridline-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gridline-problem-types.yml
- group: other
  href: https://artifacts.apis.io/gridline/hosts/gridline-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gridline-hosts.yml
- group: other
  href: https://artifacts.apis.io/gridline/vendors/gridline-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gridline-vendors.yml
- group: build
  href: https://artifacts.apis.io/gridline/packages/gridline-packages.yml
  title: ''
  type: SDKs
  url: packages/gridline-packages.yml
- group: build
  href: https://artifacts.apis.io/gridline/packages/gridline-packages.yml
  title: ''
  type: Packages
  url: packages/gridline-packages.yml
- group: auth
  href: https://artifacts.apis.io/gridline/security/gridline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gridline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gridlines.io/
- group: docs
  title: ''
  type: Documentation
  url: https://gridlines.stoplight.io/
- group: docs
  title: ''
  type: APIReference
  url: https://gridlines.stoplight.io/
- group: start
  title: ''
  type: Login
  url: https://app.gridlines.io/
- group: operate
  title: ''
  type: Support
  url: https://ongrid.in/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ongrid.in/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ongrid.in/terms-of-service
created: '2026-10-28'
description: Gridlines is a digital onboarding infrastructure platform, branded "Gridlines by OnGrid" and operated by Handy Online Solutions Private Limited (India), for verifying customers, workers, partners, merchants and borrowers. It offers verification APIs and configurable workflows for identity checks, video KYC, Aadhaar offline verification (OVSE), DigiLocker, eSign and fraud-risk assessment, with SDKs, webhooks/status callbacks and a sandbox documented on its Stoplight developer portal, serving BFSI, lending, insurance, fintech, workforce, mobility/logistics and marketplace businesses.
image: https://gridlines.io/gridlines-logo.png
json_schemas:
- name: E-Sign-Init-Request
  property_count: 2
  slug: gridline-e-sign-init-request
jsonld:
- class_count: 7
  name: Gridline Context
  property_count: 24
  slug: gridline-context
layout: provider
modified: '2026-10-28'
name: Gridlines
nav: Providers
network: true
overview: 'Gridlines publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Deepfake API, Digilocker API, E Sign API, and 7 more. Tagged areas include Company, Onboarding, Identity Verification, KYC, and eSigning.


  The Gridlines catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gridlines'' developer surface includes sandbox, authentication, documentation, API reference, support, and 25 more developer resources.'
plans:
- name: Gridline Plans Pricing
  plan_count: 0
  slug: gridline-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Gridline Rate Limits
  slug: gridline-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Gridlines API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: gridline-rules
scopes:
- name: Gridline Scopes
  scope_count: 0
  slug: gridline-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 70.2
    catalog_earned_first_party: 8.0
    catalog_gap: 44.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 63.5
    developer_ergonomics: 38.7
    discoverability: 71.4
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/gridline/gridline-2026-11-03T133107.png
security:
- kind: authentication
  name: Gridline Authentication
  slug: gridline-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Gridline Domain Security
  slug: gridline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: gridline-aadhaar-ovse-verification
  slug: gridline-aadhaar-ovse-verification
- name: gridline-deepfake-check
  slug: gridline-deepfake-check
- name: gridline-digilocker-document-fetch
  slug: gridline-digilocker-document-fetch
- name: gridline-esign-document
  slug: gridline-esign-document
- name: gridline-selfie-face-verification
  slug: gridline-selfie-face-verification
slug: gridline
tags:
- Company
- Onboarding
- Identity Verification
- KYC
- eSigning
- Fraud Prevention
- VideoKYC
- DigitalOnboarding
- Fintech
website: https://gridlines.io/
---
