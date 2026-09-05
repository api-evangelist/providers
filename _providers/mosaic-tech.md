---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  - '{''url'': ''https://www.mosaic.tech/'', ''status'': 301, ''note'': ''declared website redirects to https://www.hibob.com/platform/finance/ — a different registrable domain (mosaic.tech -> hibob.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/mosaic-tech-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosaic-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mosaic.tech/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.hibob.com/platform/finance/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/mosaic-tech_stock/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mosaic.tech/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mosaictech
- group: auth
  title: ''
  type: Compliance
  url: security/mosaic-tech-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mosaic-tech-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mosaic-tech-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mosaic-tech-llms.txt
coverage:
  checked: '2026-08-26'
  detail: 'Mosaic Tech was acquired by HiBob (announced 2025-02-13, closed 2025-04-01) and the brand is now fully absorbed: every mosaic.tech path 301-redirects to hibob.com, app.mosaic.tech redirects to finance-app.hibob.com, api.mosaic.tech answers 503 on every path, and the Internet Archive''s 493 recorded mosaic.tech URLs contain no /api, /docs, /developers, swagger or openapi path — Mosaic never ran a public developer program and the callable surface for this product today is HiBob''s.'
  evidence:
  - status: 301
    url: https://www.mosaic.tech/
  - status: 503
    url: https://api.mosaic.tech/openapi.json
  - status: 301
    url: https://app.mosaic.tech/
  - status: 301
    url: https://www.mosaic.tech/developers
  - status: 200
    url: https://trust.mosaic.tech/
  reason: defunct
  state: none
created: '2026-08-26'
description: Mosaic Tech (Mosaic) was a San Francisco-based Strategic Finance Platform, founded in 2019, that connected ERP, CRM, HRIS, billing and data-warehouse systems into a single financial data model for FP&A teams — real-time analytics, agile financial planning, cash-flow forecasting, headcount planning and multi-entity consolidation. HiBob announced its acquisition of Mosaic on 2025-02-13 and closed it on 2025-04-01, folding the product into HiBob's finance/FP&A suite. As of 2026-08-26 the mosaic.tech domain 301-redirects every path to hibob.com, app.mosaic.tech redirects to finance-app.hibob.com, and api.mosaic.tech answers 503 on every path. Mosaic never published a public developer portal, API reference, or machine-readable specification under its own brand — 493 archived mosaic.tech URLs in the Internet Archive contain no /api, /docs, /developers, swagger or openapi path. HiBob's own developer surface is profiled separately.
layout: provider
modified: '2026-08-26'
name: Mosaic Tech
nav: Providers
network: true
overview: Mosaic Tech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Planning, FP&A, Strategic Finance, Business Intelligence, and Analytics.
plans:
- name: Mosaic Tech Plans Pricing
  plan_count: 0
  slug: mosaic-tech-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Mosaic Tech Rate Limits
  slug: mosaic-tech-rate-limits
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 10.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mosaic-tech/refs/heads/main/screenshots/mosaic-tech-2026-09-02T150639.png
security:
- kind: domain-security
  name: Mosaic Tech Domain Security
  slug: mosaic-tech-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Mosaic Tech Trust Center
  slug: mosaic-tech-trust-center
  summary_line: SOC 2 Type II
slug: mosaic-tech
tags:
- Financial Planning
- FP&A
- Strategic Finance
- Business Intelligence
- Analytics
- Software-as-a-Service
- Acquired
website: https://www.mosaic.tech/
---
