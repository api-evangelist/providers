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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The EarthCam API provides programmatic access to EarthCam's live webcam network, construction monitoring feeds, visual intelligence data, and AI-powered analytics. Endpoints include search, camera lis
  name: EarthCam API
  slug: earthcam-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/earthcam/hosts/earthcam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/earthcam-hosts.yml
- group: other
  href: https://artifacts.apis.io/earthcam/vendors/earthcam-vendors.yml
  title: ''
  type: Vendors
  url: vendors/earthcam-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.earthcam.com/company/tos.php
- group: operate
  title: ''
  type: Support
  url: https://www.earthcam.com/support/contactus.php?d=clientsupport
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.earthcam.com/company/privacy.php
- group: company
  title: ''
  type: Newsroom
  url: https://www.earthcam.com/press/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.earthcam.com/myearthcam/help/gettingstarted.php
- group: auth
  href: https://artifacts.apis.io/earthcam/security/earthcam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/earthcam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://earthcam.com/
coverage:
  checked: '2026-10-28'
  detail: EarthCam does not provide a public developer program or API documentation; the site offers only a private /api/ endpoint that returns 403.
  evidence:
  - status: 403
    url: https://www.earthcam.com/api/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: EarthCam operates a global network of live streaming webcams covering iconic landmarks, cityscapes, construction sites, and events. It offers visual data services, AI-powered analytics, time‑lapse movies, and integration capabilities for partners. Through its platform, users can view real‑time feeds, access historical footage, and embed cameras on websites, while developers can leverage the EarthCam API to search cameras, retrieve metadata, and integrate live streams into applications.
image: https://www.earthcam.com/images/holiday_logos/SOL-EClogo.png
layout: provider
modified: '2026-10-28'
name: EarthCam
nav: Providers
network: true
overview: 'EarthCam is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Webcam, Construction, visual-data, and Artificial Intelligence.


  EarthCam''s developer surface includes support, getting-started guide, and 7 more developer resources.'
plans:
- name: Earthcam Plans Pricing
  plan_count: 0
  slug: earthcam-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Earthcam Rate Limits
  slug: earthcam-rate-limits
scopes:
- name: Earthcam Scopes
  scope_count: 0
  slug: earthcam-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 67.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/earthcam/earthcam-2026-11-03T131217.png
security:
- kind: authentication
  name: Earthcam Authentication
  slug: earthcam-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Earthcam Domain Security
  slug: earthcam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: earthcam
tags:
- Company
- Webcam
- Construction
- visual-data
- Artificial Intelligence
website: https://earthcam.com/
---
