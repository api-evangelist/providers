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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.4
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gut-wellness-club-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gut-wellness-club-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gut-wellness-club-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gut-wellness-club-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gutwellnessclub.in/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.gutwellnessclub.in/contact-1
- group: company
  title: ''
  type: Website
  url: https://www.gutwellnessclub.in/
created: '2026-07-17'
description: 'Gut Wellness Club is an India-based consumer wellness brand offering a "Gut Reset" program that promises to resolve digestive issues in 15-20 days using natural traditional foods, yoga, Ayurveda, and Naturopathy as an alternative to medication. The site is Wix-hosted and, notably for a consumer brand, exposes agent-native surfaces: a published /llms.txt and a live, hosted Wix Site MCP endpoint that lets AI agents retrieve business details, search the site, and access Wix REST APIs without scraping. It has no first-party developer API, OpenAPI, or SDKs. Surfaced via Accel portfolio mining and enriched from its real public agent surfaces.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gut-wellness-club.png
layout: provider
mcp_servers:
- description: ''
  name: Wix Site MCP (Site Visitor Assistant)
  slug: wix-site-mcp-site-visitor-assistant
modified: '2026-07-19'
name: Gut Wellness Club
nav: Providers
network: true
overview: 'Gut Wellness Club is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Wellness, Health, and Consumer.


  Gut Wellness Club''s developer surface includes support and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 11.7
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gut-wellness-club/refs/heads/main/screenshots/gut-wellness-club-2026-07-25T220445.png
security:
- kind: domain-security
  name: Gut Wellness Club Domain Security
  slug: gut-wellness-club-domain-security
  summary_line: TLSv1.3 · HSTS
slug: gut-wellness-club
tags:
- Company
- Ai
- Wellness
- Health
- Consumer
- Gut Health
- Ayurveda
- MCP
- Agent Native
website: https://www.gutwellnessclub.in/
---
