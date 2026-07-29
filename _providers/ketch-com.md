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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: REST API for the Ketch platform, powering consent collection and enforcement, data subject rights workflows, data mapping, preference management, and risk reporting. Endpoints are served from global.k
  name: Ketch Platform API
  slug: ketch-platform-api
- description: TypeScript and JavaScript Web API and consent library for collecting, storing, and enforcing consent in browser environments. Includes the ketch-web-api client, the ketch-consent library, a typed ketc
  name: Ketch Web SDK
  slug: ketch-web-sdk
- description: Native iOS (Swift) and Android (Kotlin) SDKs plus a React Native module and a CocoaPods wrapper example for collecting and enforcing consent inside mobile applications. The iOS SDK supports iOS 15 and
  name: Ketch Mobile SDKs
  slug: ketch-mobile-sdks
- description: Server-side event forwarder specification and reference implementations that relay consent and DSR events from Ketch to downstream systems. Reference implementations are available in Go (go-ketch-forw
  name: Ketch Event Forwarders
  slug: ketch-event-forwarders
- description: Ketch command line interface, written in Go, for operating against Ketch infrastructure and developer workflows.
  name: Ketch CLI
  slug: ketch-cli
- description: Tag manager templates that route consent state from Ketch into common tag platforms — the Ketch GTM consent mode template and the Ketch <> Tealium consent template.
  name: Ketch Tag Manager Templates
  slug: ketch-tag-manager-templates
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ketch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ketch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ketch.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ketch.com/ketch/reference
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ketch-com
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ketch-sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ketch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.ketch.com/blog
- group: operate
  title: ''
  type: Status
  url: https://status.ketch.com/
- group: company
  title: ''
  type: Careers
  url: https://www.ketch.com/careers
created: '2026-05-25'
description: Ketch is a San Francisco-based data permissioning and consent management platform — known as Ketch Switchbit — that helps enterprises keep customer data clean, permissioned, and AI-ready across web, mobile, and backend systems. The platform spans consent management, data subject rights (DSR) automation, AI-powered data mapping, marketing preference management, risk and reporting, a Data Sentry privacy pentest, and an AI Governance layer. The Ketch Agent Network turns privacy program insights into agent-driven actions. Builders use a public REST API hosted at global.ketchapi.com, Web/iOS/Android SDKs published across the github.com/ketch-com and github.com/ketch-sdk orgs, a Google Tag Manager template, a React Native module, and event forwarders for Node, Go, and Java. Ketch advertises 1,000+ pre-built API integrations across analytics, CRM, CDP, ecommerce, marketing, tag management, and data warehouses, with a free cookie banner tier alongside paid mid-market and enterprise
  editions.
finops:
- name: Ketch Com Finops
  service_category: Security and Compliance
  slug: ketch-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ketch-com.png
layout: provider
modified: '2026-05-25'
name: Ketch
nav: Providers
network: true
overview: 'Ketch publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Privacy, Consent, Data Permissioning, DSR, and Data Mapping.


  Ketch''s developer surface includes documentation, API reference, pricing, engineering blog, status page, and 5 more developer resources.'
plans:
- name: Ketch Com Plans Pricing
  plan_count: 5
  slug: ketch-com-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 2
  name: Ketch Com Rate Limits
  slug: ketch-com-rate-limits
score:
  band: emerging
  composite: 22.7
  delta: -2.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ketch-com/refs/heads/main/screenshots/ketch-com-2026-06-20T184030.png
security:
- kind: domain-security
  name: Ketch Com Domain Security
  slug: ketch-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ketch-com
tags:
- Privacy
- Consent
- Data Permissioning
- DSR
- Data Mapping
- AI Governance
- Preference Management
- Risk
- GDPR
- CCPA
- CPRA
- Switchbit
website: https://www.ketch.com/
---
