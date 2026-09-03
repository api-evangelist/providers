---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soldsie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soldsie.com
created: '2026-07-17'
description: 'Soldsie was a social-commerce platform founded in 2012 in San Francisco by Chris Bennett and Arrel Gray that let retailers sell directly through social media: customers bought products by commenting "Sold" on a merchant''s Facebook or Instagram post, while a backend dashboard handled invoicing, customer tracking, and waitlists. Backed by 500 Startups (now 500 Global) and e.ventures, it raised roughly $1M in seed funding and a $4M Series A (2014), and had processed over $25M in transactions across more than 1,000 merchants. The product is now defunct: the soldsie.com apex no longer resolves and www.soldsie.com returns a broken redirect, so there is no live developer portal, API, or documentation surface to enrich.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soldsie.png
layout: provider
modified: '2026-07-21'
name: Soldsie
nav: Providers
network: true
overview: Soldsie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Commerce, E-Commerce, Comment Selling, and Retail.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Soldsie Domain Security
  slug: soldsie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soldsie
tags:
- Company
- Social Commerce
- E-Commerce
- Comment Selling
- Retail
- Facebook
- Instagram
- Defunct
website: https://www.soldsie.com
---
