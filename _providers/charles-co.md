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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Token-authenticated HTTP API behind the Charles conversational commerce platform. Clients authenticate against a per-tenant "universe" host and the central api.hello-charles.com service, then work wit
  name: Charles API
  slug: charles-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charles-co-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/charles-co-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/charles-co-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/charles-co-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/charles-co-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/charles-co-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hello-charles.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/charles-co-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.hello-charles.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://c-commerce.github.io/charles-browser-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://c-commerce.github.io/charles-browser-sdk/
- group: docs
  title: ''
  type: APIReference
  url: https://c-commerce.github.io/charles-browser-sdk/
- group: company
  title: ''
  type: Blog
  url: https://www.hello-charles.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.hello-charles.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.hello-charles.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/c-commerce
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/hello-charles/workspace/charles/
- group: start
  title: ''
  type: Login
  url: https://app.hello-charles.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.hello-charles.com/apply-for-a-demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hello-charles.com/privacy-policy/
- group: other
  title: ''
  type: Imprint
  url: https://www.hello-charles.com/imprint/
created: '2026-07-17'
description: Charles (charlesAI, hello-charles.com) is a Berlin-based conversational commerce and CRM platform that lets brands sell, market, and support customers over WhatsApp, Instagram, Facebook Messenger, and Webchat. Founded in 2019, the platform connects chat-app APIs (WhatsApp Business, Messenger) with e-commerce and CRM systems such as Shopify, Salesforce, SAP, and HubSpot, and layers AI agents over them to automate the full funnel from acquisition and conversion to retention while staying GDPR compliant. Charles exposes a token-authenticated HTTP API organized around per-tenant "universe" hosts, a public Postman workspace, and a (now deprecated) JavaScript/TypeScript browser SDK published to npm. It was surfaced as a portfolio lead of Speedinvest and enriched into the API Evangelist network from its public developer surface.
image: https://www.hello-charles.com/hubfs/feature_charles.png
layout: provider
modified: '2026-07-18'
name: Charles Co
nav: Providers
network: true
overview: 'Charles Co publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversational Commerce, Messaging, WhatsApp, and CRM.


  Charles Co''s developer surface includes authentication, documentation, API reference, engineering blog, support, signup flow, and 15 more developer resources.'
random_paper: 69
score:
  band: emerging
  composite: 26.0
  delta: -1.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charles-co/refs/heads/main/screenshots/charles-co-2026-07-25T205103.png
security:
- kind: authentication
  name: Charles Co Authentication
  slug: charles-co-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Charles Co Domain Security
  slug: charles-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: charles-co
tags:
- Company
- Conversational Commerce
- Messaging
- WhatsApp
- CRM
- Customer Support
- E-Commerce
- AI Agents
website: https://www.hello-charles.com/
---
