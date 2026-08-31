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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.slintel.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/slintel-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slintel-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slintel-domain-security.yml
coverage:
  checked: '2026-08-14'
  detail: 'Slintel was absorbed into 6sense (announced 2021-10-05) and its own surface is gone: slintel.com answers a blanket HTTP 301 to 6sense.com/platform/sales on every path including /openapi.json and every /.well-known/ path, while api.slintel.com and app.slintel.com still carry DNS CNAMEs to AWS load balancers that no longer resolve.'
  evidence:
  - status: 301
    url: https://slintel.com/openapi.json
  - status: 301
    url: https://slintel.com/.well-known/agent-card.json
  - status: 200
    url: https://api.6sense.com/docs/
  - status: 403
    url: https://www.slintel.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Slintel is a B2B sales and market intelligence platform that mines buyer and technographic signals — company firmographics, technology installs, psychographics, and buying-intent scores — to help revenue teams prioritize accounts and time outreach. Founded in 2016 and backed by Accel and Sequoia, Slintel was acquired by 6sense in 2021 and its data and API services are now consolidated into the 6sense Revenue AI platform. Slintel''s programmatic surface (company identification, firmographics, lead scoring, and enrichment) is delivered through the 6sense API Portal rather than a standalone Slintel developer portal. As of a 2026-08-14 probe pass, Slintel operates no developer surface of its own: slintel.com redirects every path into 6sense.com, the historical api.slintel.com and app.slintel.com hosts are decommissioned, no /.well-known/ document or machine-readable spec is served, and no first-party SDK exists in any public package registry. The successor APIs are catalogued under
  the 6sense provider.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slintel.png
layout: provider
modified: '2026-08-14'
name: Slintel
nav: Providers
network: true
overview: Slintel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Sales Intelligence, Market Intelligence, and Data Enrichment.
random_paper: 7
score:
  band: minimal
  composite: 5.0
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Slintel Domain Security
  slug: slintel-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: slintel
tags:
- Company
- Automation
- Sales Intelligence
- Market Intelligence
- Data Enrichment
- Firmographics
- Buying Intent
- B2B
website: https://www.slintel.com
---
