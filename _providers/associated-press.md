---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Associated Press Agentic Access
  operation_count: 21
  slug: associated-press-agentic-access
  summary_line: 21 operations · 3 acting
api_count: 4
apis:
- description: Integrate your election systems with AP Elections API. Your election results delivery application retrieves election race information from AP Elections API to power election websites, reporting system
  name: AP Elections API
  slug: ap-elections-api
- description: The Account API from Associated Press — 6 operation(s) for account.
  name: Associated Press Account API
  slug: associated-press-account-api
- description: The Content API from Associated Press — 6 operation(s) for content.
  name: Associated Press Content API
  slug: associated-press-content-api
- description: The Monitors and Alerts API from Associated Press — 10 operation(s) for monitors and alerts.
  name: Associated Press Monitors and Alerts API
  slug: associated-press-monitors-and-alerts-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Associated Press AP Media Account API
  slug: open-associated-press-account-api
- collection_type: open
  name: Associated Press AP Media Account Content API
  slug: open-associated-press-content-api
- collection_type: open
  name: Associated Press AP Media Account Monitors and Alerts API
  slug: open-associated-press-monitors-and-alerts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/associated-press-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/associated-press-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/associated-press-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/associatedpress
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/associated-press
- group: start
  title: Associated Press Website
  type: Portal
  url: https://www.ap.org/
- group: start
  title: AP Developer Portal
  type: Portal
  url: https://developer.ap.org/
- group: docs
  title: Developer Documentation
  type: Documentation
  url: https://developer.ap.org/
created: '2024-04-14'
description: The Associated Press (AP) is an American not-for-profit news agency founded in 1846. The AP is the world's oldest and largest newsgathering organization, serving media companies worldwide with text, photos, video, audio, and interactive content. The AP provides developer APIs for accessing election data, news content, and media assets including the AP Elections API for real-time election results, the AP Content API for news and media asset access, and the AP Media API for digital asset management integration.
features:
- description: Real-time election results delivery for federal, state, and local elections with candidate data, race calls, and vote totals.
  name: AP Elections API
- description: Access to AP's global news content including text stories, photos, video, and graphics from AP correspondents worldwide.
  name: AP Content API
- description: Digital asset management integration for AP's extensive photo and video library with metadata, rights, and distribution capabilities.
  name: AP Media API
- description: Streaming news content delivery for applications requiring real-time news updates and content ingestion.
  name: AP DataStream
finops:
- name: Associated Press Finops
  service_category: API
  slug: associated-press-finops
graphqls:
- description: This GraphQL schema represents the conceptual data model for the Associated Press (AP) content and media APIs. The AP provides developer APIs for accessing news content, photos, video, audio, graphics
  name: Associated Press GraphQL Schema
  slug: associated-press-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/associated-press.png
integrations:
- description: AP content APIs integrate with major content management systems used by newspapers, broadcasters, and digital media publishers.
  name: Newsroom CMS Integrations
- description: Election technology vendors integrate AP Elections API for authoritative election result data in voting systems and election night reporting tools.
  name: Election Management Systems
layout: provider
modified: '2026-05-19'
name: Associated Press
nav: Providers
network: true
overview: 'Associated Press publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Content API, and Monitors and Alerts API. Tagged areas include Elections, Journalism, Media, News, and Content.


  Associated Press'' developer surface includes authentication, developer portal, documentation, and 5 more developer resources.'
plans:
- name: Associated Press Plans Pricing
  plan_count: 3
  slug: associated-press-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Associated Press Rate Limits
  slug: associated-press-rate-limits
score:
  band: thin
  composite: 32.5
  delta: -0.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 57.4
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/associated-press/refs/heads/main/screenshots/associated-press-2026-06-20T172505.png
security:
- kind: authentication
  name: Associated Press Authentication
  slug: associated-press-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Associated Press Domain Security
  slug: associated-press-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: associated-press
tags:
- Elections
- Journalism
- Media
- News
- Content
use_cases:
- description: News organizations and election management companies use the AP Elections API to power live election result dashboards and reporting.
  name: Election Coverage
- description: Media companies integrate AP content APIs to supplement their own coverage with AP newswire stories and multimedia content.
  name: News Content Integration
- description: Publishers and digital media companies access AP's photo and video archive through the Media API for editorial and commercial use.
  name: Photo and Video Licensing
website: https://www.ap.org/
---
