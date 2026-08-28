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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://juno.co/
- group: company
  title: ''
  type: About
  url: https://juno.co/about-us
- group: operate
  title: ''
  type: Support
  url: https://juno.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://juno.co/service-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://juno.co/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/juno-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Juno Technology, Inc. sells owner's representation and construction-management services plus the physical Juno Mass Timber System kit-of-parts; the entire juno.co sitemap is nine marketing pages with no developer section, and every spec, /.well-known/ and legacy API-subdomain probe missed.
  evidence:
  - status: 200
    url: https://juno.co/sitemap.xml
  - status: 404
    url: https://juno.co/openapi.json
  - status: 404
    url: https://juno.co/.well-known/api-catalog
  - status: 404
    url: https://juno.co/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Juno (juno.co), operated by Juno Technology, Inc., is a San Francisco-based owner''s representation, development-consulting and construction-management firm for prefabricated, modular and mass-timber multifamily development, working with developers from site feasibility and entitlement through delivery across North America. Juno owns the rights to the Juno Mass Timber System, a field-tested kit-of-parts building system of roughly 33 components configurable into 25+ unit types, proven on the 24-unit Juno East Austin project at 400 Comal St, Austin TX. The current company is the 2024 relaunch ("Juno 2.0") of the venture-funded Juno / Juno Residential founded in 2019 by Jonathan Scherr, BJ Siegel and Chester Chipperfield, which raised roughly $32M from Comcast Ventures, Khosla Ventures and RET Ventures before running out of money; the relaunched firm is led by co-founders Emily Mills Marineau and Jen Canchola. Juno sells professional services and a physical building system, not
  software: as of this enrichment pass it publishes a marketing site, a mass-timber system page, a contact form, a newsletter signup, terms of service and a privacy policy, and no public API, developer portal, OpenAPI specification, SDK, or machine-readable contract of any kind.'
image: https://cdn.prod.website-files.com/63bb9ddf47dd2f148dc336e3/63bba701e91f6644c348de9c_j-icon-256.png
layout: provider
modified: '2026-08-23'
name: Juno
nav: Providers
network: true
overview: 'Juno is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Construction Management, Real Estate, and Multifamily.


  Juno''s developer surface includes support and 6 more developer resources.'
plans:
- name: Juno Plans Pricing
  plan_count: 0
  slug: juno-plans-pricing
random_paper: 3
score:
  band: minimal
  composite: 10.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Juno Domain Security
  slug: juno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: juno
tags:
- Company
- Construction
- Construction Management
- Real Estate
- Multifamily
- Prefabrication
- Modular Construction
- Mass Timber
- Property Technology
- Owner's Representation
- Sustainability
- Professional Services
website: https://juno.co/
---
