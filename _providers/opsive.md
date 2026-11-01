---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: In-engine C# scripting API for Opsive's State Designer Unity asset. The StateMachine component is the main code entry point for a State Designer graph, used by other scripts to control execution, insp
  name: Opsive State Designer Scripting API
  slug: opsive-state-designer-scripting-api
- baseURL: https://unity.com
  baseurl_source: declared
  description: 'Opsive API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Opsive API
  slug: opsive-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/opsive/plans/opsive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opsive-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/opsive/rules/opsive-rules.yml
  title: ''
  type: Spectral
  url: rules/opsive-rules.yml
- group: design
  href: https://artifacts.apis.io/opsive/vocabulary/opsive-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opsive-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/opsive/cli/opsive-cli.yml
  title: ''
  type: CLI
  url: cli/opsive-cli.yml
- group: operate
  href: https://artifacts.apis.io/opsive/changelog/opsive-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opsive-changelog.yml
- group: design
  href: https://artifacts.apis.io/opsive/conformance/opsive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opsive-conformance.yml
- group: agent
  href: https://artifacts.apis.io/opsive/llms/opsive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opsive-llms.txt
- group: agent
  href: https://artifacts.apis.io/opsive/well-known/opsive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opsive-well-known.yml
- group: other
  href: https://artifacts.apis.io/opsive/hosts/opsive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opsive-hosts.yml
- group: build
  href: https://artifacts.apis.io/opsive/integrations/opsive-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/opsive-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/opsive/packages/opsive-packages.yml
  title: ''
  type: SDKs
  url: packages/opsive-packages.yml
- group: build
  href: https://artifacts.apis.io/opsive/packages/opsive-packages.yml
  title: ''
  type: Packages
  url: packages/opsive-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://opsive.com/support/documentation/state-designer/getting-started
- group: auth
  href: https://artifacts.apis.io/opsive/security/opsive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opsive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opsive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://opsive.com/support/documentation/ultimate-character-controller/
- group: operate
  title: ''
  type: Support
  url: https://opsive.com/support/
- group: operate
  title: ''
  type: Forum
  url: https://opsive.com/forum/
- group: company
  title: ''
  type: Blog
  url: https://opsive.com/news/
- group: start
  title: ''
  type: Login
  url: https://opsive.com/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opsive.com/terms-conditions/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Opsive
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Opsive/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/SD6SPWf7hW
- group: other
  title: ''
  type: Marketplace
  url: https://assetstore.unity.com/publishers/2308
created: '2026-10-18'
description: Opsive is a Unity game-development tools company that builds and sells editor assets for the Unity engine, including Behavior Designer Pro (behavior trees and AI), the Ultimate Character Controller, Third Person Controller and UFPS character controllers, the Ultimate Inventory System and State Designer, plus add-on packs (movement, senses, tactical, formations, agility, climbing, swimming, multiplayer). Products are sold through opsive.com and the Unity Asset Store, with per-product documentation, a forum and Discord community. Opsive does not publish a public web API.
image: https://opsive.com/wp-content/uploads/2026/06/logo.svg
layout: provider
modified: '2026-10-18'
name: Opsive
nav: Providers
network: true
overview: 'Opsive is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Game Development, Unity, Artificial Intelligence, and Behavior Trees.


  The Opsive catalog on APIs.io includes 1 Spectral governance ruleset.


  Opsive''s developer surface includes CLI, changelog, getting-started guide, documentation, support, engineering blog, and 19 more developer resources.'
plans:
- name: Opsive Plans Pricing
  plan_count: 2
  slug: opsive-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Opsive Rate Limits
  slug: opsive-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Opsive API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: opsive-rules
scopes:
- name: Opsive Scopes
  scope_count: 0
  slug: opsive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 15.8
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
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Opsive Authentication
  slug: opsive-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Opsive Domain Security
  slug: opsive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opsive
tags:
- Company
- Game Development
- Unity
- Artificial Intelligence
- Behavior Trees
- Character Controllers
- Inventory Systems
- Developer Tools
website: https://opsive.com/
---
