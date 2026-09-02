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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.breef.com/
- group: company
  title: ''
  type: About
  url: https://www.breef.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.breef.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.breef.com/onboarding
- group: start
  title: ''
  type: Login
  url: https://projects.breef.com/public/signin
- group: operate
  title: ''
  type: Support
  url: https://www.breef.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.breef.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.breef.com/breefingroom
- group: other
  title: ''
  type: CaseStudies
  url: https://www.breef.com/case-studies
- group: company
  title: ''
  type: Careers
  url: https://www.breef.com/careers
- group: start
  title: ''
  type: Demo
  url: https://www.breef.com/demo
- group: operate
  title: ''
  type: Community
  url: https://www.breef.com/community-standards
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breef.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breef.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.breef.com/cookie-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/breef
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/breefwork
- group: commercial
  title: ''
  type: Plans
  url: plans/breef-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breef-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/breef-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'Breef ships only an end-user SaaS product: its 483-URL sitemap carries no developer, API, docs or integrations page, no api./developer./docs./app./mcp.breef.com hostname resolves at all, and no npm, PyPI, RubyGems, crates.io or Packagist package exists — the only machine-readable contract on the estate is the customer application''s own Django REST Framework schema at projects.breef.com/api/schema/, which negotiates application/vnd.oai.openapi but answers anonymous callers with 403 "Authentication credentials were not provided", so it is an internal app backend rather than a published developer program.'
  evidence:
  - status: 200
    url: https://www.breef.com/sitemap.xml
  - status: 404
    url: https://www.breef.com/openapi.json
  - status: 404
    url: https://www.breef.com/developers
  - status: 404
    url: https://www.breef.com/integrations
  - status: 404
    url: https://www.breef.com/.well-known/api-catalog
  - status: 404
    url: https://www.breef.com/.well-known/agent-card.json
  - status: 404
    url: https://www.breef.com/llms.txt
  - status: 404
    url: https://projects.breef.com/graphql
  - status: 200
    url: https://projects.breef.com/api/
  - status: 401
    url: https://projects.breef.com/api/agencies/agency-case-studies
  - status: 403
    url: https://projects.breef.com/api/schema/
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: 'Breef is an online agency marketplace and payments platform that connects brands with vetted marketing, creative, digital and web agencies. Founded in New York in 2019 as Curated and rebranded to Breef in 2021, the company is now headquartered in Denver. Brands scope a project on the platform, receive curated pitches from hand-picked agencies across 50+ project types in days rather than months, and then run contracts, milestones and payments through Breef — including Breef(Pay), its agency-now-pay-later payment product. The network spans roughly 25,000 vetted agencies across 27 countries. Breef is a hosted end-user SaaS product: it publishes no public developer program, API reference, SDK or webhook surface.'
image: https://cdn.prod.website-files.com/5e4d24d0d11c7440ba421ee3/695fecd6ab2c876120054eb4_855332ca372b2b87e1b97fff133e4083_breef.com.jpg
layout: provider
modified: '2026-08-12'
name: Breef
nav: Providers
network: true
overview: 'Breef is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, Agencies, and Marketplace.


  Breef''s developer surface includes pricing, signup flow, support, engineering blog, and 16 more developer resources.'
plans:
- name: Breef Plans Pricing
  plan_count: 3
  slug: breef-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Breef Domain Security
  slug: breef-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breef
tags:
- Company
- Marketing
- Advertising
- Agencies
- Marketplace
- Creative Services
- Procurement
- Payments
- Software-as-a-Service
website: https://www.breef.com/
---
