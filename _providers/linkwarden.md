---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 33
  human_in_the_loop: 4
  name: Linkwarden Agentic Access
  operation_count: 62
  slug: linkwarden-agentic-access
  summary_line: 62 operations · 33 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: Linkwarden's public REST API for managing bookmarks, archives, collections, and user settings.
  name: Linkwarden API
  slug: linkwarden-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Archives API from Linkwarden — 2 operation(s) for archives.
  name: Linkwarden Archives API
  slug: linkwarden-archives-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Auth API from Linkwarden — 3 operation(s) for auth.
  name: Linkwarden Auth API
  slug: linkwarden-auth-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Avatar API from Linkwarden — 1 operation(s) for avatar.
  name: Linkwarden Avatar API
  slug: linkwarden-avatar-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Collections API from Linkwarden — 2 operation(s) for collections.
  name: Linkwarden Collections API
  slug: linkwarden-collections-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Config API from Linkwarden — 1 operation(s) for config.
  name: Linkwarden Config API
  slug: linkwarden-config-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Dashboard API from Linkwarden — 2 operation(s) for dashboard.
  name: Linkwarden Dashboard API
  slug: linkwarden-dashboard-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Favicon API from Linkwarden — 1 operation(s) for favicon.
  name: Linkwarden Favicon API
  slug: linkwarden-favicon-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Highlights API from Linkwarden — 2 operation(s) for highlights.
  name: Linkwarden Highlights API
  slug: linkwarden-highlights-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Links API from Linkwarden — 5 operation(s) for links.
  name: Linkwarden Links API
  slug: linkwarden-links-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Logins API from Linkwarden — 1 operation(s) for logins.
  name: Linkwarden Logins API
  slug: linkwarden-logins-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Migration API from Linkwarden — 1 operation(s) for migration.
  name: Linkwarden Migration API
  slug: linkwarden-migration-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Preserved API from Linkwarden — 2 operation(s) for preserved.
  name: Linkwarden Preserved API
  slug: linkwarden-preserved-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Public API from Linkwarden — 5 operation(s) for public.
  name: Linkwarden Public API
  slug: linkwarden-public-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The RSS API from Linkwarden — 2 operation(s) for rss.
  name: Linkwarden RSS API
  slug: linkwarden-rss-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Search API from Linkwarden — 1 operation(s) for search.
  name: Linkwarden Search API
  slug: linkwarden-search-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Session API from Linkwarden — 1 operation(s) for session.
  name: Linkwarden Session API
  slug: linkwarden-session-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Tags API from Linkwarden — 2 operation(s) for tags.
  name: Linkwarden Tags API
  slug: linkwarden-tags-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Tokens API from Linkwarden — 2 operation(s) for tokens.
  name: Linkwarden Tokens API
  slug: linkwarden-tokens-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Users API from Linkwarden — 4 operation(s) for users.
  name: Linkwarden Users API
  slug: linkwarden-users-api
- baseURL: https://api.linkwarden.app
  baseurl_source: declared
  description: The Worker API from Linkwarden — 2 operation(s) for worker.
  name: Linkwarden Worker API
  slug: linkwarden-worker-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/linkwarden/agentic-access/linkwarden-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/linkwarden-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/linkwarden/plans/linkwarden-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linkwarden-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/linkwarden/rules/linkwarden-rules.yml
  title: ''
  type: Spectral
  url: rules/linkwarden-rules.yml
- group: design
  href: https://artifacts.apis.io/linkwarden/json-ld/linkwarden-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linkwarden-context.jsonld
- group: design
  href: https://artifacts.apis.io/linkwarden/vocabulary/linkwarden-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linkwarden-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/linkwarden/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/linkwarden/data-model/linkwarden-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linkwarden-data-model.yml
- group: design
  href: https://artifacts.apis.io/linkwarden/errors/linkwarden-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linkwarden-problem-types.yml
- group: design
  href: https://artifacts.apis.io/linkwarden/conformance/linkwarden-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linkwarden-conformance.yml
- group: other
  href: https://artifacts.apis.io/linkwarden/hosts/linkwarden-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkwarden-hosts.yml
- group: other
  href: https://artifacts.apis.io/linkwarden/vendors/linkwarden-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linkwarden-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linkwarden.app/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linkwarden.app/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://cloud.linkwarden.app/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://linkwarden.app/blog/releases/2.6
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linkwarden.app/getting-started/apple-shortcut
- group: auth
  href: https://artifacts.apis.io/linkwarden/authentication/linkwarden-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linkwarden-authentication.yml
- group: auth
  href: https://artifacts.apis.io/linkwarden/security/linkwarden-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkwarden-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linkwarden.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linkwarden.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://linkwarden.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://linkwarden.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkwarden
created: '2026-10-28'
description: Linkwarden provides an open-source, self‑hostable bookmark manager that lets users collect, read, annotate, and fully preserve web content. It offers full‑page archival, tagging, search, and sharing features, targeting individuals and teams who need a reliable, privacy‑focused solution for organizing online resources. The platform is built with modern web technologies and can be deployed on personal servers or cloud environments, ensuring data ownership and control.
image: https://linkwarden.app/og-image.jpg
jsonld:
- class_count: 5
  name: Linkwarden Context
  property_count: 37
  slug: linkwarden-context
layout: provider
modified: '2026-10-28'
name: Linkwarden
nav: Providers
network: true
overview: 'Linkwarden publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Archives API, Auth API, Avatar API, and 18 more. Tagged areas include Company, Bookmarking, OpenSource, SelfHostable, and Productivity.


  The Linkwarden catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Linkwarden''s developer surface includes changelog, getting-started guide, authentication, documentation, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Linkwarden Plans Pricing
  plan_count: 3
  slug: linkwarden-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Linkwarden API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 5
  slug: linkwarden-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 48.1
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
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
  name: Linkwarden Authentication
  slug: linkwarden-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Linkwarden Domain Security
  slug: linkwarden-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: linkwarden-create-and-get-link
  slug: linkwarden-create-and-get-link
- name: linkwarden-manage-tags
  slug: linkwarden-manage-tags
- name: linkwarden-manage-tokens
  slug: linkwarden-manage-tokens
slug: linkwarden
tags:
- Company
- Bookmarking
- OpenSource
- SelfHostable
- Productivity
website: https://linkwarden.app/
---
