---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Zamp Agentic Access
  operation_count: 9
  slug: zamp-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 8
apis:
- baseURL: https://api.zamp.com
  baseurl_source: spec
  description: Zamp provides a developer API documented at the API Reference page.
  name: Zamp API
  slug: zamp-api
- baseURL: https://api.zamp.com
  baseurl_source: declared
  description: The Addresses API from Zamp — 1 operation(s) for addresses.
  name: Zamp Addresses API
  slug: zamp-addresses-api
- baseURL: https://api.zamp.com
  baseurl_source: declared
  description: The Calculations API from Zamp — 1 operation(s) for calculations.
  name: Zamp Calculations API
  slug: zamp-calculations-api
- baseURL: https://api.zamp.com
  baseurl_source: declared
  description: The Companies API from Zamp — 1 operation(s) for companies.
  name: Zamp Companies API
  slug: zamp-companies-api
- baseURL: https://api.zamp.com
  baseurl_source: declared
  description: The Filings API from Zamp — 1 operation(s) for filings.
  name: Zamp Filings API
  slug: zamp-filings-api
- baseURL: https://api.zamp.com
  baseurl_source: declared
  description: The Registrations API from Zamp — 1 operation(s) for registrations.
  name: Zamp Registrations API
  slug: zamp-registrations-api
- baseURL: https://api.zamp.com
  baseurl_source: declared
  description: The Tax Codes API from Zamp — 1 operation(s) for tax codes.
  name: Zamp Tax Codes API
  slug: zamp-tax-codes-api
- baseURL: https://api.zamp.com
  baseurl_source: declared
  description: The Transactions API from Zamp — 1 operation(s) for transactions.
  name: Zamp Transactions API
  slug: zamp-transactions-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/zamp/agentic-access/zamp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zamp-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/zamp/finops/zamp-finops.yml
  title: ''
  type: FinOps
  url: finops/zamp-finops.yml
- group: auth
  href: https://artifacts.apis.io/zamp/well-known/zamp-zamp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zamp-zamp-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zamp.com/terms-conditions
- group: commercial
  href: https://artifacts.apis.io/zamp/plans/zamp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zamp-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zamp/rules/zamp-rules.yml
  title: ''
  type: Spectral
  url: rules/zamp-rules.yml
- group: design
  href: https://artifacts.apis.io/zamp/json-ld/zamp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zamp-context.jsonld
- group: design
  href: https://artifacts.apis.io/zamp/vocabulary/zamp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zamp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/zamp/data-model/zamp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zamp-data-model.yml
- group: operate
  href: https://artifacts.apis.io/zamp/changelog/zamp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zamp-changelog.yml
- group: design
  href: https://artifacts.apis.io/zamp/conventions/zamp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zamp-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://zamp.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/zamp/authentication/zamp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zamp-authentication.yml
- group: design
  href: https://artifacts.apis.io/zamp/conformance/zamp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zamp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zamp/llms/zamp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zamp-llms.txt
- group: other
  href: https://artifacts.apis.io/zamp/a2a/zamp-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zamp-a2a.yml
- group: agent
  href: https://artifacts.apis.io/zamp/mcp/zamp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zamp-mcp.yml
- group: auth
  href: https://artifacts.apis.io/zamp/well-known/zamp-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zamp-support-security.txt
- group: agent
  href: https://artifacts.apis.io/zamp/well-known/zamp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zamp-well-known.yml
- group: other
  href: https://artifacts.apis.io/zamp/hosts/zamp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zamp-hosts.yml
- group: other
  href: https://artifacts.apis.io/zamp/vendors/zamp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zamp-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://zamp.statuspage.io/
- group: company
  title: ''
  type: Newsroom
  url: https://zamp.com/press
- group: auth
  href: https://artifacts.apis.io/zamp/security/zamp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zamp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zamp/security/zamp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zamp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zamp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zamp.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zamp.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://developer.zamp.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zamp.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://developer.zamp.com/guides/common-faqs
- group: company
  title: ''
  type: Blog
  url: https://zamp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zamp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developer.zamp.com/guides/trial
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zamp/workspace
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://developer.zamp.com/mcp
  - status: 200
    url: https://zamp.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Zamp provides a fully managed sales tax compliance platform with a robust API that enables businesses to automate sales tax calculations, filing, and remittance across the United States and Canada. Their solution includes features such as nexus tracking, exemption certificate management, and integration with major e‑commerce and accounting platforms. Zamp’s API trial is publicly available, allowing developers to test and integrate sales tax functionality quickly and securely.
finops:
- has_sources: true
  method: derived
  name: Zamp Finops
  primary_unit: ''
  service_category: ''
  slug: zamp-finops
  template: true
image: https://cdn.prod.website-files.com/69f3731843be4ce24ae7dea2/6a038f9f6176eacfdaa7dbe4_last-sales-n-scaled.jpg
json_schemas:
- name: GetFilingsResponse
  property_count: 3
  slug: zamp-get-filings-response
- name: GetRegistrationsResponse
  property_count: 4
  slug: zamp-get-registrations-response
- name: PostCalculationsRequest
  property_count: 10
  slug: zamp-post-calculations-request
- name: PostCalculationsResponse
  property_count: 4
  slug: zamp-post-calculations-response
- name: PostTransactionsRequest
  property_count: 13
  slug: zamp-post-transactions-request
- name: PostTransactionsResponse
  property_count: 4
  slug: zamp-post-transactions-response
jsonld:
- class_count: 10
  name: Zamp Context
  property_count: 32
  slug: zamp-context
layout: provider
mcp_servers:
- description: Remote MCP server at developer.zamp.com.
  name: Zamp MCP Server
  slug: zamp-mcp-yml
modified: '2026-10-14'
name: Zamp
nav: Providers
network: true
overview: 'Zamp is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Calculations API, and 6 more. Tagged areas include Company, Sales Tax, Automation, and Compliance.


  The Zamp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zamp''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
plans:
- name: Zamp Plans Pricing
  plan_count: 3
  slug: zamp-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Zamp API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: zamp-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 36.9
    discoverability: 64.2
    operational_transparency: 34.2
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zamp/zamp-2026-11-03T150416.png
security:
- kind: authentication
  name: Zamp Authentication
  slug: zamp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zamp Domain Security
  slug: zamp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zamp Trust Center
  slug: zamp-trust-center
  summary_line: SOC 2, GDPR
slug: zamp
tags:
- Company
- Sales Tax
- Automation
- Compliance
website: https://zamp.com
---
