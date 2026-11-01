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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Kurtosys API platform provides web services for managing data models, properties, data loading, search, and retrieval of fund and share class information.
  name: Kurtosys API
  slug: kurtosys-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kurtosys.com/
- group: agent
  href: https://artifacts.apis.io/kurtosys/well-known/kurtosys-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kurtosys-well-known.yml
- group: other
  href: https://artifacts.apis.io/kurtosys/hosts/kurtosys-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kurtosys-hosts.yml
- group: other
  href: https://artifacts.apis.io/kurtosys/vendors/kurtosys-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kurtosys-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.kurtosys.com/press
- group: auth
  href: https://artifacts.apis.io/kurtosys/security/kurtosys-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kurtosys-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kurtosys/security/kurtosys-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kurtosys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kurtosys.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kurtosys.com/api-documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kurtosys.com/api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.kurtosys.com/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kurtosys.com/get-a-demo/
- group: operate
  title: ''
  type: Support
  url: https://www.kurtosys.com/support/
- group: operate
  title: ''
  type: Support
  url: https://support.kurtosys.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kurtosys.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kurtosys
- group: operate
  title: ''
  type: Roadmap
  url: https://www.kurtosys.com/product-release-notes/
- group: start
  title: ''
  type: SignUp
  url: https://www.kurtosys.com/get-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kurtosys.com/kurtosys-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kurtosys.com/legal/privacy-policy/
coverage:
  checked: '2026-10-29'
  detail: API documentation requires a login to obtain an authentication token, preventing public access to the API spec.
  evidence:
  - status: 200
    url: https://www.kurtosys.com/api-documentation/
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: Kurtosys provides an integrated SaaS platform for automated investment reporting, fund data management, and client portal experiences, enabling financial firms to create compliant fact sheets, dynamic websites, and secure investor portals while leveraging AI-driven insights and regulatory documentation tools. The solution supports fund centres, fund websites, and investor presentations, delivering fast, flawless, and audit‑ready disclosures across multiple asset classes.
image: https://www.kurtosys.com/uploads/2026/08/27fece78385d65b3a3a63c99e18e0e29/kurtosys-donut-frame.svg
layout: provider
modified: '2026-10-29'
name: Kurtosys
nav: Providers
network: true
overview: 'Kurtosys is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, InvestmentManagement, Reporting, and DataPlatform.


  Kurtosys'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 14 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kurtosys Domain Security
  slug: kurtosys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kurtosys Trust Center
  slug: kurtosys-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: kurtosys
tags:
- Company
- FinTech
- InvestmentManagement
- Reporting
- DataPlatform
- SaaS
website: https://kurtosys.com
---
