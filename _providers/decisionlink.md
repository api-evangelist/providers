---
access_model:
  confidence: medium
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.xfactor.io/get-a-demo/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.8
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: The largest of the Xfactor.io platform services — 88 paths and 109 operations covering value propositions, companies, accounts, solutions and products, benefits and value drivers, workflows, discovery
  name: Xfactor.io Value Proposition API
  slug: xfactorio-value-proposition-api
- description: Reference-data service for the value model — accrual types, area types, case-study improvement types, cost categories, expense types, format types, impact types, and the translation/localization compo
  name: Xfactor.io Value Facts API
  slug: xfactorio-value-facts-api
- description: The Growth AI conversational service — chat sessions and history, prompt management, file upload, feedback, and long-running generation jobs for value propositions and value models with a /stream/{job
  name: Xfactor.io Value Chat API
  slug: xfactorio-value-chat-api
- description: The buyer-facing collaboration surface — a separate login, and read access to a shared value proposition's discovery, benefits, factors and assets. 8 paths, 10 operations, Auth0 bearer authentication.
  name: Xfactor.io Collaboration Manager API
  slug: xfactorio-collaboration-manager-api
artifact_total: 13
collections:
- collection_type: open
  name: Collaboration Manager
  slug: open-decisionlink-collaboration
- collection_type: open
  name: Value Chat Server
  slug: open-decisionlink-value-chat
- collection_type: open
  name: Value Facts
  slug: open-decisionlink-value-facts
- collection_type: open
  name: Value Proposition
  slug: open-decisionlink-value-proposition
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decisionlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xfactor.io/
- group: company
  title: ''
  type: Blog
  url: https://www.xfactor.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.xfactor.io/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xfactor.io/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xfactor.io/terms-of-use/
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.secureframe.com/ext/trust-center/xfactor-io/
- group: auth
  title: ''
  type: Compliance
  url: https://app.secureframe.com/ext/trust-center/xfactor-io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XFactor-IO
- group: start
  title: ''
  type: Login
  url: https://app.xfactor.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/decisionlink-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/decisionlink-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/decisionlink-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/decisionlink-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/decisionlink-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/decisionlink-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/decisionlink-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/decisionlink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/decisionlink-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/decisionlink-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/decisionlink-value-proposition-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/decisionlink-value-facts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/decisionlink-value-chat-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/decisionlink-collaboration-overlay.yaml
created: '2026-07-17'
description: 'DecisionLink pioneered enterprise Customer Value Management (CVM), giving B2B sales, marketing, and customer-success teams a platform to quantify, present, and defend the economic value their products deliver to buyers. The company has since rebranded and relaunched as Xfactor.io, a revenue-operations AI platform that builds a "digital twin" of a company''s go-to-market system: it unifies CRM, pipeline, usage, and finance signals into Xfactor Central, surfaces cross-source risk through Xfactor OpenInsights with plain-English alerts, and lets teams simulate growth scenarios before committing with Xfactor Simulation and Growth AI. Backed by Accel, the company sells to revenue and go-to-market leaders. The platform runs on a set of FastAPI services behind api.xfactor.io — Value Proposition, Value Facts, Value Chat and Collaboration Manager — which serve live OpenAPI 3.1 documents and Swagger UI reference pages anonymously, while every operation itself is protected by Auth0 bearer
  tokens. There is no developer portal, pricing page, or published onboarding path: the subscription agreement and data-processing addendum are the only places the company describes its APIs in prose, and API-based access is issued as SHA-256-hashed API keys to contracted customers. Security posture is published via a SecureFrame trust center (SOC 2 Type II).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decisionlink.png
layout: provider
modified: '2026-08-13'
name: DecisionLink
nav: Providers
network: true
overview: 'DecisionLink publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Xfactor.io Value Proposition API, Xfactor.io Value Facts API, Xfactor.io Value Chat API, and 1 more. Tagged areas include Company, Cloud Saas, Revenue Operations, Customer Value Management, and Artificial Intelligence.


  DecisionLink''s developer surface includes engineering blog, support, authentication, and 22 more developer resources.'
plans:
- name: Decisionlink Plans Pricing
  plan_count: 0
  slug: decisionlink-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Decisionlink Rate Limits
  slug: decisionlink-rate-limits
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 30.3
    contract_quality: 57.6
    developer_ergonomics: 13.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 33.7
  provenance:
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decisionlink/refs/heads/main/screenshots/decisionlink-2026-07-25T211527.png
security:
- kind: authentication
  name: Decisionlink Authentication
  slug: decisionlink-authentication
  summary_line: http/oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Decisionlink Domain Security
  slug: decisionlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Decisionlink Trust Center
  slug: decisionlink-trust-center
  summary_line: SOC 2 Type II
slug: decisionlink
tags:
- Company
- Cloud Saas
- Revenue Operations
- Customer Value Management
- Artificial Intelligence
- Go-To-Market
- Sales
- Analytics
- Value Selling
- Forecasting
website: https://www.xfactor.io/
---
