---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carson-life/refs/heads/main/llms/carson-life-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carson-life-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carson-life/refs/heads/main/well-known/carson-life-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carson-life-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carson-life/refs/heads/main/hosts/carson-life-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carson-life-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carson-life/refs/heads/main/vendors/carson-life-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carson-life-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://en.carsonlife.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carson-life/refs/heads/main/security/carson-life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carson-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.carsonlife.com/
- group: company
  title: ''
  type: Blog
  url: https://en.carsonlife.com/blogs/news
- group: company
  title: ''
  type: About
  url: https://en.carsonlife.com/pages/about-carson-life
- group: operate
  title: ''
  type: Contact
  url: https://en.carsonlife.com/pages/contactanos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.carsonlife.com/pages/carson-life-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.carsonlife.com/pages/carson-life-privacy-policy
coverage:
  checked: '2026-10-07'
  detail: Carson Life provides only an e‑commerce storefront with no public developer API.
  evidence:
  - status: 200
    url: https://en.carsonlife.com/search?q=api
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carson Life is a health and beauty e‑commerce brand offering natural skin‑care, weight‑loss, vitamin and hair‑care products. Based in the United States, the company emphasizes cruelty‑free, eco‑friendly ingredients and provides a range of bundles and individual items through its online store. The site includes a blog, store locator, and customer support resources, reflecting a consumer‑focused approach to self‑care.
image: https://cdn.shopify.com/s/files/1/0934/8056/files/logo300.png?height=628&pad_color=fff&v=1613582400&width=1200
layout: provider
modified: '2026-10-07'
name: Carson Life
nav: Providers
network: true
overview: 'Carson Life is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Beauty, E-Commerce, Skincare, and Weight‑loss.


  Carson Life''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carson Life Domain Security
  slug: carson-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carson-life
tags:
- Health
- Beauty
- E-Commerce
- Skincare
- Weight‑loss
- Vitamins
website: https://en.carsonlife.com/
---
