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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 28.4
  scored_at: '2026-08-10'
api_count: 23
apis:
- description: Automate Photoshop workflows including image editing, layer manipulation, and batch processing.
  name: Adobe Photoshop API
  slug: adobe-photoshop-api
- description: Integrate Lightroom functionality for photo organization and editing.
  name: Adobe Lightroom API
  slug: adobe-lightroom-api
- description: Automate vector graphics creation and manipulation.
  name: Adobe Illustrator API
  slug: adobe-illustrator-api
- description: Automate document layout and publishing workflows.
  name: Adobe InDesign API
  slug: adobe-indesign-api
- description: Create, convert, OCR, and manipulate PDF documents.
  name: Adobe PDF Services API
  slug: adobe-pdf-services-api
- description: Extract content and structural information from PDF documents using AI-powered analysis including text, tables, and images.
  name: Adobe PDF Extract API
  slug: adobe-pdf-extract-api
- description: Automatically tag PDF documents for accessibility compliance using AI to identify headings, reading order, tables, and document structure.
  name: Adobe PDF Accessibility Auto-Tag API
  slug: adobe-pdf-accessibility-auto-tag-api
- description: Integrate e-signature workflows and document signing.
  name: Adobe Sign API
  slug: adobe-sign-api
- description: Access and analyze digital marketing analytics data.
  name: Adobe Analytics API
  slug: adobe-analytics-api
- description: Content management and digital asset management APIs.
  name: Adobe Experience Manager API
  slug: adobe-experience-manager-api
- description: Search and license stock photos, videos, and assets.
  name: Adobe Stock API
  slug: adobe-stock-api
- description: AI-powered generative image creation and editing.
  name: Adobe Firefly API
  slug: adobe-firefly-api
- description: AI-powered audio and video APIs for automated content production at scale including dynamic graphics rendering, video reframing, translation and lip sync, text to speech, and text to avatar.
  name: Adobe Firefly Audio/Video APIs
  slug: adobe-firefly-audiovideo-apis
- description: Connect applications to Creative Cloud Libraries giving users access to stored creative elements like logos, colors, character styles, and graphics.
  name: Adobe Creative Cloud Libraries API
  slug: adobe-creative-cloud-libraries-api
- description: Embed the full Adobe Express editor and quick actions into web applications for creating and editing visual content with thousands of templates and assets.
  name: Adobe Express Embed SDK
  slug: adobe-express-embed-sdk
- description: Extend Premiere Pro with plugins, panels, and automation for video editing workflows including support for new file formats, effects, and transitions.
  name: Adobe Premiere Pro API
  slug: adobe-premiere-pro-api
- description: Create visual effects, manipulate project elements, and automate complex tasks in After Effects through plugins, scripts, and panels.
  name: Adobe After Effects API
  slug: adobe-after-effects-api
- description: Programmatically perform operations against Experience Platform data including data ingestion, catalog management, query services, and identity resolution.
  name: Adobe Experience Platform API
  slug: adobe-experience-platform-api
- description: Manage personalization activities, audiences, offers, and deliver experiences across web, mobile, and IoT channels.
  name: Adobe Target API
  slug: adobe-target-api
- description: Manage marketing campaigns, deliveries, workflows, subscriptions, and profiles through REST APIs for cross-channel campaign orchestration.
  name: Adobe Campaign API
  slug: adobe-campaign-api
- description: Access and manage marketing automation data including leads, accounts, opportunities, campaigns, and assets through REST APIs.
  name: Adobe Marketo Engage API
  slug: adobe-marketo-engage-api
- description: Integrate with Adobe Commerce through REST and GraphQL APIs for managing products, orders, customers, and building headless commerce experiences.
  name: Adobe Commerce API
  slug: adobe-commerce-api
- description: Programmatically manage users, groups, and product entitlements for Adobe enterprise organizations.
  name: Adobe User Management API
  slug: adobe-user-management-api
artifact_total: 53
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-suite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-suite-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com
- group: auth
  title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/apis
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://developer.adobe.com/support/
created: '2024-01-01'
description: Collection of Adobe Creative Cloud and Experience Cloud APIs.
features:
- AI-powered generative image creation with Firefly
- PDF document creation, conversion, and OCR
- E-signature workflows with Adobe Sign
- Digital marketing analytics and reporting
- Content management and digital asset management
- Stock photo and asset licensing
- Creative Cloud Libraries for shared design assets
- Cross-channel campaign orchestration
- Video and audio AI-powered production
- Commerce and headless storefront APIs
finops:
- name: Adobe Suite Finops
  service_category: API
  slug: adobe-suite-finops
graphqls:
- description: Integrate with Adobe Commerce through REST and GraphQL APIs for managing products, orders, customers, and building headless commerce experiences.
  name: Adobe Suite GraphQL API
  slug: adobe-suite-graphql
image: /assets/icons/adobe-suite.png
integrations:
- Adobe Creative Cloud
- Adobe Experience Cloud
- Adobe Document Cloud
- Microsoft Office 365
- Salesforce
- SAP
- Workday
- Slack
layout: provider
modified: '2026-04-18'
name: Adobe Suite
nav: Providers
network: true
overview: 'Adobe Suite publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Adobe Photoshop API, Adobe Lightroom API, Adobe PDF Services API, and 2 more. Tagged areas include Ai, Analytics, Automation, Commerce, and Creative.


  Adobe Suite''s developer surface includes developer portal, authentication, developer console, getting-started guide, engineering blog, support, and 6 more developer resources.'
plans:
- name: Adobe Suite Plans Pricing
  plan_count: 3
  slug: adobe-suite-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Adobe Suite Rate Limits
  slug: adobe-suite-rate-limits
score:
  band: developing
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 43.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 42.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/screenshots/adobe-suite-2026-06-20T165033.png
security:
- kind: domain-security
  name: Adobe Suite Domain Security
  slug: adobe-suite-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Suite Vulnerability Disclosure
  slug: adobe-suite-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-suite
tags:
- Ai
- Analytics
- Automation
- Commerce
- Creative
- Design
- Documents
- Experience
- Marketing
- Personalization
- Video
use_cases:
- Automated creative asset production
- Document workflow automation and e-signatures
- Marketing campaign orchestration and analytics
- Headless commerce and personalization
- AI-powered content generation and editing
- Enterprise user and entitlement management
website: https://developer.adobe.com
---
