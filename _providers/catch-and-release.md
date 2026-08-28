---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.catchandrelease.com/
- group: company
  title: ''
  type: About
  url: https://www.catchandrelease.com/m/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.catchandrelease.com/m/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.catchandrelease.com/m/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.catchandrelease.com/m/faq
- group: start
  title: ''
  type: SignUp
  url: https://www.catchandrelease.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.catchandrelease.com/m/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.catchandrelease.com/m/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/catch-and-release-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catch-and-release-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CatchRelease
- group: operate
  title: ''
  type: StatusPage
  url: https://status.catchandrelease.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/catch-and-release-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/catch-and-release-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/catch-and-release-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/catch-and-release-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/catch-and-release-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Catch&Release ships only an end-user web application — its 415-URL sitemap contains zero developer or API pages, its own GitHub organization (github.com/CatchRelease, 35 public repos) contains no OpenAPI or Swagger file, and every path on the product host app.catchandrelease.com returns HTTP 302 to a FusionAuth login, while the terms of use prohibit automated access outright.
  evidence:
  - status: 200
    url: https://www.catchandrelease.com/sitemap.xml
  - status: 200
    url: https://www.catchandrelease.com/openapi.json
  - status: 302
    url: https://app.catchandrelease.com/openapi.json
  - status: 404
    url: https://www.catchandrelease.com/m/api
  - status: 200
    url: https://auth.catchandrelease.com/.well-known/openid-configuration
  - status: 200
    url: https://status.catchandrelease.com/api/v2/summary.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Catch&Release is a UGC creator platform and content-licensing marketplace that helps brands and agencies discover, license, and clear rights for "found content" — real videos, photos, and footage created by everyday people and creators — for use in advertising and marketing campaigns. Its workspace lets marketing teams search and curate licensable moments, send content calls to its creator community, negotiate offers, and handle the legal clearance and rights packages, while creators earn passive income by licensing clips from their camera rolls. The platform pairs a brand/agency workspace (collections, storyboards, teams) with a creator community, using an access-first, pay-for-what-you-use model. Added to the API Evangelist network from an Accel portfolio lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catch-and-release.png
layout: provider
modified: '2026-08-12'
name: Catch&Release
nav: Providers
network: true
overview: 'Catch&Release is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Saas, Content Licensing, User Generated Content, and Creator Economy.


  Catch&Release''s developer surface includes pricing, engineering blog, support, signup flow, and 13 more developer resources.'
plans:
- name: Catch And Release Plans Pricing
  plan_count: 4
  slug: catch-and-release-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Catch And Release Rate Limits
  slug: catch-and-release-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 24.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Catch And Release Domain Security
  slug: catch-and-release-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catch-and-release
tags:
- Company
- Cloud Saas
- Content Licensing
- User Generated Content
- Creator Economy
- Video
- Advertising
- Marketing
- Media
website: https://www.catchandrelease.com/
---
