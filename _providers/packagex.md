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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Packagex Agentic Access
  operation_count: 4
  slug: packagex-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: The shipments API from PackageX — 2 operation(s) for shipments.
  name: PackageX shipments API
  slug: packagex-shipments-api
artifact_total: 8
asyncapis:
- description: ''
  name: Packagex Webhooks
  slug: packagex-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Title shipments API
  slug: open-packagex-shipments-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.packagex.io/apis/getting-started/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.packagex.io/apis/getting-started/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.packagex.io/apis/getting-started/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.packagex.io/apis/getting-started/welcome
- group: operate
  title: ''
  type: Support
  url: https://help.packagex.io/en/knowledge
- group: company
  title: ''
  type: Blog
  url: https://packagex.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/packagex-io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://packagex.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://packagex.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://packagex.statuspage.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/packagex-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/packagex-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/packagex-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/packagex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/packagex-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/packagex-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/packagex-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/packagex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/packagex-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/packagex-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/packagex-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/packagex-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/packagex-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/packagex-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/packagex-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/packagex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packagex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://packagex.io
created: '2026-07-17'
description: PackageX provides vision-AI powered logistics execution — software that turns any camera or device into an intelligent scanning agent to automate receiving, inventory management, fulfillment and dispatch across warehouses, retail and building logistics. Its REST API and mobile Vision SDKs expose shipments, deliveries, tracking, addresses, containers, manifests, documents and vision inferences (shipping-label OCR, bill-of-lading parsing, item segmentation). Authentication is API-key based via the PX-API-KEY header, with separate sandbox and production environments. Customers include WeWork, Subaru, Ricoh, Medtronic, Toyota and On Running.
image: https://cdn.prod.website-files.com/68d230940fd846bdd01f1867/6989c29e1ae181a811f47ac1_OG.webp
layout: provider
mcp_servers:
- description: ''
  name: packagex-mcp.yml
  slug: packagex-mcpyml
modified: '2026-07-20'
name: PackageX
nav: Providers
network: true
overview: 'PackageX publishes 1 API on the [APIs.io](https://apis.io/) network: shipments API. Tagged areas include Company, Logistics, Shipping, Supply Chain, and Computer Vision.


  The PackageX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PackageX''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, authentication, changelog, and 22 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 49.8
  delta: 0.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 59.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packagex/refs/heads/main/screenshots/packagex-2026-08-07T191238.png
security:
- kind: authentication
  name: Packagex Authentication
  slug: packagex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Packagex Domain Security
  slug: packagex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: packagex
tags:
- Company
- Logistics
- Shipping
- Supply Chain
- Computer Vision
- OCR
- Package Tracking
- Fulfillment
website: https://packagex.io
---
