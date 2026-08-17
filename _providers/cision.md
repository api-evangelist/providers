---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: REST API for CisionOne that allows connection of media monitoring data with internal tools and BI platforms. Provides access to mention streams, aggregated analytics, and media coverage data. Response
  name: CisionOne API
  slug: cisionone-api
- description: REST API for the Next Generation Cision Communications Cloud, Cision's earned media monitoring and analytics platform. Runs off searches already created in the platform and returns either a list of ar
  name: Next Generation Cision Communications Cloud API
  slug: cision-communications-cloud-api
- description: Public data API behind Cision Web Solutions, Cision's embeddable investor relations and online newsroom module library. Serves press release feeds and media feeds (JSON, XML and RSS), share price hist
  name: Cision Web Solutions Public API
  slug: cision-web-solutions-api
artifact_total: 10
asyncapis:
- description: ''
  name: Cision Webhooks
  slug: cision-webhooks
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/cision-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cision.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cision.atlassian.net/wiki/spaces/CSM/pages/26385776684/CisionOne+-+API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cision
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cision
- group: company
  title: ''
  type: Blog
  url: https://www.cision.com/us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cision.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://oneuptime.cision.com/
- group: other
  title: ''
  type: X
  url: https://x.com/cision
- group: commercial
  title: ''
  type: Plans
  url: plans/cision-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cision-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cision-finops.yml
- group: company
  title: ''
  type: News
  url: https://www.cision.com/pr-distribution-and-placement/prnewswire/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cision.one/docs/api/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://cision.atlassian.net/wiki/spaces/CSM/pages/25764989843/Settings+-+Cision+API
- group: operate
  title: ''
  type: HelpCenter
  url: https://cision.atlassian.net/wiki/spaces/CSM/overview
- group: operate
  title: ''
  type: Support
  url: https://www.cision.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://app.cision.one/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cision.com/legal/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cision.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cision.com/legal/security-statement/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cision-cisionone-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cision-cisionone-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/cision-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cision-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cision-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cision-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cision-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cision-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cision-packages.yml
- group: design
  title: ''
  type: Components
  url: components/cision-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cision-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cision-llms.txt
created: '2026-06-13'
description: Cision is an AI-powered PR and earned media software platform offering REST APIs for media database access, press release distribution, media monitoring, analytics, and influencer identification. CisionOne provides a REST API that connects media monitoring data with internal tools, BI platforms, and reporting systems.
finops:
- name: Cision Finops
  service_category: ''
  slug: cision-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cision.png
jsonld:
- class_count: 0
  name: Cision Context
  property_count: 5
  slug: cision-context
layout: provider
modified: '2026-08-13'
name: Cision
nav: Providers
network: true
overview: 'Cision publishes 1 API on the [APIs.io](https://apis.io/) network: CisionOne API. Tagged areas include PR Software, Public Relations, Earned Media, Media Monitoring, and Press Release Distribution.


  The Cision catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Cision''s developer surface includes authentication, documentation, engineering blog, pricing, product news, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Cision Plans Pricing
  plan_count: 5
  slug: cision-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 2
  name: Cision Rate Limits
  slug: cision-rate-limits
score:
  band: strong
  composite: 64.0
  delta: 29.4
  facets:
    commercial_clarity: 92.1
    contract_quality: 65.7
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 65.8
  previous_composite: 34.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cision/refs/heads/main/screenshots/cision-2026-06-20T174406.png
security:
- kind: authentication
  name: Cision Authentication
  slug: cision-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cision Domain Security
  slug: cision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cision
tags:
- PR Software
- Public Relations
- Earned Media
- Media Monitoring
- Press Release Distribution
- Media Database
- Influencer Identification
- Analytics
website: https://www.cision.com/
---
