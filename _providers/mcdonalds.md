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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: McDonald's does not expose a public, self-service API. Ordering, delivery integration, menu data, loyalty, and restaurant information flow through bilateral partner integrations rather than open devel
  name: McDonald's API
  slug: mcdonalds-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcdonalds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mcdonalds.com
- group: other
  title: ''
  type: Corporate
  url: https://corporate.mcdonalds.com
- group: company
  title: ''
  type: Blog
  url: https://medium.com/mcdonalds-technical-blog
- group: commercial
  title: ''
  type: Plans
  url: plans/mcdonalds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mcdonalds-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mcdonalds-finops.yml
created: '2026-03-21'
description: McDonald's is the world's leading global foodservice retailer, operating and franchising fast food restaurants serving hamburgers, chicken, breakfast items, soft drinks, milkshakes, and desserts in countries around the world. McDonald's does not operate a public developer program or publish open API documentation. Its digital surface — the Global Mobile App, MyMcDonald's Rewards loyalty, mobile order & pay, kiosks, and drive-thru personalization — runs on internal platforms, and integrations with delivery marketplaces (DoorDash, Uber Eats, Grubhub) and technology partners (Google Cloud, Dynamic Yield) are bilateral and gated to approved partners and franchisees.
finops:
- name: Mcdonalds Finops
  service_category: Restaurant / Marketplace Integration
  slug: mcdonalds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mcdonalds.png
layout: provider
modified: '2026-06-02'
name: McDonald's
nav: Providers
network: true
overview: 'McDonald''s publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Delivery, Fast Food, Loyalty, Mobile Ordering, and Ordering.


  McDonald''s'' developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Mcdonalds Plans Pricing
  plan_count: 1
  slug: mcdonalds-plans-pricing
press:
- date: '2026-05-25'
  title: 'Where Innovation Meets Scale: An Update on McDonald''s ...'
  url: https://corporate.mcdonalds.com/corpmcd/our-stories/article/digitizing-the-arches.html
- date: '2026-05-25'
  title: Dec 6, 2023
  url: https://www.googlecloudpresscorner.com/2023-12-06-McDonalds-and-Google-Cloud-Announce-Strategic-Partnership-to-Connect-Latest-Cloud-Technology-and-Apply-Generative-AI-Solutions-Across-its-Restaurants-Worldwide
- date: '2026-05-25'
  title: McDonald's Gives Its Restaurants an AI Makeover
  url: https://www.wsj.com/articles/mcdonalds-gives-its-restaurants-an-ai-makeover-2134f01e
- date: '2026-05-25'
  title: Optimising McDonald's global AI Strategy
  url: https://expleo.com/global/en/case-studies/optimising-mcdonalds-global-ai-strategy/
- date: '2026-05-25'
  title: McDonald's is experimenting with AI in ways that could ...
  url: https://www.facebook.com/masslive/posts/mcdonalds-is-experimenting-with-ai-in-ways-that-could-change-your-drive-thru-exp/1330329255807686/
random_paper: 4
rate_limits:
- limit_count: 1
  name: Mcdonalds Rate Limits
  slug: mcdonalds-rate-limits
score:
  band: minimal
  composite: 9.7
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mcdonalds/refs/heads/main/screenshots/mcdonalds-2026-06-20T185057.png
security:
- kind: domain-security
  name: Mcdonalds Domain Security
  slug: mcdonalds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcdonalds
tags:
- Delivery
- Fast Food
- Loyalty
- Mobile Ordering
- Ordering
- Restaurant
- Fortune 500
website: https://www.mcdonalds.com
---
