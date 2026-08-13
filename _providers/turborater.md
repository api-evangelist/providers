---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: Submit a single comparative rating request and receive real-time premiums and coverage back from many carriers at once, across auto, homeowners, condominium, renters, dwelling fire, and motorcycle lin
  name: TurboRater Rating and Quotes API
  slug: turborater-rating-quotes-api
- description: Capture the applicant, drivers, vehicles, dwelling, and coverage detail that a comparative rating request is built from, so a single point of data entry can be reused across every carrier quote and br
  name: TurboRater Applicants and Risk API
  slug: turborater-applicants-api
- description: Hand a completed quote from TurboRater into a downstream point-of-sale, agency management, or website platform in real time, or export it for daily download, using ITC's Turbo Tags 2.0 (.TT2) or AL3 f
  name: TurboRater Real-Time Bridge API
  slug: turborater-realtime-bridge-api
- description: Pull the quote and rate results a rating request produced, in either XML or ITC's proprietary TurboTags (TT2) format, so any third-party system can consume premiums, coverages, carrier eligibility, an
  name: TurboRater Results Retrieval API
  slug: turborater-results-retrieval-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turborater-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.turborater.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insurance-technologies-corporation
- group: docs
  title: ''
  type: Documentation
  url: https://www.turborater.com/products/rating/features/integration
- group: commercial
  title: ''
  type: Plans
  url: plans/turborater-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turborater-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turborater-finops.yml
created: '2026-07-10'
description: TurboRater is a personal lines comparative insurance rating platform from Insurance Technologies Corporation (ITC), now part of Zywave (marketed within Zywave Sales Cloud). It lets agencies, carriers, lead providers, and online aggregators quote auto, homeowners, condominium, renters, dwelling fire, and motorcycle coverage from 200+ carriers in a single workflow. ITC exposes a web service-based rating API (a service-oriented version of TurboRater it first offered to third parties in 2010, extended with a homeowner rating API in 2016) that returns real-time rates from hundreds of carriers and can pull quote data as XML or ITC's proprietary Turbo Tags (TT2) format, plus a real-time bridge that hands a completed quote into an agency point-of-sale or management system. The rating API is partner- and subscription-gated - access, carrier appointments, and the developer documentation are provisioned through ITC/Zywave sales rather than a public developer portal, so the specific endpoints
  below are honestly modeled from published behavior, not copied from a public API reference.
finops:
- name: Turborater Finops
  service_category: Insurance Software and Comparative Rating
  slug: turborater-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turborater.png
layout: provider
modified: '2026-07-10'
name: TurboRater
nav: Providers
network: true
overview: 'TurboRater publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, InsurTech, Comparative Rating, Auto Insurance, and Home Insurance.


  TurboRater''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Turborater Plans Pricing
  plan_count: 3
  slug: turborater-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Turborater Rate Limits
  slug: turborater-rate-limits
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 18.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Turborater Domain Security
  slug: turborater-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: turborater
tags:
- Insurance
- InsurTech
- Comparative Rating
- Auto Insurance
- Home Insurance
- Quotes
- Real-Time Rating
- Personal Lines
- ITC
- Zywave
website: https://www.turborater.com
---
