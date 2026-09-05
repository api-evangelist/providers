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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://nextbigideaclub.com/wp-json/members/v1
  baseurl_source: declared
  description: Membership, subscription, library and course operations.
  name: Next Big Idea Club members API
  slug: next-big-idea-club-members-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Next Big Idea Club members API
  slug: open-next-big-idea-club-members-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/next-big-idea-club-members-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://nextbigideaclub.com/
- group: start
  title: ''
  type: Login
  url: https://nextbigideaclub.com/login/
- group: operate
  title: ''
  type: Support
  url: https://nextbigideaclub.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nextbigideaclub.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nextbigideaclub.com/data-privacy/
- group: company
  title: ''
  type: Blog
  url: https://nextbigideaclub.com/magazine/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/next-big-idea-club-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/next-big-idea-club-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/next-big-idea-club-scopes.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/next-big-idea-club-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/next-big-idea-club-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/next-big-idea-club-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/next-big-idea-club-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/next-big-idea-club-domain-security.yml
created: '2026-07-17'
description: Next Big Idea Club is a nonfiction book subscription club and podcast that curates the most important new nonfiction, chosen by a selection committee of Malcolm Gladwell, Adam Grant, Susan Cain, and Daniel Pink. Members receive curated new nonfiction, an in-app library, courses, and author interviews across the web and native iOS/Android apps. The consumer experience is powered by a first-party WordPress REST API (the members/v1 namespace) secured with OAuth 2.0 / OpenID Connect via the WP OAuth Server, with Stripe integration for subscription billing. This profile was seeded as a Bloomberg Beta portfolio lead and enriched from the provider's public /wp-json/ discovery and /.well-known/ OAuth surface.
image: https://nextbigideaclub.com/wp-content/plugins/helium/themes/helium/favicon.ico
layout: provider
modified: '2026-07-20'
name: Next Big Idea Club
nav: Providers
network: true
overview: 'Next Big Idea Club publishes 1 API on the [APIs.io](https://apis.io/) network: members API. Tagged areas include Company, Books, Media, Subscription, and Nonfiction.


  Next Big Idea Club''s developer surface includes support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 12
scopes:
- name: Next Big Idea Club Scopes
  scope_count: 4
  slug: next-big-idea-club-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 33.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/next-big-idea-club/refs/heads/main/screenshots/next-big-idea-club-2026-08-07T185200.png
security:
- kind: authentication
  name: Next Big Idea Club Authentication
  slug: next-big-idea-club-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Next Big Idea Club Domain Security
  slug: next-big-idea-club-domain-security
  summary_line: TLSv1.3 · DMARC
slug: next-big-idea-club
tags:
- Company
- Books
- Media
- Subscription
- Nonfiction
- Podcast
- Education
- Membership
website: https://nextbigideaclub.com/
---
