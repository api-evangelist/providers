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
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Caldera API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Caldera API
  slug: caldera-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/caldera/rules/caldera-rules.yml
  title: ''
  type: Spectral
  url: rules/caldera-rules.yml
- group: design
  href: https://artifacts.apis.io/caldera/vocabulary/caldera-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/caldera-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/caldera/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/caldera/components/caldera-components.yml
  title: ''
  type: Components
  url: components/caldera-components.yml
- group: auth
  href: https://artifacts.apis.io/caldera/authentication/caldera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/caldera-authentication.yml
- group: design
  href: https://artifacts.apis.io/caldera/conformance/caldera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caldera-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caldera/llms/caldera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caldera-llms.txt
- group: other
  href: https://artifacts.apis.io/caldera/a2a/caldera-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/caldera-a2a.yml
- group: agent
  href: https://artifacts.apis.io/caldera/mcp/caldera-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caldera-mcp.yml
- group: agent
  href: https://artifacts.apis.io/caldera/well-known/caldera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caldera-well-known.yml
- group: other
  href: https://artifacts.apis.io/caldera/hosts/caldera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caldera-hosts.yml
- group: other
  href: https://artifacts.apis.io/caldera/vendors/caldera-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caldera-vendors.yml
- group: build
  href: https://artifacts.apis.io/caldera/packages/caldera-packages.yml
  title: ''
  type: SDKs
  url: packages/caldera-packages.yml
- group: build
  href: https://artifacts.apis.io/caldera/packages/caldera-packages.yml
  title: ''
  type: Packages
  url: packages/caldera-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caldera.xyz/terms
- group: operate
  title: ''
  type: Support
  url: https://support.caldera.xyz/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caldera.xyz/privacy
- group: auth
  href: https://artifacts.apis.io/caldera/security/caldera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caldera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caldera.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.caldera.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.caldera.xyz/metalayer/sdk/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.caldera.xyz/metalayer/sdk/getting-started
- group: company
  title: ''
  type: Blog
  url: https://caldera.xyz/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.caldera.xyz
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation does not publish a machine‑readable OpenAPI spec; the only discovered spec was a sample unrelated to Caldera.
  evidence:
  - status: 200
    url: https://docs.caldera.xyz/rollup-engine/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Caldera builds a network of purpose‑built blockchains that interoperate to settle transactions on Ethereum. The platform enables developers to create modular, scalable chain solutions, offering tools for rollups, metalayer architecture, and cross‑chain asset transfers. Caldera’s ecosystem focuses on security, composability, and developer‑friendly APIs, aiming to accelerate decentralized finance and Web3 applications.
image: https://framerusercontent.com/images/jWh1D23dsV4YtQt0EbqBZ6K2Ds.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.caldera.xyz.
  name: Caldera MCP Server
  slug: caldera-mcp-yml
modified: '2026-10-28'
name: Caldera
nav: Providers
network: true
overview: 'Caldera is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Interoperability, Ethereum, DeFi, and Platform.


  The Caldera catalog on APIs.io includes 1 Spectral governance ruleset.


  Caldera''s developer surface includes authentication, support, documentation, API reference, getting-started guide, engineering blog, and 18 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Caldera API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: caldera-rules
scopes:
- name: Caldera Scopes
  scope_count: 0
  slug: caldera-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 48.1
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/caldera/caldera-2026-11-03T123005.png
security:
- kind: authentication
  name: Caldera Authentication
  slug: caldera-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Caldera Domain Security
  slug: caldera-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: caldera
tags:
- Blockchain
- Interoperability
- Ethereum
- DeFi
- Platform
website: https://caldera.xyz
---
