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
  url: https://www.leif.org/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/leif_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leif-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leif-lifecycle.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/leif-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/leif-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leif-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leif-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leif-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Leif's entire public surface is dark — leif.org and www.leif.org terminate the TLS handshake at their Webflow edge, app.leif.org returns 504 on every path, the leiforg.zendesk.com help center is gone, and the api.leif.org / sandbox.leif.org AWS API Gateway hosts answer only the unmatched-route default "Missing Authentication Token", with the last successful Internet Archive capture of the site dated 2025-11-09.
  evidence:
  - status: 0
    url: https://www.leif.org/
  - status: 504
    url: https://app.leif.org/login
  - status: 403
    url: https://api.leif.org/openapi.json
  - status: 404
    url: https://leiforg.zendesk.com/hc/en-us
  - status: 404
    url: https://partners.leif.org/isa/leif
  reason: defunct
  state: none
created: '2026-08-25'
description: 'Leif (Leif Technologies, Inc.) was a New York City education-finance technology company, founded in 2017 by Francis Larson, Jeffrey Groeber and Richard Lee, that built an end-to-end platform for designing, originating, servicing and financing outcomes-aligned tuition products for schools and bootcamps. Its product line covered Income Share Agreements, contingent payment plans, tuition installment plans and upfront payment, alongside career-services and advisory-insights modules, and the platform handled student identity verification, credit evaluation, income verification, disbursement, payment collection and program reporting for its school partners. Leif publicly claimed more than 20,000 originations across 200+ partner schools and over $400 million in arranged financing, and it raised a strategic financing round totalling more than $60 million in 2021. Leif never operated a public developer program: the archived marketing site carries no developer portal, API reference or
  documentation nav, and the only API surface ever visible was the private JSON API behind its own student and school applications (leif.org/api/*). As of the 2026-08-25 probe the company''s entire public surface is dark — leif.org and www.leif.org fail the TLS handshake at their Webflow edge, app.leif.org returns 504 on every path, the Zendesk help center is gone, and the api.leif.org and sandbox.leif.org AWS API Gateway hosts answer only "Missing Authentication Token".'
layout: provider
modified: '2026-08-25'
name: Leif
nav: Providers
network: true
overview: Leif is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Education-Finance, Income Share Agreement, and Student Lending.
plans:
- name: Leif Plans Pricing
  plan_count: 0
  slug: leif-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Leif Rate Limits
  slug: leif-rate-limits
score:
  band: minimal
  composite: 2.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Leif Domain Security
  slug: leif-domain-security
  summary_line: DMARC
slug: leif
tags:
- Company
- Education
- Education-Finance
- Income Share Agreement
- Student Lending
- Fintech
- Financial-Services
- Tuition
- Payments
- Lending
- New York
website: https://www.leif.org/
---
