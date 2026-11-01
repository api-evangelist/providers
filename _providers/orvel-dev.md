---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Orvel Dev Agentic Access
  operation_count: 60
  slug: orvel-dev-agentic-access
  summary_line: 60 operations · 22 acting
api_count: 2
apis:
- baseURL: https://facturx.orvel.dev
  baseurl_source: declared
  description: The e-invoicing API from orvel-dev — 14 operation(s) for e-invoicing.
  name: orvel-dev E Invoicing API
  slug: orvel-dev-e-invoicing-api
- baseURL: https://facturx.orvel.dev
  baseurl_source: declared
  description: The verification API from orvel-dev — 15 operation(s) for verification.
  name: orvel-dev Verification API
  slug: orvel-dev-verification-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/orvel-dev/agentic-access/orvel-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/orvel-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/orvel-dev/plans/orvel-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orvel-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/orvel-dev/rules/orvel-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/orvel-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/orvel-dev/json-ld/orvel-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/orvel-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/orvel-dev/vocabulary/orvel-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/orvel-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/orvel-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/orvel-dev/data-model/orvel-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orvel-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/orvel-dev/authentication/orvel-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orvel-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/orvel-dev/errors/orvel-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/orvel-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/orvel-dev/conformance/orvel-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orvel-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/orvel-dev/mcp/orvel-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/orvel-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/orvel-dev/well-known/orvel-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orvel-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/orvel-dev/hosts/orvel-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orvel-dev-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://access.orvel.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orvel.dev/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://facturx.orvel.dev/docs/pricing/
- group: start
  title: ''
  type: Login
  url: https://orvel.dev/admin/login
- group: docs
  title: ''
  type: Documentation
  url: https://facturx.orvel.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://facturx.orvel.dev/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/orvel-dev/security/orvel-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orvel-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orvel.dev/
created: '2026-10-30'
description: Orvel provides e‑invoicing and accessibility tools for businesses operating in France and the EU. It offers ready‑to‑use solutions for mandatory e‑invoicing compliance (Factur‑X, CII, UBL) and the European Accessibility Act, delivered via browser, API, or AI‑assistant integrations. The platform includes a Factur‑X validator, an accessibility audit record, and developer tools, all hosted in the EU and built in Brittany, France.
image: https://orvel.dev/opengraph-image?c0b2f34618238454
json_schemas:
- name: AddressRequest
  property_count: 4
  slug: orvel-dev-address-request
- name: Body_embed_v1_invoices_embed_post
  property_count: 6
  slug: orvel-dev-body-embed-v1-invoices-embed-post
- name: Body_extract_v1_invoices_extract_post
  property_count: 1
  slug: orvel-dev-body-extract-v1-invoices-extract-post
- name: Body_validate_v1_invoices_validate_post
  property_count: 1
  slug: orvel-dev-body-validate-v1-invoices-validate-post
- name: ExtractOut
  property_count: 6
  slug: orvel-dev-extract-out
- name: InvoicePartyRequest
  property_count: 11
  slug: orvel-dev-invoice-party-request
- name: UsageOut
  property_count: 5
  slug: orvel-dev-usage-out
- name: ValidationOut
  property_count: 19
  slug: orvel-dev-validation-out
jsonld:
- class_count: 33
  name: Orvel Dev Context
  property_count: 188
  slug: orvel-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at facturx.orvel.dev.
  name: orvel-dev MCP Server
  slug: orvel-dev-mcp-yml
modified: '2026-10-30'
name: orvel-dev
nav: Providers
network: true
overview: 'orvel-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: E Invoicing API and Verification API. Tagged areas include e-invoicing, accessibility, API, France, and EU.


  The orvel-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  orvel-dev''s developer surface includes authentication, pricing, documentation, getting-started guide, and 17 more developer resources.'
plans:
- name: Orvel Dev Plans Pricing
  plan_count: 3
  slug: orvel-dev-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: orvel-dev API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: orvel-dev-rules
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 33.3
    contract_quality: 54.0
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Orvel Dev Authentication
  slug: orvel-dev-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Orvel Dev Domain Security
  slug: orvel-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orvel-dev
tags:
- e-invoicing
- accessibility
- API
- France
- EU
website: https://orvel.dev/
---
