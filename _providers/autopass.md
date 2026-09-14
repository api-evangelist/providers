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
api_count: 1
apis:
- baseURL: https://api.autopass.xyz
  baseurl_source: declared
  description: Partner parking locations (POIs)
  name: Autopass Locations API
  slug: autopass-locations-api
- baseURL: https://api.autopass.xyz
  baseurl_source: declared
  description: Completed parking transactions and invoices
  name: Autopass Orders API
  slug: autopass-orders-api
- baseURL: https://api.autopass.xyz
  baseurl_source: declared
  description: In-progress parking sessions
  name: Autopass Sessions API
  slug: autopass-sessions-api
artifact_total: 11
asyncapis:
- description: ''
  name: Autopass Webhooks
  slug: autopass-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Autopass Service Authorization Locations API
  slug: open-autopass-locations-api
- collection_type: open
  name: Autopass Service Authorization Locations Orders API
  slug: open-autopass-orders-api
- collection_type: open
  name: Autopass Service Authorization Locations Sessions API
  slug: open-autopass-sessions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/autopass-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autopass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.autopass.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.autopass.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.autopass.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.autopass.xyz/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/autopass-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autopass-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/autopass-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autopass-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/autopass-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/autopass-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autopass-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/autopass-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/autopass-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autopass.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autopass.xyz/privacy
created: '2026-07-17'
description: 'Autopass ("快速通") is a Taiwan-based mobility financial-services platform that connects service locations, car-owner apps, payments and benefits so that every driver enjoys a fast, convenient driving experience. Through its "powered by Autopass" service-authorization program, channel brand partners embed license-plate-based parking payment into their own car-owner apps: they register user license plates, surface partner parking locations (POIs) with live rates and hours, read in-progress parking sessions and completed orders, and receive entry/exit/billing/refund notifications over an OAuth 2.0 / OpenID Connect secured API. Autopass aims to become Asia''s largest provider of mobility financial services. Backed by 500 Global.'
image: https://www.autopass.xyz/autopass_og.jpg
layout: provider
modified: '2026-07-18'
name: Autopass
nav: Providers
network: true
overview: 'Autopass publishes 3 APIs on the [APIs.io](https://apis.io/) network: Locations API, Orders API, and Sessions API. Tagged areas include Company, Mobility, Parking, Payments, and Automotive.


  The Autopass catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Autopass'' developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 19
scopes:
- name: Autopass Scopes
  scope_count: 1
  slug: autopass-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
screenshot: https://raw.githubusercontent.com/api-evangelist/autopass/refs/heads/main/screenshots/autopass-2026-07-25T201842.png
security:
- kind: authentication
  name: Autopass Authentication
  slug: autopass-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Autopass Domain Security
  slug: autopass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autopass
tags:
- Company
- Mobility
- Parking
- Payments
- Automotive
- Financial-Services
- Authentication
- Taiwan
website: https://en.autopass.xyz
---
