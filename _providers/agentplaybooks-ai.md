---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AI agents to create and manage playbooks.
  name: Management API
  slug: management-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/agentplaybooks-ai/authentication/agentplaybooks-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentplaybooks-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentplaybooks-ai/conformance/agentplaybooks-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentplaybooks-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentplaybooks-ai/llms/agentplaybooks-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentplaybooks-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentplaybooks-ai/mcp/agentplaybooks-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentplaybooks-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentplaybooks-ai/well-known/agentplaybooks-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentplaybooks-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentplaybooks-ai/hosts/agentplaybooks-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentplaybooks-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentplaybooks-ai/vendors/agentplaybooks-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentplaybooks-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentplaybooks-ai/packages/agentplaybooks-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/agentplaybooks-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/agentplaybooks-ai/packages/agentplaybooks-ai-packages.yml
  title: ''
  type: Packages
  url: packages/agentplaybooks-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentplaybooks.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentplaybooks.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://agentplaybooks.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://agentplaybooks.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://agentplaybooks.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://agentplaybooks.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://agentplaybooks.ai/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/agentplaybooks-ai/security/agentplaybooks-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentplaybooks-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentplaybooks.ai/
created: '2026-11-01'
description: AgentPlaybooks provides a platform for creating, sharing, and deploying AI agent playbooks. It offers self‑hosted documentation, a blog, and tools for integrating with various LLMs and agents. Users can explore use cases, customize skills, and manage MCP servers, all in a vendor‑neutral environment. The site includes resources like documentation, privacy policy, terms, and a GitHub repository for open‑source contributions.
image: https://agentplaybooks.ai/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentplaybooks.ai.
  name: AgentPlaybooks MCP Server
  slug: agentplaybooks-ai-mcp-yml
modified: '2026-11-01'
name: AgentPlaybooks
nav: Providers
network: true
overview: 'AgentPlaybooks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Playbooks, Documentation, and Open Source.


  AgentPlaybooks'' developer surface includes authentication, documentation, engineering blog, getting-started guide, API reference, and 13 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 25.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentplaybooks Ai Authentication
  slug: agentplaybooks-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agentplaybooks Ai Domain Security
  slug: agentplaybooks-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentplaybooks-ai
tags:
- Company
- Artificial Intelligence
- Playbooks
- Documentation
- Open Source
website: https://agentplaybooks.ai/
---
