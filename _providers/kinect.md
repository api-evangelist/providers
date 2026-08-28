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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kinect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trykinect.ai
- group: company
  title: ''
  type: About
  url: https://trykinect.ai/about
- group: company
  title: ''
  type: Blog
  url: https://trykinect.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://trykinect.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trykinect.ai/legal/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kinect-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kinect-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kinect-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Kinect (Kinect AI, Inc.) is an AI revenue platform for direct-to-consumer brands, built around two products that share one brand intelligence: an AI sales rep that converses with shoppers on a brand''s own site — grounded in the full catalog, policies, and reviews, selling in the brand''s voice and guiding each visitor to the right product — and an agent-ready storefront that makes the brand legible and buyable to external AI (ChatGPT, Perplexity, Gemini, and emerging buyer agents). Kinect exposes its brand-agent surface through the open Universal Commerce Protocol (UCP) at /.well-known/ucp, advertising an MCP shopping service with catalog search and lookup capabilities, and maintains agent-native discovery documents (llms.txt, agents.md, ai-instructions). The company is white-glove and same-day to onboard, measures every deployment behind an A/B split, and is a Y Combinator company (P26) headquartered in San Francisco. Founded by Kratik Agrawal (CEO) and Varun Kandula (CTO).'
image: https://trykinect.ai/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: Kinect MCP Server
  slug: kinect-mcp-server
modified: '2026-07-19'
name: Kinect
nav: Providers
network: true
overview: 'Kinect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, E-Commerce, Agentic Commerce, and Conversational Commerce.


  Kinect''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.7
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.7
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kinect/refs/heads/main/screenshots/kinect-2026-08-07T171230.png
security:
- kind: domain-security
  name: Kinect Domain Security
  slug: kinect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kinect
tags:
- Company
- Artificial Intelligence
- E-Commerce
- Agentic Commerce
- Conversational Commerce
- Brand Agents
- D2C
- Shopify
- LLM
- Universal Commerce Protocol
website: https://www.trykinect.ai
---
