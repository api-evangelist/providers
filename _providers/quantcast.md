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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 21.4
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: 'The Quantcast Platform GraphQL API (v2) is the primary programmatic interface to the Quantcast advertising platform. It exposes queries and mutations for reporting, campaign and line item management, '
  name: Quantcast Platform GraphQL API
  slug: quantcast-platform-graphql-api
- description: The Quantcast Conversion API is a server-to-server integration that augments the browser-side Quantcast Live Tag. It accepts a JSON array of conversion events containing a conversion descriptor, a use
  name: Quantcast Conversion API
  slug: quantcast-conversion-api
- description: 'Quantcast Measure is the company''s free audience measurement product. Publishers and advertisers integrate the Quantcast Live Tag (Q Pixel) on web properties, or the Measure SDKs on iOS, Android, and '
  name: Quantcast Measure (Live Tag)
  slug: quantcast-measure-tag
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantcast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quantcast.com
- group: other
  title: ''
  type: Platform
  url: https://www.quantcast.com/platform/
- group: other
  title: ''
  type: Measure
  url: https://www.quantcast.com/measure/
- group: other
  title: ''
  type: Developers
  url: https://developers.quantcast.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.quantcast.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.quantcast.com/docs/graphql-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.quantcast.com/docs/graphql-api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.quantcast.com/docs/get-started/
- group: build
  title: ''
  type: Postman
  url: https://developers.quantcast.com/docs/QuantcastDeveloperAPI.postman_collection.json
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.quantcast.com
- group: operate
  title: ''
  type: Support
  url: https://help.quantcast.com
- group: auth
  title: ''
  type: Authentication
  url: https://developers.quantcast.com/docs/get-started/authentication/
- group: other
  title: ''
  type: Company
  url: https://www.quantcast.com/about-us/
- group: company
  title: ''
  type: Press
  url: https://www.quantcast.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.quantcast.com/resources/blog/
- group: company
  title: ''
  type: Careers
  url: https://www.quantcast.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.quantcast.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.quantcast.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.quantcast.com/login/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.quantcast.com/privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quantcast.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.quantcast.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quantcast.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/quantcast
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quantcast
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantcast
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/quantcast
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Quantcast
- group: other
  title: ''
  type: Acquisition
  url: https://www.quantcast.com/press-release/inmobi-acquires-quantcast-choice-to-enhance-frictionless-consent-management-for-publishers/
- group: build
  title: ''
  type: Packages
  url: packages/quantcast-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quantcast-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quantcast-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quantcast-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/quantcast-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quantcast-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/quantcast-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quantcast-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quantcast-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quantcast-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quantcast-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quantcast-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/quantcast-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/quantcast-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quantcast-llms.txt
created: '2026-05-25'
description: Quantcast is a San Francisco-headquartered digital advertising and audience intelligence company founded in 2006. Its flagship offering is the Quantcast Platform, an AI-driven demand-side platform (DSP) for programmatic display, video, CTV, audio, mobile, and native advertising, powered by the company's proprietary Audience Graph and Ara AI engine. Quantcast also operates Quantcast Measure, a free audience measurement product that has tagged millions of digital properties to produce demographic, psychographic, and cross-device audience insights. For programmatic access, Quantcast exposes a developer portal at developers.quantcast.com built around a GraphQL API (v2) for reporting, campaign management, and audience operations on the Quantcast Platform, secured via OAuth 2.0 client credentials. A server-to-server Conversion API augments the browser-side Live Tag for offline and signal-loss-resilient conversion tracking. Quantcast Choice, the company's IAB TCF v2-compliant Consent
  Management Platform, was acquired by InMobi in August 2023 and is now operated as part of InMobi CMP; legacy Quantcast Choice mobile SDKs remain published under the quantcast GitHub organization for reference. Quantcast also open-sources the Quantcast File System (QFS), a C++ distributed file system, and mobile/Roku measurement SDKs.
graphqls:
- description: <!--
  name: Quantcast GraphQL API
  slug: quantcast-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantcast.png
layout: provider
mcp_servers:
- description: ''
  name: Quantcast MCP candidate manifest (no server published)
  slug: quantcast-mcp-candidate-manifest-no-server-published
modified: '2026-08-13'
name: Quantcast
nav: Providers
network: true
overview: 'Quantcast publishes 1 API on the [APIs.io](https://apis.io/) network: Platform GraphQL API. Tagged areas include Advertising, AdTech, Programmatic Advertising, Demand-Side Platform, and DSP.


  Quantcast''s developer surface includes documentation, API reference, getting-started guide, support, authentication, engineering blog, signup flow, and 39 more developer resources.'
plans:
- name: Quantcast Plans Pricing
  plan_count: 0
  slug: quantcast-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Quantcast Rate Limits
  slug: quantcast-rate-limits
scopes:
- name: Quantcast Scopes
  scope_count: 2
  slug: quantcast-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 39.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quantcast/refs/heads/main/screenshots/quantcast-2026-06-20T192410.png
security:
- kind: authentication
  name: Quantcast Authentication
  slug: quantcast-authentication
  summary_line: oauth2/http/apiKey · 3 schemes
- kind: domain-security
  name: Quantcast Domain Security
  slug: quantcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quantcast
tags:
- Advertising
- AdTech
- Programmatic Advertising
- Demand-Side Platform
- DSP
- Audience Measurement
- Audience Intelligence
- Consent Management
- CMP
- Privacy
- GraphQL
- Conversion Tracking
- CTV
- Video Advertising
- Display Advertising
- Artificial Intelligence
- Audience Graph
website: https://www.quantcast.com
---
