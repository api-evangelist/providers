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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Ab5D Xyz Agentic Access
  operation_count: 16
  slug: ab5d-xyz-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 1
apis:
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Artist Tdh API from AB5D — 2 operation(s) for artist tdh.
  name: AB5D Artist Tdh API
  slug: ab5d-xyz-artist-tdh-api
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Artists API from AB5D — 2 operation(s) for artists.
  name: AB5D Artists API
  slug: ab5d-xyz-artists-api
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Bounties API from AB5D — 5 operation(s) for bounties.
  name: AB5D Bounties API
  slug: ab5d-xyz-bounties-api
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Eligibility API from AB5D — 1 operation(s) for eligibility.
  name: AB5D Eligibility API
  slug: ab5d-xyz-eligibility-api
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Holdings API from AB5D — 1 operation(s) for holdings.
  name: AB5D Holdings API
  slug: ab5d-xyz-holdings-api
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Otdh API from AB5D — 2 operation(s) for otdh.
  name: AB5D Otdh API
  slug: ab5d-xyz-otdh-api
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Receipts.json API from AB5D — 1 operation(s) for receipts.json.
  name: AB5D Receipts.json API
  slug: ab5d-xyz-receipts-json-api
- baseURL: https://ab5d.xyz
  baseurl_source: declared
  description: The Reputation API from AB5D — 1 operation(s) for reputation.
  name: AB5D Reputation API
  slug: ab5d-xyz-reputation-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/ab5d-xyz/agentic-access/ab5d-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ab5d-xyz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ab5d-xyz/rules/ab5d-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/ab5d-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/ab5d-xyz/json-ld/ab5d-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ab5d-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/ab5d-xyz/vocabulary/ab5d-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ab5d-xyz-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ab5d-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ab5d-xyz/data-model/ab5d-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ab5d-xyz-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ab5d-xyz/authentication/ab5d-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ab5d-xyz-authentication.yml
- group: design
  href: https://artifacts.apis.io/ab5d-xyz/errors/ab5d-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ab5d-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ab5d-xyz/conformance/ab5d-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ab5d-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ab5d-xyz/llms/ab5d-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ab5d-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/ab5d-xyz/a2a/ab5d-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ab5d-xyz-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ab5d-xyz/mcp/ab5d-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ab5d-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ab5d-xyz/well-known/ab5d-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ab5d-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/ab5d-xyz/hosts/ab5d-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ab5d-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/ab5d-xyz/vendors/ab5d-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ab5d-xyz-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://ab5d.xyz/register/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ab5d.xyz/privacy/
- group: auth
  href: https://artifacts.apis.io/ab5d-xyz/security/ab5d-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ab5d-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ab5d.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ab5d.xyz/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://ab5d.xyz/developers/
- group: operate
  title: ''
  type: Support
  url: https://ab5d.xyz/contact/
- group: commercial
  title: ''
  type: License
  url: https://ab5d.xyz/license/
created: '2026-10-31'
description: AB5D is a collector‑led archive and argument for the cultural significance of early generative art on Art Blocks. It treats the first five hundred Art Blocks projects (the AB[500]) as a closed cultural period, documenting, analyzing, and preserving them. The archive holds work from 493 of 500 projects, provides essays on each series, and offers a public research API, MCP server, and OpenAPI contract for developers. AB5D aims to assemble, document, and argue for the importance of this early blockchain‑native generative art era.
image: https://ab5d.xyz/brand/ab5d-logo.png
json_schemas:
- name: ChallengeRequest
  property_count: 2
  slug: ab5d-xyz-challenge-request
- name: ClaimRequest
  property_count: 3
  slug: ab5d-xyz-claim-request
- name: SubmissionRequest
  property_count: 5
  slug: ab5d-xyz-submission-request
jsonld:
- class_count: 4
  name: Ab5D Xyz Context
  property_count: 16
  slug: ab5d-xyz-context
layout: provider
mcp_servers:
- description: Remote MCP server at ab5d.xyz.
  name: AB5D MCP Server
  slug: ab5d-xyz-mcp-yml
modified: '2026-10-31'
name: AB5D
nav: Providers
network: true
overview: 'AB5D publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artist Tdh API, Artists API, Bounties API, and 5 more. Tagged areas include Company, Art, Blockchain, Generative Art, and Archives.


  The AB5D catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AB5D''s developer surface includes authentication, signup flow, documentation, support, and 19 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AB5D API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: ab5d-xyz-rules
scopes:
- name: Ab5D Xyz Scopes
  scope_count: 0
  slug: ab5d-xyz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 11.8
    contract_governance: 19.7
    contract_quality: 58.6
    developer_ergonomics: 30.2
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ab5D Xyz Authentication
  slug: ab5d-xyz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ab5D Xyz Domain Security
  slug: ab5d-xyz-domain-security
  summary_line: TLSv1.3
slug: ab5d-xyz
tags:
- Company
- Art
- Blockchain
- Generative Art
- Archives
- NFT
website: https://ab5d.xyz/
---
