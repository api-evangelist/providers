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
  band: agent-ready
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Damagerestorehq Com Agentic Access
  operation_count: 17
  slug: damagerestorehq-com-agentic-access
  summary_line: 17 operations · 14 acting
api_count: 1
apis:
- description: Provides access to median paid water damage claim data from NFIP records (2023‑2026) and related restoration cost statistics.
  name: DamageRestore HQ API
  slug: damagerestore-hq-api
- baseURL: https://damagerestorehq.com
  baseurl_source: declared
  description: dataset
  name: damagerestorehq-com Dataset API
  slug: damagerestorehq-com-dataset-api
- baseURL: https://damagerestorehq.com
  baseurl_source: declared
  description: enquiry
  name: damagerestorehq-com Enquiry API
  slug: damagerestorehq-com-enquiry-api
- baseURL: https://damagerestorehq.com
  baseurl_source: declared
  description: entities
  name: damagerestorehq-com Entities API
  slug: damagerestorehq-com-entities-api
- baseURL: https://damagerestorehq.com
  baseurl_source: declared
  description: The mcp API from damagerestorehq-com — 1 operation(s) for mcp.
  name: damagerestorehq-com MCP API
  slug: damagerestorehq-com-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/damagerestorehq-com/agentic-access/damagerestorehq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/damagerestorehq-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/damagerestorehq-com/rules/damagerestorehq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/damagerestorehq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/damagerestorehq-com/vocabulary/damagerestorehq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/damagerestorehq-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/damagerestorehq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://damagerestorehq.com/terms
- group: design
  href: https://artifacts.apis.io/damagerestorehq-com/errors/damagerestorehq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/damagerestorehq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/damagerestorehq-com/conformance/damagerestorehq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/damagerestorehq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/damagerestorehq-com/llms/damagerestorehq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/damagerestorehq-com-llms.txt
- group: build
  href: https://artifacts.apis.io/damagerestorehq-com/mcp/damagerestorehq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/damagerestorehq-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/damagerestorehq-com/mcp/damagerestorehq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/damagerestorehq-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/damagerestorehq-com/well-known/damagerestorehq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/damagerestorehq-com-security.txt
- group: agent
  href: https://artifacts.apis.io/damagerestorehq-com/well-known/damagerestorehq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/damagerestorehq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/damagerestorehq-com/hosts/damagerestorehq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/damagerestorehq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/damagerestorehq-com/vendors/damagerestorehq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/damagerestorehq-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/damagerestorehq-com/authentication/damagerestorehq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/damagerestorehq-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/damagerestorehq-com/security/damagerestorehq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/damagerestorehq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/damagerestorehq-com/security/damagerestorehq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/damagerestorehq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://damagerestorehq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://damagerestorehq.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://damagerestorehq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://damagerestorehq.com/privacy/
- group: operate
  title: ''
  type: Support
  url: mailto:quotes@damagerestorehq.com
- group: build
  title: ''
  type: Postman
  url: https://damagerestorehq.com/
created: '2026-10-29'
description: DamageRestore HQ provides data-driven insights into water damage restoration costs across the United States, leveraging over 106,000 NFIP claim records from 2023‑2026. The service offers median payout statistics, regional cost breakdowns, and connects users with local restoration professionals. It also supplies an OpenAPI 3.1 endpoint for programmatic access to claim data and related metrics.
image: https://damagerestorehq.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at damagerestorehq.com.
  name: damagerestorehq-com MCP Server
  slug: damagerestorehq-com-mcp-yml
modified: '2026-10-29'
name: damagerestorehq-com
nav: Providers
network: true
overview: 'damagerestorehq-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dataset API, Enquiry API, Entities API, and 2 more. Tagged areas include WaterDamage, Insurance, Restoration, US, and Data.


  The damagerestorehq-com catalog on APIs.io includes 1 Spectral governance ruleset.


  damagerestorehq-com''s developer surface includes authentication, API reference, support, and 20 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: damagerestorehq-com API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 1
  slug: damagerestorehq-com-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 49.4
    developer_ergonomics: 29.0
    discoverability: 75.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 23.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/damagerestorehq-com/damagerestorehq-com-2026-11-03T130026.png
security:
- kind: authentication
  name: Damagerestorehq Com Authentication
  slug: damagerestorehq-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Damagerestorehq Com Domain Security
  slug: damagerestorehq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Damagerestorehq Com Vulnerability Disclosure
  slug: damagerestorehq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: damagerestorehq-com-skill
  slug: damagerestorehq-com-skill
slug: damagerestorehq-com
tags:
- WaterDamage
- Insurance
- Restoration
- US
- Data
website: https://damagerestorehq.com/
---
