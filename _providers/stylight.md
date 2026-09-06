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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stylight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.stylight.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stylight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stylight.com/
- group: company
  title: ''
  type: About
  url: https://www.stylight.com/about/
- group: company
  title: ''
  type: Blog
  url: https://blog.stylight.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.stylight.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.stylight.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.stylight.com/legal-notice
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/stylight-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stylight-well-known.yml
created: '2026-07-17'
description: Stylight is an online fashion and home-decor shopping aggregator that curates and compares products from more than 100 retailers, letting shoppers browse women's and men's apparel, footwear, accessories, beauty and home furnishings across many brands in one place and then complete the purchase on the partner retailer's own store. The platform operates localized sites across the US, UK, Germany, Austria, Switzerland, France, Italy, Spain, Belgium, the Netherlands and Canada, runs an editorial style magazine, and monetizes through affiliate partnerships with the retailers it links to. HV Capital was an early backer. Stylight publishes no public developer API; this profile captures its public web, legal and security surface for the API Evangelist network.
image: https://images.cdn.inspogroup.net/MG2P4BqftCeq2sQBik9HlhsUObdvtHT_QrY7U9wFoEY/czM6L/y9zdG/F0aWMuc3R5bGlnaHQuZGUvZnJvbnRlbmQvZGlzdC92YzM2MTE5L2ltYWdlcy9jb20vb2ctaW1hZ2Utc3RhbmRhcmQudmMzNjExOS5wbmc
layout: provider
modified: '2026-07-21'
name: Stylight
nav: Providers
network: true
overview: 'Stylight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fashion, E-Commerce, and Shopping.


  Stylight''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stylight/refs/heads/main/screenshots/stylight-2026-09-02T161051.png
security:
- kind: domain-security
  name: Stylight Domain Security
  slug: stylight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stylight Vulnerability Disclosure
  slug: stylight-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stylight
tags:
- Company
- Consumer
- Fashion
- E-Commerce
- Shopping
- Retail
- Aggregator
- Affiliates
website: https://www.stylight.com/
---
