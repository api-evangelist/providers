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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steelbrick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.steelbrick.com
created: '2026-07-17'
description: 'SteelBrick was a Configure-Price-Quote (CPQ) SaaS vendor backed by IVP and Shasta Ventures before it was acquired by Salesforce (announced December 2015, closed 2016) and folded into the product now shipped as Salesforce CPQ (formerly Salesforce Revenue Cloud). The steelbrick.com domain is no longer an independent surface: its apex 301-redirects to salesforce.com/sales/cpq/ and the www host serves a broken default CloudFront certificate. There is no standalone SteelBrick developer portal, documentation, or public API — any live API surface belongs to Salesforce CPQ. This profile is retained as a portfolio lead / acquisition record; enrichment found no independent API artifacts to harvest.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/steelbrick.png
layout: provider
modified: '2026-08-21'
name: Steelbrick
nav: Providers
network: true
overview: Steelbrick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, CPQ, Quote-to-Cash, and Sales.
random_paper: 14
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
screenshot: https://raw.githubusercontent.com/api-evangelist/steelbrick/refs/heads/main/screenshots/steelbrick-2026-09-02T160830.png
security:
- kind: domain-security
  name: Steelbrick Domain Security
  slug: steelbrick-domain-security
  summary_line: DMARC
slug: steelbrick
tags:
- Company
- Enterprise Saas
- CPQ
- Quote-to-Cash
- Sales
- Acquired
- Salesforce
website: https://www.steelbrick.com
---
