---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: The Edworking API is a single GraphQL endpoint.
  name: Edworking GraphQL API
  slug: edworking-graphql-api
- description: MCP tools list for Edworking Knowledge Base.
  name: Edworking Knowledge Base MCP
  slug: edworking-knowledge-base-mcp
- baseURL: https://gateway.edworking.com
  baseurl_source: declared
  description: 'edworking-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: edworking-com API
  slug: edworking-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/edworking-com/plans/edworking-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edworking-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/edworking-com/rules/edworking-com-rules.yml
  title: ''
  type: Spectral
  url: rules/edworking-com-rules.yml
- group: design
  href: https://artifacts.apis.io/edworking-com/vocabulary/edworking-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/edworking-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://edworking.com/trust/responsible-disclosure
- group: design
  href: https://artifacts.apis.io/edworking-com/conformance/edworking-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edworking-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/edworking-com/llms/edworking-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edworking-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/edworking-com/mcp/edworking-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/edworking-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/edworking-com/well-known/edworking-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/edworking-com-security.txt
- group: agent
  href: https://artifacts.apis.io/edworking-com/well-known/edworking-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edworking-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/edworking-com/hosts/edworking-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edworking-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/edworking-com/vendors/edworking-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/edworking-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://edworking.com/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.edworking.com
- group: start
  title: ''
  type: Login
  url: https://app.edworking.com/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://edworking.com/startups/resources/remote-onboarding-checklist
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Edworking
- group: auth
  href: https://artifacts.apis.io/edworking-com/security/edworking-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/edworking-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/edworking-com/security/edworking-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edworking-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edworking.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.edworking.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edworking.com/
- group: company
  title: ''
  type: Blog
  url: https://edworking.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://edworking.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edworking.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edworking.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://edworking.com/contact
coverage:
  checked: '2026-10-30'
  detail: GraphQL endpoint requires an access token, preventing unauthenticated schema discovery.
  evidence:
  - status: 200
    url: https://gateway.edworking.com/
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Edworking provides an all‑in‑one collaborative workspace that combines task management, document editing, chat, meetings, file sharing, and AI‑powered assistance into a single platform. Designed for remote and hybrid teams, it aims to reduce tool‑switching by unifying workflows, enabling teams to coordinate, communicate, and manage work efficiently. The service supports integrations with popular tools and offers AI features to enhance productivity.
image: https://edworking.com/images/brand/og.png
json_schemas:
- name: Edworking Com Mcp Tools
  property_count: 0
  slug: edworking-com-mcp-tools
layout: provider
mcp_servers:
- description: Remote MCP server at help.edworking.com.
  name: edworking-com MCP Server
  slug: edworking-com-mcp-yml
modified: '2026-10-30'
name: edworking-com
nav: Providers
network: true
overview: 'edworking-com is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Productivity, Workspace, Artificial Intelligence, and Task Management.


  The edworking-com catalog on APIs.io includes 1 Spectral governance ruleset.


  edworking-com''s developer surface includes getting-started guide, documentation, engineering blog, pricing, support, and 21 more developer resources.'
plans:
- name: Edworking Com Plans Pricing
  plan_count: 3
  slug: edworking-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Edworking Com Rate Limits
  slug: edworking-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: edworking-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: edworking-com-rules
scopes:
- name: Edworking Com Scopes
  scope_count: 0
  slug: edworking-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.0
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 19.0
    discoverability: 70.0
    operational_transparency: 15.8
  previous_composite: 45.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/edworking-com/edworking-com-2026-11-03T131321.png
security:
- kind: authentication
  name: Edworking Com Authentication
  slug: edworking-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Edworking Com Domain Security
  slug: edworking-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Edworking Com Vulnerability Disclosure
  slug: edworking-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: edworking-com
tags:
- Collaboration
- Productivity
- Workspace
- Artificial Intelligence
- Task Management
website: https://edworking.com/
---
