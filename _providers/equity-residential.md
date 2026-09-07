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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equity-residential-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equity-residential
- group: company
  title: ''
  type: Website
  url: https://www.equityapartments.com
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.equityapartments.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/equityresidential
- group: company
  title: ''
  type: Blog
  url: https://blog.equityapartments.com/
- group: start
  title: ''
  type: Login
  url: https://login.equityapartments.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.equityapartments.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.equityapartments.com/terms
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/equity-residential-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/equity-residential-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/equity-residential-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: 'Equity Residential is an apartment REIT with no developer program of any kind: six hosts were probed for the full /.well-known/ discovery set plus /apis.json, /apis.yml and /openapi.json and not one document was served, the first-party GitHub organization has zero public repositories, and the only api.* host in the namespace (api.eqr.com) is an undocumented F5 BIG-IP gateway that rejects every unauthenticated request.'
  evidence:
  - status: 403
    url: https://api.eqr.com/openapi.json
  - status: 404
    url: https://login.equityapartments.com/.well-known/openid-configuration
  - status: 302
    url: https://www.equityapartments.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/orgs/equityresidential/repos
  - status: 200
    url: https://www.equityapartments.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: 'Equity Residential (NYSE: EQR) is an S&P 500 company and one of the largest publicly traded apartment real estate investment trusts (REITs) in the United States. The company owns and operates high-quality apartment communities in affluent, dynamic urban and high-density suburban markets where today''s renters want to live, work, and play.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equity-residential.png
layout: provider
modified: '2026-09-06'
name: Equity Residential
nav: Providers
network: true
overview: 'Equity Residential is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Apartments, Fortune 500, Housing, Multifamily, and Property-Management.


  Equity Residential''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Equity Residential Plans Pricing
  plan_count: 0
  slug: equity-residential-plans-pricing
press:
- date: '2026-05-25'
  title: Equity Residential saw AI, automation bump in 2025
  url: https://www.multifamilydive.com/news/equity-residential-2025-earnings-q4/811880/
- date: '2026-05-25'
  title: Big apartment landlords lean in to AI and proptechs as ...
  url: https://funnelleasing.com/businessinsider_ai_proptech_adds_business_flexibility/
- date: '2026-05-25'
  title: 'AI in Residential Real Estate: Efficiency Gains and Equity ...'
  url: https://papers.ssrn.com/sol3/Delivery.cfm/6784680.pdf?abstractid=6784680&mirid=1
- date: '2026-05-25'
  title: Dirk Wakeham's Post
  url: https://www.linkedin.com/posts/dirkwakeham_avalonbay-communities-and-equity-residential-activity-7463285335716704256-Sf7l
- date: '2026-05-25'
  title: eqr-def14a_20200625.htm
  url: https://www.sec.gov/Archives/edgar/data/906107/000156459020017733/eqr-def14a_20200625.htm
random_paper: 0
rate_limits:
- limit_count: 0
  name: Equity Residential Rate Limits
  slug: equity-residential-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 4.1
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/equity-residential/refs/heads/main/screenshots/equity-residential-2026-06-20T180807.png
security:
- kind: domain-security
  name: Equity Residential Domain Security
  slug: equity-residential-domain-security
  summary_line: TLSv1.3 · DMARC
slug: equity-residential
tags:
- Apartments
- Fortune 500
- Housing
- Multifamily
- Property-Management
- Real-Estate
- REIT
website: https://www.equityapartments.com
---
