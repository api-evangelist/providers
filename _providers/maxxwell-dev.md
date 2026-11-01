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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Local desktop and CLI tool API for managing coding agents, fleets, and sessions.
  name: Maxxwell API
  slug: maxxwell-api
- baseURL: https://maxxwell.dev
  baseurl_source: declared
  description: 'Rindler API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Rindler API
  slug: maxxwell-dev-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/maxxwell-dev/rules/maxxwell-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/maxxwell-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/maxxwell-dev/vocabulary/maxxwell-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/maxxwell-dev-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/maxxwell-dev/security/maxxwell-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/maxxwell-dev-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/maxxwell-dev/conformance/maxxwell-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maxxwell-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/maxxwell-dev/llms/maxxwell-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maxxwell-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/maxxwell-dev/well-known/maxxwell-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/maxxwell-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/maxxwell-dev/well-known/maxxwell-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maxxwell-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/maxxwell-dev/hosts/maxxwell-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maxxwell-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/maxxwell-dev/vendors/maxxwell-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maxxwell-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rindler-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/rindler-ai/ide-releases/releases/latest
- group: company
  title: ''
  type: Blog
  url: https://maxxwell.dev/blog/
- group: auth
  href: https://artifacts.apis.io/maxxwell-dev/security/maxxwell-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/maxxwell-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/maxxwell-dev/security/maxxwell-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maxxwell-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maxxwell.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maxxwell.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.maxxwell.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.maxxwell.dev/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://maxxwell.dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maxxwell.dev/privacy
coverage:
  checked: '2026-10-29'
  detail: Documentation provides usage guides but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.maxxwell.dev
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Rindler, operating under the Maxxwell brand, provides a local desktop and CLI tool that manages coding agents. Maxxwell enables users to run multiple coding agents simultaneously, offering features like fleet management, session tracking, and integration with AI runtimes such as Claude and Codex. The platform is free for individuals and offers paid plans for teams, emphasizing privacy by keeping credentials on the user’s machine.
image: https://maxxwell.dev/og.png
layout: provider
modified: '2026-10-29'
name: Rindler
nav: Providers
network: true
overview: 'Rindler is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, DeveloperTools, OpenSource, and Automation.


  The Rindler catalog on APIs.io includes 1 Spectral governance ruleset.


  Rindler''s developer surface includes changelog, engineering blog, documentation, getting-started guide, pricing, and 15 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Rindler API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: maxxwell-dev-rules
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Maxxwell Dev Domain Security
  slug: maxxwell-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Maxxwell Dev Vulnerability Disclosure
  slug: maxxwell-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: maxxwell-dev
tags:
- Company
- AI
- DeveloperTools
- OpenSource
- Automation
website: https://maxxwell.dev
---
