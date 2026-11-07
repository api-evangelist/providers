---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 81
  human_in_the_loop: 0
  name: Track Agentic Access
  operation_count: 136
  slug: track-agentic-access
  summary_line: 136 operations · 81 acting
api_count: 2
apis:
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Accounts API from Track — 11 operation(s) for accounts.
  name: Track Accounts API
  slug: track-accounts-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Catalogue API from Track — 21 operation(s) for catalogue.
  name: Track Catalogue API
  slug: track-catalogue-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Contracts API from Track — 4 operation(s) for contracts.
  name: Track Contracts API
  slug: track-contracts-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Expenses API from Track — 3 operation(s) for expenses.
  name: Track Expenses API
  slug: track-expenses-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Imports API from Track — 8 operation(s) for imports.
  name: Track Imports API
  slug: track-imports-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Ledger API from Track — 2 operation(s) for ledger.
  name: Track Ledger API
  slug: track-ledger-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Payments API from Track — 7 operation(s) for payments.
  name: Track Payments API
  slug: track-payments-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Portal API from Track — 3 operation(s) for portal.
  name: Track Portal API
  slug: track-portal-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Revenue API from Track — 23 operation(s) for revenue.
  name: Track Revenue API
  slug: track-revenue-api
- baseURL: https://api.trackroyalty.com
  baseurl_source: declared
  description: The Open API API from Track — 1 operation(s) for open api.
  name: Track Open API
  slug: track-open-api-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/track/agentic-access/track-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/track-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/track/rules/track-rules.yml
  title: ''
  type: Spectral
  url: rules/track-rules.yml
- group: design
  href: https://artifacts.apis.io/track/json-ld/track-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/track-context.jsonld
- group: design
  href: https://artifacts.apis.io/track/vocabulary/track-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/track-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/track/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/track/data-model/track-data-model.yml
  title: ''
  type: DataModel
  url: data-model/track-data-model.yml
- group: design
  href: https://artifacts.apis.io/track/errors/track-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/track-problem-types.yml
- group: design
  href: https://artifacts.apis.io/track/conformance/track-conformance.yml
  title: ''
  type: Conformance
  url: conformance/track-conformance.yml
- group: other
  href: https://artifacts.apis.io/track/hosts/track-hosts.yml
  title: ''
  type: Hosts
  url: hosts/track-hosts.yml
- group: other
  href: https://artifacts.apis.io/track/vendors/track-vendors.yml
  title: ''
  type: Vendors
  url: vendors/track-vendors.yml
- group: auth
  href: https://artifacts.apis.io/track/authentication/track-authentication.yml
  title: ''
  type: Authentication
  url: authentication/track-authentication.yml
- group: auth
  href: https://artifacts.apis.io/track/security/track-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/track-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trackroyalty.com
created: '2026-10-29'
description: 'Track Royalties Inc. (brand: Track) provides a global banking, accounting, and payment infrastructure tailored for the music industry. It enables artists, labels, and rights holders to manage royalty collections, automate payouts, and gain real‑time financial insights across streaming platforms and other revenue sources. The platform aims to simplify complex royalty workflows, offering APIs for integration with music services, fintech partners, and enterprise systems, while ensuring compliance with industry standards and supporting scalable, secure transactions worldwide.'
image: https://framerusercontent.com/images/oZje8yQQ8PZLn8jW3K6rBwcc.png?width=381&height=81
json_schemas:
- name: ContractDetails
  property_count: 36
  slug: track-contract-details
- name: PatchedContract
  property_count: 31
  slug: track-patched-contract
- name: PatchedRevenueStatement
  property_count: 32
  slug: track-patched-revenue-statement
- name: PortalRoyaltyStatement
  property_count: 21
  slug: track-portal-royalty-statement
- name: RevenueStatement
  property_count: 32
  slug: track-revenue-statement
- name: RoyaltyStatement
  property_count: 22
  slug: track-royalty-statement
jsonld:
- class_count: 120
  name: Track Context
  property_count: 239
  slug: track-context
layout: provider
modified: '2026-10-29'
name: Track
nav: Providers
network: true
overview: 'Track publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Catalogue API, Contracts API, and 7 more. Tagged areas include Music, Fintech, Royalties, Payments, and Banking.


  The Track catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Track''s developer surface includes authentication and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Track API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 2
  slug: track-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.8
    developer_ergonomics: 18.3
    discoverability: 66.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/track/track-2026-11-03T144943.png
security:
- kind: authentication
  name: Track Authentication
  slug: track-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Track Domain Security
  slug: track-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-labels
  slug: track-list-labels
slug: track
tags:
- Music
- Fintech
- Royalties
- Payments
- Banking
website: https://trackroyalty.com
---
