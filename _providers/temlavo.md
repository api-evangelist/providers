---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.temlavo.com
  baseurl_source: declared
  description: Invoice document operations of the Temlavo Invoice Extraction API (OpenAPI 3.1, version 1.0.0) — create an invoice document and receive an upload authorization, confirm a direct upload so it is admitt
  name: Temlavo Documents API
  slug: temlavo-documents-api
- baseURL: https://api.temlavo.com
  baseurl_source: declared
  description: Usage operation of the Temlavo Invoice Extraction API — retrieve current or historical processing usage for the account. Bearer API key authentication.
  name: Temlavo Usage API
  slug: temlavo-usage-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/plans/temlavo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/temlavo-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/security/temlavo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/temlavo-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/llms/temlavo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/temlavo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/hosts/temlavo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/temlavo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/vendors/temlavo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/temlavo-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/packages/temlavo-packages.yml
  title: ''
  type: Packages
  url: packages/temlavo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://temlavo.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@temlavo/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://temlavo.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://temlavo.com/docs/api-reference
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/security/temlavo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/temlavo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/security/temlavo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/temlavo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://temlavo.com
- group: docs
  title: ''
  type: Documentation
  url: https://temlavo.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://temlavo.com/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://temlavo.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://temlavo.com/security
- group: start
  title: ''
  type: SignUp
  url: https://temlavo.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://temlavo.com/sign-in
created: '2026-10-02'
description: Temlavo provides an Invoice Extraction API that transforms invoice PDFs and images into structured JSON accounting data. The service extracts line items, performs consistency checks, flags duplicate signals, and supplies explicit review outcomes. It aims to streamline automation workflows for developers handling financial documents.
image: https://temlavo.com/opengraph-image-1c1a04?1ecd09803a86c066
layout: provider
modified: '2026-10-05'
name: Temlavo
nav: Providers
network: true
overview: 'Temlavo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Documents API and Usage API. Tagged areas include Company, Invoices, Extraction, and Accounting.


  Temlavo''s developer surface includes API reference, documentation, pricing, support, signup flow, and 14 more developer resources.'
plans:
- name: Temlavo Plans Pricing
  plan_count: 3
  slug: temlavo-plans-pricing
random_paper: 12
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.4
    catalog_earned_first_party: 12.0
    catalog_gap: 65.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.6
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 50.8
    developer_ergonomics: 38.1
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 29.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/temlavo/refs/heads/main/screenshots/temlavo-2026-10-11T130742.png
security:
- kind: domain-security
  name: Temlavo Domain Security
  slug: temlavo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Temlavo Vulnerability Disclosure
  slug: temlavo-vulnerability-disclosure
  summary_line: no policy recorded
slug: temlavo
tags:
- Company
- Invoices
- Extraction
- Accounting
website: https://temlavo.com
---
