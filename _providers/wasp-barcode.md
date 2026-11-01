---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Asset tracking and inventory management API documented on the provider's website.
  name: Wasp Barcode API
  slug: wasp-barcode-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/wasp-barcode/plans/wasp-barcode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wasp-barcode-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/wasp-barcode/changelog/wasp-barcode-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wasp-barcode-changelog.yml
- group: agent
  href: https://artifacts.apis.io/wasp-barcode/llms/wasp-barcode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wasp-barcode-llms.txt
- group: agent
  href: https://artifacts.apis.io/wasp-barcode/well-known/wasp-barcode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wasp-barcode-well-known.yml
- group: other
  href: https://artifacts.apis.io/wasp-barcode/hosts/wasp-barcode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wasp-barcode-hosts.yml
- group: other
  href: https://artifacts.apis.io/wasp-barcode/vendors/wasp-barcode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wasp-barcode-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.waspbarcode.com/about-us/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.waspbarcode.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.waspbarcode.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.waspbarcode.com/about-us/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.waspbarcode.com/asset-tracking/pricing
- group: other
  title: ''
  type: Leadership
  url: https://www.waspbarcode.com/about-us/management
- group: start
  title: ''
  type: GettingStarted
  url: https://www.waspbarcode.com/buzz/how-onboarding-can-improve-employee-retention
- group: docs
  title: ''
  type: Documentation
  url: https://dev.waspbarcode.com/
- group: auth
  href: https://artifacts.apis.io/wasp-barcode/security/wasp-barcode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wasp-barcode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waspbarcode.com/
coverage:
  checked: '2026-10-27'
  detail: Provider's documentation pages are HTML/JS without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://dev.waspbarcode.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Wasp Barcode Technologies provides industry‑leading asset tracking and inventory management software, barcode scanners, printers, and labeling supplies for businesses of all sizes. Their platform helps companies manage physical assets, streamline inventory processes, and integrate barcode technology into operations.
image: https://www.waspbarcode.com/wp-content/uploads/2026/01/BarcodeRFIDandMobileScanners.webp
layout: provider
modified: '2026-10-27'
name: Wasp Barcode
nav: Providers
network: true
overview: 'Wasp Barcode is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Asset Tracking, Inventory Management, Barcode Technology, and Software.


  Wasp Barcode''s developer surface includes changelog, support, pricing, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Wasp Barcode Plans Pricing
  plan_count: 7
  slug: wasp-barcode-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wasp Barcode Domain Security
  slug: wasp-barcode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wasp-barcode
tags:
- Company
- Asset Tracking
- Inventory Management
- Barcode Technology
- Software
website: https://waspbarcode.com/
---
