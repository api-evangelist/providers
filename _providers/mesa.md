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
api_count: 1
apis:
- baseURL: https://api.joinmesa.com/v1
  baseurl_source: declared
  description: Exchange API keys for a session token.
  name: Mesa Authentication API
  slug: mesa-authentication-api
- baseURL: https://api.joinmesa.com/v1
  baseurl_source: declared
  description: Retrieve invoices for the authenticated user.
  name: Mesa Invoices API
  slug: mesa-invoices-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mesa Partner Authentication API
  slug: open-mesa-authentication-api
- collection_type: open
  name: Mesa Partner Authentication Invoices API
  slug: open-mesa-invoices-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mesa-partner-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.joinmesa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.joinmesa.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinmesa.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinmesa.com/partner-api/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinmesa.com/embedded-ui/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/mesa-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://partners.joinmesa.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@joinmesa.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinmesa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinmesa.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.joinmesa.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.joinmesa.com
- group: design
  title: ''
  type: Conventions
  url: conventions/mesa-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/mesa-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mesa-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mesa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mesa-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mesa-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mesa-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mesa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mesa-domain-security.yml
created: '2026-07-17'
description: Mesa is a Boulder, Colorado fintech that provides embedded electronic-invoicing, payments, and invoice-financing (early-payment) infrastructure for B2B supplier networks. Suppliers get paid early via ACH while Mesa automates repayment once the buyer settles. Mesa ships as drop-in embedded UI — a JavaScript SDK (MesaClient) that renders Mesa's onboarding, dashboard, and instant-payout flows in an origin-pinned iframe inside a partner's web app — backed by a Partner REST API for user authentication and invoice retrieval. Auth is via API keys (clientId/clientSecret) exchanged for a short-lived JWT, with optional OIDC (Okta, Azure AD, Google). Backed by Matrix Partners; SOC 2.
image: https://www.joinmesa.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Mesa
nav: Providers
network: true
overview: 'Mesa publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Invoices API. Tagged areas include Company, Fintech, Payments, Invoice Financing, and Embedded Finance.


  Mesa''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, and 17 more developer resources.'
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/mesa/refs/heads/main/screenshots/mesa-2026-08-07T172620.png
security:
- kind: authentication
  name: Mesa Authentication
  slug: mesa-authentication
  summary_line: apiKey/http/openIdConnect · 3 schemes
- kind: domain-security
  name: Mesa Domain Security
  slug: mesa-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Mesa Trust Center
  slug: mesa-trust-center
  summary_line: SOC 2
slug: mesa
tags:
- Company
- Fintech
- Payments
- Invoice Financing
- Embedded Finance
- Early Payment
- ACH
- Supplier Payments
- B2B
website: https://www.joinmesa.com
---
