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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- baseURL: https://api.mojeek.com
  baseurl_source: spec
  description: Mojeek provides a Web Search API and Site Search API for developers to embed search functionality.
  name: Mojeek Search API
  slug: mojeek-search-api
- baseURL: https://api.mojeek.com
  baseurl_source: declared
  description: 'Mojeek API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Mojeek API
  slug: mojeek-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/mojeek/rules/mojeek-rules.yml
  title: ''
  type: Spectral
  url: rules/mojeek-rules.yml
- group: design
  href: https://artifacts.apis.io/mojeek/vocabulary/mojeek-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mojeek-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/mojeek/security/mojeek-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mojeek-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mojeek/authentication/mojeek-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mojeek-authentication.yml
- group: design
  href: https://artifacts.apis.io/mojeek/conformance/mojeek-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mojeek-conformance.yml
- group: auth
  href: https://artifacts.apis.io/mojeek/well-known/mojeek-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mojeek-security.txt
- group: agent
  href: https://artifacts.apis.io/mojeek/well-known/mojeek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mojeek-well-known.yml
- group: other
  href: https://artifacts.apis.io/mojeek/hosts/mojeek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mojeek-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mojeek.com/about/terms.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mojeek.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mojeek.com/about/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.mojeek.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mojeek
- group: auth
  href: https://artifacts.apis.io/mojeek/security/mojeek-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mojeek-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mojeek/security/mojeek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mojeek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mojeek.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mojeek.com/support/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.mojeek.com/services/search/web-search-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mojeek.com/support/api/search/quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://www.mojeek.com/support/
- group: company
  title: ''
  type: Blog
  url: https://blog.mojeek.com/
coverage:
  checked: '2026-10-27'
  detail: Mojeek's documentation provides API guides but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications are publicly available.
  evidence:
  - status: 404
    url: https://www.mojeek.com/openapi.json
  - status: 404
    url: https://www.mojeek.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Mojeek is an independent search engine company offering alternative web search services. It provides a Web Search API, Site Search API, and customizable search boxes for developers and businesses. Mojeek emphasizes privacy, community support, and open access to its search technology, with documentation, pricing, and support resources available online.
layout: provider
modified: '2026-10-27'
name: Mojeek
nav: Providers
network: true
overview: 'Mojeek is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Search API, and 1 more. Tagged areas include Search, Privacy, API, Open-source, and Community.


  The Mojeek catalog on APIs.io includes 1 Spectral governance ruleset.


  Mojeek''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Mojeek API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mojeek-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 11.4
    developer_ergonomics: 47.6
    discoverability: 55.4
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mojeek Authentication
  slug: mojeek-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mojeek Domain Security
  slug: mojeek-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mojeek Vulnerability Disclosure
  slug: mojeek-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mojeek
tags:
- Search
- Privacy
- API
- Open-source
- Community
website: https://www.mojeek.com/
---
