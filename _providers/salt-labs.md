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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salt-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saltlabs.com/
- group: company
  title: ''
  type: Blog
  url: https://www.saltlabs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.saltlabs.com/contact-salt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saltlabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saltlabs.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.saltlabs.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/salt-labs-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/salt-labs-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/salt-labs-plans-pricing.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/salt-labs_stock/
coverage:
  checked: '2026-08-26'
  detail: Salt Labs ships an employee-facing mobile rewards app and an employer program sold through a demo form; its full 30-URL sitemap has no developer, docs or API section, no api./developer./ docs. subdomain resolves, and every contract-discovery path on www.saltlabs.com and app.saltlabs.com returns a discriminating 404 — the only machine-readable thing it publishes is the Atlassian Statuspage JSON feed at status.saltlabs.com.
  evidence:
  - status: 200
    url: https://www.saltlabs.com/sitemap.xml
  - status: 404
    url: https://www.saltlabs.com/openapi.json
  - status: 404
    url: https://app.saltlabs.com/api/v1/openapi.json
  - status: 404
    url: https://www.saltlabs.com/.well-known/agent-card.json
  - status: 200
    url: https://status.saltlabs.com/api/v2/summary.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Salt Labs is the New York company behind Salt, an employee rewards and loyalty benefit for hourly and frontline workers. Founded in 2022 by Jason Lee and founding members of DailyPay, Salt turns time worked into a points-based asset: an employee earns one Salt for every hour on the job through the Salt Rewards mobile app, and redeems accumulated Salt for merchandise, travel, experiences, education benefits, and investment products such as stock and treasury bonds. Salt is sold to employers across transportation, contact centers, hospitality, and parking services as a retention and engagement program modeled on airline miles and credit-card points. Salt Labs was acquired by Chime Financial in June 2024 and now operates as "Salt, a Chime Company", with founder Jason Lee leading the Chime Enterprise business unit. Salt Labs publishes no public developer program, API reference, or machine-readable contract; its only machine-readable first-party surface is the Atlassian Statuspage
  at status.saltlabs.com, which exposes public JSON and RSS availability feeds for the Salt App Backend.'
image: https://cdn.prod.website-files.com/673d09a76252e35aac1b746f/67a3ee4ca2a4290b140b26d8_Salt-opengraph.jpg
layout: provider
modified: '2026-08-26'
name: Salt Labs
nav: Providers
network: true
overview: 'Salt Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Rewards, Loyalty, Human Resources, and Employee Benefits.


  Salt Labs'' developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Salt Labs Plans Pricing
  plan_count: 0
  slug: salt-labs-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 13.4
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
    operational_transparency: 15.8
  previous_composite: 13.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Salt Labs Domain Security
  slug: salt-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: salt-labs
tags:
- Company
- Employee Rewards
- Loyalty
- Human Resources
- Employee Benefits
- Frontline Workers
- Financial Wellness
- Fintech
- Employee Engagement
- Employee Retention
website: https://www.saltlabs.com/
---
