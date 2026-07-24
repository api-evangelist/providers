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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: The fbn.com member application - account, farm, and field management plus access to agronomy insights, pricing transparency, and marketplace ordering. Member-only product, not a public API.
  name: FBN Member Platform
  slug: member-platform
- description: Precision-agronomy product that ingests planting, application, and harvest data from 60+ precision monitor types, normalizes it, and benchmarks performance across the FBN network. Surface is the FBN m
  name: FBN Analytics
  slug: analytics
- description: Direct-to-farmer e-commerce marketplace for crop inputs - seed, crop protection, adjuvants, and animal health - with transparent pricing and direct-to-farm delivery. Member-only ordering surface.
  name: FBN Direct Marketplace
  slug: marketplace
- description: Farm operating loans, equipment financing, and crop insurance issued through FBN's lending and insurance affiliates.
  name: FBN Finance
  slug: finance
- description: FBN's sustainability and Scope-3 program. Captures field-level practice data from growers, computes outcomes, and sells the verified sustainable bushels and emissions data to grain buyers and consumer
  name: Gradable (Sustainability / Scope 3)
  slug: gradable
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fbn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fbn.com/
- group: operate
  title: ''
  type: FAQ
  url: https://www.fbn.com/community/faq
- group: company
  title: ''
  type: News
  url: https://www.fbn.com/community
- group: operate
  title: ''
  type: Contact
  url: https://www.fbn.com/contact
created: '2026-05-23'
description: Farmers Business Network (FBN) is a direct-to-farmer ag platform combining a member network, e-commerce for crop inputs (seed, chemistry, animal health), agronomy and precision analytics, financing and crop insurance, and a sustainability / Scope-3 program (Gradable). FBN Analytics ingests precision data from 60+ monitor types and integrates with John Deere Operations Center and CNH AFS Connect to pull machine, planting, application, and harvest data into the FBN platform. FBN is a Field to Market Qualified Data Management Partner via the Fieldprint API. FBN does not publish a public developer portal; partner integrations are arranged directly.
finops:
- name: Fbn Finops
  service_category: API
  slug: fbn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fbn.png
layout: provider
modified: '2026-05-23'
name: Farmers Business Network
nav: Providers
network: true
overview: 'Farmers Business Network publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Marketplace, Precision Ag, and Farm Finance.


  Farmers Business Network''s developer surface includes FAQ, product news, and 3 more developer resources.'
plans:
- name: Fbn Plans Pricing
  plan_count: 1
  slug: fbn-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Fbn Rate Limits
  slug: fbn-rate-limits
score:
  band: emerging
  composite: 18.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Fbn Domain Security
  slug: fbn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fbn
tags:
- Agriculture
- AgTech
- Marketplace
- Precision Ag
- Farm Finance
- Sustainability
- Scope 3
website: https://www.fbn.com/
---
