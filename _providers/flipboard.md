---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Flipboard supports RSS feeds as the primary integration mechanism for publishers and content creators. Publishers can submit RSS feeds to be featured as Flipboard Magazines, enabling content distribut
  name: Flipboard RSS Feeds
  slug: rss-feeds
- description: Flipboard has implemented the ActivityPub protocol, making its content available to the broader Fediverse. Starting in 2023, Flipboard began federating its magazines and curators via ActivityPub, allo
  name: Flipboard ActivityPub
  slug: activitypub
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flipboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flipboard.com/
- group: company
  title: ''
  type: About
  url: https://about.flipboard.com/
- group: start
  title: ''
  type: Portal
  url: https://about.flipboard.com/forpublishers/
- group: docs
  title: ''
  type: Documentation
  url: https://about.flipboard.com/rss-guidelines/
- group: other
  title: ''
  type: Validator
  url: https://feedvalidator.flipboard.com/
- group: company
  title: ''
  type: Blog
  url: https://engineering.flipboard.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flipboard
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Flipboard/activitypub
- group: operate
  title: ''
  type: Support
  url: https://flipboard.helpshift.com/hc/en/
- group: operate
  title: ''
  type: Contact
  url: https://flipboard.helpshift.com/hc/en/1-flipboard/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.flipboard.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.flipboard.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://about.flipboard.com/cookie-policy/
- group: docs
  title: ''
  type: CommunityGuidelines
  url: https://about.flipboard.com/community-guidelines/
- group: other
  title: ''
  type: X
  url: https://x.com/flipboard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flipboard
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/flipboard
created: '2024-01-01'
description: Flipboard is a content curation and social magazine platform that aggregates articles, videos, and social media posts into personalized, magazine-style feeds. Founded in 2010, Flipboard allows users to curate content into magazines around topics of interest and follow curators and publishers. Flipboard has embraced open web standards, implementing ActivityPub to federate with the Fediverse and supporting RSS for publisher content distribution.
finops:
- name: Flipboard Finops
  service_category: API
  slug: flipboard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flipboard.png
layout: provider
modified: '2026-04-28'
name: Flipboard
nav: Providers
network: true
overview: 'Flipboard publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ActivityPub, Content Curation, Digital Publishing, Fediverse, and News.


  Flipboard''s developer surface includes developer portal, documentation, engineering blog, support, and 14 more developer resources.'
plans:
- name: Flipboard Plans Pricing
  plan_count: 3
  slug: flipboard-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Flipboard Rate Limits
  slug: flipboard-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 20.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flipboard/refs/heads/main/screenshots/flipboard-2026-06-20T181315.png
security:
- kind: domain-security
  name: Flipboard Domain Security
  slug: flipboard-domain-security
  summary_line: TLSv1.3 · DMARC
slug: flipboard
tags:
- ActivityPub
- Content Curation
- Digital Publishing
- Fediverse
- News
- RSS
- Social-Media
website: https://flipboard.com/
---
