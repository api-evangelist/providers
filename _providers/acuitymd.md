---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.acuitymd.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.acuitymd.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.acuitymd.com/company/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.acuitymd.com/resources/blog
- group: start
  title: ''
  type: Login
  url: https://app.acuitymd.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acuitymd.com/company/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acuitymd.com/company/legal/contracts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acuitymd
- group: other
  title: ''
  type: AppExchange
  url: https://appexchange.salesforce.com/appxListingDetail?listingId=93076337-adfe-41f9-a479-b0692d991452
- group: other
  title: ''
  type: Marketplace
  url: https://app.snowflake.com/marketplace/listing/GZ2FTZ5OMHSBI/acuitymd-acuitymd-encounters-data-mart-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acuitymd-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acuitymd-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acuitymd-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acuitymd-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acuitymd-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/acuitymd-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acuitymd-domain-security.yml
coverage:
  checked: '2026-08-14'
  detail: AcuityMD ships no first-party developer surface at all — its entire integration layer is published inside host platforms, as the "AcuityMD for Salesforce" managed package on the Salesforce AppExchange and the AcuityMD Encounters Data Mart on Snowflake Marketplace, plus a contract-only enterprise Data Connector, so there is no AcuityMD-hosted spec, reference or key issuance to read.
  evidence:
  - status: 200
    url: https://appexchange.salesforce.com/appxListingDetail?listingId=93076337-adfe-41f9-a479-b0692d991452
  - status: 200
    url: https://app.snowflake.com/marketplace/listing/GZ2FTZ5OMHSBI/acuitymd-acuitymd-encounters-data-mart-us
  - status: 404
    url: https://api.acuitymd.com/openapi.json
  - status: 404
    url: https://www.acuitymd.com/openapi.json
  reason: marketplace-only
  state: gated
created: '2026-07-17'
description: 'AcuityMD is a MedTech commercial intelligence platform that combines precise medical device market data, AI-powered insights (AcuityAI), and workflow tools to help commercial teams accelerate product adoption and revenue growth. Used by 500+ medical device companies, the platform spans Market Intelligence, Care Journeys, Targeting, Pipeline, Contracts, Territories and Forecasting. AcuityMD is a closed enterprise SaaS product: it exposes no public developer API, but integrates via a Salesforce AppExchange app, a Snowflake Marketplace listing, and an enterprise Data Connector that delivers market intelligence into customer data warehouses. Backed by ICONIQ Capital and Redpoint Ventures.'
image: https://cdn.prod.website-files.com/6985dd9e41b26a29ef1c43dc/69863643e052c9604d901fe1_acuitymd-opengraph.jpg
layout: provider
modified: '2026-08-14'
name: AcuityMD
nav: Providers
network: true
overview: 'AcuityMD is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, MedTech, Medical Devices, and Market Intelligence.


  AcuityMD''s developer surface includes support, engineering blog, changelog, and 14 more developer resources.'
plans:
- name: Acuitymd Plans Pricing
  plan_count: 0
  slug: acuitymd-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Acuitymd Rate Limits
  slug: acuitymd-rate-limits
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 20.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acuitymd/refs/heads/main/screenshots/acuitymd-2026-07-25T181538.png
security:
- kind: domain-security
  name: Acuitymd Domain Security
  slug: acuitymd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Acuitymd Trust Center
  slug: acuitymd-trust-center
  summary_line: SOC 2 Type 1
slug: acuitymd
tags:
- Company
- Healthcare
- MedTech
- Medical Devices
- Market Intelligence
- Sales Intelligence
- Commercial Analytics
- Data
website: https://www.acuitymd.com/
---
