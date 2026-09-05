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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upequity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upequity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.upequity.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://www.upequity.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upequity.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upequity
- group: other
  title: ''
  type: Licensing
  url: https://www.upequity.com/licensing
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upequity-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/upequity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upequity-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: UpEquity is a HubSpot-hosted mortgage lender marketing site with no developer channel at all — /openapi.json, /swagger.json, /graphql and every /.well-known/ path return the HubSpot 404 page, and api./docs./developers./developer./app./portal.upequity.com do not resolve in DNS, so there was no host to probe beyond www.
  evidence:
  - status: 404
    url: https://www.upequity.com/openapi.json
  - status: 404
    url: https://www.upequity.com/.well-known/agent-card.json
  - status: 0
    url: https://api.upequity.com/
  - status: 200
    url: https://www.upequity.com/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'UpEquity is an Austin, Texas based, veteran-owned proptech mortgage lender and title company founded in 2019 that operates a "Buy Before You Sell" / Trade Up program for homeowners who are purchasing and selling at the same time. The company advances the equity trapped in a client''s existing home so the client can make a non-contingent — effectively all-cash — offer on a new home, move once, and sell the old home afterward, with UpEquity making a backup offer on the departing residence. It also runs UpEquity Title and originates mortgages directly under NMLS #2101265, licensed across roughly twenty US states. Distribution is through real-estate agents and loan officers rather than a developer channel: as of this profiling pass UpEquity publishes no developer portal, no API reference, and no machine-readable API contract of any kind on any host it controls.'
image: https://20424362.fs1.hubspotusercontent-na1.net/hubfs/20424362/UpEquity%20Brand%20Assets/UpEquityLogo-01.svg
layout: provider
modified: '2026-09-02'
name: UpEquity
nav: Providers
network: true
overview: 'UpEquity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Mortgage, Lending, and Financial Services.


  UpEquity''s developer surface includes support and 9 more developer resources.'
plans:
- name: Upequity Plans Pricing
  plan_count: 0
  slug: upequity-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Upequity Rate Limits
  slug: upequity-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Upequity Domain Security
  slug: upequity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: upequity
tags:
- Company
- Real Estate
- Mortgage
- Lending
- Financial Services
- Proptech
- Home Buying
- Title Insurance
- Fintech
website: https://www.upequity.com/
---
