---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Normapi Com Agentic Access
  operation_count: 14
  slug: normapi-com-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 3
apis:
- baseURL: https://api.normapi.de
  baseurl_source: declared
  description: API for German e‑invoicing supporting validation, parsing and generation of XRechnung and ZUGFeRD invoices.
  name: NormAPI REST API
  slug: normapi-rest-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/normapi-com/plans/normapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/normapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/normapi-com/conformance/normapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/normapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/normapi-com/llms/normapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/normapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/normapi-com/mcp/normapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/normapi-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/normapi-com/well-known/normapi-com-normapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/normapi-com-normapi-security.txt
- group: agent
  href: https://artifacts.apis.io/normapi-com/well-known/normapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/normapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/normapi-com/hosts/normapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/normapi-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/normapi-com/packages/normapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/normapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/normapi-com/packages/normapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/normapi-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://normapi.com/en/security
- group: start
  title: ''
  type: Sandbox
  url: https://normapi.com/en/account/playground
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.normapi.de</code
- group: auth
  href: https://artifacts.apis.io/normapi-com/security/normapi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/normapi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/normapi-com/security/normapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/normapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://normapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://normapi.com/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://normapi.com/openapi.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://normapi.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://normapi.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://normapi.com/en/privacy
created: '2026-10-26'
description: NormAPI provides a German e‑invoicing API supporting XRechnung and ZUGFeRD standards. It offers validation and generation of invoices via REST endpoints, with a free tier of 50 invoices per month and enterprise plans. The service includes documentation, pricing, and legal information, targeting developers and businesses needing compliant e‑invoices in Germany.
image: https://normapi.com/en/opengraph-image-1nh35u?aea9578972dfe4f7
json_schemas:
- name: CustomerAllowance
  property_count: 2
  slug: normapi-com-customer-allowance
- name: CustomerMonth
  property_count: 5
  slug: normapi-com-customer-month
- name: CustomerPage
  property_count: 4
  slug: normapi-com-customer-page
- name: InvoiceRequest
  property_count: 24
  slug: normapi-com-invoice-request
- name: ParseResult
  property_count: 10
  slug: normapi-com-parse-result
- name: RuleExplained
  property_count: 3
  slug: normapi-com-rule-explained
- name: ValidationResult
  property_count: 8
  slug: normapi-com-validation-result
jsonld:
- class_count: 25
  name: Normapi Com Context
  property_count: 140
  slug: normapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at normapi.com.
  name: NormAPI MCP Server
  slug: normapi-com-mcp-yml
modified: '2026-10-26'
name: NormAPI
nav: Providers
network: true
overview: 'NormAPI publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Company, E-Invoicing, XRechnung, ZUGFeRD, and Germany.


  The NormAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NormAPI''s developer surface includes sandbox, documentation, API reference, pricing, and 16 more developer resources.'
plans:
- name: Normapi Com Plans Pricing
  plan_count: 5
  slug: normapi-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: NormAPI API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: normapi-com-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 67.5
    catalog_earned_first_party: 12.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 47.1
    developer_ergonomics: 23.8
    discoverability: 80.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/normapi-com/normapi-com-2026-11-03T140306.png
security:
- kind: authentication
  name: Normapi Com Authentication
  slug: normapi-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Normapi Com Domain Security
  slug: normapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Normapi Com Vulnerability Disclosure
  slug: normapi-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: normapi-com
tags:
- Company
- E-Invoicing
- XRechnung
- ZUGFeRD
- Germany
website: https://normapi.com
---
