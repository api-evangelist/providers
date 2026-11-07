---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aol Agentic Access
  operation_count: 4
  slug: aol-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: 'AOL runs no developer portal of its own. App registration and the human documentation for the OAuth 2.0 / OpenID Connect endpoints AOL serves at api.login.aol.com live on the Yahoo Developer Network, '
  name: Yahoo Developer Network (legacy documentation for the AOL identity stack)
  slug: yahoo-developer-network-legacy-documentation-for-the-aol-identity-stack
- baseURL: https://api.login.aol.com
  baseurl_source: declared
  description: 'OpenID Connect userinfo and JWKS endpoints served by AOL at api.login.aol.com under issuer https://api.login.aol.com. Standard claims including sub, name, email, email_verified, locale, birthdate and '
  name: AOL OpenID Connect API
  slug: aol-openid-connect-api
- baseURL: https://api.login.yahoo.com
  baseurl_source: declared
  description: OAuth 2.0 Authorization Code grant endpoints
  name: AOL O Auth2 API
  slug: aol-oauth2-api
artifact_total: 17
collections:
- collection_type: open
  name: Yahoo (formerly AOL) OAuth 2.0 and OpenID Connect OAuth2 API
  slug: open-aol-oauth2-api
- collection_type: open
  name: Yahoo (formerly AOL) OAuth 2.0 and OAuth2 OpenID Connect API
  slug: open-aol-openid-connect-api
- collection_type: open
  name: Yahoo (formerly AOL) OAuth 2.0 and OpenID Connect API
  slug: open-aol
common:
- group: commercial
  href: https://artifacts.apis.io/aol/finops/aol-finops.yml
  title: ''
  type: FinOps
  url: finops/aol-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.aol.com/news/
- group: other
  href: https://artifacts.apis.io/aol/overlays/aol-oauth2-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aol-oauth2-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/aol/agentic-access/aol-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aol-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/aol/authentication/aol-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aol-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aol/scopes/aol-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aol-scopes.yml
- group: design
  href: https://artifacts.apis.io/aol/conventions/aol-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aol-conventions.yml
- group: design
  href: https://artifacts.apis.io/aol/errors/aol-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aol-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aol/data-model/aol-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aol-data-model.yml
- group: design
  href: https://artifacts.apis.io/aol/conformance/aol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aol-conformance.yml
- group: design
  href: https://artifacts.apis.io/aol/lifecycle/aol-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aol-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aol.com/
- group: agent
  href: https://artifacts.apis.io/aol/well-known/aol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aol-well-known.yml
- group: auth
  href: https://artifacts.apis.io/aol/well-known/aol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aol-security.txt
- group: auth
  href: https://artifacts.apis.io/aol/security/aol-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aol-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aol/security/aol-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aol-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aol/security/aol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aol-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/aol/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aol/llms/aol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aol-llms.txt
- group: build
  href: https://artifacts.apis.io/aol/packages/aol-packages.yml
  title: ''
  type: Packages
  url: packages/aol-packages.yml
- group: operate
  href: https://artifacts.apis.io/aol/rate-limits/aol-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aol-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aol/plans/aol-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aol-plans-pricing.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aol
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aol
- group: company
  title: ''
  type: Website
  url: https://www.aol.com
- group: operate
  title: ''
  type: Support
  url: https://help.aol.com/
- group: start
  title: ''
  type: SignUp
  url: https://login.aol.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.aol.com/terms/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.aol.com/privacy/index.html
created: '2026-03-23'
description: AOL is a consumer internet media and communications brand — AOL.com news, AOL Mail, AOL Search and AOL Desktop — operated by AOL Media LLC. Founded as America Online, it was acquired by Verizon in 2015, folded into Oath and then Yahoo, and sold on to the Italian software company Bending Spoons in 2026; the security.txt AOL serves today points its PGP key at bendingspoons.com. AOL runs no developer program and publishes no product API. Its one publicly callable, machine-readable contract is the OpenID Connect provider at api.login.aol.com, which serves a full discovery document under its own issuer and lets a third-party application sign a user in with their AOL account. The legacy developer documentation for that identity stack is hosted by Yahoo Inc., which runs a sibling deployment of the same Oath-era OAuth 2.0 / OIDC platform.
finops:
- has_sources: true
  method: derived
  name: Aol Finops
  primary_unit: ''
  service_category: ''
  slug: aol-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aol.png
layout: provider
modified: '2026-10-06'
name: AOL
nav: Providers
network: true
overview: 'AOL publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including OpenID Connect API, O Auth2 API, and 1 more. Tagged areas include Digital Media, News, Entertainment, Advertising, and Identity.


  The AOL catalog on APIs.io includes 1 Spectral governance ruleset.


  AOL''s developer surface includes engineering blog, authentication, support, signup flow, and 25 more developer resources.'
plans:
- name: Aol Plans Pricing
  plan_count: 0
  slug: aol-plans-pricing
press:
- date: ''
  title: Bending Spoons' Post
  url: https://www.linkedin.com/posts/bendingspoons_big-news-were-acquiring-aol-the-iconic-activity-7389337958274846720-grwP
- date: ''
  title: Preparing for the workforce in the age of AI
  url: https://www.aol.com/news/preparing-workforce-age-ai-033320503.html
- date: ''
  title: AOL is sold in reputed $1.5B deal to tech conglomerate
  url: https://www.aol.com/articles/ve-got-owner-aol-sold-201343341.html
- date: ''
  title: Bending Spoons' acquisition of AOL shows the value ...
  url: https://www.artificialintelligence-news.com/news/bending-spoons-acquisition-of-aol-shows-the-value-of-legacy-platforms/
- date: ''
  title: BBB warns about AI search use, details how to use it smartly
  url: https://www.aol.com/news/bbb-warns-ai-search-details-201446520.html
random_paper: 4
rate_limits:
- limit_count: 0
  name: Aol Rate Limits
  slug: aol-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: AOL API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: aol-rules
scopes:
- name: Aol Scopes
  scope_count: 4
  slug: aol-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 49.9
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 28.9
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aol/aol-2026-06-20T172055.png
security:
- kind: authentication
  name: Aol Authentication
  slug: aol-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Aol Domain Security
  slug: aol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aol Vulnerability Disclosure
  slug: aol-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: revoke-aol-access
  slug: aol-revoke-aol-access
- name: sign-in-with-aol
  slug: aol-sign-in-with-aol
slug: aol
tags:
- Digital Media
- News
- Entertainment
- Advertising
- Identity
- OpenID Connect
- Authentication
- Email
- Consumer Internet
- Fortune 1000
website: https://www.aol.com
---
