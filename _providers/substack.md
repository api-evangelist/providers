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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: 'Narrowly scoped official API that returns public Substack profile data for a given LinkedIn handle. Access requires accepting the Developer API Terms of Use, applying via form, and generating a token '
  name: Substack Developer API
  slug: substack-developer-api
- description: Per-publication public RSS feeds available at https://{publication}.substack.com/feed for syndication and read-only access to posts.
  name: Substack RSS Feeds
  slug: substack-rss-feeds
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/substack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/substack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://substack.com/
- group: company
  title: ''
  type: About
  url: https://substack.com/about
- group: operate
  title: ''
  type: Help
  url: https://support.substack.com/
- group: company
  title: ''
  type: Blog
  url: https://on.substack.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://substack.com/pricing
- group: company
  title: ''
  type: Jobs
  url: https://substack.com/jobs
- group: operate
  title: ''
  type: Contact
  url: https://substack.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://substack.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://substack.com/privacy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://substack.com/vulnerability-disclosure
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/substackinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/substack
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SubstackInc
created: '2026-05-08'
description: Substack is an independent newsletter and media platform that lets writers, podcasters, video creators, and other culture makers publish directly to readers and monetize through paid subscriptions. Founded in 2017 by Chris Best (CEO), Jairaj Sethi (CTO), and Hamish McKenzie (CWO) and headquartered in San Francisco with a New York City office, Substack provides built-in subscription billing, paid posts, podcasting, chat, video, Notes, and a cross-publication recommendations network. Creators keep 90 percent of subscription revenue (less credit card fees) and own their mailing lists and content. The platform reports more than five million paid subscriptions and tens of millions of weekly active readers. Substack does not offer a general-purpose public REST API for managing publications, posts, or subscribers. It does publish a narrowly scoped official Developer API (released April 2026) that allows token-authenticated lookup of public Substack profiles by LinkedIn handle, gated
  by an application and Terms-of-Use process. Read access to public content is otherwise available via per-publication RSS feeds, and the broader integration ecosystem relies on reverse-engineered, unofficial JSON endpoints used by the Substack web application.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/substack.png
layout: provider
modified: '2026-05-25'
name: Substack
nav: Providers
network: true
overview: 'Substack publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Newsletters, Publishing, Creator Economy, Subscriptions, and Email.


  Substack''s developer surface includes engineering blog, pricing, and 13 more developer resources.'
random_paper: 52
score:
  band: emerging
  composite: 14.3
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/substack/refs/heads/main/screenshots/substack-2026-06-20T194631.png
security:
- kind: domain-security
  name: Substack Domain Security
  slug: substack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Substack Vulnerability Disclosure
  slug: substack-vulnerability-disclosure
  summary_line: disclosure policy published
slug: substack
tags:
- Newsletters
- Publishing
- Creator Economy
- Subscriptions
- Email
- Podcasting
- Notes
- Media
- Independent Media
- Paid Content
website: https://substack.com/
---
