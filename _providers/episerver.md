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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: GraphQL Content Graph API that indexes CMS/Commerce content for fast, federated querying across the Optimizely platform.
  name: Optimizely Graph (Content Graph)
  slug: optimizely-graph-content-graph
- description: REST API and multi-language SDKs for feature flags, experimentation and rollouts, with the self-hosted Optimizely Agent as a microservice front end.
  name: Optimizely Feature Experimentation REST API
  slug: optimizely-feature-experimentation-rest-api
- description: Headless Content Delivery, Content Management and Content Definitions REST APIs for the Optimizely (Episerver) CMS.
  name: Content Management REST API (CMS 12)
  slug: content-management-rest-api-cms-12
artifact_total: 8
asyncapis:
- description: ''
  name: Episerver Webhooks
  slug: episerver-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.optimizely.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developers.optimizely.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.optimizely.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developers.optimizely.com/content-management-system/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developers.optimizely.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.optimizely.com
- group: company
  title: ''
  type: Blog
  url: https://www.optimizely.com/insights/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optimizely
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optimizely.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.developers.optimizely.com/deprecated-products/docs/deprecated-products
- group: commercial
  title: ''
  type: Pricing
  url: https://www.optimizely.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optimizely.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimizely.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.optimizely.com/trust-center/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/episerver-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.optimizely.com/trust-center/security
- group: build
  title: ''
  type: Packages
  url: packages/episerver-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/episerver-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/episerver-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/episerver-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/episerver-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/episerver-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/episerver-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/episerver-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/episerver-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/episerver-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/episerver-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/episerver-vulnerability-disclosure.yml
created: '2026-07-17'
description: Episerver is a digital experience platform (DXP) vendor that rebranded to Optimizely in 2021 after Episerver acquired Optimizely; the developer surface now ships under the Optimizely brand. The platform combines content management (CMS / Content Cloud), a headless Content Delivery and Content Management REST API, the Optimizely Graph (Content Graph) GraphQL API, Commerce (Configured Commerce and Commerce Connect), Feature Experimentation and Web Experimentation, the Optimizely Data Platform (ODP), the Content Marketing Platform (CMP), and Opti ID for unified OIDC identity. Developers integrate via first-party SDKs for JavaScript, React, Python, Java, C#/.NET, Ruby, PHP, Go and Swift, the EPiServer.CMS .NET libraries on NuGet, REST and GraphQL APIs, and webhooks. This profile was seeded as a portfolio lead and enriched by the API Evangelist pipeline from Optimizely's public developer documentation.
image: https://logo.clearbit.com/optimizely.com
layout: provider
modified: '2026-07-19'
name: Episerver
nav: Providers
network: true
overview: 'Episerver publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Content Management, Digital Experience Platform, and CMS.


  The Episerver catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Episerver''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 21 more developer resources.'
random_paper: 53
score:
  band: developing
  composite: 52.0
  delta: -1.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 63.2
  previous_composite: 53.1
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/episerver/refs/heads/main/screenshots/episerver-2026-07-25T213522.png
security:
- kind: authentication
  name: Episerver Authentication
  slug: episerver-authentication
  summary_line: oauth2/openIdConnect/apiKey/http · 6 schemes
- kind: domain-security
  name: Episerver Domain Security
  slug: episerver-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Episerver Vulnerability Disclosure
  slug: episerver-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Episerver Trust Center
  slug: episerver-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA
slug: episerver
tags:
- Company
- Enterprise
- Content Management
- Digital Experience Platform
- CMS
- Commerce
- Experimentation
- Personalization
- GraphQL
- SDKs
website: https://www.optimizely.com
---
