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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/mmob/well-known/mmob-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mmob-status-security.txt
- group: agent
  href: https://artifacts.apis.io/mmob/well-known/mmob-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mmob-well-known.yml
- group: other
  href: https://artifacts.apis.io/mmob/hosts/mmob-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mmob-hosts.yml
- group: other
  href: https://artifacts.apis.io/mmob/vendors/mmob-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mmob-vendors.yml
- group: build
  href: https://artifacts.apis.io/mmob/packages/mmob-packages.yml
  title: ''
  type: SDKs
  url: packages/mmob-packages.yml
- group: build
  href: https://artifacts.apis.io/mmob/packages/mmob-packages.yml
  title: ''
  type: Packages
  url: packages/mmob-packages.yml
- group: auth
  href: https://artifacts.apis.io/mmob/security/mmob-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mmob-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mmob.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.mmob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mmob.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mmob.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mmob.com/legal-pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mmob.com/legal-pages/privacy-policy
created: '2026-10-21'
description: MMOB provides an API integration toolkit for embedded finance, enabling businesses to embed financial services quickly and securely across channels. Their platform aggregates, transforms, and orchestrates APIs from multiple partners, offering products such as onboarding, payments, and compliance tools. MMOB focuses on rapid deployment, scalability, and improving adoption rates for embedded services, targeting fintechs, banks, and enterprises seeking to enhance their product offerings with integrated financial capabilities.
image: https://cdn.prod.website-files.com/6842c05545ec90209c9ad9d4/688367b02eb18e4c29777948_opengraph.jpg
layout: provider
modified: '2026-10-21'
name: MMOB
nav: Providers
network: true
overview: 'MMOB is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, EmbeddedFinance, APIIntegration, and Platform.


  MMOB''s developer surface includes documentation, engineering blog, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 10.5
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
  name: Mmob Domain Security
  slug: mmob-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mmob
tags:
- Company
- Fintech
- EmbeddedFinance
- APIIntegration
- Platform
website: https://www.mmob.com/
---
