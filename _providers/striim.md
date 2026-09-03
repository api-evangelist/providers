---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-03'
api_count: 3
apis:
- baseURL: https://striim.stoplight.io
  baseurl_source: declared
  description: 'REST API to create and manage (deploy, start, stop, undeploy, drop) Striim applications, execute TQL commands, retrieve monitoring and file lineage data, plus WActionStore queries (GET /wactions/def, '
  name: Striim Application Management REST API
  slug: striim-application-management-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/striim-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/striim-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.striim.com/feed/
- group: build
  title: ''
  type: Packages
  url: packages/striim-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/striim-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/striim-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/striim-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/striim-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/striim-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/striim-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/striim-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/striim-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/striim-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/striim-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/striim-sandbox.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/striim-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/striim-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.striim.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.striim.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.striim.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/striim
- group: operate
  title: ''
  type: Support
  url: https://www.striim.com/contact-us/
created: '2026-07-02'
description: Unified data integration and streaming platform offering change data capture (CDC), real-time streaming analytics, and data validation. Exposes a token-authenticated REST API (WActionStore queries, system health, Application Management) consumed against your own Striim instance or Striim Cloud service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/striim.png
layout: provider
mcp_servers:
- description: ''
  name: Striim MCP AgentLink
  slug: striim-mcp-agentlink
modified: '2026-09-03'
name: Striim
nav: Providers
network: true
overview: 'Striim publishes 1 API on the [APIs.io](https://apis.io/) network: Application Management REST API. Tagged areas include Data, Streaming, Change Data Capture, Real-Time, and Data Integration.


  Striim''s developer surface includes authentication, engineering blog, changelog, sandbox, pricing, support, and 17 more developer resources.'
plans:
- name: Striim Plans Pricing
  plan_count: 4
  slug: striim-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Striim Rate Limits
  slug: striim-rate-limits
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 39.3
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 4.5
    contract_quality: 52.4
    developer_ergonomics: 44.6
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 9.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/striim/refs/heads/main/screenshots/striim-2026-09-02T161015.png
security:
- kind: authentication
  name: Striim Authentication
  slug: striim-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Striim Domain Security
  slug: striim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Striim Trust Center
  slug: striim-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR, PCI DSS
slug: striim
tags:
- Data
- Streaming
- Change Data Capture
- Real-Time
- Data Integration
- Streaming Analytics
---
