---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Attestwire Com Agentic Access
  operation_count: 21
  slug: attestwire-com-agentic-access
  summary_line: 21 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: Paddle-hosted subscription checkout, and the customer portal.
  name: Attestwire Billing API
  slug: attestwire-com-billing-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: The Diagnose API from Attestwire — 1 operation(s) for diagnose.
  name: Attestwire Diagnose API
  slug: attestwire-com-diagnose-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: Validation, generation, evidence bundles and e-mail delivery. Metered.
  name: Attestwire Invoices API
  slug: attestwire-com-invoices-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: Self-serve API key issuance.
  name: Attestwire Keys API
  slug: attestwire-com-keys-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: Health and machine-readable descriptions.
  name: Attestwire Meta API
  slug: attestwire-com-meta-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: The Peppol API from Attestwire — 1 operation(s) for peppol.
  name: Attestwire Peppol API
  slug: attestwire-com-peppol-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: The Recipient API from Attestwire — 1 operation(s) for recipient.
  name: Attestwire Recipient API
  slug: attestwire-com-recipient-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: Shareable proof that a check ran. Public, unauthenticated, and free on every plan.
  name: Attestwire Records API
  slug: attestwire-com-records-api
- baseURL: https://api.attestwire.com
  baseurl_source: declared
  description: The Vat API from Attestwire — 1 operation(s) for vat.
  name: Attestwire Vat API
  slug: attestwire-com-vat-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/attestwire-com/agentic-access/attestwire-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/attestwire-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/attestwire-com/rate-limits/attestwire-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/attestwire-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/attestwire-com/plans/attestwire-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/attestwire-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/attestwire-com/rules/attestwire-com-rules.yml
  title: ''
  type: Spectral
  url: rules/attestwire-com-rules.yml
- group: design
  href: https://artifacts.apis.io/attestwire-com/json-ld/attestwire-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/attestwire-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/attestwire-com/vocabulary/attestwire-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/attestwire-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/attestwire-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/attestwire-com/data-model/attestwire-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/attestwire-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/attestwire-com/changelog/attestwire-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/attestwire-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://attestwire.com/security
- group: auth
  href: https://artifacts.apis.io/attestwire-com/authentication/attestwire-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/attestwire-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/attestwire-com/lifecycle/attestwire-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/attestwire-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/attestwire-com/errors/attestwire-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/attestwire-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/attestwire-com/conformance/attestwire-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/attestwire-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/attestwire-com/llms/attestwire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/attestwire-com-llms.txt
- group: build
  href: https://artifacts.apis.io/attestwire-com/mcp/attestwire-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/attestwire-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/attestwire-com/mcp/attestwire-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/attestwire-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/attestwire-com/well-known/attestwire-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/attestwire-com-security.txt
- group: agent
  href: https://artifacts.apis.io/attestwire-com/well-known/attestwire-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/attestwire-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/attestwire-com/hosts/attestwire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attestwire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/attestwire-com/vendors/attestwire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attestwire-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/attestwire-com/packages/attestwire-com-packages.yml
  title: ''
  type: SDKs
  url: packages/attestwire-com-packages.yml
- group: build
  href: https://artifacts.apis.io/attestwire-com/packages/attestwire-com-packages.yml
  title: ''
  type: Packages
  url: packages/attestwire-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://attestwire.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://attestwire.com/changelog
- group: auth
  href: https://artifacts.apis.io/attestwire-com/security/attestwire-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/attestwire-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/attestwire-com/security/attestwire-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/attestwire-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/attestwire-com/security/attestwire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attestwire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://attestwire.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.attestwire.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.attestwire.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.attestwire.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://attestwire.com/playground
- group: operate
  title: ''
  type: Support
  url: mailto:hello@attestwire.com
- group: commercial
  title: ''
  type: Pricing
  url: https://attestwire.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://attestwire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://attestwire.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.attestwire.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attestwire
created: '2026-11-02'
description: Attestwire provides an online service to validate European e‑invoices such as XRechnung and Peppol. Users can paste invoice XML to see which rule failed, get plain‑language explanations, and understand required fixes. The platform also offers a Model Context Protocol (MCP) that lets AI assistants call fourteen compliance tools without an API key, with optional paid plans for higher limits. Documentation, guides, and a rule reference are available publicly.
image: https://attestwire.com/og.png
json_schemas:
- name: InvoiceInput
  property_count: 43
  slug: attestwire-com-invoice-input
- name: ParseResult
  property_count: 9
  slug: attestwire-com-parse-result
- name: SendAccepted
  property_count: 17
  slug: attestwire-com-send-accepted
- name: TeachingError
  property_count: 8
  slug: attestwire-com-teaching-error
- name: ValidationRecord
  property_count: 14
  slug: attestwire-com-validation-record
- name: ValidationResult
  property_count: 17
  slug: attestwire-com-validation-result
jsonld:
- class_count: 51
  name: Attestwire Com Context
  property_count: 226
  slug: attestwire-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.attestwire.com.
  name: Attestwire MCP Server
  slug: attestwire-com-mcp-yml
modified: '2026-11-02'
name: Attestwire
nav: Providers
network: true
overview: 'Attestwire publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Diagnose API, Invoices API, and 6 more. Tagged areas include Attestwire, E-invoice, Validation, XRechnung, and PEPPOL.


  The Attestwire catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Attestwire''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 32 more developer resources.'
plans:
- name: Attestwire Com Plans Pricing
  plan_count: 4
  slug: attestwire-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Attestwire Com Rate Limits
  slug: attestwire-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Attestwire API Rules
  rule_count: 71
  severity_counts:
    error: 51
    hint: 0
    info: 9
    warn: 11
  slug: attestwire-com-rules
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 66.5
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 67.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Attestwire Com Authentication
  slug: attestwire-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Attestwire Com Domain Security
  slug: attestwire-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Attestwire Com Vulnerability Disclosure
  slug: attestwire-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Attestwire Com Trust Center
  slug: attestwire-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 2
skills:
- name: invoice-processing
  slug: attestwire-com-invoice-processing
- name: vat-verification
  slug: attestwire-com-vat-verification
slug: attestwire-com
tags:
- Attestwire
- E-invoice
- Validation
- XRechnung
- PEPPOL
- MCP
website: https://attestwire.com/
---
