---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.pharmacann.com/
- group: company
  title: ''
  type: About
  url: https://www.pharmacann.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.pharmacann.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.pharmacann.com/news?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.pharmacann.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pharmacann.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pharmacann.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pharmacann
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pharmacann-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pharmacann-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: PharmaCann is a vertically integrated cannabis cultivator, processor and dispensary operator whose entire public web presence is a Squarespace marketing brochure — the sitemap lists 68 URLs, all news, brands, careers, store locator and legal pages, with no developer, API or docs section — and neither api.pharmacann.com nor developer.pharmacann.com resolves in DNS.
  evidence:
  - status: 200
    url: https://www.pharmacann.com/sitemap.xml
  - status: 404
    url: https://www.pharmacann.com/openapi.json
  - status: 404
    url: https://www.pharmacann.com/api-docs
  - status: 404
    url: https://www.pharmacann.com/.well-known/agent-card.json
  - status: 0
    url: https://api.pharmacann.com/
  - status: 0
    url: https://developer.pharmacann.com/
  - status: 404
    url: https://www.verilife.com/openapi.json
  - status: 404
    url: https://www.livwell.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: PharmaCann is one of the largest vertically integrated cannabis companies in the United States, founded in 2014 and operating cultivation centers, processing facilities and retail dispensaries across eight states — Colorado, Illinois, Maryland, Massachusetts, Michigan, New York, Ohio and Pennsylvania. The company runs nine cultivation and processing facilities (Denver CO, Dwight IL, Lothian and Stevensville MD, Holliston MA, Warren MI, Hamptonburgh NY, Buckeye Lake OH and Olyphant PA) and sells through two retail banners, LivWell (Colorado and Michigan) and Verilife (Illinois, Maryland, Massachusetts, Michigan, New York, Ohio and Pennsylvania), alongside a house of product brands including Matter, Magnitude, Full Melt, CAM, P3, LivWell Flower, Hash and PC Nursery. PharmaCann is a physical-goods operator in a federally restricted, state-regulated industry; it publishes no developer program, no public API and no machine-readable API contract.
image: http://static1.squarespace.com/static/60736ce59afd9c3ea39b0d41/t/60a329cd64e66350b0f99fa1/1621305805736/PharmaCann+Social+Logo.png?format=1500w
layout: provider
modified: '2026-08-26'
name: PharmaCann
nav: Providers
network: true
overview: 'PharmaCann is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cannabis, Retail, Agriculture, and Consumer Goods.


  PharmaCann''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Pharmacann Plans Pricing
  plan_count: 0
  slug: pharmacann-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Pharmacann Rate Limits
  slug: pharmacann-rate-limits
score:
  band: minimal
  composite: 10.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Pharmacann Domain Security
  slug: pharmacann-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pharmacann
tags:
- Company
- Cannabis
- Retail
- Agriculture
- Consumer Goods
- Manufacturing
- Health
- Dispensary
website: https://www.pharmacann.com/
---
