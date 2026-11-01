---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://platform.versori.com/api/v2
  baseurl_source: declared
  description: Versori Platform API
  name: Versori Platform API
  slug: versori-platform-api
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/versori/changelog/versori-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/versori-changelog.yml
- group: design
  href: https://artifacts.apis.io/versori/conventions/versori-conventions.yml
  title: ''
  type: Conventions
  url: conventions/versori-conventions.yml
- group: auth
  href: https://artifacts.apis.io/versori/authentication/versori-authentication.yml
  title: ''
  type: Authentication
  url: authentication/versori-authentication.yml
- group: design
  href: https://artifacts.apis.io/versori/conformance/versori-conformance.yml
  title: ''
  type: Conformance
  url: conformance/versori-conformance.yml
- group: agent
  href: https://artifacts.apis.io/versori/llms/versori-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/versori-llms.txt
- group: other
  href: https://artifacts.apis.io/versori/a2a/versori-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/versori-a2a.yml
- group: agent
  href: https://artifacts.apis.io/versori/well-known/versori-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/versori-well-known.yml
- group: other
  href: https://artifacts.apis.io/versori/hosts/versori-hosts.yml
  title: ''
  type: Hosts
  url: hosts/versori-hosts.yml
- group: other
  href: https://artifacts.apis.io/versori/vendors/versori-vendors.yml
  title: ''
  type: Vendors
  url: vendors/versori-vendors.yml
- group: build
  href: https://artifacts.apis.io/versori/packages/versori-packages.yml
  title: ''
  type: SDKs
  url: packages/versori-packages.yml
- group: build
  href: https://artifacts.apis.io/versori/packages/versori-packages.yml
  title: ''
  type: Packages
  url: packages/versori-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.versori.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.versori.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.versori.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.versori.com/latest/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.versori.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.versori.com/latest/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.versori.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.versori.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/versori
- group: auth
  href: https://artifacts.apis.io/versori/security/versori-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/versori-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://versori.com/
created: '2026-10-21'
description: Versori is an agentic integration platform that enables businesses to build fully custom integrations with AI workflow automation software. It helps save budget and reallocate resources by providing enterprise integration tools and codeless automation, allowing instant creation of custom integrations across services.
image: https://cdn.prod.website-files.com/666c3706c64cb8892954a0d7/69038b5b987f53a44eea46a8_Versori%20Custom%20Integrations.png
layout: provider
modified: '2026-10-21'
name: Versori
nav: Providers
network: true
overview: 'Versori is listed with 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Company, Integration, Artificial Intelligence, Automation, and Platform.


  Versori''s developer surface includes changelog, authentication, engineering blog, getting-started guide, documentation, API reference, and 16 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 34.4
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Versori Authentication
  slug: versori-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Versori Domain Security
  slug: versori-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: versori
tags:
- Company
- Integration
- Artificial Intelligence
- Automation
- Platform
website: https://versori.com/
---
