---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-09-15'
api_count: 10
apis:
- baseURL: https://qa.api.zinnia.io
  baseurl_source: declared
  description: Enterprise API for enforcing policy transactions and validations across the in-force annuity and life book - financial and non-financial transaction management, policy party management, systematic pro
  name: Zinnia Policy Transactions API
  slug: zinnia-policy-transactions-api
- baseURL: https://api.zinnia.io
  baseurl_source: declared
  description: Central policy record service for the life and annuity policy lifecycle - policy detail retrieval by plan code and policy number, policy version history with filtering and pagination, one-time premium
  name: Zinnia Policy Service API
  slug: zinnia-policy-service-api
- baseURL: https://uat.api.zinnia.io
  baseurl_source: declared
  description: Headless order entry API that lets external distribution platforms, banks, broker-dealers and IMOs electronically initiate, save-and-resume, validate and submit life insurance and annuity applications
  name: Zinnia Market Connect Order Entry API
  slug: zinnia-market-connect-order-entry-api
- baseURL: https://dev.api.zinnia.io
  baseurl_source: declared
  description: Illustration generation service for life and annuity products - synchronous and asynchronous illustration requests, in-force, new-business and administration calculation modes, raw numeric projections
  name: Zinnia Illustration Generation API
  slug: zinnia-illustration-generation-api
- baseURL: https://api.zinnia.io
  baseurl_source: declared
  description: The Enterprise Document Service (EDS) is the system of record for documents across Zinnia's life insurance and annuity platforms. Documents are stored once and can be retrieved, updated or searched th
  name: Zinnia Enterprise Documents API
  slug: zinnia-enterprise-documents-api
- baseURL: https://api.zinnia.io
  baseurl_source: declared
  description: Life new business API covering application intake, requirement and case orchestration, party and agent validation, and DTCC-referenced downstream handoff for the Zinnia life new business platform.
  name: Zinnia New Business API
  slug: zinnia-new-business-api
- baseURL: https://api.zinnia.io
  baseurl_source: declared
  description: Annuity new business API for application submission, case status, requirements and DTCC participant resolution on the Zinnia annuity origination platform.
  name: Zinnia New Business Annuity API
  slug: zinnia-new-business-annuity-api
- baseURL: https://uat.api.zinnia.io
  baseurl_source: declared
  description: Product configuration and reference data service - product definitions, features, eligibility rules and related metadata for insurance and financial offerings, so partners can configure, present and i
  name: Zinnia Product Service API
  slug: zinnia-product-service-api
- baseURL: https://api.zinnia.io
  baseurl_source: declared
  description: Case orchestration API for creating and retrieving case instances that group the documents, requirements and transactions belonging to a single piece of work across the Zinnia platform.
  name: Zinnia Case Management API
  slug: zinnia-case-management-api
- baseURL: https://uat.api.zinnia.io
  baseurl_source: declared
  description: Client case manager for the illustration workflow - create, search, retrieve and update the client-level cases that illustration requests are generated against.
  name: Zinnia Illustration Client Cases API
  slug: zinnia-illustration-client-cases-api
artifact_total: 15
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/security/zinnia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zinnia-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/authentication/zinnia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zinnia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zinnia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.zinnia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zinnia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zinnia.com/
- group: company
  title: ''
  type: Blog
  url: https://zinnia.com/insights
- group: operate
  title: ''
  type: Support
  url: https://zinnia.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zinnia.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zinnia.com/privacy-policy
- group: other
  title: ''
  type: OpenIDConnect
  url: https://login.zinnia.com/.well-known/openid-configuration
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/scopes/zinnia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zinnia-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/conventions/zinnia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zinnia-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/errors/zinnia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zinnia-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/data-model/zinnia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zinnia-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/lifecycle/zinnia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zinnia-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/changelog/zinnia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zinnia-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/conformance/zinnia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zinnia-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/well-known/zinnia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zinnia-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/llms/zinnia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zinnia-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developers.zinnia.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/plans/zinnia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zinnia-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zinnia/refs/heads/main/rate-limits/zinnia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zinnia-rate-limits.yml
created: '2026-09-13'
description: Zinnia is an Eldridge-backed insurance technology and third-party administration company that provides the policy administration, new business, order entry, illustration, document and in-force servicing infrastructure behind a large share of the US life insurance and annuity market. Formerly SE2, and now the parent of Policygenius, Ebix's life and annuity software assets, AnnuityNet, VitalQuote, WinFlex, SmartOffice and Zahara, Zinnia runs an enterprise API gateway at api.zinnia.io and publishes ten OpenAPI contracts on a Kong developer portal at developers.zinnia.com covering case management, enterprise documents, illustration generation, product configuration, new business for life and annuity, Market Connect headless order entry, policy detail, and 102 policy transaction operations. Zinnia contributed its Enterprise API framework to the Insured Retirement Institute, whose first four standardized in-force annuity transaction APIs are built on it.
image: https://zinnia.com/assets/brand/zinnia-logo-horizontal-full-color.svg
layout: provider
modified: '2026-09-13'
name: Zinnia
nav: Providers
network: true
overview: 'Zinnia publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Policy Transactions API, Policy Service API, Market Connect Order Entry API, and 7 more. Tagged areas include Insurance, Life Insurance, Annuities, Policy Administration, and Insurtech.


  Zinnia''s developer surface includes authentication, documentation, API reference, engineering blog, support, changelog, and 18 more developer resources.'
plans:
- name: Zinnia Plans Pricing
  plan_count: 0
  slug: zinnia-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Zinnia Rate Limits
  slug: zinnia-rate-limits
scopes:
- name: Zinnia Scopes
  scope_count: 0
  slug: zinnia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 59.7
    developer_ergonomics: 47.0
    discoverability: 81.5
    operational_transparency: 15.8
  previous_composite: 48.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Zinnia Authentication
  slug: zinnia-authentication
  summary_line: openIdConnect/http · 3 schemes
- kind: domain-security
  name: Zinnia Domain Security
  slug: zinnia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zinnia
tags:
- Insurance
- Life Insurance
- Annuities
- Policy Administration
- Insurtech
- Financial-Services
- Third Party Administration
- New Business
- Order Entry
- Document-Management
- Underwriting
- Enterprise
website: https://zinnia.com/
---
