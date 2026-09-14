---
access_model:
  confidence: high
  label: Licensed, trial on request
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: true
  try_now: false
api_count: 1
apis:
- baseURL: http://{netprobeHost}:7136/v1
  baseurl_source: declared
  description: 'OpenAPI 3.0 REST plug-in on the Geneos Netprobe. Third-party applications PUT JSON to create or update dataviews, rows and streams on a named managed entity and sampler, DELETE them, and GET a health '
  name: Geneos Netprobe REST API
  slug: netprobe-rest-api
- description: 'JSON over HTTP(S) service exposed by the Geneos Gateway so third-party applications can run commands, list available commands and command targets, resolve XPath targets, snapshot a dataview, read the '
  name: Geneos Gateway REST Command Service
  slug: gateway-rest
- description: XML-RPC server exposed by the Netprobe API and API-STREAMS plug-ins so in-house applications, in any language with an XML-RPC client, can create custom dataviews, add and update headlines, rows, colum
  name: Geneos XML-RPC Instrumentation API
  slug: xml-rpc
- description: 'Browser-delivered dashboard server that renders Geneos Active Dashboards and dataviews without the Active Console desktop client. Managed as a Geneos component (webserver) and documented as a product '
  name: Geneos Web Dashboard
  slug: web-dashboard
- description: Scripting integration point where any executable that emits CSV on stdout becomes a Geneos sampler. The Toolkit is how most custom and third-party monitoring is bolted onto Geneos, and it is the targe
  name: Geneos Toolkit (Scripting) Plug-in
  slug: toolkit
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.itrsgroup.com/
- group: other
  title: ''
  type: ProductPage
  url: https://www.itrsgroup.com/platform/geneos
- group: docs
  title: ''
  type: Documentation
  url: https://docs.itrsgroup.com/docs/geneos/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.itrsgroup.com/docs/geneos/current/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.itrsgroup.com/docs/geneos/5.14.0/api/rest-api/?v=/v1/rest-api.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.itrsgroup.com/docs/geneos/current/getting-started/quickstart/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.itrsgroup.com
- group: operate
  title: ''
  type: Community
  url: https://community.itrsgroup.com/
- group: company
  title: ''
  type: Blog
  url: https://www.itrsgroup.com/blog
- group: learn
  title: ''
  type: Training
  url: https://www.itrsgroup.com/services/training/geneos
- group: operate
  title: ''
  type: Contact
  url: https://www.itrsgroup.com/about/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.itrsgroup.com/products/free-trials
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.itrsgroup.com/legal/terms-of-web-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.itrsgroup.com/legal/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ITRS-Group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itrsgroup
- group: build
  title: ''
  type: Packages
  url: packages/geneos-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/geneos-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/geneos-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/geneos-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/geneos-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/geneos-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/geneos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/geneos-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/geneos-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/geneos-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/geneos-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/geneos-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/geneos-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/geneos-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/geneos-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/geneos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/geneos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geneos-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/geneos-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/geneos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geneos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/geneos-finops.yml
created: '2024-01-15'
description: 'Geneos is ITRS Group''s real-time monitoring and observability platform for trading systems, applications and infrastructure, deployed across investment banks, hedge funds, exchanges, telcos and government. It is customer-deployed software rather than a hosted API: Netprobes collect high-frequency telemetry at the edge, Gateways aggregate and rule over it, and each tier exposes its own programmable surface. The Netprobe ships a published OpenAPI 3.0 REST plug-in for pushing dataviews and streams into monitoring, an XML-RPC Instrumentation API for in-house applications to publish custom dataviews, and the Gateway exposes a JSON/Server-Sent-Events REST command service for running commands, snoozing entities, snapshotting dataviews and validating setup. ITRS also publishes first-party Go tooling (cordial, including the geneos CLI) and a Rust toolkit library on GitHub.'
finops:
- name: Geneos Finops
  service_category: API
  slug: geneos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geneos.png
layout: provider
modified: '2026-09-12'
name: Geneos
nav: Providers
network: true
overview: 'Geneos publishes 1 API on the [APIs.io](https://apis.io/) network: Netprobe REST API. Tagged areas include APM, Capital Markets, Infrastructure, ITRS, and Monitoring.


  Geneos'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, training material, signup flow, and 32 more developer resources.'
plans:
- name: Geneos Plans Pricing
  plan_count: 0
  slug: geneos-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Geneos Rate Limits
  slug: geneos-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/geneos/refs/heads/main/screenshots/geneos-2026-06-20T181719.png
security:
- kind: authentication
  name: Geneos Authentication
  slug: geneos-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Geneos Domain Security
  slug: geneos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Geneos Vulnerability Disclosure
  slug: geneos-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Geneos Trust Center
  slug: geneos-trust-center
  summary_line: ISO/IEC 27001
slug: geneos
tags:
- APM
- Capital Markets
- Infrastructure
- ITRS
- Monitoring
- Observability
- Real-Time
- Trading Systems
- XML-RPC
- OpenAPI
website: https://www.itrsgroup.com/
---
