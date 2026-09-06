---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.fbn.com
  baseurl_source: spec
  description: FBN Direct is the member-facing ecommerce marketplace offering 7,200+ crop protection, seed, fertilizer, livestock, and farm supply products at transparent pricing with direct-to-farm delivery. Delive
  name: FBN Direct Inputs Marketplace
  slug: fbn-direct-inputs-marketplace
- baseURL: https://www.fbn.com
  baseurl_source: spec
  description: 'FBN Insights and seed analytics deliver personalized benchmarking, seed performance analysis, and crowdsourced agronomic data from the network. Delivered as a member-facing product surface; no public '
  name: FBN Analytics and Insights
  slug: fbn-analytics
- baseURL: https://www.fbn.com
  baseurl_source: spec
  description: FBN Crop Marketing lets members review local bids, manage contracts, track scale tickets, and receive payments through a technology platform. Delivered as a member-facing product surface; no public de
  name: FBN Crop Marketing
  slug: fbn-crop-marketing
- baseURL: https://www.fbn.com
  baseurl_source: spec
  description: FBN Finance offers agricultural operating lines, equipment and land loans, refinancing, and crop insurance to member farms. Delivered as a member-facing product surface; no public developer API is doc
  name: FBN Finance
  slug: fbn-finance
- baseURL: https://www.fbn.com
  baseurl_source: spec
  description: 'Norm is FBN''s LLM-based AI agronomy advisor, answering members'' questions on seed selection, crop protection, pest and disease management, irrigation, fertilization, and rotation. Free for registered '
  name: Norm AI Advisor
  slug: norm-ai-advisor
- description: The fbn.com member application - account, farm, and field management plus access to agronomy insights, pricing transparency, and marketplace ordering. Member-only product, not a public API.
  name: FBN Member Platform
  slug: member-platform
- description: Precision-agronomy product that ingests planting, application, and harvest data from 60+ precision monitor types, normalizes it, and benchmarks performance across the FBN network. Surface is the FBN m
  name: FBN Analytics
  slug: analytics
- description: Direct-to-farmer e-commerce marketplace for crop inputs - seed, crop protection, adjuvants, and animal health - with transparent pricing and direct-to-farm delivery. Member-only ordering surface.
  name: FBN Direct Marketplace
  slug: marketplace
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Farmers Business Network API
  slug: open-farmers-business-network
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farmers-business-network-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/farmers-business-network
- group: company
  title: ''
  type: Website
  url: https://www.fbn.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.fbn.com/community/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/farmers-business-network-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/farmers-business-network-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/farmers-business-network-finops.yml
created: '2026-06-20'
description: Farmers Business Network (FBN) is a farmer-to-farmer ag-tech network serving 117,000+ member farms across the U.S. and Canada. Its membership platform pairs the FBN Direct inputs marketplace with seed and farm analytics, crop marketing, agricultural financing, and Norm, an AI agronomy advisor. FBN exposes these as member-facing web and mobile product surfaces; it does not publish a public or partner developer API.
finops:
- name: Farmers Business Network Finops
  service_category: Marketplace and Financial Services
  slug: farmers-business-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farmers-business-network.png
layout: provider
modified: '2026-06-20'
name: Farmers Business Network
nav: Providers
network: true
overview: 'Farmers Business Network publishes 5 APIs on the [APIs.io](https://apis.io/) network, including FBN Direct Inputs Marketplace, FBN Analytics and Insights, FBN Crop Marketing, and 2 more. Tagged areas include AgTech, Agriculture, Marketplace, Farm Analytics, and AI Advisor.


  Farmers Business Network''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Farmers Business Network Plans Pricing
  plan_count: 3
  slug: farmers-business-network-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Farmers Business Network Rate Limits
  slug: farmers-business-network-rate-limits
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Farmers Business Network Domain Security
  slug: farmers-business-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: farmers-business-network
tags:
- AgTech
- Agriculture
- Marketplace
- Farm Analytics
- AI Advisor
website: https://www.fbn.com
---
