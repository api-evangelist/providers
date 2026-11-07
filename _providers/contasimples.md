---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.8
  scored_at: '2026-11-06'
api_count: 10
apis:
- description: Technical reference of Conta Simples API endpoints.
  name: Conta Simples API
  slug: conta-simples-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Accounts API from Contasimples — 1 operation(s) for accounts.
  name: Contasimples Accounts API
  slug: contasimples-accounts-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Attachments API from Contasimples — 2 operation(s) for attachments.
  name: Contasimples Attachments API
  slug: contasimples-attachments-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Categories API from Contasimples — 2 operation(s) for categories.
  name: Contasimples Categories API
  slug: contasimples-categories-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Cost Centers API from Contasimples — 2 operation(s) for cost centers.
  name: Contasimples Cost Centers API
  slug: contasimples-cost-centers-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Credit Cards API from Contasimples — 6 operation(s) for credit cards.
  name: Contasimples Credit Cards API
  slug: contasimples-credit-cards-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Oauth API from Contasimples — 1 operation(s) for oauth.
  name: Contasimples OAuth API
  slug: contasimples-oauth-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Statements API from Contasimples — 3 operation(s) for statements.
  name: Contasimples Statements API
  slug: contasimples-statements-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Suppliers API from Contasimples — 2 operation(s) for suppliers.
  name: Contasimples Suppliers API
  slug: contasimples-suppliers-api
- baseURL: https://api-sandbox.contasimples.com
  baseurl_source: declared
  description: The Users API from Contasimples — 2 operation(s) for users.
  name: Contasimples Users API
  slug: contasimples-users-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/contasimples/rules/contasimples-rules.yml
  title: ''
  type: Spectral
  url: rules/contasimples-rules.yml
- group: operate
  href: https://artifacts.apis.io/contasimples/changelog/contasimples-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contasimples-changelog.yml
- group: design
  href: https://artifacts.apis.io/contasimples/conventions/contasimples-conventions.yml
  title: ''
  type: Conventions
  url: conventions/contasimples-conventions.yml
- group: auth
  href: https://artifacts.apis.io/contasimples/authentication/contasimples-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contasimples-authentication.yml
- group: operate
  href: https://artifacts.apis.io/contasimples/lifecycle/contasimples-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/contasimples-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/contasimples/lifecycle/contasimples-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/contasimples-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/contasimples/conformance/contasimples-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contasimples-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contasimples/llms/contasimples-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contasimples-llms.txt
- group: agent
  href: https://artifacts.apis.io/contasimples/well-known/contasimples-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contasimples-well-known.yml
- group: other
  href: https://artifacts.apis.io/contasimples/hosts/contasimples-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contasimples-hosts.yml
- group: other
  href: https://artifacts.apis.io/contasimples/vendors/contasimples-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contasimples-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.contasimples.com/br/operacao/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.contasimples.com/br/api-reference/introducao
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.contasimples.com/br/comece-aqui/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.contasimples.com/
- group: auth
  href: https://artifacts.apis.io/contasimples/security/contasimples-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contasimples-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contasimples.com
coverage:
  checked: '2026-10-10'
  detail: API documentation is a JavaScript‑rendered Next.js site, no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://developers.contasimples.com/br/api-reference/introducao
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Contasimples provides a digital banking platform for businesses in Brazil, offering corporate credit cards, payment services, expense management, and financial automation. The service includes features such as Pix transfers, batch payments, invoicing, and integration with ERP systems. It aims to simplify financial operations for startups and SMEs, providing tools for credit, cash flow management, and real‑time analytics.
layout: provider
modified: '2026-10-10'
name: Contasimples
nav: Providers
network: true
overview: 'Contasimples is listed with 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Categories API, and 7 more. Tagged areas include Company.


  The Contasimples catalog on APIs.io includes 1 Spectral governance ruleset.


  Contasimples'' developer surface includes changelog, authentication, API reference, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Contasimples API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: contasimples-rules
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.5
    catalog_earned_first_party: 0.0
    catalog_gap: 82.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 15.3
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 22.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/contasimples/contasimples-2026-11-03T125203.png
security:
- kind: authentication
  name: Contasimples Authentication
  slug: contasimples-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Contasimples Domain Security
  slug: contasimples-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contasimples
tags:
- Company
website: https://contasimples.com
---
