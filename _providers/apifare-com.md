---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Apifare Com Agentic Access
  operation_count: 19
  slug: apifare-com-agentic-access
  summary_line: 19 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'Human docs for apifare: get a key, connect your agent, how the prepaid balance, caps and 402 top-ups work, and the API reference.'
  name: Apifare API
  slug: apifare-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/apifare-com/agentic-access/apifare-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apifare-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/apifare-com/rate-limits/apifare-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apifare-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apifare-com/plans/apifare-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apifare-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apifare-com/rules/apifare-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apifare-com-rules.yml
- group: build
  href: https://artifacts.apis.io/apifare-com/cli/apifare-com-cli.yml
  title: ''
  type: CLI
  url: cli/apifare-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/apifare-com/authentication/apifare-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apifare-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/apifare-com/errors/apifare-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apifare-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apifare-com/conformance/apifare-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apifare-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apifare-com/llms/apifare-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apifare-com-llms.txt
- group: build
  href: https://artifacts.apis.io/apifare-com/mcp/apifare-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apifare-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/apifare-com/mcp/apifare-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apifare-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/apifare-com/hosts/apifare-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apifare-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/apifare-com/packages/apifare-com-packages.yml
  title: ''
  type: SDKs
  url: packages/apifare-com-packages.yml
- group: build
  href: https://artifacts.apis.io/apifare-com/packages/apifare-com-packages.yml
  title: ''
  type: Packages
  url: packages/apifare-com-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://apifare.com/tools/c/news
- group: auth
  href: https://artifacts.apis.io/apifare-com/security/apifare-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apifare-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apifare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apifare.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apifare.com/docs#api
- group: start
  title: ''
  type: GettingStarted
  url: https://apifare.com/docs#get-started
- group: operate
  title: ''
  type: Support
  url: https://apifare.com/terms
- group: company
  title: ''
  type: Blog
  url: https://apifare.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apifare
- group: commercial
  title: ''
  type: Pricing
  url: https://apifare.com/docs#pricing
- group: start
  title: ''
  type: SignUp
  url: https://apifare.com/start?origin=site
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apifare.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apifare.com/privacy
created: '2026-10-30'
description: Apifare provides a prepaid, capped, auditable API balance for AI agents, enabling a single key to access any API the agent calls. Users receive a virtual fare card that tracks usage, enforces hard caps, and offers a kill‑switch with signed receipts for each transaction. The service includes free starter credits, transparent pricing, and integrates with major AI models and tooling, positioning it as a universal billing layer for autonomous agents.
image: https://apifare.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at apifare.com requiring an API key.
  name: apifare-com MCP Server
  slug: apifare-com-mcp-yml
modified: '2026-10-30'
name: apifare-com
nav: Providers
network: true
overview: 'apifare-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Payments, Prepaid, Billing, and Agent.


  The apifare-com catalog on APIs.io includes 1 Spectral governance ruleset.


  apifare-com''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 20 more developer resources.'
plans:
- name: Apifare Com Plans Pricing
  plan_count: 2
  slug: apifare-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Apifare Com Rate Limits
  slug: apifare-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: apifare-com API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 0
  slug: apifare-com-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.9
    catalog_earned_first_party: 0.0
    catalog_gap: 50.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 57.3
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 66.7
    operational_transparency: 24.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apifare Com Authentication
  slug: apifare-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apifare Com Domain Security
  slug: apifare-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apifare-com
tags:
- AI
- Payments
- Prepaid
- Billing
- Agent
website: https://apifare.com/
---
