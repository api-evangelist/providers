---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mashable Agentic Access
  operation_count: 2
  slug: mashable-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://newsapi.org/v2
  baseurl_source: declared
  description: Search across all indexed articles.
  name: Mashable Articles API
  slug: mashable-articles-api
- baseURL: https://newsapi.org/v2
  baseurl_source: declared
  description: Top headline retrieval.
  name: Mashable Headlines API
  slug: mashable-headlines-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mashable via News Articles API
  slug: open-mashable-articles-api
- collection_type: open
  name: Mashable via News Articles Headlines API
  slug: open-mashable-headlines-api
- collection_type: open
  name: Mashable via News API
  slug: open-mashable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mashable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mashable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mashable-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mashable.com/
- group: company
  title: ''
  type: About
  url: https://mashable.com/about
- group: other
  title: ''
  type: Advertising
  url: https://mashable.com/advertise
- group: company
  title: ''
  type: Newsletter
  url: https://mashable.com/newsletter
- group: docs
  title: ''
  type: Documentation
  url: https://newsapi.org/s/mashable-api
- group: other
  title: ''
  type: RSS
  url: http://feeds.mashable.com/mashable
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mashable.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mashable.com/terms
- group: other
  title: ''
  type: X
  url: https://twitter.com/mashable
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/mashable/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/mashable/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/mashable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mashable
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mashable
created: '2026-03-24'
description: Mashable is a digital media and entertainment company covering tech, culture, and digital trends. Founded in 2005, Mashable has grown into a global, multi-platform media and entertainment company. Mashable does not publish a first-party REST API, but its headlines and articles are accessible via the third-party News API REST service.
finops:
- name: Mashable Finops
  service_category: API
  slug: mashable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mashable.png
layout: provider
modified: '2026-05-19'
name: Mashable
nav: Providers
network: true
overview: 'Mashable publishes 2 APIs on the [APIs.io](https://apis.io/) network: Articles API and Headlines API. Tagged areas include Articles, Digital Culture, Headlines, Media, and News.


  Mashable''s developer surface includes authentication, documentation, YouTube channel, GitHub presence, and 13 more developer resources.'
plans:
- name: Mashable Plans Pricing
  plan_count: 3
  slug: mashable-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Mashable Rate Limits
  slug: mashable-rate-limits
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mashable/refs/heads/main/screenshots/mashable-2026-06-20T185014.png
security:
- kind: authentication
  name: Mashable Authentication
  slug: mashable-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mashable Domain Security
  slug: mashable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mashable
tags:
- Articles
- Digital Culture
- Headlines
- Media
- News
- Technology News
website: https://mashable.com/
---
