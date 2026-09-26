---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: The GrabCAD Print API lets partner and enterprise software drive Stratasys 3D printers and GrabCAD Print workflows programmatically — submitting and managing print jobs, retrieving printer and job sta
  name: GrabCAD Print API
  slug: grabcad-print-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://grabcad.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://grabcad.com/en/software-development-kit
- group: docs
  title: ''
  type: Documentation
  url: https://help.grabcad.com
- group: docs
  title: ''
  type: APIReference
  url: https://print-api.grabcad.com/public/documentation
- group: company
  title: ''
  type: Blog
  url: https://blog.grabcad.com
- group: operate
  title: ''
  type: Support
  url: https://help.grabcad.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GrabCAD
- group: start
  title: ''
  type: SignUp
  url: https://grabcad.com/profile/register
- group: start
  title: ''
  type: Login
  url: https://grabcad.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grabcad.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grabcad.com/privacy_policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/well-known/grabcad-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/grabcad-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/well-known/grabcad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/grabcad-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/security/grabcad-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/grabcad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/grabcad
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/security/grabcad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grabcad-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/authentication/grabcad-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grabcad-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/lifecycle/grabcad-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/grabcad-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/llms/grabcad-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grabcad-llms.txt
created: '2026-07-17'
description: GrabCAD, a Stratasys company, operates a connected additive-manufacturing platform spanning the GrabCAD Community Library of free CAD models, GrabCAD Print and Print Pro for driving Stratasys 3D printers, GrabCAD Shop for shop-floor job management, and the GrabCAD Software Development Kit / Software Partner Program. For developers, GrabCAD exposes the GrabCAD Print API (print-api.grabcad.com) plus a family of SDKs — MTConnect data streaming, a Printer Connectivity SDK for ERP/PLM/MES integration, a PLM SDK, and an FDM printer emulator — that let ISVs and enterprises integrate Stratasys printers and GrabCAD Print into their own manufacturing software ecosystems.
image: https://d1pspl52z5rk07.cloudfront.net/static/favicon.ico
layout: provider
modified: '2026-07-19'
name: GrabCAD
nav: Providers
network: true
overview: 'GrabCAD publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B, 3D Printing, Additive Manufacturing, and CAD.


  GrabCAD''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 25.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/grabcad/refs/heads/main/screenshots/grabcad-2026-07-25T220149.png
security:
- kind: authentication
  name: Grabcad Authentication
  slug: grabcad-authentication
  summary_line: account-login · 1 scheme
- kind: domain-security
  name: Grabcad Domain Security
  slug: grabcad-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Grabcad Vulnerability Disclosure
  slug: grabcad-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: grabcad
tags:
- Company
- B2B
- 3D Printing
- Additive Manufacturing
- CAD
- Manufacturing
- Hardware
- Developer SDK
website: https://grabcad.com
---
