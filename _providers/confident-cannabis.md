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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.0
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Client organization information
  name: Confident Cannabis Client Info API
  slug: confident-cannabis-client-info-api
- description: Client relationship management
  name: Confident Cannabis Clients API
  slug: confident-cannabis-clients-api
- description: The Lab Info API from Confident Cannabis — 1 operation(s) for lab info.
  name: Confident Cannabis Lab Info API
  slug: confident-cannabis-lab-info-api
- description: View associated labs
  name: Confident Cannabis Labs API
  slug: confident-cannabis-labs-api
- description: Order lifecycle state transitions
  name: Confident Cannabis Order Status API
  slug: confident-cannabis-order-status-api
- description: View orders and order details
  name: Confident Cannabis Orders API
  slug: confident-cannabis-orders-api
- description: Reference data for sample metadata
  name: Confident Cannabis Reference Data API
  slug: confident-cannabis-reference-data-api
- description: Upload sample images and documents
  name: Confident Cannabis Sample Files API
  slug: confident-cannabis-sample-files-api
- description: View samples and test results
  name: Confident Cannabis Samples API
  slug: confident-cannabis-samples-api
- description: Submit and manage test results
  name: Confident Cannabis Test Results API
  slug: confident-cannabis-test-results-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clients Client Info API
  slug: open-confident-cannabis-client-info-api
- collection_type: open
  name: Client Info Clients API
  slug: open-confident-cannabis-clients-api
- collection_type: open
  name: Clients Client Info Lab Info API
  slug: open-confident-cannabis-lab-info-api
- collection_type: open
  name: Clients Client Info Labs API
  slug: open-confident-cannabis-labs-api
- collection_type: open
  name: Clients Client Info Order Status API
  slug: open-confident-cannabis-order-status-api
- collection_type: open
  name: Clients Client Info Orders API
  slug: open-confident-cannabis-orders-api
- collection_type: open
  name: Clients Client Info Reference Data API
  slug: open-confident-cannabis-reference-data-api
- collection_type: open
  name: Clients Client Info Sample Files API
  slug: open-confident-cannabis-sample-files-api
- collection_type: open
  name: Clients Client Info Samples API
  slug: open-confident-cannabis-samples-api
- collection_type: open
  name: Clients Client Info Test Results API
  slug: open-confident-cannabis-test-results-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/confident-cannabis-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/confident-cannabis-client-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.confidentlims.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://confidentlims.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://confidentlims.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://confidentlims.readme.io/reference
- group: auth
  title: ''
  type: Authentication
  url: authentication/confident-cannabis-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confident-cannabis-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/confident-cannabis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/confident-cannabis-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/confident-cannabis-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/confident-cannabis-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/confident-cannabis-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.confidentlims.com/ai-info
- group: agent
  title: ''
  type: WellKnown
  url: well-known/confident-cannabis-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/confident-cannabis-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confident-cannabis-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ConfidentCannabis
- group: company
  title: ''
  type: Blog
  url: https://www.confidentlims.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.confidentlims.com/
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
created: '2026-07-17'
description: Confident Cannabis (CC Software LLC, operating as Confident LIMS) is a cloud-based Laboratory Information Management System for analytical testing labs and their clients across cannabis and hemp, food and beverage, environmental, agriculture, nutraceuticals, cosmetics, oil and gas, and industrial chemical testing. Its public v0 REST API lets labs manage samples, orders, and the order-status lifecycle, submit per-compound test results, and upload Certificates of Analysis, while testing clients read their labs, orders, samples, and results. Authentication is API-key based with optional HMAC-SHA256 request signing. Founded 2015 and backed by Bullpen Capital, the platform serves 100+ labs and 15,000+ active testing clients.
image: https://cdn.prod.website-files.com/64d6509bb299ffdf28c03cc4/65005f8fc24b671e1c5f5e68_webclip.jpg
layout: provider
mcp_servers:
- description: ''
  name: Confident Cannabis MCP Server
  slug: confident-cannabis-mcp-server
modified: '2026-07-18'
name: Confident Cannabis
nav: Providers
network: true
overview: 'Confident Cannabis publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Client Info API, Clients API, Lab Info API, and 7 more. Tagged areas include Company, Cannabis, Laboratory, LIMS, and Testing.


  Confident Cannabis'' developer surface includes documentation, API reference, authentication, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 59.3
    developer_ergonomics: 33.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 44.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/confident-cannabis/refs/heads/main/screenshots/confident-cannabis-2026-07-25T210247.png
security:
- kind: authentication
  name: Confident Cannabis Authentication
  slug: confident-cannabis-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Confident Cannabis Domain Security
  slug: confident-cannabis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: confident-cannabis
tags:
- Company
- Cannabis
- Laboratory
- LIMS
- Testing
- Compliance
- Certificate of Analysis
- Life Sciences
website: https://www.confidentlims.com
---
