---
access_model:
  confidence: high
  label: No public API program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - researched
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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.hallmark.com
- group: company
  title: ''
  type: About
  url: https://corporate.hallmark.com/
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.hallmark.com/hallmark-news/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://corporate.hallmark.com/feed/
- group: company
  title: ''
  type: Blog
  url: https://ideas.hallmark.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://ideas.hallmark.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://care.hallmark.com/s/
- group: company
  title: ''
  type: Careers
  url: https://careers.hallmark.com/
- group: company
  title: ''
  type: Partners
  url: https://corporate.hallmark.com/business-opportunities/
- group: other
  title: ''
  type: X-Suppliers
  url: https://corporate.hallmark.com/citizenship/hallmark-community/supplier-partnerships/
- group: other
  title: ''
  type: X-BusinessSolutions
  url: https://www.hallmarkbusiness.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hallmark.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hallmark.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hallmark-cards
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hallmark-cards/refs/heads/main/security/hallmark-cards-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hallmark-cards-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hallmark-cards/refs/heads/main/well-known/hallmark-cards-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/hallmark-cards-well-known.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hallmark-cards/refs/heads/main/plans/hallmark-cards-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hallmark-cards-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hallmark-cards/refs/heads/main/rate-limits/hallmark-cards-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hallmark-cards-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hallmark-cards/refs/heads/main/finops/hallmark-cards-finops.yml
  title: ''
  type: FinOps
  url: finops/hallmark-cards-finops.yml
coverage:
  checked: '2026-09-17'
  detail: Hallmark sells physical greeting cards, gifts and ornaments plus television media; developer.hallmark.com does not resolve and api.hallmark.com is a stock ASP.NET template whose only link (/Help) 404s, with no spec, discovery document, agent card or llms.txt on any of five Hallmark hosts.
  evidence:
  - status: 0
    url: https://developer.hallmark.com/docs
  - status: 404
    url: https://api.hallmark.com/Help
  - status: 404
    url: https://api.hallmark.com/openapi.json
  - status: 404
    url: https://www.hallmark.com/.well-known/api-catalog
  - status: 404
    url: https://www.hallmark.com/llms.txt
  - status: 404
    url: https://www.hallmarkbusiness.com/developers/
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Hallmark Cards, Inc. is a privately held, family-owned greeting card, gift, gift wrap and ornament company headquartered in Kansas City, Missouri, founded in 1910 by J.C. Hall. Its portfolio spans Hallmark greeting cards and Keepsake Ornaments sold through Hallmark Gold Crown stores and mass retailers, the Crayola and Hallmark Business Connections (B2B greeting card programs) subsidiaries, and Hallmark Media (Hallmark Channel, Hallmark+). Hallmark publishes no public developer program: developer.hallmark.com does not resolve, api.hallmark.com serves a stock ASP.NET template with no documented endpoints, and no OpenAPI, GraphQL, MCP, A2A agent card, llms.txt or /.well-known discovery document was found on any Hallmark host on 2026-09-17. Retail and supply-chain partners integrate through bilateral EDI (Hallmark Global Services) and Hallmark Business Connections'' CRM/SSO integrations, none of which are documented publicly.'
finops:
- name: Hallmark Cards Finops
  service_category: Retail / Consumer Goods Partner API
  slug: hallmark-cards-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hallmark-cards.png
layout: provider
modified: '2026-09-17'
name: Hallmark Cards
nav: Providers
network: true
overview: 'Hallmark Cards is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Greeting Cards, Gifts, Retail, Consumer Goods, and Stationery.


  Hallmark Cards'' developer surface includes engineering blog, support, and 17 more developer resources.'
plans:
- name: Hallmark Cards Plans Pricing
  plan_count: 0
  slug: hallmark-cards-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Hallmark Cards Rate Limits
  slug: hallmark-cards-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hallmark-cards/refs/heads/main/screenshots/hallmark-cards-2026-06-20T182502.png
security:
- kind: domain-security
  name: Hallmark Cards Domain Security
  slug: hallmark-cards-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hallmark-cards
tags:
- Greeting Cards
- Gifts
- Retail
- Consumer Goods
- Stationery
- Gift Wrap
- Media
- Business Greetings
- Fortune 1000
website: https://www.hallmark.com
---
