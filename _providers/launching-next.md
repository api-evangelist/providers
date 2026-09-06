---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
api_count: 1
apis:
- description: Launching Next provides an RSS feed for the latest startup listings published on the platform. The feed allows developers, aggregators, and readers to programmatically consume new startup entries as t
  name: Launching Next RSS Feed
  slug: rss-feed
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/launching-next-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.launchingnext.com/
- group: start
  title: ''
  type: Portal
  url: https://www.launchingnext.com/submit/
- group: other
  title: ''
  type: RSSFeed
  url: https://www.launchingnext.com/feed/
- group: other
  title: ''
  type: X
  url: https://x.com/LaunchingNext
created: '2026-03-24'
description: Launching Next is a startup discovery and submission platform that publishes daily listings of new and trending tech startups and side projects worldwide. Founded as a long-running startup directory, the platform has featured over 45,000 startups and side projects, making it a go-to resource for founders, investors, and early adopters looking to discover what is being built next. Entrepreneurs can submit their startups for free, with an optional paid fast-track review.
finops:
- name: Launching Next Finops
  service_category: API
  slug: launching-next-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/launching-next.png
layout: provider
modified: '2026-04-28'
name: Launching Next
nav: Providers
network: true
overview: 'Launching Next publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Discovery, Product Launch, and Startups.


  Launching Next''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: Launching Next Plans Pricing
  plan_count: 3
  slug: launching-next-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Launching Next Rate Limits
  slug: launching-next-rate-limits
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/launching-next/refs/heads/main/screenshots/launching-next-2026-06-20T184328.png
security:
- kind: domain-security
  name: Launching Next Domain Security
  slug: launching-next-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: launching-next
tags:
- Discovery
- Product Launch
- Startups
website: https://www.launchingnext.com/
---
