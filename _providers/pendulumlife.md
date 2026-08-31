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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pendulumlife-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pendulumlife-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://pendulumlife.com
- group: company
  title: ''
  type: Blog
  url: https://pendulumlife.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://pendulumlife.com/pages/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://pendulumlife.com/products
- group: start
  title: ''
  type: SignUp
  url: https://pendulumlife.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pendulumlife.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pendulumlife.com/policies/privacy-policy
created: '2026-07-17'
description: 'Pendulum (pendulumlife.com) is a direct-to-consumer probiotics and metabolic-health company founded by PhD scientists from Johns Hopkins, Harvard, Berkeley and Stanford. It sells next-generation probiotic supplements such as Metabolic Daily, Akkermansia, Glucose Control (a medical probiotic clinically shown to improve A1C in type 2 diabetes) and Polyphenol Booster. Surfaced as a portfolio company of felicis and added to the API Evangelist network for enrichment. Enrichment finding: the site is a Shopify-hosted storefront and Pendulum publishes no first-party developer API, SDKs, or documentation; the only machine surface is Shopify''s platform customer-account OIDC discovery endpoint.'
image: https://pendulumlife.com/cdn/shop/files/Pendulum_Logo_Registered_Petal_8e91b0c1-3451-4839-871e-b0b2612e30f3.png?v=1621028826
layout: provider
modified: '2026-07-20'
name: Pendulumlife
nav: Providers
network: true
overview: 'Pendulumlife is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Probiotics, Consumer, and Supplements.


  Pendulumlife''s developer surface includes engineering blog, support, pricing, signup flow, and 5 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Pendulumlife Domain Security
  slug: pendulumlife-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pendulumlife
tags:
- Company
- Health
- Probiotics
- Consumer
- Supplements
- Metabolic Health
- E-Commerce
website: https://pendulumlife.com
---
