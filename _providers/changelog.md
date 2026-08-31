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
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: The Changelog podcast RSS feed provides access to all episodes of The Changelog, a weekly podcast covering software development, open source, and the people and projects behind the code. The feed retu
  name: The Changelog Podcast RSS Feed
  slug: podcast-rss
- description: The Changelog Master Feed aggregates all Changelog podcast shows into a single RSS feed. This is the one-stop subscription for all developer-focused audio content produced by Changelog Media, includin
  name: Changelog Master Feed RSS
  slug: master-feed-rss
- description: The Changelog News RSS feed surfaces the latest developer news curated by the Changelog team. Changelog News is a weekly newsletter and short podcast covering what is happening in software development
  name: Changelog News RSS Feed
  slug: news-rss
- description: The Changelog platform is an open source Elixir and Phoenix application that powers changelog.com. The source code is publicly available on GitHub and includes the full CMS, podcast management, episod
  name: Changelog Open Source Platform (GitHub)
  slug: github-platform
artifact_total: 36
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/thechangelog/changelog.com/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/thechangelog/changelog.com/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/changelog-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/changelog
- group: company
  title: ''
  type: Website
  url: https://changelog.com/
- group: other
  title: ''
  type: Podcast
  url: https://changelog.com/podcast
- group: other
  title: ''
  type: Podcast
  url: https://changelog.com/master
- group: company
  title: ''
  type: Newsletter
  url: https://changelog.com/news
- group: other
  title: ''
  type: RSSFeed
  url: https://changelog.com/podcast/feed
- group: other
  title: ''
  type: RSSFeed
  url: https://changelog.com/master/feed
- group: other
  title: ''
  type: RSSFeed
  url: https://changelog.com/news/feed
- group: other
  title: ''
  type: Sponsorship
  url: https://changelog.com/sponsor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://changelog.com/privacy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/thechangelog
- group: other
  title: ''
  type: Repository
  url: https://github.com/thechangelog/changelog.com
- group: other
  title: ''
  type: Podcast
  url: https://podcasts.apple.com/us/podcast/the-changelog-software-development-open-source/id341623264
- group: other
  title: ''
  type: Podcast
  url: https://open.spotify.com/show/5bBki72YeKSLUqyD94qsuJ
- group: other
  title: ''
  type: X
  url: https://x.com/changelog
- group: other
  title: ''
  type: Shows
  url: ''
created: '2026-03-24'
description: Changelog is a media company and podcast network for developers covering open source and software development. Founded by Adam Stacoviak and Jerod Santo, Changelog produces world-class developer podcasts including The Changelog, which features deep technical interviews and conversations with the people and teams driving open source software forward. Changelog also publishes a weekly developer news newsletter and operates an open source platform (changelog.com) built with Elixir and Phoenix.
features:
- name: Developer Podcasts
- name: Open Source Focus
- name: Weekly Newsletter
- name: Podcast Network
- name: RSS Feeds
- name: Master Feed
- name: Developer Community
- name: Episode Notes
- name: Guest Interviews
- name: Live Events
- name: Open Source Platform
- name: Elixir and Phoenix
- name: Sponsorships
finops:
- name: Changelog Finops
  service_category: API
  slug: changelog-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/changelog.png
integrations:
- name: Apple Podcasts
- name: Spotify
- name: Overcast
- name: Pocket Casts
- name: RSS
- name: GitHub
- name: YouTube
- name: Fireside
layout: provider
modified: '2026-04-23'
name: Changelog
nav: Providers
network: true
overview: 'Changelog publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Community, Media, Open-Source, and Podcasts.


  Changelog''s developer surface includes GitHub presence and 17 more developer resources.'
plans:
- name: Changelog Plans Pricing
  plan_count: 3
  slug: changelog-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Changelog Rate Limits
  slug: changelog-rate-limits
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  open_source:
    applies: true
    score: 25.0
  previous_composite: 15.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/changelog/refs/heads/main/screenshots/changelog-2026-06-20T174212.png
security:
- kind: domain-security
  name: Changelog Domain Security
  slug: changelog-domain-security
  summary_line: TLSv1.3 · DMARC
slug: changelog
tags:
- Developer Community
- Media
- Open-Source
- Podcasts
use_cases:
- name: Developer Education
- name: Open Source Promotion
- name: Podcast Distribution
- name: Newsletter Aggregation
- name: Developer News Consumption
- name: Conference and Event Coverage
- name: Sponsor Content Distribution
website: https://changelog.com/
---
