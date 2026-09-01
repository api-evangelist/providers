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
- group: company
  title: ''
  type: Website
  url: https://www.krunchdata.io/
- group: operate
  title: ''
  type: Contact
  url: https://calendly.com/jordan-chung/krunch-demo
- group: auth
  title: ''
  type: DomainSecurity
  url: security/krunch-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/krunch-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Krunch ships software only as client engagements - its entire public surface is one Next.js marketing page whose only link is a Calendly booking URL, and every docs, developer, pricing and contract path on it returns 404 with no api., docs. or developer.krunchdata.io host in DNS to try instead.
  evidence:
  - status: 200
    url: https://www.krunchdata.io/
  - status: 404
    url: https://www.krunchdata.io/developers
  - status: 404
    url: https://www.krunchdata.io/openapi.json
  - status: 404
    url: https://www.krunchdata.io/.well-known/agent-card.json
  - status: 404
    url: https://www.krunchdata.io/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Krunch is an on-demand product studio that delivers product management, engineering, and marketing as a service, using AI and code to compress the build cycle for its clients. The team was accepted into the 500 Startup Accelerator program in Silicon Valley and markets prior engagements with Alibaba, Google, Camunda, New Relic, Polkadot, and Bowtie. Krunch operates as a services agency rather than an API provider - as of this enrichment pass it publishes a single-page marketing site with a Calendly booking link and no public developer portal, documentation, API reference, SDKs, or machine-readable API artifacts of any kind.
image: https://www.krunchdata.io/favicon.ico
layout: provider
modified: '2026-08-13'
name: Krunch
nav: Providers
network: true
overview: Krunch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Services, Product Management, and Engineering.
plans:
- name: Krunch Plans Pricing
  plan_count: 0
  slug: krunch-plans-pricing
random_paper: 0
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 5
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/krunch/refs/heads/main/screenshots/krunch-2026-08-07T171340.png
security:
- kind: domain-security
  name: Krunch Domain Security
  slug: krunch-domain-security
  summary_line: TLSv1.3 · HSTS
slug: krunch
tags:
- Company
- Consulting
- Services
- Product Management
- Engineering
- Marketing
- Artificial Intelligence
- Agency
website: https://www.krunchdata.io/
---
