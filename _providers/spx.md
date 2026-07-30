---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Spx Agentic Access
  operation_count: 13
  slug: spx-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 5
apis:
- description: Save and load custom JSON data
  name: SPX Graphics Data API
  slug: spx-data-api
- description: Invoke functions in custom SPX extensions
  name: SPX Graphics Extensions API
  slug: spx-extensions-api
- description: File listing from the ASSETS folder
  name: SPX Graphics Files API
  slug: spx-files-api
- description: Control individual rundown items (play, stop, continue, update)
  name: SPX Graphics Item API
  slug: spx-item-api
- description: Control rundown focus and item playback
  name: SPX Graphics Rundown API
  slug: spx-rundown-api
artifact_total: 18
collections:
- collection_type: open
  name: SPX Graphics Control API
  slug: open-spx-graphics-control-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spx-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spxgraphics
- group: company
  title: ''
  type: Website
  url: https://spxgraphics.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TuomoKu/SPX-GC
- group: docs
  title: ''
  type: Documentation
  url: https://spxgc.tawk.help/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://spxgc.tawk.help/
- group: company
  title: ''
  type: Blog
  url: https://spxgraphics.com/blog
created: '2026-05-02'
description: SPX Graphics is an open-source, browser-based graphics control system for live video productions and live streams. It provides a REST API for external control of graphics templates, rundowns, and playback via integrations with CasparCG, OBS, vMix, and similar broadcast software. SPX enables operators to trigger, control, and update live graphics overlays programmatically or via UI.
examples:
- key_count: 4
  name: Spx Direct Playout Example
  slug: spx-direct-playout-example
- key_count: 4
  name: Spx Load Rundown Example
  slug: spx-load-rundown-example
finops:
- name: Spx Finops
  service_category: API
  slug: spx-finops
image: https://spxgraphics.com/wp-content/uploads/2021/05/spx-logo.png
json_schemas:
- name: SPX Rundown Item
  property_count: 8
  slug: spx-rundown-item
json_structures:
- name: Spx Rundown Item Structure
  property_count: 0
  slug: spx-rundown-item-structure
jsonld:
- class_count: 20
  name: Spx Context
  property_count: 4
  slug: spx-context
layout: provider
modified: '2026-05-19'
name: SPX Graphics
nav: Providers
network: true
overview: 'SPX Graphics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Data API, Extensions API, Files API, and 2 more. Tagged areas include Broadcast, Graphics, Live Production, Media, and Streaming.


  The SPX Graphics catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SPX Graphics'' developer surface includes GitHub presence, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Spx Plans Pricing
  plan_count: 3
  slug: spx-plans-pricing
press:
- date: '2026-05-25'
  title: 'S&P Global: Essential Intelligence'
  url: https://www.spglobal.com/en
- date: '2026-05-25'
  title: SPX Announces Purchase of ULC Robotics
  url: https://spx.com/spx-announces-purchase-of-ulc-robotics/
- date: '2026-05-25'
  title: Lone Star Announces Sale of SPX FLOW to ITT Inc. - Via TT
  url: https://via.tt.se/pressmeddelande/4177141/lone-star-announces-sale-of-spx-flow-to-itt-inc?publisherId=259167&lang=en
- date: '2026-05-25'
  title: ITT CEO Luca Savi Discusses SPX FLOW Acquisition on ...
  url: https://www.linkedin.com/posts/itt_itt-flow-nyse-activity-7437515093598281728-QW7g
- date: '2026-05-25'
  title: SPX FLOW and Siemens collaborate on revolutionary ...
  url: https://www.prnewswire.com/news-releases/spx-flow-and-siemens-collaborate-on-revolutionary-digital-twin-and-ai-product-design-302363262.html
random_paper: 19
rate_limits:
- limit_count: 5
  name: Spx Rate Limits
  slug: spx-rate-limits
rules:
- name: SPX Graphics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spx-jsonschema-spectral-rules
- name: SPX Graphics API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: spx-rules
score:
  band: developing
  composite: 42.2
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 10.9
    discoverability: 57.4
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spx/refs/heads/main/screenshots/spx-2026-06-20T194423.png
security:
- kind: domain-security
  name: Spx Domain Security
  slug: spx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: spx
tags:
- Broadcast
- Graphics
- Live Production
- Media
- Streaming
- Video Production
- Fortune 1000
website: https://spxgraphics.com
---
