---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Podcast Co Agentic Access
  operation_count: 11
  slug: podcast-co-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://public-api.pod.co
  baseurl_source: declared
  description: The episodes API from Podcast.co — 3 operation(s) for episodes.
  name: Podcast.co Episodes API
  slug: podcast-co-episodes-api
- baseURL: https://public-api.pod.co
  baseurl_source: declared
  description: The podcast page API from Podcast.co — 1 operation(s) for podcast page.
  name: Podcast.co podcast page API
  slug: podcast-co-podcast-page-api
- baseURL: https://public-api.pod.co
  baseurl_source: declared
  description: The podcasts API from Podcast.co — 7 operation(s) for podcasts.
  name: Podcast.co Podcasts API
  slug: podcast-co-podcasts-api
- baseURL: https://public-api.pod.co
  baseurl_source: declared
  description: The subscribe button API from Podcast.co — 1 operation(s) for subscribe button.
  name: Podcast.co subscribe button API
  slug: podcast-co-subscribe-button-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/podcast-co/agentic-access/podcast-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/podcast-co-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/podcast-co/plans/podcast-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/podcast-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/podcast-co/rules/podcast-co-rules.yml
  title: ''
  type: Spectral
  url: rules/podcast-co-rules.yml
- group: design
  href: https://artifacts.apis.io/podcast-co/vocabulary/podcast-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/podcast-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/podcast-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/podcast-co/components/podcast-co-components.yml
  title: ''
  type: Components
  url: components/podcast-co-components.yml
- group: design
  href: https://artifacts.apis.io/podcast-co/lifecycle/podcast-co-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/podcast-co-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/podcast-co/errors/podcast-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/podcast-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/podcast-co/conformance/podcast-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/podcast-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/podcast-co/llms/podcast-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/podcast-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/podcast-co/well-known/podcast-co-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/podcast-co-help-security.txt
- group: agent
  href: https://artifacts.apis.io/podcast-co/well-known/podcast-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/podcast-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/podcast-co/hosts/podcast-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/podcast-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/podcast-co/vendors/podcast-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/podcast-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.podcast.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.podcast.co/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://help.podcast.co/en/articles/2707433-create-setup-a-podcast-network
- group: docs
  title: ''
  type: Documentation
  url: https://help.podcast.co/
- group: docs
  title: ''
  type: APIReference
  url: https://developers-36dc921ce4.podcast.co/openapi_specs/public
- group: auth
  href: https://artifacts.apis.io/podcast-co/security/podcast-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/podcast-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://podcast.co/
- group: company
  title: ''
  type: Blog
  url: https://blog.podcast.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.podcast.co/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.podcast.co/
- group: operate
  title: ''
  type: Support
  url: https://help.podcast.co/en/
- group: start
  title: ''
  type: SignUp
  url: https://studio.podcast.co/login
created: '2026-10-28'
description: Podcast.co provides a SaaS platform that enables individuals and businesses to create, host, distribute, and monetize podcasts. Users can record, edit, and publish audio episodes, manage private podcast networks, and integrate with major podcast directories. The service offers analytics, customizable players, and tools for audience growth, making it a comprehensive solution for podcast production and distribution.
image: https://cdn.prod.website-files.com/625431f4d13ef362a77a5ed9/62667e4a28cb826f878ae102_Logo_Full.svg
layout: provider
modified: '2026-10-28'
name: Podcast.co
nav: Providers
network: true
overview: 'Podcast.co publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Episodes API, podcast page API, Podcasts API, and 1 more. Tagged areas include Podcasting, Hosting, Audio, SaaS, and Media.


  The Podcast.co catalog on APIs.io includes 1 Spectral governance ruleset.


  Podcast.co''s developer surface includes getting-started guide, documentation, API reference, engineering blog, pricing, support, signup flow, and 19 more developer resources.'
plans:
- name: Podcast Co Plans Pricing
  plan_count: 1
  slug: podcast-co-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Podcast Co Rate Limits
  slug: podcast-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Podcast.co API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: podcast-co-rules
scopes:
- name: Podcast Co Scopes
  scope_count: 0
  slug: podcast-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 42.0
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Podcast Co Authentication
  slug: podcast-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Podcast Co Domain Security
  slug: podcast-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-podcast
  slug: podcast-co-get-podcast
slug: podcast-co
tags:
- Podcasting
- Hosting
- Audio
- SaaS
- Media
website: https://podcast.co/
---
