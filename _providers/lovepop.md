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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.lovepop.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lovepop.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.lovepop.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.lovepop.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.lovepop.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lovepop.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lovepop.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lovepop-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lovepop-domain-security.yml
created: '2026-07-17'
description: Lovepop is a Boston-based consumer greeting-card and gifting company, founded in 2014 and known for its intricate laser-cut 3D pop-up cards inspired by Vietnamese "kirigami" paper engineering. The company sells directly to consumers through its Shopify-powered storefront at lovepop.com and through retail partners, offering pop-up greeting cards, gift boxes, flowers, and personalized gifting. Lovepop was accelerated by Techstars and appeared on ABC's Shark Tank. It is tracked in the API Evangelist network as a Techstars portfolio company; as of this pass Lovepop publishes no first-party developer API, SDKs, or developer portal, and its public digital surface is a standard Shopify commerce storefront (including Shopify Customer Account OIDC/OAuth well-known documents served on the domain).
image: https://www.lovepop.com/cdn/shop/files/lovepop-logo.png
layout: provider
modified: '2026-07-20'
name: Lovepop
nav: Providers
network: true
overview: 'Lovepop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Greeting Cards, Gifting, E-Commerce, and Retail.


  Lovepop''s developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lovepop/refs/heads/main/screenshots/lovepop-2026-08-07T171815.png
security:
- kind: domain-security
  name: Lovepop Domain Security
  slug: lovepop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lovepop
tags:
- Company
- Greeting Cards
- Gifting
- E-Commerce
- Retail
- Consumer Products
- Shopify
- Techstars
website: https://www.lovepop.com/
---
