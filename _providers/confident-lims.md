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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Confident Lims Agentic Access
  operation_count: 45
  slug: confident-lims-agentic-access
  summary_line: 45 operations · 17 acting
api_count: 10
apis:
- description: Client organization information
  name: Confident LIMS Client Info API
  slug: confident-lims-client-info-api
- description: Client relationship management
  name: Confident LIMS Clients API
  slug: confident-lims-clients-api
- description: Lab organization information
  name: Confident LIMS Lab Info API
  slug: confident-lims-lab-info-api
- description: View associated labs
  name: Confident LIMS Labs API
  slug: confident-lims-labs-api
- description: Order lifecycle state transitions
  name: Confident LIMS Order Status API
  slug: confident-lims-order-status-api
- description: View orders and order details
  name: Confident LIMS Orders API
  slug: confident-lims-orders-api
- description: Reference data for sample metadata
  name: Confident LIMS Reference Data API
  slug: confident-lims-reference-data-api
- description: Upload sample images and documents
  name: Confident LIMS Sample Files API
  slug: confident-lims-sample-files-api
- description: View samples and test results
  name: Confident LIMS Samples API
  slug: confident-lims-samples-api
- description: Submit and manage test results
  name: Confident LIMS Test Results API
  slug: confident-lims-test-results-api
arazzos:
- description: A testing client confirms identity, lists recently changed orders, and pulls the finalized sample details for the first order (read-only client credentials).
  name: Confident LIMS — client results sync
  slug: confident-lims-client-results-sync
- description: A lab creates an order for a testing client, verifies it into the workflow, submits test results for a sample, attaches the COA, and completes the order.
  name: Confident LIMS — lab order to finalized results
  slug: confident-lims-lab-order-to-results
artifact_total: 28
asyncapis:
- description: ''
  name: Confident Lims Webhooks
  slug: confident-lims-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clients Client Info API
  slug: open-confident-lims-client-info-api
- collection_type: open
  name: Client Info Clients API
  slug: open-confident-lims-clients-api
- collection_type: open
  name: Clients Client Info Lab Info API
  slug: open-confident-lims-lab-info-api
- collection_type: open
  name: Clients Client Info Labs API
  slug: open-confident-lims-labs-api
- collection_type: open
  name: Clients Client Info Order Status API
  slug: open-confident-lims-order-status-api
- collection_type: open
  name: Clients Client Info Orders API
  slug: open-confident-lims-orders-api
- collection_type: open
  name: Clients Client Info Reference Data API
  slug: open-confident-lims-reference-data-api
- collection_type: open
  name: Clients Client Info Sample Files API
  slug: open-confident-lims-sample-files-api
- collection_type: open
  name: Clients Client Info Samples API
  slug: open-confident-lims-samples-api
- collection_type: open
  name: Clients Client Info Test Results API
  slug: open-confident-lims-test-results-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/confident-lims-clients-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://confidentlims.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://confidentlims.readme.io/reference
- group: docs
  title: ''
  type: APIReference
  url: https://confidentlims.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.confidentlims.com/products/api
- group: operate
  title: ''
  type: Support
  url: https://help.confidentlims.com/
- group: company
  title: ''
  type: Blog
  url: https://www.confidentlims.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.confidentcannabis.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confidentlims.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.confidentlims.com/register
- group: start
  title: ''
  type: Login
  url: https://accounts.confidentlims.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.confidentlims.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confidentlims.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: conformance/confident-lims-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/confident-lims-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/confident-lims-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/confident-lims-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/confident-lims-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/confident-lims-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/confident-lims-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/confident-lims-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confident-lims-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/confident-lims-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confident-lims-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confident-lims-domain-security.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confident-lims-lab-order-to-results.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confident-lims-client-results-sync.yml
created: '2026-07-17'
description: Confident LIMS (CC Software LLC, formerly Confident Cannabis, founded 2015) is a cloud-based Laboratory Information Management System for high-velocity analytical testing labs and their testing clients. It manages samples from accession through workflow, results, and reporting, automates regulatory compliance (ISO 17025, TNI/NELAP, SOC 2, FDA 21 CFR Part 11), and gives clients a self-service ordering and results portal. It serves cannabis, food & beverage, agriculture, nutraceuticals, cosmetics, environmental, industrial chemicals, and oil & gas labs. The Confident Cannabis REST API (v0, api.confidentcannabis.com) exposes labs, clients, and shared reference data with API-key + HMAC-SHA256 request signing and result webhooks.
image: https://files.readme.io/ebcaf628c1535f1f7354303ab5d660f8ee74c181042849f2f2954f5c025a3e1d-Brand_Symbol.svg
layout: provider
mcp_servers:
- description: ''
  name: confident-lims-mcp.yml
  slug: confident-lims-mcpyml
modified: '2026-07-18'
name: Confident LIMS
nav: Providers
network: true
overview: 'Confident LIMS publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Client Info API, Clients API, Lab Info API, and 7 more. Tagged areas include Company, LIMS, Laboratory Information Management, Analytical Testing, and Cannabis Testing.


  The Confident LIMS catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Confident LIMS''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 49.2
  delta: -3.4
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 30.3
    contract_quality: 69.4
    developer_ergonomics: 45.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 13.2
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/confident-lims/refs/heads/main/screenshots/confident-lims-2026-07-25T210248.png
security:
- kind: authentication
  name: Confident Lims Authentication
  slug: confident-lims-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Confident Lims Domain Security
  slug: confident-lims-domain-security
  summary_line: TLSv1.3 · DMARC
slug: confident-lims
tags:
- Company
- LIMS
- Laboratory Information Management
- Analytical Testing
- Cannabis Testing
- Compliance
- Sample Management
- Lab Software
website: https://confidentlims.readme.io/
---
