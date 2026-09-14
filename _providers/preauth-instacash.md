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
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api.preauth.io/v1
  baseurl_source: declared
  description: Create and manage pre-authorization orders.
  name: PreAuth (Instacash) Orders API
  slug: preauth-instacash-orders-api
artifact_total: 7
asyncapis:
- description: Preauth delivers order lifecycle notifications as HTTP POST requests to a URL the merchant configures in the developer panel (https://dashboard.preauth.io/panel/devs). Faithfully modeled from https://
  name: Preauth Webhooks
  slug: preauth-instacash-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Preauth Orders API
  slug: open-preauth-instacash-orders-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/preauth-instacash-orders-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/preauth-instacash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://preauth.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.preauth.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.preauth.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.preauth.io/api-rest
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.preauth.io/primeros-pasos
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/preauth-soporte/shared_invite/zt-18pzujyy8-F6cZBsHmZ_5OZFd16fnnWw
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.preauth.io/register
- group: auth
  title: ''
  type: Authentication
  url: authentication/preauth-instacash-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/preauth-instacash-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/preauth-instacash-packages.yml
- group: design
  title: ''
  type: Components
  url: components/preauth-instacash-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/preauth-instacash-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/preauth-instacash-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/preauth-instacash-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/preauth-instacash-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/preauth-instacash-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/preauth-instacash-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/preauth-instacash-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/preauth-instacash-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/preauth-instacash-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/preauth-instacash-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/preauth-instacash-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/preauth-instacash-well-known.yml
created: '2026-07-17'
description: Preauth is a Latin American fintech (the payment-guarantee product associated with the Instacash / Reevalúa lineage, surfaced via 500 Global) that lets businesses take and manage payment guarantees through card pre-authorization. A merchant creates an order via the REST API, the buyer's card is pre-authorized (funds reserved) through the hosted Preauth widget, and the merchant can later capture all or part of the reserved amount, update it, cancel it to release the hold, or run a card liveness check. It operates across Chile, Colombia, Mexico, Peru, and Argentina and integrates with Izipay, Kushki, dLocal, Stripe, Mercadopago, and Conekta as payment processors. Authentication is a per-request x-auth-token API key, and order lifecycle events are delivered by webhooks.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/preauth-instacash.png
layout: provider
modified: '2026-07-20'
name: PreAuth (Instacash)
nav: Providers
network: true
overview: 'PreAuth (Instacash) publishes 1 API on the [APIs.io](https://apis.io/) network: Orders API. Tagged areas include Company, Payments, Payment Pre-Authorization, Payment Guarantees, and Fintech.


  The PreAuth (Instacash) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PreAuth (Instacash)''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 19 more developer resources.'
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/preauth-instacash/refs/heads/main/screenshots/preauth-instacash-2026-08-17T124847.png
security:
- kind: authentication
  name: Preauth Instacash Authentication
  slug: preauth-instacash-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Preauth Instacash Domain Security
  slug: preauth-instacash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Preauth Instacash Trust Center
  slug: preauth-instacash-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II
slug: preauth-instacash
tags:
- Company
- Payments
- Payment Pre-Authorization
- Payment Guarantees
- Fintech
- Latin America
- Cards
website: https://preauth.io
---
