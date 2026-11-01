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
  score: 3.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DiffCI provides AI‑agent enabled CI analysis APIs as described in their documentation.
  name: DiffCI API
  slug: diffci-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/diffci-com/cli/diffci-com-cli.yml
  title: ''
  type: CLI
  url: cli/diffci-com-cli.yml
- group: agent
  href: https://artifacts.apis.io/diffci-com/llms/diffci-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diffci-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/diffci-com/mcp/diffci-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/diffci-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/diffci-com/hosts/diffci-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diffci-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/diffci-com/vendors/diffci-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diffci-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://diffci.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DiffCI
- group: docs
  title: ''
  type: Documentation
  url: https://diffci.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://diffci.com/mcp-server
- group: auth
  href: https://artifacts.apis.io/diffci-com/security/diffci-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diffci-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diffci.com/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://diffci.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: DiffCI provides change‑aware continuous‑integration analysis and test selection tooling. It offers an open‑core CLI and hosted service that measures CI waste by identifying impacted tests and jobs after code changes, enabling developers to run only necessary tests while preserving full‑run safety. The project is open‑source, with a commercial SaaS offering for larger teams, and integrates with GitHub Actions, npm, and AI agents to optimize CI cost and reliability.
image: https://diffci.com/assets/diffci-social-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at diffci.com.
  name: diffci-com MCP Server
  slug: diffci-com-mcp-yml
modified: '2026-10-30'
name: diffci-com
nav: Providers
network: true
overview: 'diffci-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CI, TestSelection, OpenSource, and SaaS.


  diffci-com''s developer surface includes CLI, documentation, getting-started guide, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diffci Com Domain Security
  slug: diffci-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diffci-com
tags:
- Company
- CI
- TestSelection
- OpenSource
- SaaS
website: https://diffci.com/
---
