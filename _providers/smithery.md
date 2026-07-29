---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 60
  human_in_the_loop: 12
  name: Smithery Agentic Access
  operation_count: 107
  slug: smithery-agentic-access
  summary_line: 107 operations · 60 acting · 12 human-in-the-loop
api_count: 9
apis:
- description: The connect API from Smithery — 12 operation(s) for connect.
  name: Smithery connect API
  slug: smithery-connect-api
- description: The connect.mcp API from Smithery — 1 operation(s) for connect.mcp.
  name: Smithery connect.mcp API
  slug: smithery-connect-mcp-api
- description: The domains API from Smithery — 2 operation(s) for domains.
  name: Smithery domains API
  slug: smithery-domains-api
- description: The Health API from Smithery — 1 operation(s) for health.
  name: Smithery Health API
  slug: smithery-health-api
- description: The namespaces API from Smithery — 3 operation(s) for namespaces.
  name: Smithery namespaces API
  slug: smithery-namespaces-api
- description: The organizations API from Smithery — 2 operation(s) for organizations.
  name: Smithery organizations API
  slug: smithery-organizations-api
- description: Browse the MCP server registry, manage server configuration, and handle deployments
  name: Smithery servers API
  slug: smithery-servers-api
- description: Discover and search reusable prompt-based skills for MCP servers
  name: Smithery skills API
  slug: smithery-skills-api
- description: The tokens API from Smithery — 1 operation(s) for tokens.
  name: Smithery tokens API
  slug: smithery-tokens-api
artifact_total: 32
collections:
- collection_type: open
  name: Smithery Platform API
  slug: open-smithery-documented
- collection_type: open
  name: Smithery Platform API
  slug: open-smithery
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smithery-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smithery-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smithery-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smithery-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smithery-ai
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs
- group: build
  title: ''
  type: CLI
  url: https://smithery.ai/docs/concepts/cli
- group: company
  title: ''
  type: Website
  url: https://smithery.ai/
- group: other
  title: ''
  type: Playground
  url: https://smithery.ai/playground
- group: company
  title: ''
  type: Blog
  url: https://smithery.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/skills
- group: auth
  title: ''
  type: Authentication
  url: https://smithery.ai/account/api-keys
- group: build
  title: ''
  type: SDKs
  url: https://github.com/smithery-ai/typescript-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/smithery-ai/cli
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/smithery-ai/smithery-cookbook
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs/concepts/what_is_mcp
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs/use/deep-linking
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs/use/token-scoping
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs/use/uplink
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs/use/listing_your_client
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs/build/publish
- group: docs
  title: ''
  type: Documentation
  url: https://smithery.ai/docs/build/triggers
- group: build
  title: ''
  type: SampleCode
  url: https://smithery.ai/docs/cookbooks/typescript_oauth_client
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.smithery.run
- group: build
  title: ''
  type: Tools
  url: https://github.com/smithery-ai/agent.pw
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/smithery-ai/mouseless
- group: build
  title: ''
  type: Tools
  url: https://github.com/smithery-ai/mcp-to-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/smithery-ai/workers-biscuit
- group: build
  title: ''
  type: Tools
  url: https://github.com/smithery-ai/registry
created: '2025-08-19'
description: Smithery is a platform for discovering, deploying, and managing Model Context Protocol (MCP) servers and skills. It operates a public registry of community-built MCP extensions that AI agents can use to access external tools, data sources, and services, plus a Connect gateway that bundles connections in a namespace behind a single MCP endpoint at mcp.smithery.run. The platform exposes APIs for server registry browsing, server deployment, skill publishing, namespace management, scoped service tokens, connection lifecycle, trigger subscriptions, and an MCP transport endpoint for AI-agent integration.
examples:
- key_count: 2
  name: Smithery Create Connection Example
  slug: smithery-create-connection-example
- key_count: 2
  name: Smithery Create Service Token Example
  slug: smithery-create-service-token-example
- key_count: 2
  name: Smithery Get Server Example
  slug: smithery-get-server-example
- key_count: 2
  name: Smithery List Servers Example
  slug: smithery-list-servers-example
- key_count: 2
  name: Smithery List Skills Example
  slug: smithery-list-skills-example
- key_count: 2
  name: Smithery List Triggers Example
  slug: smithery-list-triggers-example
- key_count: 2
  name: Smithery Mcp Endpoint Example
  slug: smithery-mcp-endpoint-example
finops:
- name: Smithery Finops
  service_category: API
  slug: smithery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smithery.png
json_schemas:
- name: Smithery MCP Server
  property_count: 11
  slug: smithery-server
- name: Smithery Skill
  property_count: 8
  slug: smithery-skill
json_structures:
- name: Smithery Server Structure
  property_count: 0
  slug: smithery-server-structure
jsonld:
- class_count: 25
  name: Smithery Context
  property_count: 0
  slug: smithery-context
layout: provider
mcp_servers:
- description: Hosted MCP gateway endpoint that bundles all connections in a namespace behind a single URL
  name: Smithery MCP Server (mcp.smithery.run)
  slug: smithery-mcp-server-mcpsmitheryrun
- description: 'Smithery-built tool: Rust MCP server for macOS desktop control'
  name: mouseless
  slug: mouseless
modified: '2026-05-22'
name: Smithery
nav: Providers
network: true
overview: 'Smithery publishes 9 APIs on the [APIs.io](https://apis.io/) network, including connect API, connect.mcp API, domains API, and 6 more. Tagged areas include Artificial Intelligence, Large Language Models, MCP, Model Context Protocol, and AI Agents.


  The Smithery catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Smithery''s developer surface includes authentication, documentation, CLI, engineering blog, tooling, and 24 more developer resources.'
plans:
- name: Smithery Plans Pricing
  plan_count: 3
  slug: smithery-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Smithery Rate Limits
  slug: smithery-rate-limits
rules:
- name: Smithery API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: smithery-jsonschema-spectral-rules
- name: Smithery API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: smithery-rules
score:
  band: developing
  composite: 55.3
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.8
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Smithery Authentication
  slug: smithery-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smithery Domain Security
  slug: smithery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smithery
tags:
- Artificial Intelligence
- Large Language Models
- MCP
- Model Context Protocol
- AI Agents
- Developer Tools
- Registry
- Skills
- Tool Discovery
website: https://smithery.ai/
---
