---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 40
  human_in_the_loop: 1
  name: Getziztu Com Agentic Access
  operation_count: 56
  slug: getziztu-com-agentic-access
  summary_line: 56 operations · 40 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Characters in a project
  name: getziztu-com Characters API
  slug: getziztu-com-characters-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Credit balance and ledger
  name: getziztu-com Credits API
  slug: getziztu-com-credits-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Director AI (planning, chat)
  name: getziztu-com Director API
  slug: getziztu-com-director-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Film export
  name: getziztu-com Export API
  slug: getziztu-com-export-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Paid media generation (first frames, clips, music, character images)
  name: getziztu-com Generate API
  slug: getziztu-com-generate-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Background jobs
  name: getziztu-com Jobs API
  slug: getziztu-com-jobs-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Media file download
  name: getziztu-com Media API
  slug: getziztu-com-media-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Spec and discovery
  name: getziztu-com Meta API
  slug: getziztu-com-meta-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Music tracks in a project
  name: getziztu-com Music API
  slug: getziztu-com-music-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Locations in a project
  name: getziztu-com Places API
  slug: getziztu-com-places-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Film projects
  name: getziztu-com Projects API
  slug: getziztu-com-projects-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: 'AI Script Writer (text only): guided draft, editor chat, Script Doctor, versions, import and export, script to shots'
  name: getziztu-com Script API
  slug: getziztu-com-script-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: Shots / scenes in a project
  name: getziztu-com Shots API
  slug: getziztu-com-shots-api
- baseURL: https://getziztu.com/api/v1
  baseurl_source: declared
  description: 'Studio apps: animate (AI Animation Generator), manga (AI Manga Maker), kamishibai (AI Story Video Generator), zukai (AI Explainer Video Maker), manzai (AI Comedy Skit Maker)'
  name: getziztu-com Tools API
  slug: getziztu-com-tools-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/getziztu-com/agentic-access/getziztu-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getziztu-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/getziztu-com/plans/getziztu-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getziztu-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/getziztu-com/rules/getziztu-com-rules.yml
  title: ''
  type: Spectral
  url: rules/getziztu-com-rules.yml
- group: design
  href: https://artifacts.apis.io/getziztu-com/vocabulary/getziztu-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getziztu-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/getziztu-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/getziztu-com/changelog/getziztu-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getziztu-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/getziztu-com/security/getziztu-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/getziztu-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/getziztu-com/conformance/getziztu-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getziztu-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getziztu-com/llms/getziztu-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getziztu-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/getziztu-com/well-known/getziztu-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getziztu-com-security.txt
- group: agent
  href: https://artifacts.apis.io/getziztu-com/well-known/getziztu-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getziztu-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getziztu-com/hosts/getziztu-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getziztu-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getziztu-com/vendors/getziztu-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getziztu-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getziztu.com/privacy
- group: start
  title: ''
  type: Login
  url: https://getziztu.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://getziztu.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://getziztu.com/docs
- group: auth
  href: https://artifacts.apis.io/getziztu-com/authentication/getziztu-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getziztu-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/getziztu-com/security/getziztu-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getziztu-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getziztu-com/security/getziztu-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getziztu-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getziztu.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://getziztu.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://getziztu.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getziztu.com/terms
- group: operate
  title: ''
  type: Support
  url: https://getziztu.com/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://getziztu.com/mcp
  - status: 200
    url: https://getziztu.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Ziztu (getziztu.com) offers an AI-powered reel maker that generates short-form videos, voiceovers, captions, and music in 55 viral styles. Users can input a topic to receive a finished reel or a longer YouTube video up to an hour, with the first reel free. The platform supports multiple languages and provides a web interface for creating engaging social media content.
image: https://getziztu.com/seo/og/default.png?v=1aae5a8c
layout: provider
modified: '2026-10-30'
name: getziztu-com
nav: Providers
network: true
overview: 'getziztu-com publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Characters API, Credits API, Director API, and 11 more. Tagged areas include Company, Artificial Intelligence, Video, Social Media, and Content Creation.


  The getziztu-com catalog on APIs.io includes 1 Spectral governance ruleset.


  getziztu-com''s developer surface includes changelog, API reference, authentication, pricing, engineering blog, support, and 19 more developer resources.'
plans:
- name: Getziztu Com Plans Pricing
  plan_count: 3
  slug: getziztu-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: getziztu-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: getziztu-com-rules
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 44.9
    developer_ergonomics: 20.8
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/getziztu-com/getziztu-com-2026-11-03T132809.png
security:
- kind: authentication
  name: Getziztu Com Authentication
  slug: getziztu-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Getziztu Com Domain Security
  slug: getziztu-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getziztu Com Vulnerability Disclosure
  slug: getziztu-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: getziztu-com-cancel-job
  slug: getziztu-com-cancel-job
- name: getziztu-com-generate-full-media
  slug: getziztu-com-generate-full-media
- name: getziztu-com-manage-project-lifecycle
  slug: getziztu-com-manage-project-lifecycle
- name: getziztu-com-start-tool-run
  slug: getziztu-com-start-tool-run
slug: getziztu-com
tags:
- Company
- Artificial Intelligence
- Video
- Social Media
- Content Creation
website: https://getziztu.com/
---
