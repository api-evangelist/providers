---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Invoicexml Com Agentic Access
  operation_count: 61
  slug: invoicexml-com-agentic-access
  summary_line: 61 operations · 58 acting
api_count: 1
apis:
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Convert API from invoicexml-com — 16 operation(s) for convert.
  name: invoicexml-com Convert API
  slug: invoicexml-com-convert-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Create API from invoicexml-com — 12 operation(s) for create.
  name: invoicexml-com Create API
  slug: invoicexml-com-create-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Embed API from invoicexml-com — 5 operation(s) for embed.
  name: invoicexml-com Embed API
  slug: invoicexml-com-embed-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Extract API from invoicexml-com — 3 operation(s) for extract.
  name: invoicexml-com Extract API
  slug: invoicexml-com-extract-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Home API from invoicexml-com — 1 operation(s) for home.
  name: invoicexml-com Home API
  slug: invoicexml-com-home-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The InvoiceXml.Api API from invoicexml-com — 1 operation(s) for invoicexml.api.
  name: invoicexml-com Invoice Xml.Api API
  slug: invoicexml-com-invoicexml-api-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Me API from invoicexml-com — 1 operation(s) for me.
  name: invoicexml-com Me API
  slug: invoicexml-com-me-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Parse API from invoicexml-com — 1 operation(s) for parse.
  name: invoicexml-com Parse API
  slug: invoicexml-com-parse-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Render API from invoicexml-com — 4 operation(s) for render.
  name: invoicexml-com Render API
  slug: invoicexml-com-render-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Transform API from invoicexml-com — 5 operation(s) for transform.
  name: invoicexml-com Transform API
  slug: invoicexml-com-transform-api
- baseURL: https://api.invoicexml.com
  baseurl_source: declared
  description: The Validate API from invoicexml-com — 12 operation(s) for validate.
  name: invoicexml-com Validate API
  slug: invoicexml-com-validate-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/invoicexml-com/agentic-access/invoicexml-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/invoicexml-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/invoicexml-com/plans/invoicexml-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/invoicexml-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/invoicexml-com/rules/invoicexml-com-rules.yml
  title: ''
  type: Spectral
  url: rules/invoicexml-com-rules.yml
- group: design
  href: https://artifacts.apis.io/invoicexml-com/json-ld/invoicexml-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/invoicexml-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/invoicexml-com/vocabulary/invoicexml-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/invoicexml-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/invoicexml-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/invoicexml-com/data-model/invoicexml-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/invoicexml-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.invoicexml.com/trust
- group: design
  href: https://artifacts.apis.io/invoicexml-com/errors/invoicexml-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/invoicexml-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/invoicexml-com/conformance/invoicexml-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/invoicexml-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/invoicexml-com/llms/invoicexml-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/invoicexml-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/invoicexml-com/well-known/invoicexml-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/invoicexml-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/invoicexml-com/hosts/invoicexml-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/invoicexml-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/invoicexml-com/vendors/invoicexml-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/invoicexml-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/invoicexml-com/packages/invoicexml-com-packages.yml
  title: ''
  type: SDKs
  url: packages/invoicexml-com-packages.yml
- group: build
  href: https://artifacts.apis.io/invoicexml-com/packages/invoicexml-com-packages.yml
  title: ''
  type: Packages
  url: packages/invoicexml-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.invoicexml.com/account/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.invoicexml.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.invoicexml.com</code
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InvoiceXML
- group: auth
  href: https://artifacts.apis.io/invoicexml-com/security/invoicexml-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/invoicexml-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/invoicexml-com/security/invoicexml-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invoicexml-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/invoicexml-com/security/invoicexml-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/invoicexml-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/invoicexml-com/security/invoicexml-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invoicexml-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.invoicexml.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.invoicexml.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.invoicexml.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.invoicexml.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.invoicexml.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.invoicexml.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.invoicexml.com/privacy
created: '2026-10-30'
description: InvoiceXML provides a RESTful e‑invoicing service that creates, validates, converts, renders, extracts and validates invoices in multiple European standards (Peppol BIS, XRechnung, Factur‑X, ZUGFeRD, UBL, CII). The platform offers a public OpenAPI 3.1 specification, free online conversion tools, a 30‑day free trial with no credit‑card required, and detailed documentation covering API reference, pricing, and compliance. It targets businesses needing automated invoice processing and compliance with EN 16931. The service is hosted at api.invoicexml.com and documented at www.invoicexml.com.
image: https://www.invoicexml.com/img/logo.svg
json_schemas:
- name: CreateInvoiceEmailRequest
  property_count: 3
  slug: invoicexml-com-create-invoice-email-request
- name: CreateInvoiceRequest
  property_count: 2
  slug: invoicexml-com-create-invoice-request
- name: CreateOrderRequest
  property_count: 2
  slug: invoicexml-com-create-order-request
- name: InvoiceJsonResponse
  property_count: 3
  slug: invoicexml-com-invoice-json-response
- name: MeResponse
  property_count: 6
  slug: invoicexml-com-me-response
- name: ValidationResponse
  property_count: 6
  slug: invoicexml-com-validation-response
jsonld:
- class_count: 58
  name: Invoicexml Com Context
  property_count: 184
  slug: invoicexml-com-context
layout: provider
modified: '2026-10-30'
name: invoicexml-com
nav: Providers
network: true
overview: 'invoicexml-com publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Convert API, Create API, Embed API, and 8 more. Tagged areas include Company, E-Invoicing, API, Finance, and Compliance.


  The invoicexml-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  invoicexml-com''s developer surface includes changelog, documentation, API reference, pricing, engineering blog, and 26 more developer resources.'
plans:
- name: Invoicexml Com Plans Pricing
  plan_count: 4
  slug: invoicexml-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Invoicexml Com Rate Limits
  slug: invoicexml-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: invoicexml-com API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 5
  slug: invoicexml-com-rules
scopes:
- name: Invoicexml Com Scopes
  scope_count: 0
  slug: invoicexml-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 88.9
    contract_governance: 79.1
    contract_quality: 52.7
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Invoicexml Com Authentication
  slug: invoicexml-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Invoicexml Com Domain Security
  slug: invoicexml-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Invoicexml Com Trust Center
  slug: invoicexml-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: invoicexml-com
tags:
- Company
- E-Invoicing
- API
- Finance
- Compliance
- European Standards
website: https://www.invoicexml.com/
---
