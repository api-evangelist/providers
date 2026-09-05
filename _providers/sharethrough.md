---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST-ish reporting API enabling publishers to pull programmatic performance data for their Sharethrough inventory. A single POST /v2/programmatic endpoint takes a query object (startDate, endDate, gro
  name: Sharethrough Publisher Reporting API
  slug: sharethrough-publisher-reporting-api
- description: OpenRTB 2.x bid endpoint at /universal/v1, integrated through the first-party sharethrough bidder adapter in Prebid.js (adapter version 4.3.0, IAB GVL ID 80). Supports banner, native and video/CTV, th
  name: Sharethrough Header Bidding (Prebid) API
  slug: sharethrough-header-bidding-prebid-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.sharethrough.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.sharethrough.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.sharethrough.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sharethrough
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sharethrough
- group: company
  title: ''
  type: Blog
  url: https://www.sharethrough.com/blog
- group: other
  title: ''
  type: X
  url: https://x.com/sharethrough
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sharethrough.com/publisher-platform-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy-center.sharethrough.com
- group: operate
  title: ''
  type: Contact
  url: https://www.sharethrough.com/contact
- group: commercial
  title: ''
  type: Plans
  url: plans/sharethrough-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sharethrough-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sharethrough-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sharethrough-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sharethrough-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sharethrough-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sharethrough-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sharethrough-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sharethrough-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sharethrough-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sharethrough-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/sharethrough-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sharethrough-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sharethrough-llms.txt
- group: other
  title: ''
  type: SellersJSON
  url: sellers-json/sharethrough-sellers-json.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sharethrough-context.jsonld
created: '2026-06-13'
description: 'Sharethrough is an omnichannel programmatic advertising exchange (SSP) for native, display, video and CTV inventory, and one of the largest independent ad marketplaces. Publishers monetise through the Prebid.js header-bidding adapter and server-to-server OpenRTB; demand partners buy through the exchange. Two API surfaces exist: a bearer-token Publisher Reporting API at publisher-api.sharethrough.com/v2 whose public reference is now behind a support-site sign-in, and the unauthenticated OpenRTB bid endpoint at btlr.sharethrough.com/universal/v1 used by the Prebid adapter. The company''s richest machine-readable artifact is its IAB sellers.json (5,189 sellers). Sharethrough merged with Equativ in 2024 and has operated under the Equativ brand since June 2025; the Sharethrough exchange and its endpoints continue to run.'
finops:
- name: Sharethrough Finops
  service_category: ''
  slug: sharethrough-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sharethrough.png
jsonld:
- class_count: 7
  name: Sharethrough Context
  property_count: 12
  slug: sharethrough-context
layout: provider
modified: '2026-08-12'
name: Sharethrough
nav: Providers
network: true
overview: 'Sharethrough publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Native Advertising, Programmatic Advertising, SSP, DSP, and OpenRTB.


  The Sharethrough catalog on APIs.io includes 1 JSON-LD context.


  Sharethrough''s developer surface includes documentation, support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Sharethrough Plans Pricing
  plan_count: 2
  slug: sharethrough-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Sharethrough Rate Limits
  slug: sharethrough-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.0
    catalog_earned_first_party: 8.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 14.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 30.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sharethrough/refs/heads/main/screenshots/sharethrough-2026-06-20T193746.png
security:
- kind: authentication
  name: Sharethrough Authentication
  slug: sharethrough-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sharethrough Domain Security
  slug: sharethrough-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sharethrough
tags:
- Native Advertising
- Programmatic Advertising
- SSP
- DSP
- OpenRTB
- Ad Exchange
- Header Bidding
- CTV
- Sustainability
website: https://www.sharethrough.com
---
