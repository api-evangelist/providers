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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Packagex Agentic Access
  operation_count: 4
  slug: packagex-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.packagex.io
  baseurl_source: declared
  description: The shipments API from PackageX — 2 operation(s) for shipments.
  name: PackageX Shipments API
  slug: packagex-shipments-api
artifact_total: 8
asyncapis:
- description: ''
  name: Packagex Webhooks
  slug: packagex-webhooks
collections:
- collection_type: open
  name: API Title shipments API
  slug: open-packagex-shipments-api
common:
- group: other
  href: https://artifacts.apis.io/packagex/capabilities/packagex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/packagex-capability-edges.yml
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
  href: https://artifacts.apis.io/packagex/authentication/packagex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/packagex-authentication.yml
- group: build
  href: https://artifacts.apis.io/packagex/packages/packagex-packages.yml
  title: ''
  type: Packages
  url: packages/packagex-packages.yml
- group: build
  href: https://artifacts.apis.io/packagex/packages/packagex-packages.yml
  title: ''
  type: SDKs
  url: packages/packagex-packages.yml
- group: agent
  href: https://artifacts.apis.io/packagex/mcp/packagex-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/packagex-mcp.yml
- group: agent
  href: https://artifacts.apis.io/packagex/llms/packagex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/packagex-llms.txt
- group: other
  href: https://artifacts.apis.io/packagex/overlays/packagex-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/packagex-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/packagex/conformance/packagex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/packagex-conformance.yml
- group: design
  href: https://artifacts.apis.io/packagex/errors/packagex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/packagex-problem-types.yml
- group: design
  href: https://artifacts.apis.io/packagex/lifecycle/packagex-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/packagex-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/packagex/lifecycle/packagex-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/packagex-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/packagex/changelog/packagex-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/packagex-changelog.yml
- group: start
  href: https://artifacts.apis.io/packagex/sandbox/packagex-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/packagex-sandbox.yml
- group: design
  href: https://artifacts.apis.io/packagex/conventions/packagex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/packagex-conventions.yml
- group: design
  href: https://artifacts.apis.io/packagex/data-model/packagex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/packagex-data-model.yml
- group: design
  href: https://artifacts.apis.io/packagex/asyncapi/packagex-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/packagex-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/packagex/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/packagex/agentic-access/packagex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/packagex-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/packagex/security/packagex-domain-security.yml
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
modified: '2026-07-20'
name: PackageX
nav: Providers
network: true
overview: 'PackageX publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Shipments API. Tagged areas include Company, Logistics, Shipping, Supply Chain, and Computer Vision.


  The PackageX catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PackageX''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, authentication, changelog, and 23 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: PackageX API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: packagex-rules
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/packagex/packagex-2026-08-07T191238.png
security:
- kind: authentication
  name: Packagex Authentication
  slug: packagex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Packagex Domain Security
  slug: packagex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: Create and purchase a PackageX shipment
  slug: packagex-create-shipment
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
