---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Token-authenticated REST API for the AppNeta SaaS platform. v4 (Intelligent Alarms) and v3 (Classic) expose monitoring data, monitoring policies, Monitoring Point provisioning, web-application and net
  name: AppNeta REST API
  slug: appneta-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Appneta Broadcom Software Observer Webhooks
  slug: appneta-broadcom-software-observer-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.appneta.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.broadcom.com/appneta
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api/api-v4.html
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api/api-access-tokens.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/appneta-broadcom-software-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.appneta.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appneta
- group: operate
  title: ''
  type: StatusPage
  url: https://status.broadcom.com/services/appneta/
- group: operate
  title: ''
  type: Deprecation
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/release-notes/release-notes-saas.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appneta-broadcom-software-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appneta-broadcom-software-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appneta-broadcom-software-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appneta-broadcom-software-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/appneta-broadcom-software-observer-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appneta-broadcom-software-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appneta-broadcom-software-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/appneta-broadcom-software-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.broadcom.com/support/trust-center
- group: operate
  title: ''
  type: Support
  url: https://support.broadcom.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appneta.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.appneta.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadcom.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy/policy
created: '2026-07-17'
description: AppNeta is a network performance monitoring (NPM) platform, now part of Broadcom's Enterprise Software (IT Operations Management) portfolio, delivering continuous end-to-end visibility into application, network-path, and end-user experience across SaaS, cloud, and internet-facing environments. Distributed Monitoring Points run active synthetic tests (network path, web/HTTP, and browser-based experience) and stream metrics to the AppNeta SaaS platform. AppNeta exposes a token-authenticated REST API (v3 for Classic and v4 for Intelligent Alarms) for retrieving monitoring data, managing monitoring policies, provisioning Monitoring Points, and integrating performance telemetry into external observability and data pipelines.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appneta-broadcom-software.png
layout: provider
modified: '2026-07-18'
name: AppNeta (Broadcom Software)
nav: Providers
network: true
overview: 'AppNeta (Broadcom Software) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Network Monitoring, Network Performance, Observability, and Application Performance.


  The AppNeta (Broadcom Software) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AppNeta (Broadcom Software)''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, changelog, support, and 17 more developer resources.'
random_paper: 69
score:
  band: developing
  composite: 49.9
  delta: 5.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 44.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/appneta-broadcom-software/refs/heads/main/screenshots/appneta-broadcom-software-2026-07-25T200813.png
security:
- kind: authentication
  name: Appneta Broadcom Software Authentication
  slug: appneta-broadcom-software-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appneta Broadcom Software Domain Security
  slug: appneta-broadcom-software-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Appneta Broadcom Software Trust Center
  slug: appneta-broadcom-software-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, SOC 2, SOC 3, HIPAA, PCI DSS, FedRAMP
slug: appneta-broadcom-software
tags:
- Company
- Network Monitoring
- Network Performance
- Observability
- Application Performance
- Digital Experience Monitoring
- Synthetic Monitoring
- IT Operations
- Broadcom
- Ai Infrastructure
website: https://www.appneta.com/
---
