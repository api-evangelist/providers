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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.evaneos.com/
- group: operate
  title: ''
  type: Support
  url: https://www.evaneos.com/about-us/contact/
- group: start
  title: ''
  type: Login
  url: https://www.evaneos.com/login
- group: company
  title: ''
  type: Blog
  url: https://tech.evaneos.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evaneos.com/evaneos/general-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evaneos.com/evaneos/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evaneos
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/evaneos-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evaneos-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/evaneos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.evaneos.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evaneos-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evaneos-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/evaneos-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/evaneos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evaneos-rate-limits.yml
coverage:
  checked: '2026-08-17'
  detail: The only API Evaneos markets is a partner/affiliate product-feed API offered on request via partner.evaneos.net ("we can provide an API with multiple product feed options"), with no reference, no spec and no developer portal — developer.evaneos.com and docs.evaneos.com do not resolve, and www.evaneos.com/openapi.json returns 404.
  evidence:
  - status: 403
    url: https://partner.evaneos.net/marketing-partnerships/
  - status: 404
    url: https://www.evaneos.com/openapi.json
  - status: 200
    url: https://www.evaneos.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Evaneos is a French online marketplace for tailor-made travel, founded in 2009 and headquartered in Paris. It connects travelers directly with a curated, continuously-evaluated network of 600+ expert local travel agencies across 160+ destinations, who design fully customized itineraries. A certified B Corp since 2022, Evaneos champions an ethical model in which at least 85% of each trip's cost benefits local economies, and it has served more than 800,000 travelers at a 97% satisfaction rate. Backed by Partech, the company runs a coordinated vulnerability disclosure program but publishes no public product API — the only API it markets is a partner/affiliate product-feed API offered on request through partner.evaneos.net — while publishing a real llms.txt for AI agents; its GitHub organization hosts internal DevOps, security, and AI tooling.
image: https://images.prismic.io/evaneos/ad9Xa51ZCF7ETNBk_spenser-sembrat-zpMLd4VXlGk-unsplash-2.jpg?auto=format,compress&rect=0,425,6000,3150&w=1200&h=630
layout: provider
modified: '2026-08-17'
name: Evaneos
nav: Providers
network: true
overview: 'Evaneos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Travel, Tourism, and Tailor-Made Trips.


  Evaneos'' developer surface includes support, engineering blog, and 14 more developer resources.'
plans:
- name: Evaneos Plans Pricing
  plan_count: 0
  slug: evaneos-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Evaneos Rate Limits
  slug: evaneos-rate-limits
score:
  band: emerging
  composite: 14.4
  delta: -0.8
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 15.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evaneos/refs/heads/main/screenshots/evaneos-2026-07-25T213708.png
security:
- kind: domain-security
  name: Evaneos Domain Security
  slug: evaneos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Evaneos Vulnerability Disclosure
  slug: evaneos-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: evaneos
tags:
- Company
- Marketplace
- Travel
- Tourism
- Tailor-Made Trips
- Local Agencies
- Sustainable Travel
- B Corp
- France
website: https://www.evaneos.com/
---
