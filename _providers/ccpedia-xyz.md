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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://ccpedia.xyz
  baseurl_source: declared
  description: Public unauthenticated REST API over the CCPEDIA corpus
  name: CCPEDIA REST API
  slug: ccpedia-rest-api
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/ccpedia-xyz/changelog/ccpedia-xyz-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ccpedia-xyz-changelog.yml
- group: design
  href: https://artifacts.apis.io/ccpedia-xyz/conformance/ccpedia-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ccpedia-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ccpedia-xyz/llms/ccpedia-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ccpedia-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/ccpedia-xyz/mcp/ccpedia-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ccpedia-xyz-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ccpedia-xyz/well-known/ccpedia-xyz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ccpedia-xyz-security.txt
- group: agent
  href: https://artifacts.apis.io/ccpedia-xyz/well-known/ccpedia-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ccpedia-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/ccpedia-xyz/hosts/ccpedia-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ccpedia-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/ccpedia-xyz/vendors/ccpedia-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ccpedia-xyz-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ccpedia.xyz/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://ccpedia.xyz/status
- group: auth
  title: ''
  type: Security
  url: https://ccpedia.xyz/security
- group: start
  title: ''
  type: Sandbox
  url: https://ccpedia.xyz/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ccpedia.xyz/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digital-asset
- group: operate
  title: ''
  type: ChangeLog
  url: https://ccpedia.xyz/releases
- group: company
  title: ''
  type: Blog
  url: https://ccpedia.xyz/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://ccpedia.xyz/docs?q=validator%20onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ccpedia.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://ccpedia.xyz/api/v1/reference
- group: auth
  href: https://artifacts.apis.io/ccpedia-xyz/security/ccpedia-xyz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ccpedia-xyz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ccpedia-xyz/security/ccpedia-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ccpedia-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ccpedia.xyz/
created: '2026-11-04'
description: CCPEDIA is the central knowledge hub for the Canton Network ecosystem, providing indexed, searchable CIPs, documentation, discussions, and whitepapers. It serves developers, researchers, and community members seeking up-to-date blockchain protocol information and resources.
image: https://ccpedia.xyz/opengraph-image?e6f3c1ac252d8af1
layout: provider
mcp_servers:
- description: Remote MCP server at ccpedia.xyz.
  name: CCPEDIA MCP Server
  slug: ccpedia-xyz-mcp-yml
modified: '2026-11-04'
name: CCPEDIA
nav: Providers
network: true
overview: 'CCPEDIA is listed with 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Company, Blockchain, Knowledge Hub, Canton Network, and Open Data.


  CCPEDIA''s developer surface includes changelog, sandbox, engineering blog, getting-started guide, documentation, API reference, and 16 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 34.4
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ccpedia Xyz Domain Security
  slug: ccpedia-xyz-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Ccpedia Xyz Vulnerability Disclosure
  slug: ccpedia-xyz-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ccpedia-xyz
tags:
- Company
- Blockchain
- Knowledge Hub
- Canton Network
- Open Data
website: https://ccpedia.xyz/
---
