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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: Calendar Overlay is Cloudwell's flagship SharePoint app for combining SharePoint lists and libraries, Outlook and Exchange calendars, Planner plans, and iCalendar feeds into a unified calendar surface
  name: Cloudwell Calendar Overlay
  slug: calendar-overlay
- description: Org Chart for SharePoint and Microsoft Teams renders an interactive organization hierarchy from Entra ID/Azure AD reporting structure. Distributed as an SPFx solution; no public REST API.
  name: Cloudwell Org Chart
  slug: org-chart
- description: Staff Directory provides searchable, filterable employee directories across SharePoint and Teams, sourced from Microsoft Graph and Entra ID. Distributed as an SPFx solution; no public REST API.
  name: Cloudwell Staff Directory
  slug: staff-directory
- description: Team Members consolidates Microsoft 365 groups and Teams, SharePoint groups, and Azure AD groups and departments into a single view inside SharePoint. Distributed as an SPFx solution; no public REST A
  name: Cloudwell Team Members
  slug: team-members
- description: Viva Announcements lets users view Viva Connections announcements anywhere in SharePoint via an SPFx web part. No public REST API.
  name: Cloudwell Viva Announcements
  slug: viva-announcements
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudwell-opal-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudwell
- group: company
  title: ''
  type: Website
  url: https://cloudwell.io/
- group: other
  title: ''
  type: AppSource
  url: https://appsource.microsoft.com/en-us/marketplace/apps?search=cloudwell
- group: operate
  title: ''
  type: Support
  url: https://cloudwell.io/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudwell.io/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://cloudwell.io/feed/
created: '2024-01-01'
description: 'Cloudwell (cloudwell.io) is a Microsoft 365 and Azure-focused software partner founded in 2012, offering a suite of SharePoint and Teams apps: Calendar Overlay, Org Chart, Staff Directory, Team Members, and Viva Announcements - all distributed via Microsoft AppSource. Cloudwell does not publish a public REST API; their products are consumed inside SharePoint Online, Microsoft Teams, and Viva Connections via SharePoint Framework (SPFx) web parts and the Microsoft Graph API. The "opal" suffix in this repository name is preserved for index continuity but Cloudwell does not currently ship a product named Opal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudwell-opal.png
layout: provider
modified: '2026-04-25'
name: Cloudwell
nav: Providers
network: true
overview: 'Cloudwell publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AppSource, Calendar Overlay, Microsoft 365, Microsoft Partner, and Org Chart.


  Cloudwell''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 12.2
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudwell-opal/refs/heads/main/screenshots/cloudwell-opal-2026-06-20T174624.png
security:
- kind: domain-security
  name: Cloudwell Opal Domain Security
  slug: cloudwell-opal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudwell-opal
tags:
- AppSource
- Calendar Overlay
- Microsoft 365
- Microsoft Partner
- Org Chart
- SharePoint
- SPFx
- Staff Directory
- Teams
- Viva Connections
website: https://cloudwell.io/
---
