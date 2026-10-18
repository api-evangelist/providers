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
- description: Pagero provides e‑invoicing and financial automation APIs, referenced from Thomson Reuters solution pages.
  name: Pagero API
  slug: pagero-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagero/refs/heads/main/well-known/pagero-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pagero-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagero/refs/heads/main/well-known/pagero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pagero-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pagero/refs/heads/main/hosts/pagero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pagero-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pagero/refs/heads/main/vendors/pagero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pagero-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pagero/refs/heads/main/packages/pagero-packages.yml
  title: ''
  type: SDKs
  url: packages/pagero-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pagero/refs/heads/main/packages/pagero-packages.yml
  title: ''
  type: Packages
  url: packages/pagero-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://europe.thomsonreuters.com/trust-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thomsonreuters.com/en/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.thomsonreuters.com/en-us/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pagero.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pagero.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://europe.thomsonreuters.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://europe.thomsonreuters.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://europe.thomsonreuters.com/resource-center/guides
- group: company
  title: ''
  type: Blog
  url: https://europe.thomsonreuters.com/resource-center/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pagero
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagero/refs/heads/main/security/pagero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pagero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pagero.com
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on api.pagero.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.pagero.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Pagero provides a cloud-based platform for electronic invoicing, tax and legal solutions, enabling businesses to automate e‑invoicing, accounts payable, and compliance across Europe and Latin America. Integrated with Thomson Reuters, Pagero connects to multiple standards such as Peppol, ViDA, and local tax regimes, offering a unified solution for B2B financial processes and supply‑chain automation.
image: https://www.datocms-assets.com/80283/1763132389-1200_630.png
layout: provider
modified: '2026-10-13'
name: Pagero
nav: Providers
network: true
overview: 'Pagero is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Invoicing, AP Automation, Compliance, and B2B.


  Pagero''s developer surface includes support, documentation, engineering blog, and 15 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pagero Domain Security
  slug: pagero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pagero
tags:
- Company
- E-Invoicing
- AP Automation
- Compliance
- B2B
website: https://www.pagero.com
---
