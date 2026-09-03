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
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: HappyCo's gRPC API for property inspections, reports, templates, accounts, users, partner account provisioning, assets, folders, and streaming events.
  name: HappyCo API (Happy API)
  slug: happyco-api-happy-api
artifact_total: 5
asyncapis:
- description: ''
  name: Happyco Events
  slug: happyco-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/happyco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://happy.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.happy.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.happy.co/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.happy.co/downloads/overview.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/happy-co
- group: operate
  title: ''
  type: Support
  url: https://support.happy.co/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.happy.co/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://happy.co/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://happy.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://happy.co/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://happy.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://happy.co/master-subscription-agreement
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.happy.co/hc/en-us/articles/27219606661780-Release-Updates
- group: operate
  title: ''
  type: StatusPage
  url: https://happyco.statuspage.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/happyco-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/happyco-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/happyco-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/happyco-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/happyco-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/happyco-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/happyco-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://happy.co/press/happyco-announces-soc-2-type-ii-security-certification
- group: auth
  title: ''
  type: TrustCenter
  url: security/happyco-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/happyco-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/happyco-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/happyco-events.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/happyco-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: HappyCo is a PropTech company (founded 2011, San Diego) whose real-time multifamily operations platform powers property inspections, AI-led maintenance, centralized maintenance, and asset performance for nearly 4 million units globally. Its developer-facing Happy API is a high-performance gRPC API (grpc.happyco.com) exposing inspection, report, template, account, account-provisioning (Partner API), asset, and folder services, plus server-streaming event notifications and a flexible MyID/IntegrationID system. Generated client libraries are published for Ruby, Go, and Java, and the platform integrates with major property-management systems (Yardi, RealPage, Entrata, MRI, ResMan, AppFolio, Buildium).
image: https://cdn.prod.website-files.com/6414ce4dcbfbc386d105ceb9/69a0a5421dfd02fb3bb57b77_OG-Home.avif
layout: provider
modified: '2026-07-19'
name: HappyCo
nav: Providers
network: true
overview: 'HappyCo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PropTech, Real-Estate, Property Management, and Inspections.


  The HappyCo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HappyCo''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 22 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 44.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/happyco/refs/heads/main/screenshots/happyco-2026-07-25T220650.png
security:
- kind: authentication
  name: Happyco Authentication
  slug: happyco-authentication
  summary_line: http-basic · 1 scheme
- kind: domain-security
  name: Happyco Domain Security
  slug: happyco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Happyco Trust Center
  slug: happyco-trust-center
  summary_line: SOC 2 Type II
slug: happyco
tags:
- Company
- PropTech
- Real-Estate
- Property Management
- Inspections
- Maintenance
- Multifamily
- gRPC
website: https://happy.co
---
