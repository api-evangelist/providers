---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dreamscape-immersive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamscapeimmersive.com/
- group: company
  title: ''
  type: Careers
  url: https://dreamscape-immersive.breezy.hr
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/dreamscape-immersive_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dreamscape-immersive-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/dreamscape-immersive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dreamscape-immersive-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Dreamscape Immersive is a location-based VR venue operator with no developer program at all — the two backends its consumer booking site calls, api.techscapevr.com and api.hq.dev.techscapevr.com (resolved from REACT_APP_API_DOMAIN in the shipped React bundle), are private AWS API Gateway hosts that answer 403 {"message":"Forbidden"} to every anonymous path including /openapi.json and /graphql; no developer subdomain exists at all (api., developer., developers., docs. and status..dreamscapeimmersive.com and the techscapevr.com apex all fail DNS), and the website itself returns a genuine HTTP 404 for every path except /, /index.html and /manifest.json, including /robots.txt, /llms.txt and every /.well-known/ path.
  evidence:
  - status: 403
    url: https://api.techscapevr.com/openapi.json
  - status: 403
    url: https://api.hq.dev.techscapevr.com/openapi.json
  - status: 404
    url: https://dreamscapeimmersive.com/llms.txt
  - status: 404
    url: https://dreamscapeimmersive.com/.well-known/agent-card.json
  - status: 404
    url: https://dreamscapeimmersive.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: Dreamscape Immersive is an entertainment and technology company founded in 2016 and headquartered in Culver City, California, that produces story-based, full-roam virtual reality experiences in which up to six people share a physical stage and see fully rendered avatars of one another inside a virtual 3D environment. It operates location-based VR venues in the United States, licenses its platform to international operators, and is a partner in the Dreamscape Learn education joint venture. Its public surface is a consumer ticketing and booking website; as of August 2026 the company publishes no developer portal, API documentation, SDK, or machine-readable specification, and the single backend its website calls is a private, key-gated AWS API Gateway host that returns 403 to anonymous requests.
image: https://s3.amazonaws.com/dreamscape-web/ds_metadata.jpg
layout: provider
modified: '2026-08-12'
name: Dreamscape Immersive
nav: Providers
network: true
overview: Dreamscape Immersive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Virtual Reality, Immersive Experiences, Location Based Entertainment, and Entertainment.
plans:
- name: Dreamscape Immersive Plans Pricing
  plan_count: 0
  slug: dreamscape-immersive-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 0
  name: Dreamscape Immersive Rate Limits
  slug: dreamscape-immersive-rate-limits
score:
  band: minimal
  composite: 6.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: domain-security
  name: Dreamscape Immersive Domain Security
  slug: dreamscape-immersive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dreamscape-immersive
tags:
- Company
- Virtual Reality
- Immersive Experiences
- Location Based Entertainment
- Entertainment
- Media
- Ticketing
- Education Technology
website: https://dreamscapeimmersive.com/
---
