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
  url: https://www.endgame.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/endgame-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/endgame-llms.txt
created: '2026-07-17'
description: 'Endgame was an endpoint security company building endpoint protection, threat hunting, and adversary detection technology, and was surfaced into the API Evangelist network as a venture-portfolio lead. It no longer operates as an independent company: Endgame was acquired by Elastic N.V. and its technology was folded into Elastic Security. As of a live probe on 2026-07-20 the endgame.com domain is retained as a redirect only — the site root and every /.well-known/ discovery path answer HTTP 301 to https://www.elastic.co/security/endpoint-security. Endgame publishes no developer portal, API documentation, OpenAPI description, SDKs, CLI, webhook or event surface, changelog, status page, or MCP server of its own. This profile is retained as a verified-defunct record pointing at the successor product at Elastic; teams evaluating the technology should integrate against Elastic Security.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/endgame.png
layout: provider
modified: '2026-07-20'
name: Endgame
nav: Providers
network: true
overview: Endgame is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Endpoint Security, Threat Detection, and Security Operations.
random_paper: 7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/endgame/refs/heads/main/screenshots/endgame-2026-07-25T213311.png
security:
- kind: domain-security
  name: Endgame Domain Security
  slug: endgame-domain-security
  summary_line: TLSv1.3 · HSTS
slug: endgame
tags:
- Company
- Cybersecurity
- Endpoint Security
- Threat Detection
- Security Operations
- Acquired
website: https://www.endgame.com/
---
