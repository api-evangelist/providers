---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Rig provides a desktop app and cloud integration for managing development processes. Documentation is at https://userig.app/docs
  name: Rig API
  slug: rig-api
- baseURL: https://acp.userig.app
  baseurl_source: declared
  description: 'Rig API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Rig API
  slug: userig-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/userig/plans/userig-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/userig-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/userig/rules/userig-rules.yml
  title: ''
  type: Spectral
  url: rules/userig-rules.yml
- group: design
  href: https://artifacts.apis.io/userig/vocabulary/userig-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/userig-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/userig/authentication/userig-authentication.yml
  title: ''
  type: Authentication
  url: authentication/userig-authentication.yml
- group: design
  href: https://artifacts.apis.io/userig/conformance/userig-conformance.yml
  title: ''
  type: Conformance
  url: conformance/userig-conformance.yml
- group: agent
  href: https://artifacts.apis.io/userig/llms/userig-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/userig-llms.txt
- group: auth
  href: https://artifacts.apis.io/userig/well-known/userig-snag-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/userig-snag-security.txt
- group: auth
  href: https://artifacts.apis.io/userig/well-known/userig-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/userig-security.txt
- group: agent
  href: https://artifacts.apis.io/userig/well-known/userig-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/userig-well-known.yml
- group: other
  href: https://artifacts.apis.io/userig/hosts/userig-hosts.yml
  title: ''
  type: Hosts
  url: hosts/userig-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.userig.app
- group: operate
  title: ''
  type: StatusPage
  url: https://status.userig.app
- group: auth
  title: ''
  type: Security
  url: https://userig.app/security
- group: start
  title: ''
  type: Login
  url: https://community.userig.app/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rig-local
- group: operate
  title: ''
  type: ChangeLog
  url: https://userig.app/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://userig.app/for-solo-developers
- group: auth
  href: https://artifacts.apis.io/userig/security/userig-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/userig-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/userig/security/userig-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/userig-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://userig.app/
- group: docs
  title: ''
  type: Documentation
  url: https://userig.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://userig.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://userig.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://userig.app/privacy
- group: company
  title: ''
  type: Blog
  url: https://userig.app/blog
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the API host (api.userig.app) despite probing common spec URLs.
  evidence:
  - status: 404
    url: https://api.userig.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Rig is a local development process manager for Mac and Windows. It provides a desktop app that discovers, starts, stops, and watches every process in a project from a single window, integrating scripts, Procfiles, Laravel artisan sidecars, and managed services like Postgres or Redis. The tool offers a control plane, AI integration via Rig Cloud, and free hobby tier, with paid Mesh plans for teams.
image: https://userig.app/rig-og-image.png
layout: provider
modified: '2026-10-19'
name: Rig
nav: Providers
network: true
overview: 'Rig is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Development, Mac, Windows, and Process-Manager.


  The Rig catalog on APIs.io includes 1 Spectral governance ruleset.


  Rig''s developer surface includes authentication, support, changelog, getting-started guide, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Userig Plans Pricing
  plan_count: 4
  slug: userig-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Rig API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: userig-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
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
  name: Userig Authentication
  slug: userig-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Userig Domain Security
  slug: userig-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Userig Vulnerability Disclosure
  slug: userig-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: userig
tags:
- Company
- Development
- Mac
- Windows
- Process-Manager
website: https://userig.app/
---
