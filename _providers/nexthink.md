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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Nexthink Agentic Access
  operation_count: 17
  slug: nexthink-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 7
apis:
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The Campaigns API from Nexthink — 1 operation(s) for campaigns.
  name: Nexthink Campaigns API
  slug: nexthink-campaigns-api
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The device-deletions API from Nexthink — 1 operation(s) for device-deletions.
  name: Nexthink device-deletions API
  slug: nexthink-device-deletions-api
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The enrichment API from Nexthink — 1 operation(s) for enrichment.
  name: Nexthink enrichment API
  slug: nexthink-enrichment-api
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The Execute API from Nexthink — 2 operation(s) for execute.
  name: Nexthink Execute API
  slug: nexthink-execute-api
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The Export API from Nexthink — 2 operation(s) for export.
  name: Nexthink Export API
  slug: nexthink-export-api
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The Handoff API API from Nexthink — 1 operation(s) for handoff api.
  name: Nexthink Handoff API API
  slug: nexthink-handoff-api-api
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The Remote actions API from Nexthink — 3 operation(s) for remote actions.
  name: Nexthink Remote actions API
  slug: nexthink-remote-actions-api
- baseURL: https://instance.api.us.nexthink.cloud
  baseurl_source: declared
  description: The Workflows API from Nexthink — 5 operation(s) for workflows.
  name: Nexthink Workflows API
  slug: nexthink-workflows-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Campaigns API
  slug: open-nexthink-campaigns-api
- collection_type: open
  name: Campaigns device-deletions API
  slug: open-nexthink-device-deletions-api
- collection_type: open
  name: Campaigns enrichment API
  slug: open-nexthink-enrichment-api
- collection_type: open
  name: Campaigns Execute API
  slug: open-nexthink-execute-api
- collection_type: open
  name: Campaigns Export API
  slug: open-nexthink-export-api
- collection_type: open
  name: Campaigns Handoff API API
  slug: open-nexthink-handoff-api-api
- collection_type: open
  name: Campaigns Remote actions API
  slug: open-nexthink-remote-actions-api
- collection_type: open
  name: Campaigns Workflows API
  slug: open-nexthink-workflows-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nexthink-campaigns-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nexthink.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexthink.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nexthink.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nexthink.com/api/api-credentials
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexthink-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nexthink-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexthink-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexthink-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexthink-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nexthink-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nexthink.com/platform/whats-new
- group: design
  title: ''
  type: DataModel
  url: data-model/nexthink-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexthink-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nexthink.com/trust-center
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.nexthink.com/trust-center
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexthink-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nexthink-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexthink-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nexthink-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nexthink-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.nexthink.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nexthink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexthink-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nexthink.com/blog
- group: operate
  title: ''
  type: Support
  url: https://community.nexthink.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nexthink
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nexthink.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.nexthink.com/legal/services-terms
- group: company
  title: ''
  type: Website
  url: https://www.nexthink.com
created: '2026-07-17'
description: Nexthink is a digital employee experience (DEX) management company. Its Infinity platform combines real-time endpoint analytics, employee sentiment, and automated remediation so IT teams can proactively detect and fix issues across every device. Nexthink exposes a set of OAuth 2.0-secured public APIs — NQL (query), Remote Actions, Workflows, Enrichment, Campaigns, Data Management, and Spark — that let external tools pull DEX data and drive endpoint automation. Backed by Index Ventures; added to the API Evangelist network and enriched from Nexthink's published developer documentation.
image: https://www.nexthink.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Nexthink MCP Server
  slug: nexthink-mcp-server
modified: '2026-07-20'
name: Nexthink
nav: Providers
network: true
overview: 'Nexthink publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, device-deletions API, enrichment API, and 5 more. Tagged areas include Company, Business Applications, Digital Employee Experience, Endpoint Analytics, and IT Operations.


  Nexthink''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 24 more developer resources.'
random_paper: 12
scopes:
- name: Nexthink Scopes
  scope_count: 1
  slug: nexthink-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexthink/refs/heads/main/screenshots/nexthink-2026-08-07T185209.png
security:
- kind: authentication
  name: Nexthink Authentication
  slug: nexthink-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Nexthink Domain Security
  slug: nexthink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nexthink Vulnerability Disclosure
  slug: nexthink-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Nexthink Trust Center
  slug: nexthink-trust-center
  summary_line: trust center published
slug: nexthink
tags:
- Company
- Business Applications
- Digital Employee Experience
- Endpoint Analytics
- IT Operations
- Automation
- Observability
- DEX
website: https://www.nexthink.com
---
