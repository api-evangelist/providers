---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: The Tempo product itself - a hosted AI app builder where users prompt, generate, edit, and preview React / Next.js applications in the browser. Combines a visual canvas, AI-generated code, and live pr
  name: Tempo Web App
  slug: web-app
- description: Official documentation for using Tempo - prompts and generation, working with the canvas, code editing, integrations with auth / database / hosting providers, and exporting projects.
  name: Tempo Documentation
  slug: docs
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tempo-labs/refs/heads/main/plans/tempo-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tempo-labs-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tempo-labs/refs/heads/main/rate-limits/tempo-labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tempo-labs-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tempo-labs/refs/heads/main/finops/tempo-labs-finops.yml
  title: ''
  type: FinOps
  url: finops/tempo-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tempo.new/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tempo-labs/refs/heads/main/security/tempo-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tempo-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tempo.new/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tempo.new/
- group: other
  title: ''
  type: X
  url: https://x.com/tempolabs_ai
created: '2026-05-23'
description: Tempo (Tempo Labs) is an AI app builder at tempo.new positioned around the "Prompt. Develop. Design. Collaborate." loop - users describe an app in natural language, Tempo generates code, and developers iterate either in the visual canvas or directly in code. The product targets design-to-code and prompt-to-code workflows for React / Next.js apps and is primarily consumed as a hosted web product rather than as an API. Public developer surface is limited; integrations and connected services (auth, database, hosting) are surfaced inside the product rather than via a documented public API.
finops:
- has_sources: false
  method: generated
  name: Tempo Labs Finops
  primary_unit: ''
  service_category: API
  slug: tempo-labs-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tempo-labs.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.tempo.new over HTTP.
  name: Tempo Labs MCP Server
  slug: tempo-labs
modified: '2026-10-06'
name: Tempo Labs
nav: Providers
network: true
overview: 'Tempo Labs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI App Builder, Design to Code, Prompt to Code, Low-Code, and React.


  Tempo Labs'' developer surface includes engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Tempo Labs Plans Pricing
  plan_count: 1
  slug: tempo-labs-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Tempo Labs Rate Limits
  slug: tempo-labs-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 60.0
    operational_transparency: 5.3
  previous_composite: 14.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/tempo-labs/refs/heads/main/screenshots/tempo-labs-2026-06-20T195100.png
security:
- kind: domain-security
  name: Tempo Labs Domain Security
  slug: tempo-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tempo-labs
tags:
- AI App Builder
- Design to Code
- Prompt to Code
- Low-Code
- React
- Next.js
- Developer Tools
website: https://tempo.new/
---
