---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sps Commerce Agentic Access
  operation_count: 6
  slug: sps-commerce-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.spscommerce.com/submissions
  baseurl_source: declared
  description: 'The Trading Partner Submission API allows Community Buying Organizations to automate the submission of new vendors to their Community program with SPS Commerce (create trading-partner leads, list and '
  name: SPS Commerce Trading Partner Submission API
  slug: sps-commerce-trading-partner-submission-api
- baseURL: https://api.spscommerce.com
  baseurl_source: declared
  description: Inventory API for listing and reading items by SPS item ID and creating inventory imports. Its OpenAPI is published on the SPS Dev Center CDN, but the Dev Center service catalog marks the service inac
  name: SPS Commerce Inventory API
  slug: sps-commerce-inventory-api
- description: Transaction API (v5) for creating, filtering, getting and deleting EDI/XML transaction files and viewing interaction history across the SPS retail network. Documented in Dev Center; no machine-readabl
  name: SPS Commerce Transaction API
  slug: sps-commerce-transaction-api
- description: Shipping Doc API for retrieving shipping label and packing slip schemas and samples, and rendering labels (PDF/ZPL) and packing slips individually or in batches. Documented in Dev Center; no machine-r
  name: SPS Commerce Shipping Doc API
  slug: sps-commerce-shipping-doc-api
- baseURL: https://api.spscommerce.com/submissions
  baseurl_source: declared
  description: The Import API from SPS Commerce — 1 operation(s) for import.
  name: SPS Commerce Import API
  slug: sps-commerce-import-api
artifact_total: 19
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/agentic-access/sps-commerce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sps-commerce-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/rate-limits/sps-commerce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sps-commerce-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/rules/sps-commerce-rules.yml
  title: ''
  type: Spectral
  url: rules/sps-commerce-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/json-ld/sps-commerce-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sps-commerce-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/vocabulary/sps-commerce-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sps-commerce-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/data-model/sps-commerce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sps-commerce-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/conventions/sps-commerce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sps-commerce-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/sandbox/sps-commerce-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sps-commerce-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.spscommerce.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/lifecycle/sps-commerce-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sps-commerce-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/lifecycle/sps-commerce-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sps-commerce-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/errors/sps-commerce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sps-commerce-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/conformance/sps-commerce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sps-commerce-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/overlays/sps-commerce-inventory-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sps-commerce-inventory-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/llms/sps-commerce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sps-commerce-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/well-known/sps-commerce-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sps-commerce-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/well-known/sps-commerce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sps-commerce-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/hosts/sps-commerce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sps-commerce-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/vendors/sps-commerce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sps-commerce-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spscommerce.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.spscommerce.com/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/authentication/sps-commerce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sps-commerce-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/security/sps-commerce-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sps-commerce-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/security/sps-commerce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sps-commerce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spscommerce.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developercenter.spscommerce.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developercenter.spscommerce.com/#/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.spscommerce.com/partners/developers/dev-center/
- group: start
  title: ''
  type: SignUp
  url: https://developercenter.spscommerce.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://www.spscommerce.com/login/
- group: operate
  title: ''
  type: Support
  url: https://www.spscommerce.com/customer-support/support/
- group: company
  title: ''
  type: Blog
  url: https://www.spscommerce.com/community/articles/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SPSCommerce
- group: docs
  title: ''
  type: APIStyleGuide
  url: https://spscommerce.github.io/sps-api-standards/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.spscommerce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spscommerce.com/about/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spscommerce.com/about/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sps-commerce/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/SPSCommerce
created: '2026-10-09'
description: SPS Commerce (Minneapolis, MN) is a retail supply-chain network and cloud services company offering EDI, sales and item data solutions that connect suppliers, retailers, distributors, 3PLs and logistics providers across 300,000+ trading relationships. Its Dev Center (developercenter.spscommerce.com) exposes OAuth-secured API services such as the Transaction API, Shipping Doc API and Trading Partner Submission API, plus MCP documentation, and the company publishes its open SPS API Standards and Spectral ruleset on GitHub.
image: https://www.spscommerce.com/wp-content/uploads/2019/03/sps_logo_only.png
json_schemas:
- name: inline_response_200
  property_count: 2
  slug: sps-commerce-inline-response-200
- name: InventoryImportRequest
  property_count: 2
  slug: sps-commerce-inventory-import-request
- name: SubmissionFormOutput
  property_count: 29
  slug: sps-commerce-submission-form-output
- name: SubmissionFormsResponse
  property_count: 2
  slug: sps-commerce-submission-forms-response
- name: TradingPartnerInput
  property_count: 34
  slug: sps-commerce-trading-partner-input
- name: TradingPartnerResponse
  property_count: 2
  slug: sps-commerce-trading-partner-response
jsonld:
- class_count: 25
  name: Sps Commerce Context
  property_count: 172
  slug: sps-commerce-context
layout: provider
modified: '2026-10-09'
name: SPS Commerce
nav: Providers
network: true
overview: 'SPS Commerce publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Trading Partner Submission API, Inventory API, Import API, and 2 more. Tagged areas include Company, EDI, Retail, Supply Chain, and Commerce.


  The SPS Commerce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SPS Commerce''s developer surface includes sandbox, authentication, getting-started guide, documentation, signup flow, support, engineering blog, and 33 more developer resources.'
plans:
- name: Sps Commerce Plans Pricing
  plan_count: 0
  slug: sps-commerce-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Sps Commerce Rate Limits
  slug: sps-commerce-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: SPS Commerce API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: sps-commerce-rules
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 67.9
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/sps-commerce/refs/heads/main/screenshots/sps-commerce-2026-10-11T130252.png
security:
- kind: authentication
  name: Sps Commerce Authentication
  slug: sps-commerce-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Sps Commerce Domain Security
  slug: sps-commerce-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Sps Commerce Trust Center
  slug: sps-commerce-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: sps-commerce
tags:
- Company
- EDI
- Retail
- Supply Chain
- Commerce
- Trading Partners
- API Standards
website: https://www.spscommerce.com/
---
