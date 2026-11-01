---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 176
  human_in_the_loop: 8
  name: Mentio Dev Agentic Access
  operation_count: 352
  slug: mentio-dev-agentic-access
  summary_line: 352 operations · 176 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Alerts API from mentio-dev — 11 operation(s) for alerts.
  name: mentio-dev Alerts API
  slug: mentio-dev-alerts-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Analytics API from mentio-dev — 5 operation(s) for analytics.
  name: mentio-dev Analytics API
  slug: mentio-dev-analytics-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The API keys API from mentio-dev — 2 operation(s) for api keys.
  name: mentio-dev API keys API
  slug: mentio-dev-api-keys-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Attention API from mentio-dev — 2 operation(s) for attention.
  name: mentio-dev Attention API
  slug: mentio-dev-attention-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Auth API from mentio-dev — 1 operation(s) for auth.
  name: mentio-dev Auth API
  slug: mentio-dev-auth-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Billing API from mentio-dev — 5 operation(s) for billing.
  name: mentio-dev Billing API
  slug: mentio-dev-billing-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Company API from mentio-dev — 1 operation(s) for company.
  name: mentio-dev Company API
  slug: mentio-dev-company-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Feeds API from mentio-dev — 3 operation(s) for feeds.
  name: mentio-dev Feeds API
  slug: mentio-dev-feeds-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Filters API from mentio-dev — 1 operation(s) for filters.
  name: mentio-dev Filters API
  slug: mentio-dev-filters-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Groups API from mentio-dev — 2 operation(s) for groups.
  name: mentio-dev Groups API
  slug: mentio-dev-groups-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Keywords API from mentio-dev — 4 operation(s) for keywords.
  name: mentio-dev Keywords API
  slug: mentio-dev-keywords-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Members API from mentio-dev — 4 operation(s) for members.
  name: mentio-dev Members API
  slug: mentio-dev-members-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Mentions API from mentio-dev — 5 operation(s) for mentions.
  name: mentio-dev Mentions API
  slug: mentio-dev-mentions-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The People API from mentio-dev — 7 operation(s) for people.
  name: mentio-dev People API
  slug: mentio-dev-people-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Segments API from mentio-dev — 2 operation(s) for segments.
  name: mentio-dev Segments API
  slug: mentio-dev-segments-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The System API from mentio-dev — 1 operation(s) for system.
  name: mentio-dev System API
  slug: mentio-dev-system-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Usage API from mentio-dev — 2 operation(s) for usage.
  name: mentio-dev Usage API
  slug: mentio-dev-usage-api
- baseURL: https://api.mentio.dev
  baseurl_source: declared
  description: The Views API from mentio-dev — 2 operation(s) for views.
  name: mentio-dev Views API
  slug: mentio-dev-views-api
artifact_total: 36
asyncapis:
- description: ''
  name: Mentio Dev Webhooks
  slug: mentio-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/mentio-dev/agentic-access/mentio-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mentio-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/mentio-dev/rate-limits/mentio-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mentio-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mentio-dev/plans/mentio-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mentio-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mentio-dev/rules/mentio-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/mentio-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/mentio-dev/json-ld/mentio-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mentio-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/mentio-dev/vocabulary/mentio-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mentio-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mentio-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mentio-dev/asyncapi/mentio-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mentio-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/mentio-dev/data-model/mentio-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mentio-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/mentio-dev/cli/mentio-dev-cli.yml
  title: ''
  type: CLI
  url: cli/mentio-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/mentio-dev/conventions/mentio-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mentio-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/mentio-dev/authentication/mentio-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mentio-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/mentio-dev/errors/mentio-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mentio-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mentio-dev/conformance/mentio-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mentio-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mentio-dev/llms/mentio-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mentio-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/mentio-dev/well-known/mentio-dev-modelcontextprotocol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mentio-dev-modelcontextprotocol-security.txt
- group: agent
  href: https://artifacts.apis.io/mentio-dev/well-known/mentio-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mentio-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/mentio-dev/hosts/mentio-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mentio-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/mentio-dev/vendors/mentio-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mentio-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mentio.dev/terms/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@mentio-dev/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mentio.dev/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://mentio.dev/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mentio-dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mentio.dev/changelog
- group: auth
  href: https://artifacts.apis.io/mentio-dev/security/mentio-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mentio-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mentio.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mentio.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mentio.dev/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mentio.dev/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://mentio.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://mentio.dev/blog
created: '2026-10-30'
description: Mentio provides a social listening API that aggregates data from platforms like Reddit, Hacker News, GitHub, Bluesky, LinkedIn, Stack Overflow, YouTube, TikTok, Instagram, and more. It scores mentions with AI, offers REST endpoints, webhooks, and MCP integration, and includes SDKs for TypeScript and Python. The service targets developers and AI agents needing real‑time brand monitoring and audience insights.
image: https://mentio.dev/og.png
json_schemas:
- name: Alert
  property_count: 10
  slug: mentio-dev-alert
- name: FilterGroup
  property_count: 41
  slug: mentio-dev-filter-group
- name: KeywordHealth
  property_count: 11
  slug: mentio-dev-keyword-health
- name: Keyword
  property_count: 20
  slug: mentio-dev-keyword
- name: Mention
  property_count: 16
  slug: mentio-dev-mention
- name: View
  property_count: 6
  slug: mentio-dev-view
jsonld:
- class_count: 44
  name: Mentio Dev Context
  property_count: 202
  slug: mentio-dev-context
layout: provider
modified: '2026-10-30'
name: mentio-dev
nav: Providers
network: true
overview: 'mentio-dev publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Analytics API, API keys API, and 15 more. Tagged areas include Company, Social Listening, AI Integration, SDKs, and Real-time Monitoring.


  The mentio-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  mentio-dev''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, pricing, and 25 more developer resources.'
plans:
- name: Mentio Dev Plans Pricing
  plan_count: 3
  slug: mentio-dev-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Mentio Dev Rate Limits
  slug: mentio-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: mentio-dev API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 4
  slug: mentio-dev-rules
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 68.2
    developer_ergonomics: 58.9
    discoverability: 67.9
    operational_transparency: 71.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mentio Dev Authentication
  slug: mentio-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mentio Dev Domain Security
  slug: mentio-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: mentio-dev-billing-view-wallet-and-invoices
  slug: mentio-dev-billing-view-wallet-and-invoices
- name: mentio-dev-create-and-retrieve-group
  slug: mentio-dev-create-and-retrieve-group
- name: mentio-dev-create-test-run-alert
  slug: mentio-dev-create-test-run-alert
- name: mentio-dev-invite-member
  slug: mentio-dev-invite-member
slug: mentio-dev
tags:
- Company
- Social Listening
- AI Integration
- SDKs
- Real-time Monitoring
website: https://mentio.dev/
---
