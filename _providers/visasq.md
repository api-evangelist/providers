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
  url: security/visasq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corp.visasq.co.jp/en/
created: '2026-07-17'
description: VisasQ Inc. is a Tokyo-headquartered knowledge-sharing and spot-consulting platform that connects companies seeking specialized insight with a global network of roughly 800,000 experts across 190 countries and diverse industries and job functions. Its flagship "ビザスクdirect" service arranges one-on-one expert consultations, and it has launched "AI Scout" to deliver precision expert matches in under five minutes, 24/7. The company operates six global offices with multilingual support and over 600 employees, serving Japan and the United States as primary markets. VisasQ was surfaced as a portfolio company of DCM Ventures. As of this enrichment pass it publishes no public API, developer portal, OpenAPI specification, SDKs, or MCP surface; only domain-security posture could be probed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/visasq.png
layout: provider
modified: '2026-07-21'
name: VisasQ
nav: Providers
network: true
overview: VisasQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Expert Network, Knowledge Sharing, and Consulting.
random_paper: 12
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
screenshot: https://raw.githubusercontent.com/api-evangelist/visasq/refs/heads/main/screenshots/visasq-2026-09-02T170026.png
security:
- kind: domain-security
  name: Visasq Domain Security
  slug: visasq-domain-security
  summary_line: TLSv1.3
slug: visasq
tags:
- Company
- Enterprise
- Expert Network
- Knowledge Sharing
- Consulting
- Professional Services
- Japan
website: https://corp.visasq.co.jp/en/
---
