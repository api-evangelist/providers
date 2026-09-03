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
  url: security/workbounce-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workbounce-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workbounce-llms.txt
- group: company
  title: ''
  type: Website
  url: http://workbounce.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workbounce
created: '2026-07-17'
description: Workbounce was an AI-powered revenue and sales enablement platform that gave sales reps instant answers to deal-blocking questions by connecting company documents and knowledge to AI-powered search, delivered through a Slack bot and Chrome extension. Co-founded by Adam Smith and Rowan Bailey and backed by Index Ventures. As of July 2026 workbounce.com returns HTTP 402 (Vercel DEPLOYMENT_DISABLED) and the company appears defunct; no public API, developer docs, SDKs, or packages were ever published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workbounce.png
layout: provider
modified: '2026-07-21'
name: Workbounce
nav: Providers
network: true
overview: Workbounce is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Sales Enablement, Revenue Enablement, and Artificial Intelligence.
random_paper: 16
score:
  band: minimal
  composite: 6.1
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Workbounce Domain Security
  slug: workbounce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workbounce
tags:
- Company
- Business Applications
- Sales Enablement
- Revenue Enablement
- Artificial Intelligence
- Slack
- Defunct
website: http://workbounce.com
---
