---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dynamsoft/plans/dynamsoft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynamsoft-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/dynamsoft/authentication/dynamsoft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynamsoft-authentication.yml
- group: agent
  href: https://artifacts.apis.io/dynamsoft/llms/dynamsoft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynamsoft-llms.txt
- group: other
  href: https://artifacts.apis.io/dynamsoft/hosts/dynamsoft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynamsoft-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynamsoft/vendors/dynamsoft-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynamsoft-vendors.yml
- group: build
  href: https://artifacts.apis.io/dynamsoft/packages/dynamsoft-packages.yml
  title: ''
  type: SDKs
  url: packages/dynamsoft-packages.yml
- group: build
  href: https://artifacts.apis.io/dynamsoft/packages/dynamsoft-packages.yml
  title: ''
  type: Packages
  url: packages/dynamsoft-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.dynamsoft.com/support/livehelp/
- group: auth
  title: ''
  type: Security
  url: https://www.dynamsoft.com/company/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynamsoft.com/privacy-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://www.dynamsoft.com/company/news/
- group: start
  title: ''
  type: Login
  url: https://www.dynamsoft.com/api-common/Login/Login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.dynamsoft.com/panorama/release-notes/
- group: auth
  href: https://artifacts.apis.io/dynamsoft/security/dynamsoft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamsoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dynamsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dynamsoft.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dynamsoft.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dynamsoft.com/purchase-center/
- group: company
  title: ''
  type: Blog
  url: https://www.dynamsoft.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.dynamsoft.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dynamsoft/
coverage:
  checked: '2026-10-27'
  detail: The developer documentation at https://www.dynamsoft.com/docs/ provides HTML pages but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.dynamsoft.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Dynamsoft provides SDKs for document capture, barcode reading, and MRZ scanning across web, mobile, and desktop platforms. Their Dynamsoft Web TWAIN product enables developers to integrate scanning and barcode capabilities directly into web applications using JavaScript. The company offers trial licenses, detailed developer documentation, and a range of SDKs for various use cases such as mobile document scanning, barcode reading, and server-side processing.
layout: provider
modified: '2026-10-26'
name: Dynamsoft Web TWAIN
nav: Providers
network: true
overview: 'Dynamsoft Web TWAIN is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SDK, Document-Capture, Barcode, and MRZ.


  Dynamsoft Web TWAIN''s developer surface includes authentication, support, changelog, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Dynamsoft Plans Pricing
  plan_count: 1
  slug: dynamsoft-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 46.4
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dynamsoft Authentication
  slug: dynamsoft-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dynamsoft Domain Security
  slug: dynamsoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dynamsoft
tags:
- Company
- SDK
- Document-Capture
- Barcode
- MRZ
- Web
website: https://www.dynamsoft.com/
---
