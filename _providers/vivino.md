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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vivino-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vivino.com/
- group: operate
  title: ''
  type: Support
  url: https://www.vivino.com/contact
created: '2026-07-17'
description: Vivino is the world's largest online wine marketplace and wine-discovery mobile app, founded in 2010 in Copenhagen, Denmark by Heini Zachariassen and Theis Sondergaard. Users scan a wine label to get community ratings, reviews, and tasting notes drawn from a database of more than 15 million wines and tens of millions of members, and can buy wine directly through the integrated marketplace. As of an enrichment pass on 2026-07-21, Vivino does not publish an official public API or developer portal (the former developer.vivino.com subdomain 301-redirects to the main site), so this profile carries identity and domain-security signals only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vivino.png
layout: provider
modified: '2026-07-21'
name: vivino
nav: Providers
network: true
overview: 'vivino is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wine, Marketplace, E-Commerce, and Mobile App.


  vivino''s developer surface includes support and 2 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Vivino Domain Security
  slug: vivino-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vivino
tags:
- Company
- Wine
- Marketplace
- E-Commerce
- Mobile App
- Ratings and Reviews
- Food and Beverage
- Consumer
website: https://www.vivino.com/
---
