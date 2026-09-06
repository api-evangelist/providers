---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: ViX is the world's largest Spanish-language streaming service offering over 65,000 hours of content across free (ad-supported) and premium subscription tiers. ViX provides programmatic advertising acc
  name: ViX Streaming Platform
  slug: vix-streaming
- description: TelevisaUnivision's advertising technology platform enables brands and agencies to reach U.S. Spanish-speaking and bilingual audiences through data-driven linear TV, addressable TV, connected TV (ViX)
  name: TelevisaUnivision Advertising Platform
  slug: advertising-platform
- description: Uforia is the largest Spanish-language audio platform in the United States, operating 40 radio stations and delivering streaming audio content. It provides advertisers access to the U.S. Hispanic audi
  name: Uforia Audio Platform
  slug: uforia-audio
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/univision-communications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corporate.televisaunivision.com
- group: company
  title: ''
  type: About
  url: https://corporate.televisaunivision.com/our-company/
- group: company
  title: ''
  type: Blog
  url: https://corporate.televisaunivision.com/press/press-releases/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/televisaunivision
- group: build
  title: ''
  type: GitHub
  url: https://github.com/televisa-univision
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/univision-communications/refs/heads/main/vocabulary/univision-communications-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/univision-communications/refs/heads/main/json-ld/univision-communications-context.jsonld
created: '2026-03-24'
description: TelevisaUnivision (formerly Univision Communications) is the world's leading Spanish-language media company, operating television networks (Univision, UniMás, TUDN, Galavisión), the ViX streaming platform, Uforia audio platform, and a suite of advanced advertising technology solutions. The company serves advertisers and media partners through programmatic ad platforms, first-party audience data, and content partnerships rather than a public developer API.
finops:
- name: Univision Communications Finops
  service_category: Media and Advertising
  slug: univision-communications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/univision-communications.png
jsonld:
- class_count: 24
  name: Univision Communications Context
  property_count: 27
  slug: univision-communications-context
layout: provider
modified: '2026-05-03'
name: TelevisaUnivision (Univision Communications)
nav: Providers
network: true
overview: 'TelevisaUnivision (Univision Communications) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Streaming, Hispanic, Advertising, and Television.


  The TelevisaUnivision (Univision Communications) catalog on APIs.io includes 1 JSON-LD context.


  TelevisaUnivision (Univision Communications)''s developer surface includes engineering blog, GitHub presence, and 6 more developer resources.'
plans:
- name: Univision Communications Plans Pricing
  plan_count: 1
  slug: univision-communications-plans-pricing
press:
- date: '2026-05-25'
  title: Veritone® Announces Multi-Market Agreement with Univision ...
  url: https://financialpost.com/pmn/press-releases-pmn/business-wire-news-releases-pmn/veritone-announces-multi-market-agreement-with-univision-radio-network-to-provide-near-real-time-intelligence-for-ad-campaigns-and-branded-solutions
- date: '2026-05-25'
  title: Univision Local Media Joins the Sinclair and ...
  url: https://www.nexstar.tv/univision-local-media-joins-sinclair-nexstar-consortium-promote-broadcast-spectrum-aggregation-innovation-monetization/
- date: '2026-05-25'
  title: Univision Partners With Google to Transform Its Business ...
  url: https://www.googlecloudpresscorner.com/2021-04-26-Univision-Partners-With-Google-to-Transform-Its-Business-and-Become-the-Media-Company-of-Tomorrow
- date: '2026-05-25'
  title: Univision Partners With Google to Transform Its Business ...
  url: https://www.prnewswire.com/news-releases/univision-partners-with-google-to-transform-its-business-and-become-the-media-company-of-tomorrow-301276246.html
- date: '2026-05-25'
  title: Veritone® Announces Multi-Market Agreement with Univision ...
  url: https://investors.veritone.com/news-events/press-releases/detail/167/veritone-announces-multi-market-agreement-with-univision-radio-network-to-provide-near-real-time-intelligence-for-ad-campaigns-and-branded-solutions
random_paper: 13
rate_limits:
- limit_count: 1
  name: Univision Communications Rate Limits
  slug: univision-communications-rate-limits
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 15.2
    contract_quality: 14.7
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 10.5
  previous_composite: 18.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/univision-communications/refs/heads/main/screenshots/univision-communications-2026-06-20T200411.png
security:
- kind: domain-security
  name: Univision Communications Domain Security
  slug: univision-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: univision-communications
tags:
- Media
- Streaming
- Hispanic
- Advertising
- Television
- Radio
- Content
website: https://corporate.televisaunivision.com
---
