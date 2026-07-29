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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Retraced Agentic Access
  operation_count: 54
  slug: retraced-agentic-access
  summary_line: 54 operations · 22 acting
api_count: 17
apis:
- description: The Certificates API from Retraced — 2 operation(s) for certificates.
  name: Retraced Certificates API
  slug: retraced-certificates-api
- description: The Companies API from Retraced — 3 operation(s) for companies.
  name: Retraced Companies API
  slug: retraced-companies-api
- description: The Files API from Retraced — 1 operation(s) for files.
  name: Retraced Files API
  slug: retraced-files-api
- description: The Guides API from Retraced — 8 operation(s) for guides.
  name: Retraced Guides API
  slug: retraced-guides-api
- description: The Order Hub / Attachment Templates API from Retraced — 1 operation(s) for order hub / attachment templates.
  name: Retraced Order Hub / Attachment Templates API
  slug: retraced-order-hub-attachment-templates-api
- description: The Order Hub / Order Lines API from Retraced — 2 operation(s) for order hub / order lines.
  name: Retraced Order Hub / Order Lines API
  slug: retraced-order-hub-order-lines-api
- description: The Order Hub / Orders API from Retraced — 2 operation(s) for order hub / orders.
  name: Retraced Order Hub / Orders API
  slug: retraced-order-hub-orders-api
- description: The Product / BOM Headers API from Retraced — 3 operation(s) for product / bom headers.
  name: Retraced Product / BOM Headers API
  slug: retraced-product-bom-headers-api
- description: The Product / BOM Lines API from Retraced — 3 operation(s) for product / bom lines.
  name: Retraced Product / BOM Lines API
  slug: retraced-product-bom-lines-api
- description: The Product / BOM Placements API from Retraced — 2 operation(s) for product / bom placements.
  name: Retraced Product / BOM Placements API
  slug: retraced-product-bom-placements-api
- description: The Product / Material Headers API from Retraced — 3 operation(s) for product / material headers.
  name: Retraced Product / Material Headers API
  slug: retraced-product-material-headers-api
- description: The Product / Material Lines API from Retraced — 3 operation(s) for product / material lines.
  name: Retraced Product / Material Lines API
  slug: retraced-product-material-lines-api
- description: The Product / Style Properties API from Retraced — 1 operation(s) for product / style properties.
  name: Retraced Product / Style Properties API
  slug: retraced-product-style-properties-api
- description: The Product / Style Types API from Retraced — 1 operation(s) for product / style types.
  name: Retraced Product / Style Types API
  slug: retraced-product-style-types-api
- description: The Product / Styles API from Retraced — 4 operation(s) for product / styles.
  name: Retraced Product / Styles API
  slug: retraced-product-styles-api
- description: The Product / Supply Chains API from Retraced — 1 operation(s) for product / supply chains.
  name: Retraced Product / Supply Chains API
  slug: retraced-product-supply-chains-api
- description: The Release Notes API from Retraced — 1 operation(s) for release notes.
  name: Retraced Release Notes API
  slug: retraced-release-notes-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.retraced.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://publicapi.retraced.com/
- group: docs
  title: ''
  type: Documentation
  url: https://publicapi.retraced.com/
- group: docs
  title: ''
  type: APIReference
  url: https://publicapi.retraced.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://publicapi.retraced.com/api/v2/guides
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/retraced-openapi-original.json
- group: operate
  title: ''
  type: ChangeLog
  url: https://publicapi.retraced.com/api/v2/release-notes
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.retraced.com/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.retraced.com/pages/legal
- group: operate
  title: ''
  type: Support
  url: https://www.retraced.com/pages/contact
- group: auth
  title: ''
  type: Authentication
  url: authentication/retraced-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/retraced-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/retraced-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/retraced-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/retraced-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/retraced-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/retraced-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/retraced-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/retraced-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/retraced-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/retraced-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/retraced-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/retraced-domain-security.yml
created: '2026-07-17'
description: Retraced is an AI-first supply chain transparency and compliance platform for the fashion and textile industry. It helps brands and suppliers manage multi-tier traceability (fiber to finish), certified-materials validation, material composition, Digital Product Passports, supplier collaboration, and regulatory compliance across frameworks such as CSDDD, AGEC, and LKSG. Retraced exposes a versioned Public API v2 for machine-to-machine access to products (styles), bills of materials, material composition, certificates, companies with ESG data, supply chains, files, and Order Hub purchase/sales orders — the same data model that powers the Retraced dashboard. Backed by Partech.
image: https://cdn.shopify.com/s/files/1/0568/3524/4150/files/iso-retraced.svg?v=1760701227
layout: provider
mcp_servers:
- description: ''
  name: retraced-mcp.yml
  slug: retraced-mcpyml
modified: '2026-07-20'
name: Retraced
nav: Providers
network: true
overview: 'Retraced publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Companies API, Files API, and 14 more. Tagged areas include Company, Applicative Saas, Supply Chain, Sustainability, and Compliance.


  Retraced''s developer surface includes documentation, API reference, getting-started guide, changelog, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 32
score:
  band: thin
  composite: 36.8
  delta: -2.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 31.5
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Retraced Authentication
  slug: retraced-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Retraced Domain Security
  slug: retraced-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: retraced
tags:
- Company
- Applicative Saas
- Supply Chain
- Sustainability
- Compliance
- Fashion
- Traceability
- Digital Product Passport
- ESG
website: https://www.retraced.com/
---
