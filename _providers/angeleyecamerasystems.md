---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API surface not documented publicly
  name: AngelEye Health API
  slug: angeleye-health-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.angeleyehealth.com/
- group: other
  href: https://artifacts.apis.io/angeleyecamerasystems/hosts/angeleyecamerasystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angeleyecamerasystems-hosts.yml
- group: other
  href: https://artifacts.apis.io/angeleyecamerasystems/vendors/angeleyecamerasystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/angeleyecamerasystems-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.angeleyehealth.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.angeleyehealth.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.angeleyehealth.com/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://www.angeleyehealth.com/blog/
- group: auth
  href: https://artifacts.apis.io/angeleyecamerasystems/security/angeleyecamerasystems-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/angeleyecamerasystems-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/angeleyecamerasystems/security/angeleyecamerasystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angeleyecamerasystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.angeleyehealth.com
coverage:
  checked: 2026-09-24
  detail: No OpenAPI or other machine‑readable contract found at common endpoints (e.g., https://api.angeleyehealth.com/openapi.json returned 404)
  evidence:
  - status: 404
    url: https://api.angeleyehealth.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: AngelEye Health provides a complete HIPAA‑compliant NICU patient engagement platform that integrates parents into the child’s care team, offering camera‑based monitoring, milk‑tracker, and digital road‑map solutions to empower families and support care teams across over 350 hospitals. The platform includes AI‑driven insights, secure data handling, and a suite of tools for clinicians and families alike, aiming to improve outcomes and streamline NICU discharge processes.
image: https://www.angeleyehealth.com/wp-content/uploads/bg-hero-home02-1024x514.png
layout: provider
modified: '2026-09-24'
name: Angeleyecamerasystems
nav: Providers
network: true
overview: 'Angeleyecamerasystems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include NICU, Camera System, Feeding Management, and Hospital Solutions.


  Angeleyecamerasystems'' developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/angeleyecamerasystems/angeleyecamerasystems-2026-10-11T094034.png
security:
- kind: domain-security
  name: Angeleyecamerasystems Domain Security
  slug: angeleyecamerasystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Angeleyecamerasystems Trust Center
  slug: angeleyecamerasystems-trust-center
  summary_line: HIPAA
slug: angeleyecamerasystems
tags:
- NICU
- Camera System
- Feeding Management
- Hospital Solutions
website: https://www.angeleyehealth.com
---
