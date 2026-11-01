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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: In-game rewarded-video ad API. A game server exchanges client credentials for a Bearer token, then requests ad opportunities for a player and reports the playback lifecycle (start, progress, complete,
  name: PlayerWON API
  slug: playerwon-api
artifact_total: 7
common:
- group: start
  href: https://artifacts.apis.io/simulmedia/sandbox/simulmedia-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/simulmedia-sandbox.yml
- group: other
  href: https://artifacts.apis.io/simulmedia/hosts/simulmedia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simulmedia-hosts.yml
- group: other
  href: https://artifacts.apis.io/simulmedia/vendors/simulmedia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simulmedia-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.simulmedia.com/team
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Simulmedia/playerwon-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Simulmedia/playerwon-sdk/releases
- group: auth
  href: https://artifacts.apis.io/simulmedia/security/simulmedia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simulmedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simulmedia.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Simulmedia
- group: company
  title: ''
  type: Blog
  url: https://simulmedia.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.simulmedia.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://platform.simulmedia.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://simulmedia.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.simulmedia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simulmedia.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simulmedia.com/terms
- group: operate
  href: https://artifacts.apis.io/simulmedia/changelog/simulmedia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/simulmedia-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/simulmedia/plans/simulmedia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simulmedia-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.playerwon.com/developers
coverage:
  checked: '2026-10-20'
  detail: PlayerWON's ad-server API page on playerwon.com is a JS-rendered marketing page with no endpoint reference, and no OpenAPI, AsyncAPI or GraphQL contract is served on game.simulmedia-apis.com or in the Simulmedia GitHub org; the API is known only from the open-source SDK.
  evidence:
  - status: 200
    url: https://www.playerwon.com/playerwon-ad-server-api
  - status: 200
    url: https://simulmedia.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Simulmedia is a technology-driven television advertising company that helps advertisers, agencies, and growth marketers plan, buy, and measure campaigns across linear TV, connected TV (CTV), and games. Its products include the Performance TV media-buying service, the AI-powered TV+ media-buying platform, and Simulmedia Self-Serve. Through PlayerWON, Simulmedia operates an in-game rewarded-video engagement and monetization platform for free-to-play console and PC games, exposed to game developers through the PlayerWON API and a first-party Unity/Unreal SDK. Simulmedia is a portfolio company of Union Square Ventures. This profile was enriched by the API Evangelist pipeline from the company's public developer surface and the open-source PlayerWON SDK.
image: https://logo.clearbit.com/simulmedia.com
layout: provider
modified: '2026-08-13'
name: Simulmedia
nav: Providers
network: true
overview: 'Simulmedia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Television, Connected TV, and Games.


  Simulmedia''s developer surface includes sandbox, engineering blog, signup flow, support, changelog, and 14 more developer resources.'
plans:
- name: Simulmedia Plans Pricing
  plan_count: 0
  slug: simulmedia-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Simulmedia Rate Limits
  slug: simulmedia-rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 67.9
    operational_transparency: 21.1
  previous_composite: 31.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/simulmedia/simulmedia-2026-09-02T155606.png
security:
- kind: authentication
  name: Simulmedia Authentication
  slug: simulmedia-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Simulmedia Domain Security
  slug: simulmedia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: playerwon-rewarded-video
  slug: simulmedia-playerwon-rewarded-video
- name: playerwon-token-broker
  slug: simulmedia-playerwon-token-broker
slug: simulmedia
tags:
- Company
- Advertising
- Television
- Connected TV
- Games
- AdTech
- Rewarded Video
- Media Buying
website: https://simulmedia.com
---
