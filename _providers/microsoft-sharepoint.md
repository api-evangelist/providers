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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft Sharepoint Agentic Access
  operation_count: 15
  slug: microsoft-sharepoint-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 10
apis:
- description: 'The Microsoft Graph SharePoint Sites API provides access to SharePoint sites, lists, and document libraries through the unified Microsoft Graph endpoint. It enables developers to manage site content, '
  name: Microsoft Graph SharePoint Sites API
  slug: graph-sites-api
- description: 'The SharePoint Webhooks API enables applications to subscribe to change notifications on SharePoint lists and libraries. When items are created, updated, or deleted, SharePoint sends notifications to '
  name: SharePoint Webhooks API
  slug: webhooks-api
- description: 'The SharePoint Search REST API provides full-text search capabilities across SharePoint content including sites, lists, libraries, and documents. It supports keyword query language, query refinement, '
  name: SharePoint Search REST API
  slug: search-api
- description: 'The SharePoint Framework (SPFx) is a development model for building client-side web parts, extensions, and adaptive card extensions for SharePoint and Microsoft Teams. It uses modern web technologies '
  name: SharePoint Framework (SPFx)
  slug: framework
- description: The $batch API from Microsoft SharePoint — 1 operation(s) for $batch.
  name: Microsoft SharePoint $batch API
  slug: microsoft-sharepoint-batch-api
- description: The Files API from Microsoft SharePoint — 3 operation(s) for files.
  name: Microsoft SharePoint Files API
  slug: microsoft-sharepoint-files-api
- description: The ListItems API from Microsoft SharePoint — 2 operation(s) for listitems.
  name: Microsoft SharePoint ListItems API
  slug: microsoft-sharepoint-listitems-api
- description: The Lists API from Microsoft SharePoint — 2 operation(s) for lists.
  name: Microsoft SharePoint Lists API
  slug: microsoft-sharepoint-lists-api
- description: The Site API from Microsoft SharePoint — 1 operation(s) for site.
  name: Microsoft SharePoint Site API
  slug: microsoft-sharepoint-site-api
- description: The Web API from Microsoft SharePoint — 2 operation(s) for web.
  name: Microsoft SharePoint Web API
  slug: microsoft-sharepoint-web-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SharePoint REST $batch $batch $batch API
  slug: open-microsoft-sharepoint-batch-api
- collection_type: open
  name: SharePoint REST $batch $batch Files API
  slug: open-microsoft-sharepoint-files-api
- collection_type: open
  name: SharePoint REST $batch $batch ListItems API
  slug: open-microsoft-sharepoint-listitems-api
- collection_type: open
  name: SharePoint REST $batch $batch Lists API
  slug: open-microsoft-sharepoint-lists-api
- collection_type: open
  name: SharePoint REST $batch $batch Site API
  slug: open-microsoft-sharepoint-site-api
- collection_type: open
  name: SharePoint REST $batch $batch Web API
  slug: open-microsoft-sharepoint-web-api
- collection_type: open
  name: SharePoint REST API
  slug: open-microsoft-sharepoint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-sharepoint-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-sharepoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-sharepoint-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/sharepoint/dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/sharepoint
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SharePoint
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SPBlog
created: '2024-01-01'
description: Microsoft SharePoint is a web-based collaboration platform that provides document management, content management, and team collaboration capabilities. It offers REST APIs, Microsoft Graph integration, and the SharePoint Framework for customization and extension.
finops:
- name: Microsoft Sharepoint Finops
  service_category: API
  slug: microsoft-sharepoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-sharepoint.png
layout: provider
modified: '2026-05-19'
name: Microsoft SharePoint
nav: Providers
network: true
overview: 'Microsoft SharePoint publishes 6 APIs on the [APIs.io](https://apis.io/) network, including $batch API, Files API, ListItems API, and 3 more. Tagged areas include Collaboration, Content Management, Microsoft, Microsoft-365, and SharePoint.


  Microsoft SharePoint''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Microsoft Sharepoint Plans Pricing
  plan_count: 3
  slug: microsoft-sharepoint-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Microsoft Sharepoint Rate Limits
  slug: microsoft-sharepoint-rate-limits
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 52.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-sharepoint/refs/heads/main/screenshots/microsoft-sharepoint-2026-06-20T185531.png
security:
- kind: authentication
  name: Microsoft Sharepoint Authentication
  slug: microsoft-sharepoint-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Sharepoint Domain Security
  slug: microsoft-sharepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-sharepoint
tags:
- Collaboration
- Content Management
- Microsoft
- Microsoft-365
- SharePoint
website: https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration
---
