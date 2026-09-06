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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urban-jungle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myurbanjungle.com/
- group: company
  title: ''
  type: About
  url: https://myurbanjungle.com/about_us
- group: company
  title: ''
  type: Partners
  url: https://myurbanjungle.com/partners
- group: company
  title: ''
  type: Partners
  url: https://hello.myurbanjungle.com/partner-with-us/
- group: company
  title: ''
  type: Blog
  url: https://myurbanjungle.com/explore/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://myurbanjungle.com/explore/rss/
- group: operate
  title: ''
  type: Support
  url: https://myurbanjungle.zendesk.com/hc/en-gb
- group: operate
  title: ''
  type: Contact
  url: https://myurbanjungle.com/contact_us
- group: start
  title: ''
  type: Login
  url: https://myurbanjungle.com/account_manager
- group: company
  title: ''
  type: Careers
  url: https://myurbanjungle.com/explore/careers/
- group: other
  title: ''
  type: Team
  url: https://myurbanjungle.com/explore/meet-the-team/
- group: commercial
  title: ''
  type: Legal
  url: https://myurbanjungle.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myurbanjungle.com/legal/privacy_policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://myurbanjungle.com/legal/tac
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/urban-jungle-insurance/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@urbanjungle_ins
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/urbanjungle_ins
- group: design
  title: ''
  type: Conformance
  url: conformance/urban-jungle-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urban-jungle-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/urban-jungle-well-known.yml
created: '2026-07-25'
description: Urban Jungle Services Ltd is a London-based direct-to-consumer insurtech, founded in 2016 by Jimmy Williams and Greg Smyth to sell home insurance to "Generation Rent" — renters, sharers and students the traditional UK market underserves. It is an FCA-authorised intermediary (FRN 782061, company number 10414152, England and Wales) and a certified B Corp, selling contents, buildings and contents, students contents, tenants liability, landlord, home emergency and public liability cover through its own digital journey at myurbanjungle.com, and claiming over 100,000 customers. Its API posture is partner-gated and undocumented in public. Urban Jungle announced a partnership programme and quote API in 2018, positioned so lettings agents, PropTech firms, institutional landlords and eCommerce sites can serve Urban Jungle quotes inside their own apps without being directly FCA-regulated themselves, but there is no developer portal, no reference documentation, no machine- readable specification
  and no self-serve signup. The only route in is a partnerships email address on a marketing page. No ACORD, AL3 or NGDS reference appears anywhere on the company's site or in its front-end bundles.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Urban Jungle
nav: Providers
network: true
overview: 'Urban Jungle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Insurtech, Property and Casualty, and Home Insurance.


  Urban Jungle''s developer surface includes engineering blog, support, legal docs, YouTube channel, and 17 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 9.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: UK
      standard: uk-gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urban-jungle/refs/heads/main/screenshots/urban-jungle-2026-09-02T165148.png
security:
- kind: domain-security
  name: Urban Jungle Domain Security
  slug: urban-jungle-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: urban-jungle
tags:
- Insurance
- United Kingdom
- Insurtech
- Property and Casualty
- Home Insurance
- Renters Insurance
- Embedded Insurance
- Underwriting
- Brokers
- Direct to Consumer
website: https://myurbanjungle.com/
---
