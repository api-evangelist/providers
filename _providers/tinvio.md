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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tinvio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jaz.ai/tinvio
- group: company
  title: ''
  type: Blog
  url: https://www.jaz.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jaz.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.jaz.ai/
created: '2026-07-17'
description: Tinvio is a Singapore-based B2B commerce and payments SaaS that helped merchants and their suppliers manage ordering, invoicing, and business payments across Southeast Asia. The company was backed by Partech. As of 2026 Tinvio has been integrated into Jaz (jaz.ai), an AI-powered accounting platform for modern businesses, and now operates as a feature within Jaz rather than as a standalone product; tinvio.com redirects to the Jaz landing page. Tinvio does not currently publish a public developer portal, API reference, SDK, CLI, or OpenAPI definition, so this profile captures the company identity and its live domain-security posture for the API Evangelist network rather than an API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tinvio.png
layout: provider
modified: '2026-07-21'
name: Tinvio
nav: Providers
network: true
overview: 'Tinvio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B Commerce, Payments, Supplier Management, and Accounting.


  Tinvio''s developer surface includes engineering blog, pricing, signup flow, and 2 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tinvio/refs/heads/main/screenshots/tinvio-2026-09-02T163810.png
security:
- kind: domain-security
  name: Tinvio Domain Security
  slug: tinvio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tinvio
tags:
- Company
- B2B Commerce
- Payments
- Supplier Management
- Accounting
- Fintech
- Software-as-a-Service
- Southeast Asia
website: https://www.jaz.ai/tinvio
---
