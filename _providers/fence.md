---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Fence Agentic Access
  operation_count: 12
  slug: fence-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dev-api.fence.finance
  baseurl_source: declared
  description: Obtain a bearer access token for a machine-to-machine integration.
  name: Fence Authentication API
  slug: fence-authentication-api
- baseURL: https://dev-api.fence.finance
  baseurl_source: declared
  description: Monitor declaration runs and per-asset results.
  name: Fence Declaration monitoring API
  slug: fence-declaration-monitoring-api
- baseURL: https://dev-api.fence.finance
  baseurl_source: declared
  description: Register supporting documents and inspect upload status.
  name: Fence Documents API
  slug: fence-documents-api
- baseURL: https://dev-api.fence.finance
  baseurl_source: declared
  description: Validate or submit payment transactions in bulk.
  name: Fence Payments API
  slug: fence-payments-api
- baseURL: https://dev-api.fence.finance
  baseurl_source: declared
  description: Create and process asset portfolio declarations.
  name: Fence Portfolio declarations API
  slug: fence-portfolio-declarations-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/fence/agentic-access/fence-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fence-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fence/rules/fence-rules.yml
  title: ''
  type: Spectral
  url: rules/fence-rules.yml
- group: design
  href: https://artifacts.apis.io/fence/json-ld/fence-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fence-context.jsonld
- group: design
  href: https://artifacts.apis.io/fence/vocabulary/fence-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fence-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fence/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fence/data-model/fence-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fence-data-model.yml
- group: design
  href: https://artifacts.apis.io/fence/conventions/fence-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fence-conventions.yml
- group: design
  href: https://artifacts.apis.io/fence/conventions/fence-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fence-conventions.yml
- group: auth
  href: https://artifacts.apis.io/fence/authentication/fence-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fence-authentication.yml
- group: design
  href: https://artifacts.apis.io/fence/errors/fence-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fence-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fence/conformance/fence-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fence-conformance.yml
- group: other
  href: https://artifacts.apis.io/fence/overlays/fence-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fence-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/fence/llms/fence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fence-llms.txt
- group: agent
  href: https://artifacts.apis.io/fence/well-known/fence-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fence-well-known.yml
- group: other
  href: https://artifacts.apis.io/fence/hosts/fence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fence-hosts.yml
- group: other
  href: https://artifacts.apis.io/fence/vendors/fence-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fence-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://fence.finance/security
- group: company
  title: ''
  type: Blog
  url: https://fence.finance/blog/8-abf-learnings
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fence.finance/
- group: auth
  href: https://artifacts.apis.io/fence/security/fence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fence.finance/
- group: docs
  title: ''
  type: APIReference
  url: https://fence.finance/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://fence.finance/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fence.finance/privacy/
created: '2026-10-29'
description: Fence is a tech‑native facility agency for asset‑backed finance, providing real‑time control and transparency for lenders and originators. It builds the operating layer that connects assets such as credit cards, invoices, BNPL purchases, auto loans, leases, and mortgages with capital instantly, enabling faster, cheaper financing while maintaining full traceability and compliance.
image: https://fence.finance/assets/fence_logo.png
json_schemas:
- name: AsyncPaymentsAccepted
  property_count: 6
  slug: fence-async-payments-accepted
- name: BulkOperationResult
  property_count: 8
  slug: fence-bulk-operation-result
- name: DealSpecificAsset
  property_count: 3
  slug: fence-deal-specific-asset
- name: DeclarationRunAsset
  property_count: 7
  slug: fence-declaration-run-asset
- name: DeclarationRun
  property_count: 8
  slug: fence-declaration-run
- name: PortfolioDeclaration
  property_count: 6
  slug: fence-portfolio-declaration
jsonld:
- class_count: 29
  name: Fence Context
  property_count: 71
  slug: fence-context
layout: provider
modified: '2026-10-29'
name: Fence
nav: Providers
network: true
overview: 'Fence publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Declaration monitoring API, Documents API, and 2 more. Tagged areas include Company, Fintech, Asset-Backed-Finance, Real-Time, and API.


  The Fence catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fence''s developer surface includes authentication, engineering blog, documentation, API reference, support, and 19 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 0
  name: Fence Rate Limits
  slug: fence-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Fence API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: fence-rules
scopes:
- name: Fence Scopes
  scope_count: 0
  slug: fence-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 64.1
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fence Authentication
  slug: fence-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fence Domain Security
  slug: fence-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: authentication
  slug: fence-authentication-skill
- name: declaration-monitoring
  slug: fence-declaration-monitoring-skill
- name: documents
  slug: fence-documents-skill
- name: payments
  slug: fence-payments-skill
- name: portfolio-declarations
  slug: fence-portfolio-declarations-skill
slug: fence
tags:
- Company
- Fintech
- Asset-Backed-Finance
- Real-Time
- API
website: https://fence.finance/
---
