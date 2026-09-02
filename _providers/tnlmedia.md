---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 4.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The header-bidding demand endpoint operated by Ad2iction, TNL Mediagene's ad-technology subsidiary (acquired by TNL Media Group in 2020). Publishers reach it through the `ad2iction` bidder adapter shi
  name: Ad2iction Prebid Bid Endpoint
  slug: ad2iction-prebid-bid-endpoint
artifact_total: 4
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/prebid/Prebid.js/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tnlmedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tnlmediagene.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tnlmediagene.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tnlmediagene.com/terms
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prebid.org/dev-docs/bidders/ad2iction.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tnlmediagene
- group: company
  title: ''
  type: Blog
  url: https://www.tnlmediagene.com/news
- group: design
  title: ''
  type: Components
  url: components/tnlmedia-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/tnlmedia-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tnlmedia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tnlmedia-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tnlmedia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tnlmedia-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tnlmedia-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/tnlmedia-content-signals.yml
created: '2026-07-17'
description: TNL Mediagene is a next-generation digital and technology media group serving millennial and Gen Z audiences across Asia. Formed from the 2023 merger of Taiwan's The News Lens and Japan's Mediagene, the group operates more than twenty media brands spanning news, business, technology, lifestyle, and sports — including The News Lens, INSIDE, Cool3c, Gizmodo Japan, Business Insider Japan, Lifehacker Japan, Roomie, and licensed titles such as Digiday Japan and Glossy Japan. Beyond publishing, the company runs advertising and marketing technology (the Ad2iction DSP), an AI-driven customer data and audience analytics platform, e-commerce properties, and market-research services. It is a portfolio company of 500 Global and is listed on Nasdaq as TNMG. The group publishes no developer portal, no OpenAPI, and no SDK. Its one public, machine-readable integration surface is the Ad2iction header-bidding adapter shipped inside Prebid.js — a first-party-maintained open-source module that
  posts bid requests to https://ads.ad2iction.com/html/prebid/, documented on the Prebid.org bidder registry rather than on a TNL Mediagene developer site.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tnlmedia.png
layout: provider
modified: '2026-08-12'
name: TNL Mediagene
nav: Providers
network: true
overview: 'TNL Mediagene publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Publishing, Advertising, and AdTech.


  TNL Mediagene''s developer surface includes API reference, engineering blog, and 14 more developer resources.'
plans:
- name: Tnlmedia Plans Pricing
  plan_count: 0
  slug: tnlmedia-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Tnlmedia Rate Limits
  slug: tnlmedia-rate-limits
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 13.8
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tnlmedia Domain Security
  slug: tnlmedia-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tnlmedia
tags:
- Company
- Media
- Publishing
- Advertising
- AdTech
- Marketing
- Digital Media
- Content
- Analytics
- E-Commerce
- Header Bidding
- Programmatic
- Prebid
website: https://www.tnlmediagene.com
---
