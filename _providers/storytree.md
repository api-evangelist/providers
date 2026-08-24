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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.3
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://simpleprints.com
- group: company
  title: ''
  type: Website
  url: https://getsimpleprints.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storytree-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/storytree-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/storytree-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storytree-domain-security.yml
created: '2026-07-17'
description: 'Storytree Inc. is a Palo Alto consumer photo company, backed by 500 Global, that operates SimplePrints (simpleprints.com, formerly getsimpleprints.com) — a mobile-first service that turns the photos on your phone into physical products: layflat and mini photo books, canvas prints, metal prints and metal desk prints, photo cards, and wall calendars. The app pulls images directly from the phone with no exporting or reformatting, and the business adds a referral program, promotional discounts, and a schools program. SimplePrints is a business-to-consumer mobile app and does NOT publish a developer API, SDKs, OpenAPI, or a developer portal. The one machine-consumable surface it exposes is a Wix-hosted llms.txt and a generic Wix Site MCP endpoint for agentic access to public site content (business details, site search, and a bridge to Wix business-solution APIs).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storytree.png
layout: provider
mcp_servers:
- description: ''
  name: Storytree MCP Server
  slug: storytree-mcp-server
modified: '2026-07-21'
name: Storytree
nav: Providers
network: true
overview: Storytree is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Photo Printing, Consumer, Mobile App, and Photography.
random_paper: 1
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  provenance:
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Storytree Domain Security
  slug: storytree-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: storytree
tags:
- Company
- Photo Printing
- Consumer
- Mobile App
- Photography
- E-Commerce
- Wix
- MCP
website: https://simpleprints.com
---
