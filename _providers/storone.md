---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The S1 REST API manages a StorONE storage system: create and manage applications, volumes, snapshots, shares, file systems and object stores; register hosts and mappings; configure NAS servers, floati'
  name: StorONE S1 REST API
  slug: storone-s1-rest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Storone Notifications Events
  slug: storone-notifications-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.storone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onestor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onestor.com/books/rest-api/chapter/api-reference-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.onestor.com/books/getting-started
- group: operate
  title: ''
  type: Support
  url: https://storone.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.storone.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storone.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storone.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.storone.com/request-a-demo/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/storone-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/storone-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storone-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/storone-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/storone-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/storone-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/storone-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/storone-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/storone-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/storone-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/storone-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/storone-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/storone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/storone-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/storone-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storone-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.storone.com/quality-policy/
created: '2026-08-29'
description: StorONE builds S1, a software-defined enterprise storage platform that consolidates block, file and object storage onto a single hardware-agnostic engine, with auto-tiering across flash and disk, snapshots, replication, erasure coding and NAS/object services managed as one system. S1 is delivered as software that customers deploy on their own commodity servers or on validated partner hardware, so the management surface — the OmniUI web console, the StorONE CLI client and the S1 REST API — is served by the customer's own controller nodes rather than by a StorONE-hosted cloud. The REST API is documented in the public StorONE Documents Repository at docs.onestor.com and covers applications, volumes, snapshots, shares, object stores, hosts, mappings, NAS servers, nodes, resources, replication, floating IPs, templates, workflows, monitoring and notifications. StorONE also serves a Model Context Protocol endpoint from its marketing site.
image: https://www.storone.com/wp-content/uploads/2023/11/logo.svg
layout: provider
mcp_servers:
- description: StorONE serves a live Model Context Protocol endpoint from its WordPress marketing site at www.storone.com. It is a real, reachable remote MCP server — it answers MCP JSON-RPC over HTTP with a spec-co
  name: StorONE MCP server
  slug: storone-mcp-server
modified: '2026-08-29'
name: StorONE
nav: Providers
network: true
overview: 'StorONE publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Storage, Enterprise Storage, Software-Defined Storage, Data Management, and Infrastructure.


  The StorONE catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StorONE''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Storone Plans Pricing
  plan_count: 0
  slug: storone-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Storone Rate Limits
  slug: storone-rate-limits
scopes:
- name: Storone Scopes
  scope_count: 0
  slug: storone-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 33.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storone/refs/heads/main/screenshots/storone-2026-09-02T160936.png
security:
- kind: authentication
  name: Storone Authentication
  slug: storone-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Storone Domain Security
  slug: storone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: storone
tags:
- Storage
- Enterprise Storage
- Software-Defined Storage
- Data Management
- Infrastructure
- Block Storage
- File Storage
- Object Storage
- Backup
- Replication
- Snapshots
- Company
website: https://www.storone.com/
---
