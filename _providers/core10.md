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
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://monarchfts.com/
- group: company
  title: ''
  type: About
  url: https://monarchfts.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://monarchfts.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://monarchfts.com/about#careers
- group: other
  title: ''
  type: Resources
  url: https://monarchfts.com/resources/
- group: other
  title: ''
  type: Industries
  url: https://monarchfts.com/industries/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monarchfts.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monarchfts.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monarch-psg/
- group: company
  title: ''
  type: Blog
  url: https://blog.core10.io/
- group: company
  title: ''
  type: BlogFeeds
  url: https://blog.core10.io/rss.xml
- group: other
  title: ''
  type: Product
  url: https://getaccrue.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/core10-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/core10-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/core10-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/core10-rate-limits.yml
coverage:
  checked: '2026-08-11'
  detail: The Core10 brand is retired — core10.io 301-redirects to monarchfts.com, where the company now trades as Monarch, an Intapp DealCloud consultancy, while the Accrue platform it acquired trades separately at getaccrue.com; Core10 sold API integration work for a decade and never published an API, a developer portal or a spec of its own, and neither successor does either.
  evidence:
  - status: 301
    url: https://core10.io/
  - status: 404
    url: https://monarchfts.com/openapi.json
  - status: 404
    url: https://monarchfts.com/llms.txt
  - status: 404
    url: https://monarchfts.com/.well-known/agent-card.json
  - status: 404
    url: https://getaccrue.com/developers
  - status: 404
    url: https://api.getaccrue.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/core10
  reason: defunct
  state: none
created: '2026-08-11'
description: 'Core10, Inc. is a U.S.-based fintech software development and API integration firm founded in 2016 by Lee Farabaugh and Jeff Martin, headquartered in Franklin, Tennessee with delivery centers in Martin, Tennessee and Huntington, West Virginia, built on a domestic-outsourcing model it trademarked as Hereshore(R). Core10 wrote custom software, core-banking integrations and API layers for community banks, credit unions and fintechs, and acquired Accrue Technologies in 2021 to add a Salesforce-based digital lending, account opening and treasury onboarding platform. In January 2024 it spun its implementation practice out as Monarch, and the Core10 brand has since been retired: core10.io now 301-redirects to monarchfts.com, where Monarch operates as an Intapp DealCloud implementation, configuration and managed-services consultancy for private capital firms, while the Accrue platform trades independently at getaccrue.com under its own leadership. Core10 built API integrations for
  other companies for nearly a decade but never published a developer program, public API, SDK or machine-readable contract of its own, and as of 2026-08-11 neither successor brand does either.'
image: https://monarchfts.com/wp-content/uploads/cropped-monarch-favicon-192x192.webp
layout: provider
modified: '2026-08-11'
name: Core10
nav: Providers
network: true
overview: 'Core10 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial-Services, Banking, and API Integration.


  Core10''s developer surface includes engineering blog and 15 more developer resources.'
plans:
- name: Core10 Plans Pricing
  plan_count: 0
  slug: core10-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Core10 Rate Limits
  slug: core10-rate-limits
score:
  band: minimal
  composite: 7.7
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Core10 Domain Security
  slug: core10-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: core10
tags:
- Company
- Fintech
- Financial-Services
- Banking
- API Integration
- Software Development
- Digital Lending
- Account Opening
- Salesforce
- Consulting
- Professional Services
- Private Capital
- Tennessee
website: https://monarchfts.com/
---
