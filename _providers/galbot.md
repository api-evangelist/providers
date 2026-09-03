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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/galbot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://galbot.com
created: '2026-07-17'
description: Galbot (银河通用机器人, "Galaxy Universal Robotics") is the official site of a general-purpose, embodied-AI robotics company. It was surfaced through the API Evangelist network as a portfolio company of the venture firm Qiming and profiled here for API and developer-surface enrichment. As of this enrichment pass Galbot publishes only a marketing website rendered as a client-side single-page app; no public developer portal, API documentation, OpenAPI/AsyncAPI specification, SDK, or MCP surface could be discovered. The only machine-readable signals captured are the DNS, TLS, and email-authentication (SPF/DMARC) posture of the galbot.com domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/galbot.png
layout: provider
modified: '2026-07-19'
name: galbot
nav: Providers
network: true
overview: galbot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Humanoid Robots, Embodied AI, and Artificial Intelligence.
random_paper: 3
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/galbot/refs/heads/main/screenshots/galbot-2026-07-25T215402.png
security:
- kind: domain-security
  name: Galbot Domain Security
  slug: galbot-domain-security
  summary_line: TLSv1.2 · DMARC
slug: galbot
tags:
- Company
- Robotics
- Humanoid Robots
- Embodied AI
- Artificial Intelligence
- Hardware
- China
website: https://galbot.com
---
