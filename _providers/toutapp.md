---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  url: security/toutapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.toutapp.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/toutapp-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toutapp-llms.txt
created: '2026-07-17'
description: ToutApp was a sales-engagement platform founded in 2011 by Tawheed Kader that gave sales teams email templates, email tracking, campaigns, and analytics for outbound selling, backed by Andreessen Horowitz. Marketo acquired ToutApp in May 2017 and folded the product into Marketo Sales Connect (later part of Adobe after Adobe acquired Marketo in 2018). The company is defunct as a standalone business - toutapp.com now redirects to Adobe's Marketo Sales Connect page - and no independent ToutApp API or developer surface remains publicly available.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toutapp.png
layout: provider
modified: '2026-07-21'
name: ToutApp
nav: Providers
network: true
overview: ToutApp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Sales Engagement, Email Tracking, and Email Templates.
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
screenshot: https://raw.githubusercontent.com/api-evangelist/toutapp/refs/heads/main/screenshots/toutapp-2026-09-02T163958.png
security:
- kind: domain-security
  name: Toutapp Domain Security
  slug: toutapp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: toutapp
tags:
- Company
- Sales
- Sales Engagement
- Email Tracking
- Email Templates
- Marketing
- Acquired
website: https://www.toutapp.com
---
