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
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://tonal.com/
- group: company
  title: ''
  type: Blog
  url: https://tonal.com/blogs/all
- group: operate
  title: ''
  type: Support
  url: https://knowledge.tonal.com/s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TonalFitness
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tonal.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tonal.com/pages/tonal-legal-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tonal.com/pages/tonal-privacy-policies
- group: commercial
  title: ''
  type: Pricing
  url: https://tonal.com/pages/membership
- group: start
  title: ''
  type: Login
  url: https://tonal.com/account
- group: company
  title: ''
  type: Careers
  url: https://tonal.com/pages/careers
- group: operate
  title: ''
  type: Contact
  url: https://tonal.com/pages/contact
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tonal-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tonal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tonal-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tonal-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tonal-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tonal-domain-security.yml
created: '2026-07-17'
description: 'Tonal is a connected fitness company founded in 2013 by Aly Orady and headquartered in San Francisco, best known for its wall-mounted smart home gym that uses digital weight (electromagnetic resistance) and AI-powered coaching to deliver personalized strength training. The Tonal 2 hardware pairs with a subscription membership offering adaptive weight adjustment, science-backed workout programs, live and on-demand classes, and progress tracking. Tonal publishes no first-party developer API, but its Shopify-hosted storefront exposes an agent-commerce surface: an llms.txt, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and an MCP endpoint for agent-driven shopping.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tonal.png
layout: provider
mcp_servers:
- description: ''
  name: Tonal MCP Server
  slug: tonal-mcp-server
modified: '2026-07-21'
name: Tonal
nav: Providers
network: true
overview: 'Tonal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Wellness, Fitness, Strength Training, and Connected Fitness.


  Tonal''s developer surface includes engineering blog, support, pricing, and 14 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.8
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 19.8
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Tonal Domain Security
  slug: tonal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tonal
tags:
- Company
- Health Wellness
- Fitness
- Strength Training
- Connected Fitness
- Home Gym
- Coaching
- Wellness
website: https://tonal.com/
---
