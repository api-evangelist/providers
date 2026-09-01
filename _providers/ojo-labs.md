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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ojo-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ojo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ojo.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ojo.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ojolabs
- group: operate
  title: ''
  type: Support
  url: https://help.movoto.com/
- group: company
  title: ''
  type: Blog
  url: https://www.movoto.com/blog/
- group: build
  title: ''
  type: Packages
  url: packages/ojo-labs-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ojo-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ojo-labs-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ojo-labs-llms.txt
coverage:
  checked: '2026-08-26'
  detail: OJO Labs ships only end-user products — ojo.com's own sitemap lists 31 URLs and not one is a developer, API or docs page, developer.ojo.com/docs.ojo.com/api.ojo.com do not resolve, and the only programmatic surface on any company host is Movoto's internal XHR /api/ path, which www.movoto.com/robots.txt disallows for every user agent.
  evidence:
  - status: 200
    url: https://ojo.com/sitemap.xml
  - status: 200
    url: https://ojo.com/openapi.json
  - status: 200
    url: https://www.movoto.com/robots.txt
  - status: 404
    url: https://www.movoto.com/.well-known/security.txt
  - status: 404
    url: https://www.movoto.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'OJO Labs is an Austin, Texas real estate technology company founded in 2015 that operates Movoto, one of the largest consumer real estate search portals in the United States, alongside OJO''s homeownership platform for buyers, sellers and existing homeowners. The company pairs AI-driven property search and home-value tracking with human real estate advisors, and monetizes primarily through an agent referral network that routes qualified consumers to licensed brokerages. OJO acquired Movoto in 2020 and The LEAD Syndicate in 2024, launching Lever by Movoto as its industry-facing agent platform, and was itself acquired by Columbus, Ohio mortgage lender Lower in May 2025. OJO Labs is an end-user product company: it publishes no public developer program, API reference, SDK or machine-readable API contract, and its lead delivery to agent CRMs is handled through email parsing and third-party middleware rather than a documented partner API.'
image: https://ojo.com/static/media/ojo-logo.c15e6d9a.svg
layout: provider
modified: '2026-08-26'
name: OJO Labs
nav: Providers
network: true
overview: 'OJO Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, PropTech, Home Search, and Mortgage.


  OJO Labs'' developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Ojo Labs Plans Pricing
  plan_count: 0
  slug: ojo-labs-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Ojo Labs Rate Limits
  slug: ojo-labs-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Ojo Labs Domain Security
  slug: ojo-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ojo-labs
tags:
- Company
- Real-Estate
- PropTech
- Home Search
- Mortgage
- Marketplace
- Lead Generation
- Consumer
website: https://ojo.com/
---
