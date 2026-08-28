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
  url: https://www.doorstead.com/
- group: company
  title: ''
  type: Blog
  url: https://www.doorstead.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doorstead.com/compare-plans
- group: commercial
  title: ''
  type: Plans
  url: plans/doorstead-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://www.doorstead.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://tenants.doorstead.com/help
- group: start
  title: ''
  type: Login
  url: https://tenants.doorstead.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doorstead.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doorstead.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doorstead
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.doorstead.com/knowledge
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doorstead-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doorstead-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: 'Doorstead ships only end-user products — an owner app and a tenant portal — and the single API-shaped host, https://api.doorstead.com/graphql, is the private backend for those apps: it answers anonymous GraphQL introspection with HTTP 403 {"message":"Unauthorized"}, and no docs, developer or developers subdomain resolves at all.'
  evidence:
  - status: 403
    url: https://api.doorstead.com/graphql
  - status: 404
    url: https://api.doorstead.com/openapi.json
  - status: 0
    url: https://docs.doorstead.com/
  - status: 200
    url: https://www.doorstead.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Doorstead is a technology-enabled residential property management and tenant placement company headquartered in San Francisco, serving single-family and small multifamily rental owners across California, Washington, Florida, Texas, North Carolina, South Carolina, Ohio, Virginia and Massachusetts. It sells two productized services: Doorstead Place, a tenant-placement-only offering covering rental pricing guidance, listing syndication, professional photography, agent-led tours, tenant screening and digital lease signing; and Doorstead Manage, full-service property management that adds rent collection and distribution, security-deposit holding, income and expense tracking, annual 1099s, 24/7 maintenance coordination, move-in/move-out evaluations, lease renewals and turnovers. The company markets a data-driven rental pricing model and an owner and tenant portal, but publishes no public developer API, SDK, webhook surface or developer portal; its production GraphQL endpoint at api.doorstead.com
  serves its own first-party applications and rejects anonymous requests. Doorstead discontinued its legacy Rent Guarantee product in early 2025.'
image: https://cdn.doorstead.com/images/logo/logo-horizontal-dark-mode.png
layout: provider
modified: '2026-08-12'
name: Doorstead
nav: Providers
network: true
overview: 'Doorstead is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Property Management, Real-Estate, PropTech, and Rentals.


  Doorstead''s developer surface includes engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: Doorstead Plans Pricing
  plan_count: 2
  slug: doorstead-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Doorstead Rate Limits
  slug: doorstead-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Doorstead Domain Security
  slug: doorstead-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: doorstead
tags:
- Company
- Property Management
- Real-Estate
- PropTech
- Rentals
- Leasing
- Residential
- Tenant Screening
website: https://www.doorstead.com/
---
