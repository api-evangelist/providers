---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foot-locker-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/foot-locker-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/footlocker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/footlocker
- group: company
  title: ''
  type: Website
  url: https://www.footlocker.com/
- group: other
  title: ''
  type: CorporateSite
  url: https://www.footlocker-inc.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.footlocker-inc.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.footlocker.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.footlocker.com/help/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.footlocker.com/help/privacy-statement.html
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.footlocker.com/affiliates.html
coverage:
  checked: '2026-09-10'
  detail: Foot Locker publishes no developer site of its own — its one real API, the Foot Locker/Eastbay supplier inventory feed, is documented inside CommerceHub's Dsco platform, whose docs host answers HTTP 403 behind a TLS certificate that expired in December 2025.
  evidence:
  - status: 403
    url: https://gandalf.dsco.io/platform_content/fleast-updatinginventory-api/
  - status: 404
    url: https://www.footlocker.com/.well-known/api-catalog
  - status: 200
    url: https://www.footlocker.com/openapi.json
  reason: marketplace-only
  state: gated
created: '2026-03-21'
description: 'Foot Locker, Inc. is a global retailer of athletic footwear and apparel, operating the Foot Locker, Kids Foot Locker, Champs Sports, WSS and atmos banners across North America, Europe, Asia and Australia. DICK''S Sporting Goods completed its acquisition of Foot Locker, Inc. on September 8, 2025 and continues to operate the Foot Locker brand suite. Foot Locker publishes no public developer portal, API reference or machine-readable contract. Trading-partner integration runs through third-party host platforms rather than a first-party developer site: supplier inventory and dropship through CommerceHub Dsco, and the Storefronts creator/affiliate program through impact.com, each requiring a commercial agreement. The former api.footlocker.com Apigee gateway no longer resolves.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foot-locker.png
layout: provider
modified: '2026-09-10'
name: Foot Locker
nav: Providers
network: true
overview: Foot Locker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Retail, Footwear, Apparel, and E-Commerce.
press:
- date: '2026-05-25'
  title: FOOT LOCKER, INC. REPORTS PRELIMINARY FIRST ...
  url: https://www.prnewswire.com/news-releases/foot-locker-inc-reports-preliminary-first-quarter-2025-financial-results-302456491.html
- date: '2026-05-25'
  title: Foot Locker analyzes customer feedback with AI
  url: https://chainstoreage.com/foot-locker-analyzes-customer-feedback-ai
- date: '2026-05-25'
  title: How Foot Locker Stepped Into a Gen AI Marketing Journey
  url: https://www.smartly.io/resources/how-foot-locker-stepped-into-a-gen-ai-marketing-journey
- date: '2026-05-25'
  title: DICK'S Sporting Goods Completes Acquisition of Foot Locker
  url: https://www.prnewswire.com/news-releases/dicks-sporting-goods-completes-acquisition-of-foot-locker-302548690.html
- date: '2026-05-25'
  title: Foot Locker – InMoment
  url: https://inmoment.com/customer-stories/foot-locker-uses-ai-npl-text-analytics/
random_paper: 12
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 2.6
  previous_composite: 10.3
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Foot Locker Domain Security
  slug: foot-locker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: foot-locker
tags:
- Fortune 500
- Retail
- Footwear
- Apparel
- E-Commerce
- Sneakers
- Omnichannel
website: https://www.footlocker.com/
---
