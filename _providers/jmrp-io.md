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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for JMRP services (description not found)
  name: JMRP API
  slug: jmrp-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/jmrp-io/llms/jmrp-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jmrp-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/jmrp-io/well-known/jmrp-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jmrp-io-security.txt
- group: auth
  href: https://artifacts.apis.io/jmrp-io/well-known/jmrp-io-kleidos-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jmrp-io-kleidos-security.txt
- group: agent
  href: https://artifacts.apis.io/jmrp-io/well-known/jmrp-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jmrp-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/jmrp-io/hosts/jmrp-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jmrp-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/jmrp-io/vendors/jmrp-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jmrp-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/jmrp-io/packages/jmrp-io-packages.yml
  title: ''
  type: SDKs
  url: packages/jmrp-io-packages.yml
- group: build
  href: https://artifacts.apis.io/jmrp-io/packages/jmrp-io-packages.yml
  title: ''
  type: Packages
  url: packages/jmrp-io-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://jmrp.io/.well-known/security.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jmrp.io/
- group: auth
  href: https://artifacts.apis.io/jmrp-io/security/jmrp-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jmrp-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jmrp-io/security/jmrp-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jmrp-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jmrp.io/
- group: company
  title: ''
  type: Blog
  url: https://jmrp.io/blog/
- group: other
  title: ''
  type: Publications
  url: https://jmrp.io/publications/
- group: commercial
  title: ''
  type: License
  url: https://jmrp.io/license/
- group: start
  title: ''
  type: GettingStarted
  url: https://jmrp.io/cv/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.jmrp.io/
- group: operate
  title: ''
  type: Support
  url: https://jmrp.io/about/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jmrplens
- group: operate
  title: ''
  type: Roadmap
  url: https://jmrp.io/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://jmrp.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jmrp.io/privacy/
coverage:
  checked: '2026-10-30'
  detail: Access to the developer portal requires a magic word login, blocking public access to API documentation.
  evidence:
  - status: 403
    url: https://jmrp.io/tools/categories/developer/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: jmrp.io is the personal site of José Manuel Requena Plens, an embedded firmware and software engineer based in Valencia, Spain. The site showcases his professional background, open‑source projects, publications, and tools related to firmware, embedded systems, industrial communications, test automation, and network security. It provides a blog, a CV, a list of publications, and links to his GitHub, GitLab and LinkedIn profiles, serving as a hub for his engineering work and community contributions.
image: https://jmrp.io/favicon.svg
layout: provider
modified: '2026-10-30'
name: jmrp-io
nav: Providers
network: true
overview: 'jmrp-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Firmware, Embedded Systems, Open Source, and Engineer.


  jmrp-io''s developer surface includes documentation, engineering blog, getting-started guide, support, pricing, and 18 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    mcp: derived
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
- kind: domain-security
  name: Jmrp Io Domain Security
  slug: jmrp-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jmrp Io Vulnerability Disclosure
  slug: jmrp-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jmrp-io
tags:
- Company
- Firmware
- Embedded Systems
- Open Source
- Engineer
website: https://jmrp.io/
---
