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
- group: other
  href: https://artifacts.apis.io/silicondust/hosts/silicondust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/silicondust-hosts.yml
- group: other
  href: https://artifacts.apis.io/silicondust/vendors/silicondust-vendors.yml
  title: ''
  type: Vendors
  url: vendors/silicondust-vendors.yml
- group: auth
  href: https://artifacts.apis.io/silicondust/security/silicondust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/silicondust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://silicondust.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.silicondust.com/support/downloads.html
- group: operate
  title: ''
  type: Support
  url: https://www.silicondust.com/contact-support.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silicondust.com/privacy-information.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.silicondust.com/terms-and-conditions.html
- group: other
  title: ''
  type: Image
  url: https://www.silicondust.com/favicon.ico
coverage:
  checked: '2026-10-28'
  detail: SiliconDust does not provide a public developer program or API documentation.
  evidence:
  - status: 0
    url: https://api.silicondust.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: SiliconDust, the maker of HDHomeRun devices, provides networked TV tuners that enable users to stream over‑the‑air broadcast television to multiple screens and devices in their home. The company offers a range of products such as the HDHomeRun FLEX, FLEX DUO, FLEX QUATRO and FLEX 4K, supporting both ATSC 1.0 and ATSC 3.0 (NextGen TV) broadcasts. Customers can watch live TV, record shows to a USB drive, and access a free companion app for iOS, Android, Roku, Apple TV, Xbox and other platforms. SiliconDust also supplies commercial and MDU solutions for multi‑dwelling units, broadcasters and government education sectors.
layout: provider
modified: '2026-10-28'
name: SiliconDust (HDHomeRun)
nav: Providers
network: true
overview: 'SiliconDust (HDHomeRun) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Streaming, TV, and Consumer Electronics.


  SiliconDust (HDHomeRun)''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Silicondust Domain Security
  slug: silicondust-domain-security
  summary_line: TLSv1.3 · DMARC
slug: silicondust
tags:
- Company
- Hardware
- Streaming
- TV
- Consumer Electronics
website: https://silicondust.com/
---
