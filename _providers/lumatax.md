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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lumatax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.taxually.com/lumatax
created: '2026-07-17'
description: LumaTax is a US and Canadian sales tax automation platform that helps businesses automate sales tax filings, manage nexus exposure, and streamline remittance across multiple state and federal jurisdictions. The product imports transaction data from sources such as Amazon, Stripe, Shopify, and Excel, validates that data and assigns correct tax jurisdictions, generates categorized return summaries, files returns automatically, and stores past filings for audit preparation. Originally an independent Seattle fintech backed by Cowboy Ventures, LumaTax was acquired and is now offered as a product line under Taxually alongside CrossTax, EcoTax, and OneTax. As of enrichment it exposes no public developer portal, API reference, SDK, or machine-readable API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lumatax.png
layout: provider
modified: '2026-07-20'
name: LumaTax
nav: Providers
network: true
overview: LumaTax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Sales Tax, Tax Compliance, and Tax Automation.
random_paper: 8
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lumatax/refs/heads/main/screenshots/lumatax-2026-07-25T225703.png
security:
- kind: domain-security
  name: Lumatax Domain Security
  slug: lumatax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lumatax
tags:
- Company
- Fintech
- Sales Tax
- Tax Compliance
- Tax Automation
- Tax Filing
- Nexus
- Accounting
- Regulatory
website: https://www.taxually.com/lumatax
---
