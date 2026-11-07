---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Mapped API is a single GraphQL endpoint exposing every query, mutation and type of the Mapped building world model (70 queries, 99 mutations), authenticated with a Personal Access Token sent in th
  name: Mapped GraphQL API
  slug: mapped-graphql-api
- description: Hosted Mapped Model Context Protocol server with two tool sets - GraphQL generation and execution against the Mapped API, and Mapped ontology navigation. The endpoint answers anonymous tools/list with
  name: Mapped MCP Server
  slug: mapped-mcp-server
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/mapped-com/well-known/mapped-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mapped-com-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/mapped-com/plans/mapped-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mapped-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mapped-com/changelog/mapped-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mapped-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/mapped-com/conventions/mapped-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mapped-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/mapped-com/sandbox/mapped-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mapped-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/mapped-com/authentication/mapped-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mapped-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mapped-com/scopes/mapped-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mapped-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/mapped-com/lifecycle/mapped-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mapped-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mapped-com/errors/mapped-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mapped-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mapped-com/conformance/mapped-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mapped-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mapped-com/llms/mapped-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mapped-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/mapped-com/mcp/mapped-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mapped-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mapped-com/well-known/mapped-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mapped-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/mapped-com/hosts/mapped-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mapped-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/mapped-com/integrations/mapped-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/mapped-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/mapped-com/vendors/mapped-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mapped-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/mapped-com/packages/mapped-com-packages.yml
  title: ''
  type: SDKs
  url: packages/mapped-com-packages.yml
- group: build
  href: https://artifacts.apis.io/mapped-com/packages/mapped-com-packages.yml
  title: ''
  type: Packages
  url: packages/mapped-com-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.mapped.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.mapped.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mapped.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mapped.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mapped.com/guides/platform/introduction
- group: operate
  title: ''
  type: Support
  url: https://support.mapped.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.mapped.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mapped.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mapped.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mapped
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mapped.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mapped.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.mapped.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mapped.com/legal/CustomerAgreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mapped.com/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/mapped-com/security/mapped-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mapped-com-domain-security.yml
created: '2026-10-18'
description: Mapped turns any building's systems, sensors, and devices into a structured, real-time world model — the data foundation AI agents and applications need to understand and act on the physical world. Its platform normalizes building data through source and destination connectors and on-premises gateways into an ontology based on Brick, REC and Mapped classes, exposed through the Mapped GraphQL API and a Mapped MCP server for AI agents.
image: https://www.mapped.com/img/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.mapped.com over streamable HTTP requiring an API key; 2 tools listed.
  name: Mapped MCP Server
  slug: mapped
modified: '2026-10-18'
name: Mapped
nav: Providers
network: true
overview: 'Mapped is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Buildings, IoT, GraphQL, and Data Integration.


  Mapped''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 27 more developer resources.'
plans:
- name: Mapped Com Plans Pricing
  plan_count: 6
  slug: mapped-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Mapped Com Rate Limits
  slug: mapped-com-rate-limits
scopes:
- name: Mapped Com Scopes
  scope_count: 9
  slug: mapped-com-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 35.1
    developer_ergonomics: 48.8
    discoverability: 75.0
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 57.0
  provenance:
    conformance: first-party
    mcp: first-party
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mapped-com/mapped-com-2026-11-03T135324.png
security:
- kind: authentication
  name: Mapped Com Authentication
  slug: mapped-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mapped Com Domain Security
  slug: mapped-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mapped-com
tags:
- Company
- Smart Buildings
- IoT
- GraphQL
- Data Integration
- Ontology
- Physical AI
- MCP
website: https://www.mapped.com
---
