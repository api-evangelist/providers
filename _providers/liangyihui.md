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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.liangyihui.net
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liangyihui-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liangyihui-llms.txt
created: '2026-07-17'
description: 'liangyihui is a company operating the web property at liangyihui.net, surfaced as a portfolio company of the venture firm Qiming and added to the API Evangelist network for enrichment. As of this enrichment pass the company publishes no public developer program: no developer portal, no API reference or documentation, no OpenAPI, AsyncAPI or GraphQL definition, no first-party SDK packages on any public registry, and no working /.well-known/ discovery surface. The public site is served from Chinese CDN infrastructure (Tengine / kunlunpi) behind a bot shield that answers every path with the same obfuscated JavaScript challenge, so the property soft-404s and cannot be crawled or inspected. A live API host does exist at api.liangyihui.net: it answers its root with a Tomcat-served "Welcome to LYH!" page and returns genuine HTTP 404s for probe paths, indicating a real but private first-party backend for the company''s own clients rather than a documented public API. This profile records
  verified DNS, TLS and endpoint posture only; no API artifacts have been fabricated.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liangyihui.png
layout: provider
modified: '2026-07-19'
name: liangyihui
nav: Providers
network: true
overview: liangyihui is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, China, Venture Backed, Qiming Portfolio, and Private API.
random_paper: 4
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liangyihui/refs/heads/main/screenshots/liangyihui-2026-07-25T225014.png
security:
- kind: domain-security
  name: Liangyihui Domain Security
  slug: liangyihui-domain-security
  summary_line: TLSv1.3
slug: liangyihui
tags:
- Company
- China
- Venture Backed
- Qiming Portfolio
- Private API
- No Public API Program
website: https://www.liangyihui.net
---
