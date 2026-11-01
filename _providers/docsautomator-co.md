---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST API for programmatic document generation, automation management, and e‑signature workflows.
  name: DocsAutomator API
  slug: docsautomator-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/docsautomator-co/rate-limits/docsautomator-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/docsautomator-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/docsautomator-co/plans/docsautomator-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docsautomator-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/docsautomator-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/docsautomator-co/changelog/docsautomator-co-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/docsautomator-co-changelog.yml
- group: auth
  href: https://artifacts.apis.io/docsautomator-co/authentication/docsautomator-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docsautomator-co-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docsautomator.co
- group: design
  href: https://artifacts.apis.io/docsautomator-co/lifecycle/docsautomator-co-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/docsautomator-co-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/docsautomator-co/errors/docsautomator-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docsautomator-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docsautomator-co/conformance/docsautomator-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docsautomator-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docsautomator-co/llms/docsautomator-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docsautomator-co-llms.txt
- group: other
  href: https://artifacts.apis.io/docsautomator-co/a2a/docsautomator-co-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/docsautomator-co-a2a.yml
- group: agent
  href: https://artifacts.apis.io/docsautomator-co/well-known/docsautomator-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docsautomator-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/docsautomator-co/hosts/docsautomator-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docsautomator-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/docsautomator-co/vendors/docsautomator-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docsautomator-co-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.docsautomator.co/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docsautomator.co/docs/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.docsautomator.co</span
- group: auth
  href: https://artifacts.apis.io/docsautomator-co/security/docsautomator-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docsautomator-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docsautomator.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docsautomator.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docsautomator.co/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://app.docsautomator.co
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docsautomator.co/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.docsautomator.co/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docsautomator.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docsautomator.co/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docsautomator
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.docsautomator.co/openapi.json
  - status: 401
    url: https://app.docsautomator.co/mcp
  - status: 401
    url: https://api.docsautomator.co/graphql
  - status: 401
    url: https://api.docsautomator.co/mcp
  - status: 200
    url: https://docsautomator.co/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: DocsAutomator provides a platform to generate, sign, and manage documents automatically from templates in Google Docs, Word, or PDF, integrating with data sources like Airtable, Notion, Google Sheets, Zapier, ChatGPT, Claude, and a REST API. It supports e‑signatures, dynamic content, and automated filing, targeting businesses seeking no‑code document automation.
image: https://www.docsautomator.co/images/og/home.jpg
layout: provider
modified: '2026-10-30'
name: docsautomator-co
nav: Providers
network: true
overview: 'docsautomator-co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DocumentAutomation, NoCode, AI, ESignature, and Integration.


  docsautomator-co''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Docsautomator Co Plans Pricing
  plan_count: 3
  slug: docsautomator-co-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Docsautomator Co Rate Limits
  slug: docsautomator-co-rate-limits
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 58.6
    catalog_earned_first_party: 0.0
    catalog_gap: 56.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 65.3
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
  name: Docsautomator Co Authentication
  slug: docsautomator-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Docsautomator Co Domain Security
  slug: docsautomator-co-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: create-document
  slug: docsautomator-co-create-document
slug: docsautomator-co
tags:
- DocumentAutomation
- NoCode
- AI
- ESignature
- Integration
website: https://docsautomator.co/
---
