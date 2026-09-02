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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cofia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cofia-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cofia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cofia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cofia.ai
- group: auth
  title: ''
  type: Security
  url: https://cofia.ai/security
created: '2026-07-17'
description: Cofia is an AI automation platform that learns how a team actually works and automatically builds custom workflow automations without manual setup. By monitoring system events and recognizing repetitive patterns, Cofia proposes and assembles custom agents for tasks like prospect list building, outreach and follow-ups, recruiting pipeline management, and data report creation. The company markets itself as "AI automations that implement themselves." Cofia is a Y Combinator (Winter 2026) company based in New York City, founded by Moses Wayne (formerly Engineering Director at Duolingo) and Paola Martinez (formerly Senior Product Manager at Brilliant.org). It was added to the API Evangelist network as a portfolio-lead stub and enriched with what the company publishes publicly. As of this pass Cofia exposes no public developer API, OpenAPI specification, or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cofia.png
layout: provider
modified: '2026-07-18'
name: Cofia
nav: Providers
network: true
overview: Cofia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Workflow-Automation, and Agents.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
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
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cofia/refs/heads/main/screenshots/cofia-2026-07-25T205956.png
security:
- kind: domain-security
  name: Cofia Domain Security
  slug: cofia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cofia Vulnerability Disclosure
  slug: cofia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cofia
tags:
- Company
- Artificial Intelligence
- Automation
- Workflow-Automation
- Agents
- Productivity
- Y Combinator
website: https://cofia.ai
---
