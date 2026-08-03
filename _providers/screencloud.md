---
access_model:
  confidence: medium
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 6
apis:
- description: GraphQL operations for managing screens - pair and depair devices (pairScreen, depairScreen), list and search screens (allScreens, screen, screenByDeviceId, searchScreen), organize screen groups, assi
  name: ScreenCloud Studio Screens API
  slug: screencloud-studio-screens-api
- description: GraphQL operations for building and maintaining playlists - the ordered sequences of content shown on screens. Create, update, and delete playlists (createPlaylist, updatePlaylist, deletePlaylist), ad
  name: ScreenCloud Studio Playlists API
  slug: screencloud-studio-playlists-api
- description: GraphQL operations for uploading and organizing the media library - images, videos, and documents. Create and manage files (createFile, updateFileById, deleteFileById) and folders (createFolder, folde
  name: ScreenCloud Studio Media and Files API
  slug: screencloud-studio-media-files-api
- description: GraphQL operations for channels - the multi-zone layouts that compose playlists, apps, and media into a single screen experience - and for casting. Create, update, publish, and duplicate channels (cre
  name: ScreenCloud Studio Channels and Casts API
  slug: screencloud-studio-channels-casts-api
- description: GraphQL operations for signage apps and their instances - list the app catalog and categories (allApps, allAppCategories, appBySlug), create and configure app instances (createAppInstance, updateAppIn
  name: ScreenCloud Studio Apps API
  slug: screencloud-studio-apps-api
- description: GraphQL operations for proof-of-play and engagement reporting - fetch and export what played on which screen and when (getPlaybackLogs, exportPlaybackLogs), query logs and screen content histories (al
  name: ScreenCloud Studio Playback Logs API
  slug: screencloud-studio-playback-logs-api
artifact_total: 13
collections:
- collection_type: open
  name: ScreenCloud Studio API (GraphQL)
  slug: open-screencloud
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/screencloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/screencloud-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/screencloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/screencloud
- group: company
  title: ''
  type: Website
  url: https://screencloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.screencloud.com/
- group: start
  title: ''
  type: SignUp
  url: https://studio.screencloud.com
- group: commercial
  title: ''
  type: Plans
  url: plans/screencloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/screencloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/screencloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://screencloud.com/blog
created: '2026-07-05'
description: ScreenCloud is a cloud digital signage platform that turns any screen into a managed display for content, dashboards, and apps. Its developer surface is the ScreenCloud Studio API - a single public GraphQL endpoint (bearer-token authenticated, region-specific, copied from the DEVELOPER tab in Studio) that lets you automate anything you can do in Studio by hand - pairing and managing screens, building playlists and channels, uploading media and files, casting content, installing and configuring signage apps, and exporting playback logs and QR metrics. ScreenCloud also runs a Developer Platform / App framework for building custom HTML/JavaScript signage apps that can be published (with approval) to the App Store. There is no documented public WebSocket API - the Studio API is request/response GraphQL over HTTPS.
finops:
- name: Screencloud Finops
  service_category: Digital Signage and Content Management
  slug: screencloud-finops
graphqls:
- description: ScreenCloud is a cloud digital signage platform. Its documented public developer
  name: ScreenCloud Studio API (GraphQL)
  slug: screencloud-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/screencloud.png
layout: provider
modified: '2026-07-05'
name: ScreenCloud
nav: Providers
network: true
overview: 'ScreenCloud publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Signage, Screens, Content Management, GraphQL, and Media.


  ScreenCloud''s developer surface includes documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Screencloud Plans Pricing
  plan_count: 3
  slug: screencloud-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 4
  name: Screencloud Rate Limits
  slug: screencloud-rate-limits
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Screencloud Domain Security
  slug: screencloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Screencloud Trust Center
  slug: screencloud-trust-center
  summary_line: SOC 2, GDPR
slug: screencloud
tags:
- Digital Signage
- Screens
- Content Management
- GraphQL
- Media
- Playlists
- Displays
website: https://screencloud.com
---
