---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CAPTCHA solving API allowing developers to submit CAPTCHA images and retrieve solutions.
  name: ImageTyperz API
  slug: imagetyperz-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/imagetyperz/errors/imagetyperz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/imagetyperz-problem-types.yml
- group: other
  href: https://artifacts.apis.io/imagetyperz/hosts/imagetyperz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/imagetyperz-hosts.yml
- group: build
  href: https://artifacts.apis.io/imagetyperz/packages/imagetyperz-packages.yml
  title: ''
  type: SDKs
  url: packages/imagetyperz-packages.yml
- group: build
  href: https://artifacts.apis.io/imagetyperz/packages/imagetyperz-packages.yml
  title: ''
  type: Packages
  url: packages/imagetyperz-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imagetyperz.com/Forms/terms-of-service.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imagetyperz.com/Forms/privacy-policy.aspx
- group: auth
  href: https://artifacts.apis.io/imagetyperz/security/imagetyperz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imagetyperz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://imagetyperz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.imagetyperz.com/Forms/api/api.html
- group: operate
  title: ''
  type: Support
  url: https://www.imagetyperz.com/Forms/Contactus.aspx
coverage:
  checked: '2026-10-28'
  detail: API documentation is provided as HTML pages without a machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://www.imagetyperz.com/Forms/api/api.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: ImageTyperz provides a human‑powered CAPTCHA solving service with a public API that allows developers to automate the solving of image CAPTCHAs, reCAPTCHA, hCaptcha, and other challenge types. The API offers endpoints for submitting CAPTCHA images, retrieving solutions, and managing account balances, enabling integration into bots, scrapers, and automation workflows. The service emphasizes fast turnaround and high accuracy through a crowd‑sourced solving approach.
image: https://www.imagetyperz.com/Image/logo.png
layout: provider
modified: '2026-10-28'
name: ImageTyperz
nav: Providers
network: true
overview: 'ImageTyperz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CAPTCHA, Automation, Services, and Image Processing.


  ImageTyperz''s developer surface includes documentation, support, and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/imagetyperz/imagetyperz-2026-11-03T133655.png
security:
- kind: authentication
  name: Imagetyperz Authentication
  slug: imagetyperz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Imagetyperz Domain Security
  slug: imagetyperz-domain-security
  summary_line: TLSv1.2
slug: imagetyperz
tags:
- Company
- CAPTCHA
- Automation
- Services
- Image Processing
website: https://imagetyperz.com/
---
