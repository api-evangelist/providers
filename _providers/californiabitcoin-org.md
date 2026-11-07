---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://californiabitcoin.org
  baseurl_source: declared
  description: The A2a API from California Bitcoin — 1 operation(s) for a2a.
  name: California Bitcoin A2a API
  slug: californiabitcoin-org-a2a-api
- baseURL: https://californiabitcoin.org
  baseurl_source: declared
  description: The Agent API from California Bitcoin — 15 operation(s) for agent.
  name: California Bitcoin Agent API
  slug: californiabitcoin-org-agent-api
- baseURL: https://californiabitcoin.org
  baseurl_source: declared
  description: The Mcp API from California Bitcoin — 1 operation(s) for mcp.
  name: California Bitcoin MCP API
  slug: californiabitcoin-org-mcp-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/californiabitcoin-org/security/californiabitcoin-org-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/californiabitcoin-org-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/californiabitcoin-org/errors/californiabitcoin-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/californiabitcoin-org-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/californiabitcoin-org/llms/californiabitcoin-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/californiabitcoin-org-llms.txt
- group: other
  href: https://artifacts.apis.io/californiabitcoin-org/a2a/californiabitcoin-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/californiabitcoin-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/californiabitcoin-org/mcp/californiabitcoin-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/californiabitcoin-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/californiabitcoin-org/well-known/californiabitcoin-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/californiabitcoin-org-security.txt
- group: agent
  href: https://artifacts.apis.io/californiabitcoin-org/well-known/californiabitcoin-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/californiabitcoin-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/californiabitcoin-org/hosts/californiabitcoin-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/californiabitcoin-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/californiabitcoin-org/vendors/californiabitcoin-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/californiabitcoin-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://californiabitcoin.org/terms/
- group: operate
  title: ''
  type: Support
  url: https://californiabitcoin.org/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://californiabitcoin.org/privacy/
- group: docs
  title: ''
  type: APIReference
  url: https://californiabitcoin.org/developers/
- group: auth
  href: https://artifacts.apis.io/californiabitcoin-org/security/californiabitcoin-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/californiabitcoin-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/californiabitcoin-org/security/californiabitcoin-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/californiabitcoin-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://californiabitcoin.org/
- group: docs
  title: ''
  type: Documentation
  url: https://californiabitcoin.org/about/
- group: start
  title: ''
  type: GettingStarted
  url: https://californiabitcoin.org/learn/
- group: company
  title: ''
  type: Blog
  url: https://californiabitcoin.org/articles/
created: '2026-11-03'
description: California Bitcoin is an independent Bitcoin education project offering curated articles, guided lessons, and source‑backed answers. It aims to help learners explore Bitcoin through a library of resources, a membership learning journey, and community engagement, fostering deeper understanding of cryptocurrency technology and its ecosystem.
image: https://californiabitcoin.org/assets/california-bitcoin-share-2026.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at californiabitcoin.org.
  name: California Bitcoin MCP Server
  slug: californiabitcoin-org-mcp-yml
modified: '2026-11-03'
name: California Bitcoin
nav: Providers
network: true
overview: 'California Bitcoin publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: A2a API, Agent API, and MCP API. Tagged areas include Bitcoin, Education, Cryptocurrency, Learning, and Community.


  California Bitcoin''s developer surface includes support, API reference, documentation, getting-started guide, engineering blog, and 14 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 46.5
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Californiabitcoin Org Domain Security
  slug: californiabitcoin-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Californiabitcoin Org Vulnerability Disclosure
  slug: californiabitcoin-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: californiabitcoin-org
tags:
- Bitcoin
- Education
- Cryptocurrency
- Learning
- Community
website: https://californiabitcoin.org/
---
