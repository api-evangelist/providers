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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: ws://127.0.0.1:9222
  baseurl_source: declared
  description: Lightpanda's primary programmable interface. The browser runs as a CDP server (`lightpanda serve`) and exposes the Chrome DevTools Protocol over a WebSocket endpoint (default `ws://127.0.0.1:9222`). C
  name: Lightpanda CDP WebSocket Interface
  slug: lightpanda-cdp-websocket-interface
- baseURL: wss://cloud.lightpanda.io/ws
  baseurl_source: declared
  description: Managed, hosted CDP browser endpoints reached over secure WebSocket (e.g. `wss://euwest.cloud.lightpanda.io/ws`, `wss://uswest.cloud.lightpanda.io/ws`). Authentication is a `token` query-string parame
  name: Lightpanda Cloud
  slug: lightpanda-cloud
- description: The open-source command-line binary (AGPL-3.0, written in Zig). `lightpanda serve` starts the CDP-over-WebSocket server; `lightpanda fetch` retrieves and dumps a URL as HTML or markdown; `lightpanda a
  name: Lightpanda CLI / Binary
  slug: lightpanda-cli-binary
artifact_total: 11
asyncapis:
- description: AsyncAPI 2.6 description of Lightpanda's programmable interface. Lightpanda is a headless browser; it does **not** expose a REST API. Its interface is the **Chrome DevTools Protocol (CDP)**, a bidirec
  name: Lightpanda CDP over WebSocket
  slug: lightpanda-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lightpanda
  slug: open-lightpanda
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightpanda-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightpanda-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightpanda
- group: company
  title: ''
  type: Website
  url: https://lightpanda.io
- group: docs
  title: ''
  type: Documentation
  url: https://lightpanda.io/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/lightpanda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightpanda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lightpanda-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://lightpanda.io/blog
created: '2026-06-20'
description: Lightpanda is an open-source headless browser built from scratch in Zig for AI agents and large-scale automation. It is not a REST API; its programmable interface is the Chrome DevTools Protocol (CDP) exposed over a WebSocket endpoint, making it a drop-in target for Puppeteer, Playwright, and chromedp clients. It ships as an open-source binary/CLI (AGPL-3.0) and as Lightpanda Cloud, a managed CDP browser service.
finops:
- name: Lightpanda Finops
  service_category: Web and Application Services
  slug: lightpanda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightpanda.png
layout: provider
modified: '2026-06-20'
name: Lightpanda
nav: Providers
network: true
overview: 'Lightpanda publishes 2 APIs on the [APIs.io](https://apis.io/) network: CDP WebSocket Interface and Cloud. Tagged areas include Headless Browser, Browser Automation, CDP, WebSocket, and AI Agents.


  The Lightpanda catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Lightpanda''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Lightpanda Plans Pricing
  plan_count: 2
  slug: lightpanda-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Lightpanda Rate Limits
  slug: lightpanda-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Lightpanda API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: lightpanda-asyncapi-spectral-rules
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 38.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 30.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightpanda/refs/heads/main/screenshots/lightpanda-2026-06-20T184520.png
security:
- kind: domain-security
  name: Lightpanda Domain Security
  slug: lightpanda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lightpanda
tags:
- Headless Browser
- Browser Automation
- CDP
- WebSocket
- AI Agents
- Web Scraping
website: https://lightpanda.io
---
