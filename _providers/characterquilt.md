---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Branding API from CharacterQuilt — 2 operation(s) for branding.
  name: CharacterQuilt Branding API
  slug: characterquilt-branding-api
- description: The Discovery API from CharacterQuilt — 1 operation(s) for discovery.
  name: CharacterQuilt Discovery API
  slug: characterquilt-discovery-api
- description: 'CharacterQuilt''s hosted Model Context Protocol server, the agent-facing surface of its marketing agent runtime. Live and OAuth-protected at https://mcp.characterquilt.com/api/mcp: an anonymous request'
  name: CharacterQuilt MCP Server
  slug: characterquilt-mcp-server
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CharacterQuilt Brand Profiles Branding API
  slug: open-characterquilt-branding-api
- collection_type: open
  name: CharacterQuilt Brand Profiles Branding Discovery API
  slug: open-characterquilt-discovery-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/characterquilt-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.characterquilt.com
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.characterquilt.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.characterquilt.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.characterquilt.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cal.com/clintvburgess/website-demo-request
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.characterquilt.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.characterquilt.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@characterquilt.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/characterquilt-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/characterquilt-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/characterquilt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/characterquilt-scopes.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/characterquilt-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/characterquilt-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/characterquilt-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/characterquilt-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/characterquilt-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/characterquilt-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/characterquilt-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/characterquilt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/characterquilt/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/characterquilt
created: '2026-07-17'
description: 'CharacterQuilt is an AI-native marketing infrastructure company (Y Combinator Spring 2026) building computer-use agents that design and deploy enterprise marketing campaigns end-to-end. Marketing teams submit a brief and CharacterQuilt''s agents handle audience segmentation, on-brand creative generation, brand validation, and direct deployment into existing tools such as HubSpot, Marketo, WordPress, and LinkedIn — collapsing work that once took multiple agencies, ten tools, and six weeks into roughly an hour. Alongside the product, CharacterQuilt publishes a public, machine-readable brand-profiles data surface at /branding/<slug>.json: colors, typography, logos, components, and personality extracted from thousands of companies'' live websites, intended for agents, designers, and AI tools. Founded by Bhairav Mehta (CEO) and Clint Burgess and based in San Francisco.'
image: https://cdn.prod.website-files.com/678e847c65f5a9cc363424b0/68d6b1531e1346581672508b_Open%20Graph%20Image.jpg
layout: provider
mcp_servers:
- description: ''
  name: characterquilt-mcp.yml
  slug: characterquilt-mcpyml
modified: '2026-08-13'
name: CharacterQuilt
nav: Providers
network: true
overview: 'CharacterQuilt publishes 2 APIs on the [APIs.io](https://apis.io/) network: Branding API and Discovery API. Tagged areas include Company, Marketing, Artificial Intelligence, AI Agents, and Marketing Automation.


  CharacterQuilt''s developer surface includes engineering blog, pricing, signup flow, support, authentication, and 19 more developer resources.'
plans:
- name: Characterquilt Plans Pricing
  plan_count: 3
  slug: characterquilt-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Characterquilt Rate Limits
  slug: characterquilt-rate-limits
scopes:
- name: Characterquilt Scopes
  scope_count: 0
  slug: characterquilt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.8
  delta: -0.1
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 30.3
    contract_quality: 52.4
    developer_ergonomics: 26.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 46.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/characterquilt/refs/heads/main/screenshots/characterquilt-2026-07-25T205053.png
security:
- kind: authentication
  name: Characterquilt Authentication
  slug: characterquilt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Characterquilt Domain Security
  slug: characterquilt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: running-dinner-campaigns
  slug: running-dinner-campaigns
slug: characterquilt
tags:
- Company
- Marketing
- Artificial Intelligence
- AI Agents
- Marketing Automation
- Campaign Management
- Brand Identity
- Computer Use Agents
- Y Combinator
- Data
- MCP
website: https://www.characterquilt.com
---
