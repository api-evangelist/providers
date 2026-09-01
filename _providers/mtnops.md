---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://mtnops.com
- group: operate
  title: ''
  type: Support
  url: https://mtnops.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://mtnops.com/account/register
- group: start
  title: ''
  type: Login
  url: https://mtnops.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mtnops.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mtnops.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mtnops-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mtnops-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mtnops-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mtnops-domain-security.yml
created: '2026-07-17'
description: MTN OPS is an American-owned outdoor performance nutrition and lifestyle brand founded in 2014 and headquartered in Fruit Heights, Utah. The company develops, manufactures, and sells energy and nutrition supplements (pre-workout, protein, hydration, creatine, and energy bars) alongside apparel and gear for hunters, tactical professionals, military, and outdoor athletes, running a "Conquer Hunger" program that donates one meal for every order placed. MTN OPS is a direct-to-consumer, internet-first retailer operating on the Shopify platform and is backed by Norwest Venture Partners. It publishes no bespoke developer API; the only machine-readable surfaces on its domain are the Shopify New Customer Accounts OIDC discovery documents and a Shopify-generated agent-commerce llms.txt. This profile was surfaced as a Norwest portfolio lead and enriched from the provider's live public surface.
image: https://mtnops.com/cdn/shop/files/Stretch_Logo_-_Grey-Orange_881ebcf3-f902-459c-ad2e-a8d5d95c3632.svg?v=1704300859
layout: provider
modified: '2026-07-20'
name: MTN OPS
nav: Providers
network: true
overview: 'MTN OPS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Consumer Products, and Nutrition.


  MTN OPS''s developer surface includes support, signup flow, authentication, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mtnops/refs/heads/main/screenshots/mtnops-2026-08-07T184431.png
security:
- kind: authentication
  name: Mtnops Authentication
  slug: mtnops-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mtnops Domain Security
  slug: mtnops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mtnops
tags:
- Company
- E-Commerce
- Retail
- Consumer Products
- Nutrition
- Supplements
- Outdoor
- Shopify
website: https://mtnops.com
---
