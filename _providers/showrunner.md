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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/showrunner-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/showrunner-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/showrunner-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.showrunner.xyz/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.showrunner.xyz/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.showrunner.xyz/termsofservice
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/showrunner
created: '2026-07-17'
description: Showrunner is an AI streaming and animation platform built by Fable Simulation (founded by Edward Saatchi) and billed as the "Netflix of AI." It lets users create and watch AI-generated serialized animated television shows across genres, acting as directors to write, produce, voice, and remix full episodes within simulated worlds such as Sim Francisco, alongside flagship series like Exit Valley. The platform is powered by Fable's proprietary SHOW-2 model and is delivered as a consumer iOS app and Discord community. Showrunner publishes no first-party developer API; its public site is a Wix-hosted marketing property that exposes the standard Wix Site MCP endpoint for agentic access to public site content.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/showrunner.png
layout: provider
mcp_servers:
- description: ''
  name: Showrunner Site MCP (Wix)
  slug: showrunner-site-mcp-wix
modified: '2026-07-21'
name: Showrunner
nav: Providers
network: true
overview: 'Showrunner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Animation, and Entertainment.


  Showrunner''s developer surface includes support and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Showrunner Domain Security
  slug: showrunner-domain-security
  summary_line: TLSv1.3 · HSTS
slug: showrunner
tags:
- Company
- Artificial Intelligence
- Generative AI
- Animation
- Entertainment
- Media
- Streaming
website: https://www.showrunner.xyz/
---
