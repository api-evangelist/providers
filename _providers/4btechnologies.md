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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4btechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://businessleadsworld.com/
- group: company
  title: ''
  type: About
  url: https://businessleadsworld.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://businessleadsworld.com/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://businessleadsworld.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://businessleadsworld.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://businessleadsworld.com/register/
- group: start
  title: ''
  type: Login
  url: https://businessleadsworld.com/login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://businessleadsworld.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://businessleadsworld.com/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/businessleadsworld
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4btechnologies-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/4btechnologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4btechnologies-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: 'Business Leads World sells MCA and business-loan lead lists, not software: businessleadsworld.com is a React single-page storefront whose only HTTP backend is an undocumented private endpoint at https://api.expertdesignhub.com/blw (its web agency''s shared host, Bearer token from browser localStorage), and neither the site, its 35-URL sitemap nor its own hand-written llms.txt names an API, a developer portal or a reference of any kind.'
  evidence:
  - status: 200
    url: https://businessleadsworld.com/llms.txt
  - status: 200
    url: https://businessleadsworld.com/sitemap.xml
  - status: 200
    url: https://businessleadsworld.com/openapi.json
  - status: 200
    url: https://businessleadsworld.com/.well-known/agent-card.json
  - status: 404
    url: https://api.expertdesignhub.com/blw/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: Business Leads World is a US lead-generation and B2B data company serving the alternative business-finance market. Operating since 2016 from Queens, New York, it supplies merchant cash advance (MCA) and business loan leads to lenders, ISOs, funding companies and loan brokers — MCA live-transfer calls, call-back leads, aged MCA leads, business loan leads, digital marketing leads and B2B email data. Leads are sourced through SEO, PPC and email marketing and pre-qualified against published criteria (credit score above 550, no bankruptcies, at least one year in business, and monthly bank deposits above $15,000). The company sells lead lists through a self-service storefront on its own website; it publishes no public developer program, API reference or machine-readable API contract.
layout: provider
modified: '2026-09-05'
name: Business Leads World
nav: Providers
network: true
overview: 'Business Leads World is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lead Generation, Merchant Cash Advance, Business Lending, and B2B Data.


  Business Leads World''s developer surface includes engineering blog, pricing, support, signup flow, and 10 more developer resources.'
plans:
- name: 4Btechnologies Plans Pricing
  plan_count: 0
  slug: 4btechnologies-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: 4Btechnologies Rate Limits
  slug: 4btechnologies-rate-limits
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4Btechnologies Domain Security
  slug: 4btechnologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 4btechnologies
tags:
- Company
- Lead Generation
- Merchant Cash Advance
- Business Lending
- B2B Data
- Marketing
- Financial Services
website: https://businessleadsworld.com/
---
