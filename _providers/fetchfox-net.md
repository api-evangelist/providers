---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Fetchfox Net Agentic Access
  operation_count: 35
  slug: fetchfox-net-agentic-access
  summary_line: 35 operations · 17 acting
api_count: 1
apis:
- description: Public social data API providing YouTube, Instagram, TikTok, and Facebook comment endpoints.
  name: Project API
  slug: project-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/fetchfox-net/conventions/fetchfox-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fetchfox-net-conventions.yml
- group: auth
  href: https://artifacts.apis.io/fetchfox-net/authentication/fetchfox-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fetchfox-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/fetchfox-net/conformance/fetchfox-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fetchfox-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fetchfox-net/llms/fetchfox-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fetchfox-net-llms.txt
- group: other
  href: https://artifacts.apis.io/fetchfox-net/hosts/fetchfox-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fetchfox-net-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fetchfox.net/terms
- group: operate
  title: ''
  type: Support
  url: https://fetchfox.net/support
- group: operate
  title: ''
  type: StatusPage
  url: https://fetchfox.net/status
- group: start
  title: ''
  type: Sandbox
  url: https://fetchfox.net/dashboard/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fetchfox.net/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://fetchfox.net/pricing
- group: start
  title: ''
  type: Login
  url: https://fetchfox.net/login
- group: docs
  title: ''
  type: Documentation
  url: https://fetchfox.net/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://fetchfox.net/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://fetchfox.net/markdown/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apify.com/api/v2
- group: auth
  href: https://artifacts.apis.io/fetchfox-net/security/fetchfox-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fetchfox-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fetchfox.net/
created: '2026-10-30'
description: FetchFox provides structured public social media data via REST and MCP APIs, offering YouTube transcripts, Instagram profiles, TikTok posts, and Facebook comments. Developers can integrate these data streams into agents and applications, with 20 free credits per month and no credit card required. The service emphasizes easy JSON responses, comprehensive documentation, and tools for building social data-driven experiences.
image: https://fetchfox.net/social-preview
layout: provider
modified: '2026-10-30'
name: fetchfox-net
nav: Providers
network: true
overview: 'fetchfox-net publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Social Data, API, Media, YouTube, and Instagram.


  The fetchfox-net catalog on APIs.io includes 1 Spectral governance ruleset.


  fetchfox-net''s developer surface includes authentication, support, sandbox, pricing, documentation, changelog, getting-started guide, and 11 more developer resources.'
plans:
- name: Fetchfox Net Plans Pricing
  plan_count: 4
  slug: fetchfox-net-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Fetchfox Net Rate Limits
  slug: fetchfox-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: fetchfox-net API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: fetchfox-net-rules
scopes:
- name: Fetchfox Net Scopes
  scope_count: 0
  slug: fetchfox-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 74.8
    catalog_earned_first_party: 0.0
    catalog_gap: 40.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 53.6
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 60.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fetchfox Net Authentication
  slug: fetchfox-net-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fetchfox Net Domain Security
  slug: fetchfox-net-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 6
skills:
- name: fetchfox-net-credits-skill
  slug: fetchfox-net-credits-skill
- name: fetchfox-net-facebook-skill
  slug: fetchfox-net-facebook-skill
- name: fetchfox-net-instagram-skill
  slug: fetchfox-net-instagram-skill
- name: fetchfox-net-status-skill
  slug: fetchfox-net-status-skill
- name: fetchfox-net-tiktok-skill
  slug: fetchfox-net-tiktok-skill
- name: fetchfox-net-youtube-skill
  slug: fetchfox-net-youtube-skill
slug: fetchfox-net
tags:
- Social Data
- API
- Media
- YouTube
- Instagram
- TikTok
website: https://fetchfox.net/
---
