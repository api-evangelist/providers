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
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Chaldal Agentic Access
  operation_count: 35
  slug: chaldal-agentic-access
  summary_line: 35 operations · 16 acting
api_count: 1
apis:
- description: The Accounts API from Chaldal — 4 operation(s) for accounts.
  name: Chaldal Accounts API
  slug: chaldal-accounts-api
- description: The Heartbeat API from Chaldal — 2 operation(s) for heartbeat.
  name: Chaldal Heartbeat API
  slug: chaldal-heartbeat-api
- description: The Identity API from Chaldal — 4 operation(s) for identity.
  name: Chaldal Identity API
  slug: chaldal-identity-api
- description: The Organization API from Chaldal — 5 operation(s) for organization.
  name: Chaldal Organization API
  slug: chaldal-organization-api
- description: The Task API from Chaldal — 20 operation(s) for task.
  name: Chaldal Task API
  slug: chaldal-task-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: My Title Accounts API
  slug: open-chaldal-accounts-api
- collection_type: open
  name: My Title Accounts Heartbeat API
  slug: open-chaldal-heartbeat-api
- collection_type: open
  name: My Title Accounts Identity API
  slug: open-chaldal-identity-api
- collection_type: open
  name: My Title Accounts Organization API
  slug: open-chaldal-organization-api
- collection_type: open
  name: My Title Accounts Task API
  slug: open-chaldal-task-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/chaldal-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/chaldal-consolidate-consignment.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chaldal-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/chaldal-eggtransport-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chaldal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chaldal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chaldal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://chaldal.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chaldal
- group: company
  title: ''
  type: Blog
  url: https://chaldal.tech/
- group: operate
  title: ''
  type: Support
  url: https://chaldal.com/t/Help
- group: docs
  title: ''
  type: Documentation
  url: https://gogobangla.com/static/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://gogobangla.com/static/api-docs/
created: '2026-07-17'
description: Chaldal is Bangladesh's largest online grocery delivery platform, founded in 2013 in Dhaka. It pioneered the "dark store" micro-warehouse model to deliver fresh food, groceries, personal care, and baby products within one hour across Dhaka, Narayanganj, Chittagong, Jashore, Khulna, Sylhet, and Rajshahi. Beyond retail grocery, Chaldal has built out supply-chain, agriculture, and logistics technology, including its Gogo Bangla / "Egg Transport" third-party-logistics arm, which exposes a public B2B delivery API. Backed by Y Combinator and 500 Global, Chaldal partners with the UN World Food Programme, UNDP, USAID, and the World Bank. Its engineering stack is F#/.NET Core, Scala, Python, and React/React Native. This profile was enriched by the API Evangelist pipeline from Chaldal's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chaldal.png
layout: provider
mcp_servers:
- description: ''
  name: Chaldal MCP Server
  slug: chaldal-mcp-server
modified: '2026-07-18'
name: Chaldal
nav: Providers
network: true
overview: 'Chaldal publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Heartbeat API, Identity API, and 2 more. Tagged areas include Company, Grocery, Delivery, Logistics, and Third Party Logistics.


  Chaldal''s developer surface includes authentication, engineering blog, support, documentation, API reference, and 8 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 38.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chaldal/refs/heads/main/screenshots/chaldal-2026-07-25T205118.png
security:
- kind: authentication
  name: Chaldal Authentication
  slug: chaldal-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Chaldal Domain Security
  slug: chaldal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chaldal
tags:
- Company
- Grocery
- Delivery
- Logistics
- Third Party Logistics
- E-Commerce
- Supply Chain
- Bangladesh
website: https://chaldal.com
---
