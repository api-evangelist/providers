---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DATEV services as described on the developer portal.
  name: DATEV Developer API
  slug: datev-developer-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://serviceformulare.datev.de/link/ShowDoForm?FormID=7110
- group: auth
  href: https://artifacts.apis.io/datev/well-known/datev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datev-security.txt
- group: auth
  href: https://artifacts.apis.io/datev/well-known/datev-karriere-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datev-karriere-security.txt
- group: auth
  href: https://artifacts.apis.io/datev/well-known/datev-download-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datev-download-security.txt
- group: agent
  href: https://artifacts.apis.io/datev/well-known/datev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datev-well-known.yml
- group: other
  href: https://artifacts.apis.io/datev/hosts/datev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datev-hosts.yml
- group: other
  href: https://artifacts.apis.io/datev/vendors/datev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datev-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.datev.de/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datev
- group: auth
  href: https://artifacts.apis.io/datev/security/datev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datev/security/datev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datev.de/
coverage:
  checked: '2026-10-13'
  detail: The developer portal provides HTML documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://developer.datev.de/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: DATEV provides software and IT services for tax consultants, auditors, and small businesses in Germany. It offers a comprehensive suite of solutions for accounting, payroll, and tax filing, enabling secure data exchange between tax advisors and authorities. The platform supports integration via APIs for automated data transfer, compliance reporting, and financial analytics, helping clients streamline their workflows and maintain regulatory compliance.
image: https://www.datev.de/etc.clientlibs/datev.sites/clientlibs/clientlib-bottom-async/resources/images/logo.png
layout: provider
modified: '2026-10-13'
name: DATEV
nav: Providers
network: true
overview: 'DATEV is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Tax, Software, and Germany.


  DATEV''s developer surface includes documentation and 11 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 9.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/datev/datev-2026-11-03T130322.png
security:
- kind: domain-security
  name: Datev Domain Security
  slug: datev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Datev Vulnerability Disclosure
  slug: datev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: datev
tags:
- Company
- Accounting
- Tax
- Software
- Germany
website: https://www.datev.de/
---
