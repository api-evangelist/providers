---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Origin Agentic Access
  operation_count: 3
  slug: origin-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://airbrush.originmarkets.com/v3
  baseurl_source: declared
  description: The Trades API from Origin — 3 operation(s) for trades.
  name: Origin Trades API
  slug: origin-trades-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trades API
  slug: open-origin-trades-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/origin-capability-edges.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/origin-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/origin-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/origin-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/origin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/origin-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/origin-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/origin-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/origin-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/origin-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/origin-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/origin-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/origin-airbrush-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://originmarkets.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://login2.originmarkets.com/api/v1/
- group: docs
  title: ''
  type: Documentation
  url: https://airbrush.originmarkets.com/v3/
- group: docs
  title: ''
  type: APIReference
  url: https://airbrush.originmarkets.com/v3/
- group: company
  title: ''
  type: Blog
  url: https://originmarkets.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OriginMarkets/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.originmarkets.com/
- group: operate
  title: ''
  type: Support
  url: https://originmarkets.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://originmarkets.com/privacy-policy
- group: company
  title: ''
  type: About
  url: https://originmarkets.com/about
created: '2026-07-17'
description: Origin (Origin Markets) is a digital debt capital markets (DCM) platform that automates bond issuance from front to back, connecting issuers, dealers, lawyers, and market infrastructure on a single platform. Its products cover automated transaction Documentation (termsheets and final terms with collaborative review and e-signing), Structured Notes, and a Marketplace database of 1,000+ issuers. Origin publishes a read-only Trades API and the open Airbrush "universal data language" (an ISO 20022-aligned OpenAPI specification) for post-trade straight-through processing across the ecosystem.
examples:
- key_count: 41
  name: Origin Termsheet Fixed_Rate
  slug: origin-termsheet-fixed_rate
- key_count: 41
  name: Origin Termsheet Floating_Rate
  slug: origin-termsheet-floating_rate
- key_count: 35
  name: Origin Termsheet Zero_Coupon
  slug: origin-termsheet-zero_coupon
image: https://originmarkets.com/universal/svg/social-accounts.svg
layout: provider
modified: '2026-07-20'
name: Origin
nav: Providers
network: true
overview: 'Origin publishes 1 API on the [APIs.io](https://apis.io/) network: Trades API. Tagged areas include Company, Financial-Services, Capital Markets, Bond Issuance, and Debt Capital Markets.


  Origin''s developer surface includes authentication, changelog, documentation, API reference, engineering blog, support, and 18 more developer resources.'
random_paper: 18
screenshot: https://raw.githubusercontent.com/api-evangelist/origin/refs/heads/main/screenshots/origin-2026-08-07T190930.png
security:
- kind: authentication
  name: Origin Authentication
  slug: origin-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Origin Domain Security
  slug: origin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: origin
tags:
- Company
- Financial-Services
- Capital Markets
- Bond Issuance
- Debt Capital Markets
- Fixed Income
- Post-Trade
- ISO 20022
- Fintech
- Straight-Through Processing
website: https://originmarkets.com/
---
