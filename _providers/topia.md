---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/topia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.topia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.topia.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.topia.com/support-center
- group: start
  title: ''
  type: Login
  url: https://login.topia.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.topia.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.topia.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/topia-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/topia_stock/
coverage:
  checked: '2026-08-05'
  detail: Topia's only documentation surface, support.topia.com, 307-redirects to a HubSpot member login at /_hcms/mem/login, and the company's own 148-URL sitemap contains no developer, API or docs page (api./developer./developers./docs.topia.com are all NXDOMAIN), so the API behind its Workday Approved Integration and its "MCP-native" Horizon agents is reachable only by signed-in customers.
  evidence:
  - status: 307
    url: https://support.topia.com/
  - status: 200
    url: https://www.topia.com/sitemap.xml
  - status: 200
    url: https://www.topia.com/llms.txt
  - status: 404
    url: https://login.topia.com/mcp
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: Topia is a global mobility platform for distributed workforces, used by HR, Finance and Legal teams at mid-market and enterprise companies to manage international assignments, relocations, business travel, remote work and cross-border compliance across 190+ countries in a single system. Founded in 2010 and headquartered in the United States, with additional offices in the United Kingdom, Ireland and Estonia, Topia spans global talent mobility, a tax and compliance engine, cost estimation and tracking, global workforce planning, cost and immigration risk management, and business travel. In April 2026 Topia launched Horizon, an agentic AI workspace for mobility teams that the company describes as built natively into MCP (Model Context Protocol) environments. Topia integrates with HRIS, payroll, travel and expense systems including Workday (a Workday Approved Integration), SAP, ADP, Oracle, Ceridian, SAP Concur and BCD Travel. Topia publishes an llms.txt at its marketing host,
  but no public developer portal, API reference or machine-readable specification; the support center sits behind a customer login.
image: https://www.topia.com/assets/topia-logo-ywmojvFn.png
layout: provider
modified: '2026-08-05'
name: Topia
nav: Providers
network: true
overview: 'Topia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Global Mobility, Human Resources, Relocation, and Tax Compliance.


  Topia''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/topia/refs/heads/main/screenshots/topia-2026-09-02T163917.png
security:
- kind: domain-security
  name: Topia Domain Security
  slug: topia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: topia
tags:
- Company
- Global Mobility
- Human Resources
- Relocation
- Tax Compliance
- Immigration
- Business Travel
- Workforce Management
- Remote Work
- Enterprise Software
website: https://www.topia.com/
---
