---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- description: HTTPS event-ingestion API for streaming batches of newline-delimited JSON, OpenRTB 2.5-based ad-tech event records (e.g. MmxAuctionSummary) to the Metamarkets platform for near-real-time dashboarding.
  name: Metamarkets Real-Time Data Ingestion (RDI) API
  slug: metamarkets-real-time-data-ingestion-rdi-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://metamarkets.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/security/metamarkets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metamarkets-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamarkets.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metamarkets.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metamx
- group: operate
  title: ''
  type: Support
  url: mailto:support@metamarkets.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/llms/metamarkets-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metamarkets-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/packages/metamarkets-packages.yml
  title: ''
  type: Packages
  url: packages/metamarkets-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/packages/metamarkets-packages.yml
  title: ''
  type: SDKs
  url: packages/metamarkets-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/cli/metamarkets-cli.yml
  title: ''
  type: CLI
  url: cli/metamarkets-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/authentication/metamarkets-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metamarkets-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/errors/metamarkets-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/metamarkets-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/conventions/metamarkets-conventions.yml
  title: ''
  type: Conventions
  url: conventions/metamarkets-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/rate-limits/metamarkets-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/metamarkets-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/sandbox/metamarkets-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/metamarkets-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/conformance/metamarkets-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metamarkets-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/components/metamarkets-components.yml
  title: ''
  type: Components
  url: components/metamarkets-components.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.metamarkets.com/docs/real-time-data-delivery
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/vocabulary/metamarkets-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/metamarkets-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/data-model/metamarkets-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metamarkets-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/examples/metamarkets-rdi-examples.yml
  title: ''
  type: Examples
  url: examples/metamarkets-rdi-examples.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/plans/metamarkets-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/metamarkets-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/lifecycle/metamarkets-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/metamarkets-lifecycle.yml
created: '2026-07-17'
description: Metamarkets built a real-time analytics platform for the programmatic advertising industry, giving ad exchanges, DSPs, SSPs, and publishers an interactive dashboard over billions of daily bid, impression, and spend events. Its Real-Time Data Ingestion (RDI) platform ingests well-formatted, standards-based ad-tech event data (adhering to OpenRTB 2.5, IAB guidelines, and ISO date/country/language/currency standards) over an authenticated HTTPS streaming endpoint and surfaces it in the Metamarkets dashboard within seconds for querying and analysis. Metamarkets was acquired by Snap Inc. in 2017; the primary metamarkets.com site is now defunct, but the legacy developer documentation for the RDI platform remains live at docs.metamarkets.com. Surfaced as a portfolio company of Anthemis and profiled in the API Evangelist network.
examples:
- key_count: 10
  name: Metamarkets Auction Summary Record
  slug: metamarkets-auction-summary-record
- key_count: 2
  name: Metamarkets Click Record
  slug: metamarkets-click-record
- key_count: 4
  name: Metamarkets Impression Record
  slug: metamarkets-impression-record
image: https://files.readme.io/7e7ea7f-small-MMX-logo.png
layout: provider
modified: '2026-09-16'
name: Metamarkets
nav: Providers
network: true
overview: 'Metamarkets publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Analytics, and Real-Time.


  Metamarkets'' developer surface includes documentation, getting-started guide, support, CLI, authentication, sandbox, API reference, and 16 more developer resources.'
plans:
- name: Metamarkets Plans Pricing
  plan_count: 0
  slug: metamarkets-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Metamarkets Rate Limits
  slug: metamarkets-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/metamarkets/refs/heads/main/screenshots/metamarkets-2026-08-07T172649.png
security:
- kind: authentication
  name: Metamarkets Authentication
  slug: metamarkets-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Metamarkets Domain Security
  slug: metamarkets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metamarkets
tags:
- Company
- Advertising
- AdTech
- Analytics
- Real-Time
- Data Ingestion
- Programmatic Advertising
- OpenRTB
- Business Intelligence
- Defunct
website: https://metamarkets.com
---
