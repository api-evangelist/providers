---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
api_count: 1
apis:
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
- baseURL: http://{netprobeHost}:7136/v1
  baseurl_source: declared
  description: REST API plug-in
  name: Geneos REST API
  slug: geneos-rest-api-api
artifact_total: 16
common:
- group: other
  href: https://artifacts.apis.io/geneos/capabilities/geneos-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/geneos-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/geneos/overlays/geneos-netprobe-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/geneos-netprobe-rest-api-overlay.yaml
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
  href: https://artifacts.apis.io/geneos/packages/geneos-packages.yml
  title: ''
  type: Packages
  url: packages/geneos-packages.yml
- group: build
  href: https://artifacts.apis.io/geneos/packages/geneos-packages.yml
  title: ''
  type: SDKs
  url: packages/geneos-packages.yml
- group: build
  href: https://artifacts.apis.io/geneos/cli/geneos-cli.yml
  title: ''
  type: CLI
  url: cli/geneos-cli.yml
- group: start
  href: https://artifacts.apis.io/geneos/sandbox/geneos-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/geneos-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/geneos/authentication/geneos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geneos-authentication.yml
- group: design
  href: https://artifacts.apis.io/geneos/conventions/geneos-conventions.yml
  title: ''
  type: Conventions
  url: conventions/geneos-conventions.yml
- group: design
  href: https://artifacts.apis.io/geneos/conventions/geneos-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/geneos-conventions.yml
- group: design
  href: https://artifacts.apis.io/geneos/errors/geneos-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/geneos-problem-types.yml
- group: design
  href: https://artifacts.apis.io/geneos/lifecycle/geneos-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/geneos-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/geneos/lifecycle/geneos-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/geneos-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/geneos/changelog/geneos-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/geneos-changelog.yml
- group: design
  href: https://artifacts.apis.io/geneos/data-model/geneos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/geneos-data-model.yml
- group: design
  href: https://artifacts.apis.io/geneos/conformance/geneos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geneos-conformance.yml
- group: auth
  href: https://artifacts.apis.io/geneos/conformance/geneos-conformance.yml
  title: ''
  type: Compliance
  url: conformance/geneos-conformance.yml
- group: auth
  href: https://artifacts.apis.io/geneos/security/geneos-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/geneos-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/geneos/security/geneos-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/geneos-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/geneos/security/geneos-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/geneos-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/geneos/security/geneos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geneos-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/geneos/llms/geneos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/geneos-llms.txt
- group: agent
  href: https://artifacts.apis.io/geneos/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/geneos/plans/geneos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geneos-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/geneos/rate-limits/geneos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geneos-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/geneos/finops/geneos-finops.yml
  title: ''
  type: FinOps
  url: finops/geneos-finops.yml
created: '2024-01-15'
description: 'Geneos is ITRS Group''s real-time monitoring and observability platform for trading systems, applications and infrastructure, deployed across investment banks, hedge funds, exchanges, telcos and government. It is customer-deployed software rather than a hosted API: Netprobes collect high-frequency telemetry at the edge, Gateways aggregate and rule over it, and each tier exposes its own programmable surface. The Netprobe ships a published OpenAPI 3.0 REST plug-in for pushing dataviews and streams into monitoring, an XML-RPC Instrumentation API for in-house applications to publish custom dataviews, and the Gateway exposes a JSON/Server-Sent-Events REST command service for running commands, snoozing entities, snapshotting dataviews and validating setup. ITRS also publishes first-party Go tooling (cordial, including the geneos CLI) and a Rust toolkit library on GitHub.'
finops:
- has_sources: true
  method: derived
  name: Geneos Finops
  primary_unit: ''
  service_category: ''
  slug: geneos-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geneos.png
layout: provider
modified: '2026-09-12'
name: Geneos
nav: Providers
network: true
overview: 'Geneos publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API, and 4 more. Tagged areas include APM, Capital Markets, Infrastructure, ITRS, and Monitoring.


  The Geneos catalog on APIs.io includes 1 Spectral governance ruleset.


  Geneos'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, training material, signup flow, and 34 more developer resources.'
plans:
- name: Geneos Plans Pricing
  plan_count: 0
  slug: geneos-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Geneos Rate Limits
  slug: geneos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Geneos API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: geneos-rules
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 41.8
    developer_ergonomics: 80.4
    discoverability: 64.3
    operational_transparency: 68.4
  previous_composite: 61.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/geneos/geneos-2026-06-20T181719.png
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
skill_count: 3
skills:
- name: geneos-instrument-app-xmlrpc
  slug: geneos-instrument-app-xmlrpc
- name: geneos-publish-dataview
  slug: geneos-publish-dataview
- name: geneos-run-gateway-command
  slug: geneos-run-gateway-command
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
