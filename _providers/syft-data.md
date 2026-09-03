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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://app.syftdata.com/api
  baseurl_source: declared
  description: The Export API from Syft Data — 1 operation(s) for export.
  name: Syft Data Export API
  slug: syft-data-export-api
- baseURL: https://app.syftdata.com/api
  baseurl_source: declared
  description: The Lookup API from Syft Data — 1 operation(s) for lookup.
  name: Syft Data Lookup API
  slug: syft-data-lookup-api
- baseURL: https://e2.sy-d.io
  baseurl_source: declared
  description: The ingest endpoint the Syft browser tracking tag, SDK and server-side callers post behavioural and custom events to. Documented only inside the developer guide — no reference page, no published paylo
  name: Syft Data Event Collection API
  slug: syft-data-events-api
artifact_total: 15
asyncapis:
- description: ''
  name: Syft Data Webhooks
  slug: syft-data-webhooks
collections:
- collection_type: open
  name: Syft Data Event Collection API
  slug: open-syft-data-events-api
- collection_type: open
  name: Syft Data Lookup & Export API
  slug: open-syft-data-export-api
- collection_type: open
  name: Syft Data & Export Lookup API
  slug: open-syft-data-lookup-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/syft-data-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.syftdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.syftdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syftdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syftdata.com/implementation/lookup-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.syftdata.com/tutorial-basics/installation
- group: operate
  title: ''
  type: Support
  url: https://www.syftdata.com/support
- group: company
  title: ''
  type: Blog
  url: https://blog.syftdata.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syftdata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.syftdata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.syftdata.com/auth/syft-signup
- group: start
  title: ''
  type: Login
  url: https://app.syftdata.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syftdata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syftdata.com/privacy.html
- group: build
  title: ''
  type: SDKs
  url: packages/syft-data-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/syft-data-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/syft-data-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syft-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/syft-data-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/syft-data-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syft-data-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syft-data-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syft-data-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/syft-data-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/syft-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/syft-data-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/syft-data-components.yml
- group: auth
  title: ''
  type: Security
  url: security/syft-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/syft-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/syft-data-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/syft-data-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/syft-data-conformance.yml
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.syftdata.com/dpa
created: '2026-07-17'
description: Syft Data, Inc. is a B2B lead-intelligence platform that identifies and qualifies high-intent prospects from inbound website traffic and LinkedIn engagement. Its tracking pixel reveals anonymous visitors, enriches contacts, scores them against an Ideal Customer Profile, and triggers multi-channel outreach ("motions") into CRM, email, LinkedIn, and ad platforms. For developers Syft ships a schema-driven analytics SDK and CLI (npm @syftdata/*), a server-side Lookup and Export REST API secured with sk_live_ keys, outbound webhooks, and an official hosted MCP server so AI agents can query visitor data and build automations from chat.
image: https://www.syftdata.com/logo_180.png
layout: provider
mcp_servers:
- description: Official hosted MCP (Model Context Protocol) server that lets AI assistants query Syft visitor data, enqueue leads into motions, and build GTM automations from chat. Available on Pro plans.
  name: Syft MCP Server
  slug: syft-mcp-server
modified: '2026-08-13'
name: Syft Data
nav: Providers
network: true
overview: 'Syft Data publishes 3 APIs on the [APIs.io](https://apis.io/) network: Export API, Lookup API, and Event Collection API. Tagged areas include Company, Lead Intelligence, Intent Data, Website Visitor Identification, and Sales Intelligence.


  The Syft Data catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syft Data''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Syft Data Plans Pricing
  plan_count: 3
  slug: syft-data-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Syft Data Rate Limits
  slug: syft-data-rate-limits
scopes:
- name: Syft Data Scopes
  scope_count: 0
  slug: syft-data-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 25
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 70.7
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 60.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syft-data/refs/heads/main/screenshots/syft-data-2026-08-17T082227.png
security:
- kind: authentication
  name: Syft Data Authentication
  slug: syft-data-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Syft Data Domain Security
  slug: syft-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Syft Data Vulnerability Disclosure
  slug: syft-data-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Syft Data Trust Center
  slug: syft-data-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, Penetration Testing, ISO 27001
slug: syft-data
tags:
- Company
- Lead Intelligence
- Intent Data
- Website Visitor Identification
- Sales Intelligence
- Go-To-Market
- Analytics
- MCP
website: https://www.syftdata.com/
---
