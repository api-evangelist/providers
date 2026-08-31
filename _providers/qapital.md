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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.qapital.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qapital.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.qapital.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qapital
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qapital.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.qapital.com/download/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qapital.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qapital.com/terms/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.qapital.com/security/
- group: commercial
  title: ''
  type: Plans
  url: plans/qapital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qapital-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qapital-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qapital-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qapital-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/qapital-conformance.yml
coverage:
  checked: '2026-08-26'
  detail: 'Qapital ships only an end-user mobile membership app: developer.qapital.com and docs.qapital.com do not resolve at all, its sitemap lists no developer, docs or API page, and its own api.qapital.com host answers every anonymous request — /openapi.json, /swagger.json, /graphql, /docs and every /.well-known/ path — with HTTP 503 Service Unavailable, because it is the private backend for the iOS and Android apps rather than a published product.'
  evidence:
  - status: 503
    url: https://api.qapital.com/openapi.json
  - status: 404
    url: https://www.qapital.com/openapi.json
  - status: 0
    url: https://developer.qapital.com/
  - status: 404
    url: https://www.qapital.com/.well-known/agent-card.json
  - status: 200
    url: https://ifttt.com/qapital
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Qapital is a consumer personal-finance company founded in 2013 — "born in Stockholm, raised in New York City" — that packages saving, spending, investing and budgeting into a single mobile membership app built on behavioral-economics research. Its Rules engine automates transfers into user-defined Goals (round-ups, guilty pleasure, payday divvy, freelancer tax set-aside and activity-triggered saves), a Dream Team feature lets two people save collaboratively, Qapital Invest offers risk-weighted portfolios through SEC-registered advisory and brokerage partners, and a Qapital Visa debit card and Spending account run on FDIC-member partner banking. The company reports 3.5m+ app downloads and roughly $3B collectively saved by members. Qapital sells a subscription — Basic, Complete and Premier tiers — rather than a developer product: it publishes no developer portal, no API reference and no machine-readable contract of any kind. The only public automation surface it offers is a Qapital
  service on IFTTT (four triggers, three queries, one action), and its own api.qapital.com host answers anonymous requests with HTTP 503.'
image: https://www.qapital.com/images/qapital_share.png
layout: provider
modified: '2026-08-26'
name: Qapital
nav: Providers
network: true
overview: 'Qapital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Personal Finance, Savings, Banking, and Investing.


  Qapital''s developer surface includes engineering blog, support, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Qapital Plans Pricing
  plan_count: 3
  slug: qapital-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Qapital Rate Limits
  slug: qapital-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 28.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Qapital Domain Security
  slug: qapital-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Qapital Trust Center
  slug: qapital-trust-center
  summary_line: SOC 2 Type I
slug: qapital
tags:
- Company
- Personal Finance
- Savings
- Banking
- Investing
- Budgeting
- Fintech
- Consumer Applications
- Behavioral Economics
- Mobile Banking
website: https://www.qapital.com/
---
