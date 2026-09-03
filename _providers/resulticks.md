---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.resulticks.com/meeting-request.html
  - https://www.go.resul.io/book-a-meeting.html
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 7.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Resul (Resulticks) Web API is a JSON REST API served from the https://apis.resu.io base domain, documented publicly at gud.resulticks.com. Its call surface is grouped into six documented categorie
  name: Resul Web API
  slug: resulticks-web-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resulticks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.resulticks.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.resulticks.com/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.resulticks.com/terms-and-conditions.html
- group: operate
  title: ''
  type: Support
  url: https://www.resulticks.com/contact-us.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gud.resulticks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gud.resulticks.com/
- group: docs
  title: ''
  type: APIReference
  url: https://gud.resulticks.com/API-reference/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://gud.resulticks.com/Get-started/introduction/
- group: company
  title: ''
  type: Blog
  url: https://www.go.resul.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resulticks
- group: auth
  title: ''
  type: Authentication
  url: authentication/resulticks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/resulticks-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/resulticks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/resulticks-packages.yml
- group: design
  title: ''
  type: Components
  url: components/resulticks-components.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/resulticks-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/resulticks-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/resulticks-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/resulticks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/resulticks-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/resulticks-llms.txt
created: '2026-07-17'
description: Resulticks is an enterprise omnichannel marketing automation and audience engagement platform, operating under the RESUL brand. It pairs a cookie-independent customer data platform with real-time campaign orchestration across email, SMS, WhatsApp, RCS, LINE, web and mobile push, in-app messaging, voice, social and paid channels, plus audience scoring, Audience 360 journey analytics, a form generator and AI-assisted audience building. Resulticks publishes a public documentation portal at gud.resulticks.com carrying a REST API reference — account setup, data ingestion, audience and target-list management, communication creation and scheduling, and response analytics — against the base domain https://apis.resu.io, alongside web, Flutter, React Native, Cordova and iOS SDK guides. It ships no machine-readable API definition (no OpenAPI, AsyncAPI, GraphQL schema or MCP server), no public pricing, and no status or changelog page; the API host itself is not reachable from the public
  internet and is customer-scoped. Resulticks is backed by 500 Global.
image: https://www.resulticks.com/images/apple-touch-icon.png
layout: provider
modified: '2026-08-13'
name: Resulticks
nav: Providers
network: true
overview: 'Resulticks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Automation, Omnichannel, and Customer Engagement.


  Resulticks'' developer surface includes support, documentation, API reference, getting-started guide, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Resulticks Plans Pricing
  plan_count: 0
  slug: resulticks-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Resulticks Rate Limits
  slug: resulticks-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resulticks/refs/heads/main/screenshots/resulticks-2026-09-02T153607.png
security:
- kind: authentication
  name: Resulticks Authentication
  slug: resulticks-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Resulticks Domain Security
  slug: resulticks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: resulticks
tags:
- Company
- Marketing
- Marketing Automation
- Omnichannel
- Customer Engagement
- Customer Data Platform
- MarTech
- Campaign Management
- Audience
- Analytics
- Messaging
- SMS
- Email
- Push Notifications
- WhatsApp
website: https://www.resulticks.com/
---
