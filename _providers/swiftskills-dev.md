---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public MCP streaming endpoint for SwiftSkills AI agent skills.
  name: SwiftSkills MCP
  slug: swiftskills-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/swiftskills-dev/llms/swiftskills-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swiftskills-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/swiftskills-dev/mcp/swiftskills-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/swiftskills-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/swiftskills-dev/well-known/swiftskills-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swiftskills-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/swiftskills-dev/hosts/swiftskills-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swiftskills-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/swiftskills-dev/vendors/swiftskills-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swiftskills-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swiftskills.dev/privacy
- group: auth
  href: https://artifacts.apis.io/swiftskills-dev/security/swiftskills-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swiftskills-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swiftskills.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://swiftskills.dev/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://swiftskills.dev/new
- group: other
  title: ''
  type: Image
  url: https://swiftskills.dev/opengraph-image?9348d17c66563db9
created: '2026-10-31'
description: SwiftSkills provides a curated directory of AI agent skills, MCP servers, and development rules tailored for iOS, Swift, and SwiftUI developers. The platform catalogs 137 AI-powered agent skills that help automate coding, testing, and App Store Connect workflows, offering guides and resources for integrating AI agents into Apple development pipelines.
image: https://swiftskills.dev/opengraph-image?9348d17c66563db9
layout: provider
mcp_servers:
- description: Remote MCP server at swiftskills.dev.
  name: swiftskills-dev MCP Server
  slug: swiftskills-dev-mcp-yml
modified: '2026-10-31'
name: swiftskills-dev
nav: Providers
network: true
overview: 'swiftskills-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Apple, iOS, Swift, and Development.


  swiftskills-dev''s developer surface includes documentation, getting-started guide, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Swiftskills Dev Domain Security
  slug: swiftskills-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swiftskills-dev
tags:
- AI
- Apple
- iOS
- Swift
- Development
website: https://swiftskills.dev/
---
