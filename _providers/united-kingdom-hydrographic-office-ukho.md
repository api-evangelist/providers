---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/llms/united-kingdom-hydrographic-office-ukho-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/united-kingdom-hydrographic-office-ukho-llms.txt
- group: auth
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/well-known/united-kingdom-hydrographic-office-ukho-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/united-kingdom-hydrographic-office-ukho-www-security.txt
- group: agent
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/well-known/united-kingdom-hydrographic-office-ukho-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/united-kingdom-hydrographic-office-ukho-well-known.yml
- group: other
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/hosts/united-kingdom-hydrographic-office-ukho-hosts.yml
  title: ''
  type: Hosts
  url: hosts/united-kingdom-hydrographic-office-ukho-hosts.yml
- group: other
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/vendors/united-kingdom-hydrographic-office-ukho-vendors.yml
  title: ''
  type: Vendors
  url: vendors/united-kingdom-hydrographic-office-ukho-vendors.yml
- group: build
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/packages/united-kingdom-hydrographic-office-ukho-packages.yml
  title: ''
  type: SDKs
  url: packages/united-kingdom-hydrographic-office-ukho-packages.yml
- group: build
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/packages/united-kingdom-hydrographic-office-ukho-packages.yml
  title: ''
  type: Packages
  url: packages/united-kingdom-hydrographic-office-ukho-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.admiralty.co.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.admiralty.co.uk/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.admiralty.co.uk/news
- group: start
  title: ''
  type: Login
  url: https://www.admiralty.co.uk/sso/openid_connect/login/windows_aad
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.admiralty.co.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UKHO
- group: auth
  href: https://artifacts.apis.io/united-kingdom-hydrographic-office-ukho/security/united-kingdom-hydrographic-office-ukho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/united-kingdom-hydrographic-office-ukho-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ukho.gov.uk
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.ukho.gov.uk
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: The United Kingdom Hydrographic Office (UKHO) is an executive agency of the UK Ministry of Defence that sells hydrographic and marine geospatial data, nautical charts, publications and digital navigation services under the Admiralty brand. It supplies these products to mariners, shipping companies, defence users and other maritime stakeholders worldwide to support safe, efficient and compliant navigation.
layout: provider
modified: '2026-10-26'
name: United Kingdom Hydrographic Office (UKHO)
nav: Providers
network: true
overview: United Kingdom Hydrographic Office (UKHO) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hydrography, Nautical Charts, Maritime Navigation, Defence, and Marine Data.
random_paper: 5
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: United Kingdom Hydrographic Office Ukho Domain Security
  slug: united-kingdom-hydrographic-office-ukho-domain-security
  summary_line: TLSv1.3 · DMARC
slug: united-kingdom-hydrographic-office-ukho
tags:
- Hydrography
- Nautical Charts
- Maritime Navigation
- Defence
- Marine Data
- Admiralty Products
website: http://www.ukho.gov.uk
---
