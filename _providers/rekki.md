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
- acting_count: 27
  human_in_the_loop: 0
  name: Rekki Agentic Access
  operation_count: 32
  slug: rekki-agentic-access
  summary_line: 32 operations · 27 acting
api_count: 1
apis:
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The catalog API from REKKI — 12 operation(s) for catalog.
  name: REKKI catalog API
  slug: rekki-catalog-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The connect_customers API from REKKI — 2 operation(s) for connect_customers.
  name: REKKI connect_customers API
  slug: rekki-connect-customers-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The general API from REKKI — 2 operation(s) for general.
  name: REKKI general API
  slug: rekki-general-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The order-guide API from REKKI — 1 operation(s) for order-guide.
  name: REKKI order-guide API
  slug: rekki-order-guide-api
- baseURL: https://api.rekki.com
  baseurl_source: declared
  description: The orders API from REKKI — 11 operation(s) for orders.
  name: REKKI orders API
  slug: rekki-orders-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rekki.com Supplier catalog API
  slug: open-rekki-catalog-api
- collection_type: open
  name: Rekki.com Supplier catalog connect_customers API
  slug: open-rekki-connect-customers-api
- collection_type: open
  name: Rekki.com Supplier catalog general API
  slug: open-rekki-general-api
- collection_type: open
  name: Rekki.com Supplier catalog order-guide API
  slug: open-rekki-order-guide-api
- collection_type: open
  name: Rekki.com Supplier catalog orders API
  slug: open-rekki-orders-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/rekki-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://rekki.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://rekki.com/suppliers
- group: operate
  title: ''
  type: Support
  url: https://rekki.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rekki.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tandc.rekki.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rekki
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/rekki/supplier-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.rekki.com/swagger/index.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/rekki-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rekki-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rekki-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/rekki-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rekki-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rekki-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rekki-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rekki-supplier-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/rekki-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rekki-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rekki-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rekki-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rekki-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: REKKI is a food wholesale ordering platform that connects restaurants and chefs (buyers) with their suppliers. Restaurants place orders through the REKKI app, and suppliers receive, confirm, and fulfil them. REKKI publishes a public Supplier API that lets suppliers programmatically manage their product catalog (items, inventory, price lists), receive and confirm orders, report integration status back to REKKI, and manage REKKI Connect customers and their order guides. Authentication uses a supplier bearer token plus an X-REKKI-Authorization-Type header. REKKI's current product suite also includes AI agents for wholesale distributors (OrderAI, InboxAI, MenuAI) and a Marketplace. REKKI was surfaced as a portfolio company of Creandum and Point Nine.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rekki.png
layout: provider
modified: '2026-07-21'
name: REKKI
nav: Providers
network: true
overview: 'REKKI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including catalog API, connect_customers API, general API, and 2 more. Tagged areas include Company, Food, Wholesale, Ordering, and Restaurant.


  REKKI''s developer surface includes getting-started guide, support, documentation, API reference, authentication, and 18 more developer resources.'
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/rekki/refs/heads/main/screenshots/rekki-2026-09-02T153301.png
security:
- kind: authentication
  name: Rekki Authentication
  slug: rekki-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rekki Domain Security
  slug: rekki-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: rekki
tags:
- Company
- Food
- Wholesale
- Ordering
- Restaurant
- Supply Chain
- Catalog
- Order
- E-Commerce
website: https://rekki.com/
---
