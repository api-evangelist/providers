---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Blog2Social Com Agentic Access
  operation_count: 21
  slug: blog2social-com-agentic-access
  summary_line: 21 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.blog2social.com/rest/v1.0
  baseurl_source: declared
  description: The Account API from Blog2Social — 1 operation(s) for account.
  name: Blog2Social Account API
  slug: blog2social-com-account-api
- baseURL: https://api.blog2social.com/rest/v1.0
  baseurl_source: declared
  description: The Authentication API from Blog2Social — 3 operation(s) for authentication.
  name: Blog2Social Authentication API
  slug: blog2social-com-authentication-api
- baseURL: https://api.blog2social.com/rest/v1.0
  baseurl_source: declared
  description: The Insights API from Blog2Social — 5 operation(s) for insights.
  name: Blog2Social Insights API
  slug: blog2social-com-insights-api
- baseURL: https://api.blog2social.com/rest/v1.0
  baseurl_source: declared
  description: The Network API from Blog2Social — 5 operation(s) for network.
  name: Blog2Social Network API
  slug: blog2social-com-network-api
- baseURL: https://api.blog2social.com/rest/v1.0
  baseurl_source: declared
  description: The Share API from Blog2Social — 2 operation(s) for share.
  name: Blog2Social Share API
  slug: blog2social-com-share-api
- baseURL: https://api.blog2social.com/rest/v1.0
  baseurl_source: declared
  description: The User API from Blog2Social — 2 operation(s) for user.
  name: Blog2Social User API
  slug: blog2social-com-user-api
- baseURL: https://api.blog2social.com/rest/v1.0
  baseurl_source: declared
  description: The Video API from Blog2Social — 3 operation(s) for video.
  name: Blog2Social Video API
  slug: blog2social-com-video-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/blog2social-com/agentic-access/blog2social-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blog2social-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blog2social-com/rules/blog2social-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blog2social-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blog2social-com/json-ld/blog2social-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blog2social-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blog2social-com/vocabulary/blog2social-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blog2social-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blog2social-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blog2social-com/data-model/blog2social-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blog2social-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/blog2social-com/errors/blog2social-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blog2social-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blog2social-com/conformance/blog2social-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blog2social-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blog2social-com/well-known/blog2social-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blog2social-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blog2social-com/hosts/blog2social-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blog2social-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.blog2social.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://community.blog2social.com/help
- group: start
  title: ''
  type: SignUp
  url: https://community.blog2social.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.blog2social.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://en.blog2social.com/pricing/
- group: auth
  href: https://artifacts.apis.io/blog2social-com/security/blog2social-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blog2social-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blog2social.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blog2social.com/api/
created: '2026-11-02'
description: Blog2Social provides a WordPress plugin and web app for automating social media publishing. It lets users schedule, cross‑post, and manage content across more than 20 networks, offering features like auto‑posting, content recycling, and analytics for marketers and bloggers.
image: https://new.blog2social.com/en/wp-content/uploads/sites/6/2024/04/hero-single-image-en.png
json_schemas:
- name: AuthList
  property_count: 0
  slug: blog2social-com-auth-list
- name: GraphInsightsArray
  property_count: 0
  slug: blog2social-com-graph-insights-array
- name: InsightsArray
  property_count: 0
  slug: blog2social-com-insights-array
- name: InsightsV2Response
  property_count: 8
  slug: blog2social-com-insights-v2-response
- name: PostObject
  property_count: 0
  slug: blog2social-com-post-object
- name: VideoPostObject
  property_count: 0
  slug: blog2social-com-video-post-object
jsonld:
- class_count: 30
  name: Blog2Social Com Context
  property_count: 48
  slug: blog2social-com-context
layout: provider
modified: '2026-11-02'
name: Blog2Social
nav: Providers
network: true
overview: 'Blog2Social publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Insights API, and 4 more. Tagged areas include Social Media, Automation, WordPress, Marketing, and Software-as-a-Service.


  The Blog2Social catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Blog2Social''s developer surface includes support, signup flow, pricing, documentation, and 14 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Blog2Social API Rules
  rule_count: 39
  severity_counts:
    error: 30
    hint: 0
    info: 4
    warn: 5
  slug: blog2social-com-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 60.2
    developer_ergonomics: 8.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blog2Social Com Domain Security
  slug: blog2social-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: blog2social-com-insights-management
  slug: blog2social-com-insights-management
slug: blog2social-com
tags:
- Social Media
- Automation
- WordPress
- Marketing
- Software-as-a-Service
website: https://blog2social.com/
---
