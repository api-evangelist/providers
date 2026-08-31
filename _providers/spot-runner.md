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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.spotrunner.com/
- group: start
  title: ''
  type: Login
  url: https://advertiser.spotrunner.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spotrunner.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spotrunner.com/terms-and-coniditions
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spot-runner-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spot-runner-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spot-runner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spot-runner-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10225
coverage:
  checked: '2026-08-13'
  detail: Spot Runner's entire public site is four Wix pages (home, terms, privacy, accessibility) with no developer portal, docs, spec or SDK anywhere; the advertiser portal's real backend at api.spotrunner.com/v1 is live (/health returns 200) but is the SaaS product's own private API, published nowhere, and the only public machine-readable surface is the Wix platform's Site MCP endpoint.
  evidence:
  - status: 200
    url: https://www.spotrunner.com/pages-sitemap.xml
  - status: 400
    url: https://www.spotrunner.com/openapi.json
  - status: 404
    url: https://api.spotrunner.com/openapi.json
  - status: 200
    url: https://api.spotrunner.com/health
  - status: 400
    url: https://www.spotrunner.com/.well-known/agent-card.json
  - status: 200
    url: https://www.spotrunner.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Spot Runner is an AI-driven advertising technology company (backed by Battery Ventures) focused on contextual media planning for Connected TV (CTV) and online video. Its platform uses proprietary MicroModeling AI through tools such as ContextPlanner and ContextDeals to match advertiser creative to the most relevant, brand-suitable premium video ad opportunities across leading streaming networks, publishers, and TV OEMs, and to send Deal IDs directly to a buyer's DSP seat. Spot Runner also markets an "Agentic Agency" of multi-agent creative tooling for SMBs and DTC brands. The public surface is a marketing site plus an advertiser login portal; there is no published developer API, OpenAPI, or SDK. The site does expose a hosted Wix Site MCP endpoint for agentic AI access, advertised via its /llms.txt.
image: https://static.wixstatic.com/ficons/875226_5f83093056974a87a56d1050e1e3ee01~mv2.ico
layout: provider
mcp_servers:
- description: ''
  name: Spot Runner Wix Site MCP
  slug: spot-runner-wix-site-mcp
modified: '2026-08-13'
name: Spot Runner
nav: Providers
network: true
overview: 'Spot Runner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Connected TV, and CTV.


  Spot Runner''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Spot Runner Plans Pricing
  plan_count: 0
  slug: spot-runner-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Spot Runner Rate Limits
  slug: spot-runner-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Spot Runner Authentication
  slug: spot-runner-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Spot Runner Domain Security
  slug: spot-runner-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spot-runner
tags:
- Company
- Advertising
- AdTech
- Connected TV
- CTV
- Online Video
- Contextual Advertising
- Agentic AI
- Media Planning
website: https://www.spotrunner.com/
---
