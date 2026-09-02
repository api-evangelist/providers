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
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.yazio.com
- group: operate
  title: ''
  type: Support
  url: https://help.yazio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.yazio.com/hc/en-us/articles/203444951-Terms-of-Use-Privacy-Policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yazio.com/en/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.yazio.com/en/app/account/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yazio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yazio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/yazio-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yazio-domain-security.yml
coverage:
  checked: '2026-08-27'
  detail: YAZIO's only API is the undocumented private backend at yzapi.yazio.com that its own apps call — it answers 401 with an empty body to anonymous requests, issues OAuth client credentials through no public process, is linked from nowhere on yazio.com, and every OpenAPI, SDK and MCP server for it is third-party reverse-engineering whose own README states YAZIO does not publish, endorse or support it.
  evidence:
  - status: 401
    url: https://yzapi.yazio.com/v15/user
  - status: 404
    url: https://www.yazio.com/en/developers
  - status: 404
    url: https://www.yazio.com/openapi.json
  - status: 404
    url: https://yzapi.yazio.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: 'YAZIO GmbH is an Erfurt, Germany based digital health company whose nutrition app pairs calorie and macro tracking with barcode scanning, AI photo food logging, an intermittent-fasting timer, a 3,000-recipe library and body-metric tracking across iOS, Android and the web. The company describes itself as remote-first, cites more than 100 million downloads across over 150 countries, and sells a freemium product: a free tier plus a "YAZIO PRO" subscription transacted through the Apple App Store and Google Play rather than through a pricing page on yazio.com. YAZIO publishes no developer program of any kind — no developer portal, no API reference, no OpenAPI, AsyncAPI or GraphQL contract, no SDKs, no CLI, no MCP server, no changelog, no status page and no security.txt. Its apps talk to a private backend at https://yzapi.yazio.com, which is live but answers 401 with an empty body to anonymous requests and issues OAuth client credentials through no public process. Every YAZIO OpenAPI
  description, client library and MCP server in circulation is third-party reverse-engineering that states in its own README that it is unofficial and unaffiliated.'
image: https://images.yazio-cdn.com/process/plain/frontend/web/general/yazio-og-image.png
layout: provider
modified: '2026-08-27'
name: YAZIO
nav: Providers
network: true
overview: 'YAZIO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Nutrition, and Calorie Tracking.


  YAZIO''s developer surface includes support, signup flow, and 7 more developer resources.'
plans:
- name: Yazio Plans Pricing
  plan_count: 0
  slug: yazio-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Yazio Rate Limits
  slug: yazio-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Yazio Authentication
  slug: yazio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Yazio Domain Security
  slug: yazio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: yazio
tags:
- Company
- Health
- Digital Health
- Nutrition
- Calorie Tracking
- Weight Management
- Intermittent Fasting
- Fitness
- Consumer Health
- Mobile Applications
- Germany
website: https://www.yazio.com
---
