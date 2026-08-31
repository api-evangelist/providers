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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightplan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightplan.com/
- group: company
  title: ''
  type: Blog
  url: https://www.brightplan.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.brightplan.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.brightplan.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightplan.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightplan.com/privacy-notice/
- group: start
  title: ''
  type: Login
  url: https://my.brightplan.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brightplan-llms.txt
coverage:
  checked: '2026-08-08'
  detail: BrightPlan sells an employer-sponsored financial wellness benefit, not a platform — the only live API is the undocumented backend behind its own employee app at my.brightplan.com/api, which answers every specification path with a structured JSON 404 ("API url GET /api/openapi.json is invalid"), and no developer portal, API reference, SDK, package or GitHub organization exists anywhere.
  evidence:
  - status: 404
    url: https://www.brightplan.com/developers
  - status: 404
    url: https://my.brightplan.com/api/openapi.json
  - status: 404
    url: https://www.brightplan.com/.well-known/agent-card.json
  - status: 200
    url: https://www.brightplan.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: BrightPlan is a San Jose, California based financial wellness company that sells a Total Financial Wellness platform to enterprise HR and benefits teams, combining a self-service digital financial planning application, an AI-powered financial wellness coach, and access to human CFP fiduciary advisors. BrightPlan LLC is an SEC-registered investment adviser, and the product is delivered to employees as an employer-sponsored benefit rather than as a self-serve consumer subscription. The employee experience runs at my.brightplan.com and web.brightplan.com with iOS and Android apps; employer value is framed around benefits engagement, retention, and measurable financial wellbeing. BrightPlan markets HRIS and benefits-system integration to employers but publishes no public developer program, API reference, or machine-readable specification of any kind.
image: https://www.brightplan.com/wp-content/uploads/favicon.png
layout: provider
modified: '2026-08-08'
name: BrightPlan
nav: Providers
network: true
overview: 'BrightPlan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Wellness, Financial Planning, Employee Benefits, Human Resources, and Wealth Management.


  BrightPlan''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Brightplan Domain Security
  slug: brightplan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightplan
tags:
- Financial Wellness
- Financial Planning
- Employee Benefits
- Human Resources
- Wealth Management
- Financial-Services
- Retirement
- Investment Advice
- Company
website: https://www.brightplan.com/
---
