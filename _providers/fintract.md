---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Financial Document Extraction API
  name: Fintract API
  slug: fintract-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fintract/refs/heads/main/plans/fintract-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fintract-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fintract/refs/heads/main/hosts/fintract-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fintract-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fintract/refs/heads/main/vendors/fintract-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fintract-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fintract/refs/heads/main/security/fintract-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fintract-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fintract.ai/
- group: company
  title: ''
  type: Blog
  url: https://fintract.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://fintract.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.fintract.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.fintract.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.fintract.ai/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fintract.ai
coverage:
  checked: '2026-10-16'
  detail: Fintract provides documentation pages but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found on its API hosts.
  evidence:
  - status: 522
    url: https://api.fintract.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Fintract provides a Financial Document Extraction API that converts PDFs such as bank statements, invoices, and receipts into validated JSON. The service offers high‑accuracy OCR and data extraction with a simple usage‑based pricing model (e.g., $0.05 per page). Users can start for free without a credit card, and the platform includes tools for converting PDFs to Excel, CSV, and QuickBooks formats. Fintract’s API aims to streamline financial data processing for developers and businesses, supporting integrations with popular accounting software and offering a range of document‑type specific endpoints.
image: https://fintract.ai/assets/og-default.png
layout: provider
modified: '2026-10-16'
name: Fintract
nav: Providers
network: true
overview: 'Fintract is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, OCR, Document-Processing, and Fintech.


  Fintract''s developer surface includes engineering blog, pricing, signup flow, documentation, and 7 more developer resources.'
plans:
- name: Fintract Plans Pricing
  plan_count: 2
  slug: fintract-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fintract Domain Security
  slug: fintract-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fintract
tags:
- Finance
- OCR
- Document-Processing
- Fintech
website: https://fintract.ai/
---
