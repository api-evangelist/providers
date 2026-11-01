---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'RESTful API (version 3) providing broad access across a Reduct workspace: projects, recordings, media, redactions and redaction motions, highlights, comments, and reels, plus transcript retrieval, tra'
  name: Reduct API
  slug: reduct-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/reduct/plans/reduct-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reduct-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://reduct.video/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.reduct.video/
- group: docs
  title: ''
  type: Documentation
  url: https://help.reduct.video/
- group: docs
  title: ''
  type: APIReference
  url: https://help.reduct.video/en/articles/api-access
- group: start
  title: ''
  type: GettingStarted
  url: https://help.reduct.video/en/articles/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://help.reduct.video/
- group: company
  title: ''
  type: Blog
  url: https://reduct.video/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reduct-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://reduct.video/pricing
- group: start
  title: ''
  type: Login
  url: https://app.reduct.video/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reduct.video/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reduct.video/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reduct.video/
- group: auth
  title: ''
  type: Compliance
  url: https://reduct.video/security
- group: auth
  href: https://artifacts.apis.io/reduct/security/reduct-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/reduct-trust-center.yml
- group: design
  href: https://artifacts.apis.io/reduct/conformance/reduct-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reduct-conformance.yml
- group: auth
  href: https://artifacts.apis.io/reduct/authentication/reduct-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reduct-authentication.yml
- group: design
  href: https://artifacts.apis.io/reduct/conventions/reduct-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reduct-conventions.yml
- group: design
  href: https://artifacts.apis.io/reduct/lifecycle/reduct-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reduct-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reduct/data-model/reduct-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reduct-data-model.yml
- group: design
  href: https://artifacts.apis.io/reduct/components/reduct-components.yml
  title: ''
  type: Components
  url: components/reduct-components.yml
- group: agent
  href: https://artifacts.apis.io/reduct/llms/reduct-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reduct-llms.txt
- group: auth
  href: https://artifacts.apis.io/reduct/security/reduct-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reduct-domain-security.yml
created: '2026-07-17'
description: Reduct (reduct.video) is a video intelligence platform that transcribes, translates, redacts, searches, annotates, and edits audio and video through a text-based editor. Teams in legal, qualitative research, film and production, marketing, and education use it to find and share what matters across hours of footage. Reduct exposes a RESTful API (current version 3) giving broad programmatic access across a workspace — projects, recordings, media, transcripts, redactions and redaction motions, highlights, comments, and reels — with per-workspace API-key authentication on the Professional and Enterprise plans. The company is SOC 2 Type II certified with GDPR and HIPAA support.
finops:
- has_sources: true
  method: derived
  name: Reduct Finops
  primary_unit: editor
  service_category: ''
  slug: reduct-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reduct.png
layout: provider
modified: '2026-07-21'
name: Reduct
nav: Providers
network: true
overview: 'Reduct is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Application, Video, Transcription, and Translation.


  Reduct''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 17 more developer resources.'
plans:
- name: Reduct Plans Pricing
  plan_count: 3
  slug: reduct-plans-pricing
- name: Reduct Price Estimates
  plan_count: 0
  slug: reduct-price-estimates
random_paper: 23
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 43.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reduct/reduct-2026-09-02T153159.png
security:
- kind: authentication
  name: Reduct Authentication
  slug: reduct-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reduct Domain Security
  slug: reduct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reduct Trust Center
  slug: reduct-trust-center
  summary_line: SOC 2 Type II, GDPR, HIPAA
slug: reduct
tags:
- Company
- Application
- Video
- Transcription
- Translation
- Redaction
- Video Editing
- Media
- Artificial Intelligence
website: https://reduct.video/
---
