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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tvty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://tvty.tv/
coverage:
  checked: '2026-08-12'
  detail: TVTY was acquired by Nielsen in July 2021 and absorbed into its TV attribution business; tvty.tv still resolves and is renewed through MarkMonitor, but nothing listens on port 80 or 443, no www/api/docs/developer subdomain resolves, and the Internet Archive's last successful capture is 2023-06-08 before the host began 301-redirecting to an unrelated domain.
  evidence:
  - status: 0
    url: https://tvty.tv/
  - status: 0
    url: https://tvty.tv/.well-known/agent-card.json
  - status: 0
    url: https://tvty.tv/openapi.json
  - status: 200
    url: https://web.archive.org/cdx/search/cdx?url=tvty.tv&output=json&from=20230601
  reason: defunct
  state: none
created: '2026-07-17'
description: TVTY is an advertising technology company that bridges television and digital advertising through its Moment Marketing platform. Its TV Ad Alert technology detects when a brand or competitor TV spot airs and synchronizes digital media campaigns — search, social, display and marketplace advertising — to those moments so advertisers reach audiences at the point of highest attention. TVTY was a Partech portfolio company serving global brands and media agencies. The company, headquartered in Paris, was acquired by Nielsen in July 2021 and folded into Nielsen's TV attribution and ad intelligence business; the tvty.tv site stopped serving after mid-2023 and the host no longer responds, so TVTY has no independent developer surface today.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tvty.png
layout: provider
modified: '2026-08-12'
name: TVTY
nav: Providers
network: true
overview: TVTY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Marketing, and Television.
random_paper: 9
score:
  band: minimal
  composite: 5.0
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Tvty Domain Security
  slug: tvty-domain-security
  summary_line: DMARC
slug: tvty
tags:
- Company
- Advertising
- AdTech
- Marketing
- Television
- Moment Marketing
website: http://tvty.tv/
---
