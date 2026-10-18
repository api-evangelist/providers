---
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
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.1
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: https://api.suzanne3d.com
  baseurl_source: declared
  description: Submit text-to-3D and photo-to-3D jobs
  name: Suzanne Generations API
  slug: suzanne3d-generations-api
- baseURL: https://api.suzanne3d.com
  baseurl_source: declared
  description: Poll and cancel jobs
  name: Suzanne Jobs API
  slug: suzanne3d-jobs-api
- baseURL: https://api.suzanne3d.com
  baseurl_source: declared
  description: Download finished meshes
  name: Suzanne Models API
  slug: suzanne3d-models-api
- baseURL: https://api.suzanne3d.com
  baseurl_source: declared
  description: Presigned image uploads
  name: Suzanne Uploads API
  slug: suzanne3d-uploads-api
artifact_total: 17
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.suzanne3d.com/terms
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/rate-limits/suzanne3d-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/suzanne3d-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/plans/suzanne3d-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/suzanne3d-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/rules/suzanne3d-rules.yml
  title: ''
  type: Spectral
  url: rules/suzanne3d-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/json-ld/suzanne3d-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/suzanne3d-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/vocabulary/suzanne3d-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/suzanne3d-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/data-model/suzanne3d-data-model.yml
  title: ''
  type: DataModel
  url: data-model/suzanne3d-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/conventions/suzanne3d-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/suzanne3d-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/conventions/suzanne3d-conventions.yml
  title: ''
  type: Conventions
  url: conventions/suzanne3d-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/sandbox/suzanne3d-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/suzanne3d-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://www.suzanne3d.com/contact
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/security/suzanne3d-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/suzanne3d-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/authentication/suzanne3d-authentication.yml
  title: ''
  type: Authentication
  url: authentication/suzanne3d-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.suzanne3d.com/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/lifecycle/suzanne3d-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/suzanne3d-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/errors/suzanne3d-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/suzanne3d-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/errors/suzanne3d-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/suzanne3d-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/conformance/suzanne3d-conformance.yml
  title: ''
  type: Conformance
  url: conformance/suzanne3d-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/overlays/suzanne3d-openapi-generated-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/suzanne3d-openapi-generated-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/hosts/suzanne3d-hosts.yml
  title: ''
  type: Hosts
  url: hosts/suzanne3d-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/vendors/suzanne3d-vendors.yml
  title: ''
  type: Vendors
  url: vendors/suzanne3d-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://suzanne3d.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.suzanne3d.com/
- group: docs
  title: ''
  type: Documentation
  url: https://console.suzanne3d.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://console.suzanne3d.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://console.suzanne3d.com/documentation/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://console.suzanne3d.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://console.suzanne3d.com/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.suzanne3d.com/blog
- group: learn
  title: ''
  type: Tutorials
  url: https://www.suzanne3d.com/guides
- group: operate
  title: ''
  type: Support
  url: https://www.suzanne3d.com/contact
- group: company
  title: ''
  type: About
  url: https://www.suzanne3d.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suzanne3d.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suzanne3d.com/privacy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/trysuzanne
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/security/suzanne3d-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suzanne3d-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://suzanne3d.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: 'Suzanne (Suzanne 3D Inc., San Francisco) is an AI industrial-design platform that turns text prompts, photos and sketches into manufacturable 3D designs with physics and manufacturing intelligence built in. The Suzanne API at api.suzanne3d.com is a B2B surface for 3D mesh generation: submit a text-to-3D or photo-to-3D job against named models (sculptor, atelier, capture) powered by its in-house Atelier2 engine, poll the job, and download GLB, OBJ, STL or FBX output.'
image: https://suzanne3d.com/favicon.png
json_schemas:
- name: CancelResult
  property_count: 3
  slug: suzanne3d-cancel-result
- name: JobAccepted
  property_count: 4
  slug: suzanne3d-job-accepted
- name: Job
  property_count: 8
  slug: suzanne3d-job
- name: PhotoTo3dRequest
  property_count: 5
  slug: suzanne3d-photo-to3d-request
- name: TextTo3dRequest
  property_count: 4
  slug: suzanne3d-text-to3d-request
- name: UploadCreated
  property_count: 3
  slug: suzanne3d-upload-created
jsonld:
- class_count: 8
  name: Suzanne3D Context
  property_count: 19
  slug: suzanne3d-context
layout: provider
modified: '2026-10-07'
name: Suzanne
nav: Providers
network: true
overview: 'Suzanne is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Generations API, Jobs API, Models API, and 1 more. Tagged areas include Company, 3D, 3D Models, Generative AI, and Industrial Design.


  The Suzanne catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Suzanne''s developer surface includes pricing, sandbox, authentication, documentation, API reference, getting-started guide, signup flow, and 30 more developer resources.'
plans:
- name: Suzanne3D Plans Pricing
  plan_count: 3
  slug: suzanne3d-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 8
  name: Suzanne3D Rate Limits
  slug: suzanne3d-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Suzanne API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: suzanne3d-rules
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 29.9
    developer_ergonomics: 66.1
    discoverability: 71.4
    operational_transparency: 57.9
  previous_composite: 52.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/suzanne3d/refs/heads/main/screenshots/suzanne3d-2026-10-11T130510.png
security:
- kind: authentication
  name: Suzanne3D Authentication
  slug: suzanne3d-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Suzanne3D Domain Security
  slug: suzanne3d-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Suzanne3D Vulnerability Disclosure
  slug: suzanne3d-vulnerability-disclosure
  summary_line: contact published
slug: suzanne3d
tags:
- Company
- 3D
- 3D Models
- Generative AI
- Industrial Design
- CAD
- Mesh Generation
- Text-to-3D
- Photo-to-3D
- Manufacturing
website: https://suzanne3d.com
---
