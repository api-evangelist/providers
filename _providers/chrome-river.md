---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Accounts API from Chrome River — 4 operation(s) for accounts.
  name: Chrome River Accounts API
  slug: chrome-river-accounts-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Allowances API from Chrome River — 1 operation(s) for allowances.
  name: Chrome River Allowances API
  slug: chrome-river-allowances-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Cards API from Chrome River — 3 operation(s) for cards.
  name: Chrome River Cards API
  slug: chrome-river-cards-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Categories API from Chrome River — 2 operation(s) for categories.
  name: Chrome River Categories API
  slug: chrome-river-categories-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Company API from Chrome River — 2 operation(s) for company.
  name: Chrome River Company API
  slug: chrome-river-company-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Departments API from Chrome River — 2 operation(s) for departments.
  name: Chrome River Departments API
  slug: chrome-river-departments-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Labels API from Chrome River — 2 operation(s) for labels.
  name: Chrome River Labels API
  slug: chrome-river-labels-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Locations API from Chrome River — 2 operation(s) for locations.
  name: Chrome River Locations API
  slug: chrome-river-locations-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Members API from Chrome River — 3 operation(s) for members.
  name: Chrome River Members API
  slug: chrome-river-members-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Merchant Categories API from Chrome River — 1 operation(s) for merchant categories.
  name: Chrome River Merchant Categories API
  slug: chrome-river-merchant-categories-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Oauth API from Chrome River — 3 operation(s) for oauth.
  name: Chrome River OAuth API
  slug: chrome-river-oauth-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Requisitions API from Chrome River — 2 operation(s) for requisitions.
  name: Chrome River Requisitions API
  slug: chrome-river-requisitions-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Shared Links API from Chrome River — 2 operation(s) for shared links.
  name: Chrome River Shared Links API
  slug: chrome-river-shared-links-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Shipping Addresses API from Chrome River — 2 operation(s) for shipping addresses.
  name: Chrome River Shipping Addresses API
  slug: chrome-river-shipping-addresses-api
- baseURL: https://api.emburse.com/v1
  baseurl_source: spec
  description: The Transactions API from Chrome River — 2 operation(s) for transactions.
  name: Chrome River Transactions API
  slug: chrome-river-transactions-api
artifact_total: 27
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/plans/chrome-river-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chrome-river-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/rules/chrome-river-rules.yml
  title: ''
  type: Spectral
  url: rules/chrome-river-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/json-ld/chrome-river-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chrome-river-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/vocabulary/chrome-river-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chrome-river-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/data-model/chrome-river-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chrome-river-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/errors/chrome-river-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chrome-river-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/conformance/chrome-river-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chrome-river-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/llms/chrome-river-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chrome-river-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/well-known/chrome-river-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chrome-river-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/well-known/chrome-river-my-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chrome-river-my-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/well-known/chrome-river-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chrome-river-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/hosts/chrome-river-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chrome-river-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/vendors/chrome-river-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chrome-river-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.emburse.com/
- group: operate
  title: ''
  type: Support
  url: https://help.emburse.com/hc/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.emburse.com/uk/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emburse.com/uk/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.emburse.com/products/spend/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.emburse.com/company/news
- group: start
  title: ''
  type: Login
  url: https://www.emburse.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.emburse.com/company/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.emburse.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.billing.emburse.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emburse
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/authentication/chrome-river-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chrome-river-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/security/chrome-river-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chrome-river-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chrome-river/refs/heads/main/security/chrome-river-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chrome-river-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.emburse.com/products/chrome-river-is-enterprise
created: '2026-10-08'
description: Chrome River provides enterprise expense and invoice management solutions, now operating as part of Emburse. The platform offers automated expense reporting, compliance controls, analytics, and integration capabilities for large organizations, helping streamline travel and spend processes across global operations. It supports multi-currency handling, policy enforcement, receipt capture via mobile, and integrates with ERP, accounting, and travel booking systems, delivering comprehensive spend visibility and control for enterprises worldwide.
image: https://cdn.sanity.io/images/l5mo20ew/production/426919841ea68610738e9779779d780ee71f3dd0-138x24.svg
json_schemas:
- name: APIAccount
  property_count: 13
  slug: chrome-river-apiaccount
- name: APICard
  property_count: 22
  slug: chrome-river-apicard
- name: APICompany
  property_count: 9
  slug: chrome-river-apicompany
- name: APIRequisition
  property_count: 23
  slug: chrome-river-apirequisition
- name: APIStatementLine
  property_count: 16
  slug: chrome-river-apistatement-line
- name: APITransaction
  property_count: 28
  slug: chrome-river-apitransaction
jsonld:
- class_count: 14
  name: Chrome River Context
  property_count: 101
  slug: chrome-river-context
layout: provider
modified: '2026-10-08'
name: Chrome River
nav: Providers
network: true
overview: 'Chrome River publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Allowances API, Cards API, and 12 more. Tagged areas include Finance, Expense Management, Software-as-a-Service, Enterprise, and Travel.


  The Chrome River catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chrome River''s developer surface includes support, pricing, engineering blog, documentation, authentication, and 24 more developer resources.'
plans:
- name: Chrome River Plans Pricing
  plan_count: 3
  slug: chrome-river-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Chrome River API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 1
  slug: chrome-river-rules
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 22.0
    contract_quality: 62.2
    developer_ergonomics: 30.4
    discoverability: 67.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Chrome River Authentication
  slug: chrome-river-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chrome River Domain Security
  slug: chrome-river-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chrome River Vulnerability Disclosure
  slug: chrome-river-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chrome-river
tags:
- Finance
- Expense Management
- Software-as-a-Service
- Enterprise
- Travel
website: https://www.emburse.com/products/chrome-river-is-enterprise
---
