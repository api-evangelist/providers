---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://entire.io/feed.xml
- group: company
  title: ''
  type: Website
  url: https://entire.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.entire.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.entire.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.entire.io/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/entireio
- group: company
  title: ''
  type: Blog
  url: https://entire.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://entire.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://entire.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://entire.io/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://entire.io/dpa
- group: agent
  href: https://artifacts.apis.io/entire/llms/entire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/entire-llms.txt
- group: agent
  href: https://artifacts.apis.io/entire/well-known/entire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/entire-well-known.yml
- group: auth
  href: https://artifacts.apis.io/entire/well-known/entire-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entire-security.txt
- group: auth
  title: ''
  type: Security
  url: https://entire.io/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/entire/security/entire-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/entire-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/entire/security/entire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/entire-domain-security.yml
- group: design
  href: https://artifacts.apis.io/entire/conformance/entire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/entire-conformance.yml
- group: auth
  href: https://artifacts.apis.io/entire/authentication/entire-authentication.yml
  title: ''
  type: Authentication
  url: authentication/entire-authentication.yml
- group: build
  href: https://artifacts.apis.io/entire/packages/entire-packages.yml
  title: ''
  type: Packages
  url: packages/entire-packages.yml
- group: build
  href: https://artifacts.apis.io/entire/cli/entire-cli.yml
  title: ''
  type: CLI
  url: cli/entire-cli.yml
- group: agent
  href: https://artifacts.apis.io/entire/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/entire/changelog/entire-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/entire-changelog.yml
created: '2026-07-17'
description: 'Entire is a developer platform built for both humans and AI agents, founded by former GitHub CEO Thomas Dohmke and launched with a $60M seed round. It pairs fast, distributed, Git-compatible hosting with agent session management: the Entire CLI hooks into your Git workflow and captures every coding-agent session — prompts, tool calls, and decisions — as Checkpoints indexed alongside commits, creating a searchable record of how code was written. Features include session-to-commit pairing, secret detection and user-defined redaction, multi-agent parallel review, cross-agent work resumption, and a distributed Git mirroring network for fast, rate-limit-free clones.'
image: https://entire.io/favicon.svg
layout: provider
modified: '2026-10-06'
name: Entire
nav: Providers
network: true
overview: 'Entire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Developer Platform, Version Control, and Git Hosting.


  Entire''s developer surface includes documentation, getting-started guide, engineering blog, signup flow, authentication, CLI, changelog, and 16 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 48.2
    operational_transparency: 31.6
  previous_composite: 34.5
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: UK
      standard: uk-gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 3
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/entire/entire-2026-07-25T213431.png
security:
- kind: authentication
  name: Entire Authentication
  slug: entire-authentication
  summary_line: oauth2-device/bearer-token · 2 schemes
- kind: domain-security
  name: Entire Domain Security
  slug: entire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Entire Vulnerability Disclosure
  slug: entire-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: Entire Skills
  slug: entire-published-skills
slug: entire
tags:
- Company
- Developer Tools
- Developer Platform
- Version Control
- Git Hosting
- AI Agents
- Agent Infrastructure
- CLI
website: https://entire.io
---
