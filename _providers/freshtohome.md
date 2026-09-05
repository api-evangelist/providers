---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshtohome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.freshtohome.com/
- group: company
  title: ''
  type: Blog
  url: https://www.freshtohome.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.freshtohome.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.freshtohome.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.freshtohome.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.freshtohome.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freshtohome-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/freshtohome-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freshtohome-rate-limits.yml
coverage:
  checked: '2026-08-16'
  detail: 'FreshToHome is a direct-to-consumer food e-commerce business, not a software vendor, and it markets no API: there is no developer host (developers., docs., apis. all NXDOMAIN), no developer link anywhere in the site navigation or footer, no GitHub organization, and no client library on npm, PyPI, RubyGems, crates.io or Packagist. The one API host that does resolve, api.freshtohome.com, is the private backend for its own consumer web and mobile apps — it answers every path, including every /.well-known/ path and every OpenAPI/Swagger/GraphQL location, with HTTP 400 {"success":"error","message":"No token provided."}, and no public reference for it is published anywhere. The single machine-readable document the company does serve is a genuine hand-authored llms.txt at the web root, captured verbatim in llms/, and it describes seven product categories and the support and legal pages — it names no API.'
  evidence:
  - status: 200
    url: https://www.freshtohome.com/llms.txt
  - status: 400
    url: https://api.freshtohome.com/openapi.json
  - status: 404
    url: https://www.freshtohome.com/openapi.json
  - status: 404
    url: https://www.freshtohome.com/graphql
  - status: 404
    url: https://www.freshtohome.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/freshtohome
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: FreshToHome (Freshtohome Foods Private Limited) is a Bangalore-headquartered direct-to-consumer e-commerce company selling fresh, antibiotic-residue-free fish, seafood, poultry, mutton, ready-to-cook and heat-and-eat food. Founded in 2015 by Shan Kadavil, Mathew Joseph and Jayesh Jose, it runs its own farm-and-boat-to-doorstep cold chain, sourcing from thousands of fishermen and farmers and delivering across cities in India and the United Arab Emirates. The company sells through its website and its consumer iOS and Android apps. It publishes an llms.txt at its web root but operates no public developer program, API reference, or machine-readable API contract.
image: https://static.freshtohome.com/images/logo/2021/logo-medium.png
layout: provider
modified: '2026-08-16'
name: FreshToHome
nav: Providers
network: true
overview: 'FreshToHome is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Food and Beverage, Grocery, and Retail.


  FreshToHome''s developer surface includes engineering blog, support, FAQ, and 7 more developer resources.'
plans:
- name: Freshtohome Plans Pricing
  plan_count: 0
  slug: freshtohome-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Freshtohome Rate Limits
  slug: freshtohome-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshtohome/refs/heads/main/screenshots/freshtohome-2026-09-02T145540.png
security:
- kind: domain-security
  name: Freshtohome Domain Security
  slug: freshtohome-domain-security
  summary_line: TLSv1.3 · DMARC
slug: freshtohome
tags:
- Company
- E-Commerce
- Food and Beverage
- Grocery
- Retail
- Direct to Consumer
- Supply Chain
- Delivery
- India
- United Arab Emirates
website: https://www.freshtohome.com/
---
