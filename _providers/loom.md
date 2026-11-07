---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: Embed Loom's recording experience directly into your web app. The recordSDK lets users record screen, mic, and camera, and uploads the resulting video to a Loom-hosted account. Authenticated via OAuth
  name: Loom Record SDK API
  slug: loom-record-sdk
- description: Embed the Loom video player into a web page or app, with playback controls, captions, and engagement events. Includes an oEmbed endpoint for converting a Loom URL into rich embed HTML.
  name: Loom Embed SDK API
  slug: loom-embed-sdk
- description: oEmbed-compatible endpoint that returns rich embed metadata (HTML, thumbnail, width, height) for a given Loom video URL.
  name: Loom oEmbed API
  slug: loom-oembed-api
- description: SCIM 2.0 user and group provisioning endpoint for Enterprise customers. Integrates with Okta, Azure AD, OneLogin, and other IdPs to automate workspace membership.
  name: Loom SCIM Provisioning API
  slug: loom-scim-api
- description: SAML 2.0 single sign-on configuration for Enterprise workspaces. Configurable per workspace from the admin console; not a customer-callable REST API but documented as part of the Loom platform integra
  name: Loom SSO (SAML) Configuration
  slug: loom-sso-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/loom/security/loom-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/loom-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/loom/security/loom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loom-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useloom
- group: company
  title: ''
  type: Website
  url: https://www.loom.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.loom.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loom.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/loomhq
- group: commercial
  href: https://artifacts.apis.io/loom/plans/loom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loom-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/loom/rate-limits/loom-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loom-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/loom/finops/loom-finops.yml
  title: ''
  type: FinOps
  url: finops/loom-finops.yml
- group: other
  href: https://artifacts.apis.io/loom/review.yml
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/loom
created: '2026-05-08'
description: Loom is an async video messaging platform (now part of Atlassian) used by teams to record screen, voice, and camera. The Loom developer platform exposes the recordSDK and embedSDK for embedding recording and playback into other apps, plus SCIM provisioning and SSO/admin APIs available on Business and Enterprise plans.
finops:
- has_sources: true
  method: generated
  name: Loom Finops
  primary_unit: ''
  service_category: Productivity
  slug: loom-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loom.png
layout: provider
modified: '2026-05-30'
name: Loom
nav: Providers
network: true
overview: 'Loom is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Video, Async, Communications, and Software-as-a-Service.


  Loom''s developer surface includes pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Loom Plans Pricing
  plan_count: 4
  slug: loom-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Loom Rate Limits
  slug: loom-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 62.5
    operational_transparency: 13.2
  previous_composite: 19.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/loom/loom-2026-06-20T184719.png
security:
- kind: domain-security
  name: Loom Domain Security
  slug: loom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Loom Trust Center
  slug: loom-trust-center
  summary_line: FedRAMP
slug: loom
tags:
- Productivity
- Video
- Async
- Communications
- Software-as-a-Service
- Collaboration
website: https://www.loom.com/
---
