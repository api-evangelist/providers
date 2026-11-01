---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: BackNine's BOSS API provides quoting, e‑application, commission, and policy management endpoints.
  name: BOSS API
  slug: boss-api
- baseURL: https://app.back9ins.com
  baseurl_source: declared
  description: 'back9ins-com API as documented publicly: 46 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: back9ins-com API
  slug: back9ins-com-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/back9ins-com/plans/back9ins-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/back9ins-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/back9ins-com/rules/back9ins-com-rules.yml
  title: ''
  type: Spectral
  url: rules/back9ins-com-rules.yml
- group: design
  href: https://artifacts.apis.io/back9ins-com/json-ld/back9ins-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/back9ins-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/back9ins-com/vocabulary/back9ins-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/back9ins-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/back9ins-com/data-model/back9ins-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/back9ins-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://back9ins.com/security
- group: design
  href: https://artifacts.apis.io/back9ins-com/conformance/back9ins-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/back9ins-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/back9ins-com/llms/back9ins-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/back9ins-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/back9ins-com/mcp/back9ins-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/back9ins-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/back9ins-com/well-known/back9ins-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/back9ins-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/back9ins-com/well-known/back9ins-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/back9ins-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/back9ins-com/hosts/back9ins-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/back9ins-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/back9ins-com/vendors/back9ins-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/back9ins-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://back9ins.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://back9ins.com/sandbox
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.back9ins.com/#quote-amp-apply-setup
- group: auth
  href: https://artifacts.apis.io/back9ins-com/security/back9ins-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/back9ins-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/back9ins-com/security/back9ins-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/back9ins-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://back9ins.com/
- group: docs
  title: ''
  type: Documentation
  url: https://back9ins.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://back9ins.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://back9ins.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://back9ins.com/news
- group: operate
  title: ''
  type: Support
  url: https://back9ins.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/back9ins/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://github.com/back9ins/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.back9ins.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.back9ins.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.back9ins.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/back9ins
coverage:
  checked: '2026-10-30'
  detail: API documentation requires an API key sign‑up, blocking unauthenticated access to the spec.
  evidence:
  - status: 200
    url: https://app.back9ins.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-29'
description: BackNine Insurance and Financial Services Inc. provides a cloud‑based platform that simplifies life, annuity, disability and long‑term care insurance sales for agencies. Their BOSS (Back Office Support System) offers real‑time quoting, e‑applications, commission accounting, and integrated carrier partnerships, enabling agents to manage appointments, reporting and client data while maintaining control. The solution serves insurance agencies, banks and credit unions, delivering a SaaS experience with multi‑carrier support and 24/7 assistance.
image: https://back9ins.com/favicon.ico
json_schemas:
- name: GetApiV1ImpairedRiskQuotesResponse
  property_count: 8
  slug: back9ins-com-get-api-v1-impaired-risk-quotes-response
- name: GetApiV1QuoteRequestsResponse
  property_count: 2
  slug: back9ins-com-get-api-v1-quote-requests-response
- name: PostApiV1EappQuotesRequest
  property_count: 9
  slug: back9ins-com-post-api-v1-eapp-quotes-request
- name: PostApiV1EappsEappuuidAccessesCreateRequest
  property_count: 6
  slug: back9ins-com-post-api-v1-eapps-eappuuid-accesses-create-request
- name: PostApiV1ImpairedRiskQuotesRequest
  property_count: 17
  slug: back9ins-com-post-api-v1-impaired-risk-quotes-request
- name: PostApiV1TextRequest
  property_count: 13
  slug: back9ins-com-post-api-v1-text-request
jsonld:
- class_count: 54
  name: Back9Ins Com Context
  property_count: 92
  slug: back9ins-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.back9ins.com requiring OAuth.
  name: back9ins-com MCP Server
  slug: back9ins-com-mcp-yml
modified: '2026-10-29'
name: back9ins-com
nav: Providers
network: true
overview: 'back9ins-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, InsurTech, SaaS, B2B, and LifeInsurance.


  The back9ins-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  back9ins-com''s developer surface includes sandbox, getting-started guide, documentation, API reference, pricing, engineering blog, support, and 23 more developer resources.'
plans:
- name: Back9Ins Com Plans Pricing
  plan_count: 1
  slug: back9ins-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: back9ins-com API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: back9ins-com-rules
scopes:
- name: Back9Ins Com Scopes
  scope_count: 0
  slug: back9ins-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 22
      marker_coverage: 100.0
      total: 22
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 41.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Back9Ins Com Authentication
  slug: back9ins-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Back9Ins Com Domain Security
  slug: back9ins-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Back9Ins Com Trust Center
  slug: back9ins-com-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS
slug: back9ins-com
tags:
- Insurance
- InsurTech
- SaaS
- B2B
- LifeInsurance
website: https://back9ins.com/
---
