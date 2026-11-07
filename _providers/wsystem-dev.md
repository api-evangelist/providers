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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Wsystem Dev Agentic Access
  operation_count: 28
  slug: wsystem-dev-agentic-access
  summary_line: 28 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: The Billing API from wsystem-dev — 3 operation(s) for billing.
  name: wsystem-dev Billing API
  slug: wsystem-dev-billing-api
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: Official business-register lookup (FR, NO, FI, CZ, PL, EE; others via GLEIF LEI)
  name: wsystem-dev Company API
  slug: wsystem-dev-company-api
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: EU e-invoice validation (EN 16931, XRechnung; UBL, CII, ZUGFeRD/Factur-X PDF) and creation (JSON -> UBL)
  name: wsystem-dev E Invoice API
  slug: wsystem-dev-e-invoice-api
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: EU EORI customs number validation via the EC EOS service
  name: wsystem-dev EORI API
  slug: wsystem-dev-eori-api
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: The Health API from wsystem-dev — 1 operation(s) for health.
  name: wsystem-dev Health API
  slug: wsystem-dev-health-api
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: VAT + registry + sanctions in one call with a pass/review/fail verdict
  name: wsystem-dev KYB API
  slug: wsystem-dev-kyb-api
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: Name screening against EU, UN, OFAC SDN and UK sanctions lists (refreshed daily)
  name: wsystem-dev Sanctions API
  slug: wsystem-dev-sanctions-api
- baseURL: https://api.wsystem.dev
  baseurl_source: declared
  description: EU VAT number validation via VIES (27 EU states + XI Northern Ireland)
  name: wsystem-dev VAT API
  slug: wsystem-dev-vat-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/wsystem-dev/agentic-access/wsystem-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wsystem-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/wsystem-dev/plans/wsystem-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wsystem-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wsystem-dev/rules/wsystem-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/wsystem-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/wsystem-dev/json-ld/wsystem-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wsystem-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/wsystem-dev/vocabulary/wsystem-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wsystem-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/wsystem-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/wsystem-dev/data-model/wsystem-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wsystem-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/wsystem-dev/authentication/wsystem-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wsystem-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/wsystem-dev/errors/wsystem-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wsystem-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wsystem-dev/conformance/wsystem-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wsystem-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wsystem-dev/llms/wsystem-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wsystem-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/wsystem-dev/mcp/wsystem-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wsystem-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/wsystem-dev/mcp/wsystem-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wsystem-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/wsystem-dev/well-known/wsystem-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wsystem-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/wsystem-dev/well-known/wsystem-dev-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wsystem-dev-api-security.txt
- group: agent
  href: https://artifacts.apis.io/wsystem-dev/well-known/wsystem-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wsystem-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/wsystem-dev/hosts/wsystem-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wsystem-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/wsystem-dev/vendors/wsystem-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wsystem-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://wsystem.dev/status
- group: auth
  title: ''
  type: Security
  url: https://wsystem.dev/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wsystemdev
- group: auth
  href: https://artifacts.apis.io/wsystem-dev/security/wsystem-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wsystem-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wsystem-dev/security/wsystem-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wsystem-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wsystem.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://wsystem.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.wsystem.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://wsystem.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://api.wsystem.dev/billing/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wsystem.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wsystem.dev/legal/peppol-mandate-terms
created: '2026-10-31'
description: W System provides a comprehensive e‑invoicing API suite for software teams, supporting European standards such as EN 16931, Peppol, and XRechnung. The platform offers invoice validation, generation of UBL documents, buyer identifier lookup, and sandbox testing with signed receipts. It targets developers needing to integrate invoicing, ERP, or shop software to meet upcoming regulatory deadlines across Belgium, France, Germany, the UK and other EU markets.
image: https://wsystem.dev/og.png
json_schemas:
- name: CheckoutReq
  property_count: 11
  slug: wsystem-dev-checkout-req
- name: CompanyBatch
  property_count: 2
  slug: wsystem-dev-company-batch
- name: DDReport
  property_count: 3
  slug: wsystem-dev-ddreport
- name: KybCheck
  property_count: 3
  slug: wsystem-dev-kyb-check
- name: MandateIn
  property_count: 12
  slug: wsystem-dev-mandate-in
- name: SanctionsBatch
  property_count: 2
  slug: wsystem-dev-sanctions-batch
jsonld:
- class_count: 10
  name: Wsystem Dev Context
  property_count: 37
  slug: wsystem-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.wsystem.dev.
  name: wsystem-dev MCP Server
  slug: wsystem-dev-mcp-yml
modified: '2026-10-31'
name: wsystem-dev
nav: Providers
network: true
overview: 'wsystem-dev publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Company API, E Invoice API, and 5 more. Tagged areas include Company, E-Invoicing, European, and Compliance.


  The wsystem-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  wsystem-dev''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Wsystem Dev Plans Pricing
  plan_count: 6
  slug: wsystem-dev-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: wsystem-dev API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: wsystem-dev-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 23.2
    discoverability: 56.7
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wsystem Dev Authentication
  slug: wsystem-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wsystem Dev Domain Security
  slug: wsystem-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wsystem Dev Vulnerability Disclosure
  slug: wsystem-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: wsystem-dev-billing-subscribe
  slug: wsystem-dev-billing-subscribe
- name: wsystem-dev-lookup-company
  slug: wsystem-dev-lookup-company
- name: wsystem-dev-send-e-invoice
  slug: wsystem-dev-send-e-invoice
slug: wsystem-dev
tags:
- Company
- E-Invoicing
- European
- Compliance
website: https://wsystem.dev/
---
