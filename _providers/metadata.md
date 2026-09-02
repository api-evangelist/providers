---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://metadata.io/pricing
  - https://metadata.io/mcp-server
  - https://metadata.io/developers/quickstart.html
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Health API from Metadata — 1 operation(s) for health.
  name: Metadata Health API
  slug: metadata-health-api
- description: The Mcp API from Metadata — 1 operation(s) for mcp.
  name: Metadata MCP API
  slug: metadata-mcp-api
artifact_total: 10
collections:
- collection_type: open
  name: MCP Metadata Server
  slug: open-metadata-mcp-server
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/metadata-mcp-server-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/metadata-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://metadata.io
- group: operate
  title: ''
  type: Support
  url: https://help.metadata.io/
- group: company
  title: ''
  type: Blog
  url: https://metadata.io/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://metadata.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://platform.metadata.io/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metadata.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metadata.io/terms-of-use/
- group: auth
  title: ''
  type: TrustCenter
  url: security/metadata-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://metadata.io/trust-compliance
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metadata-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://metadata.io/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://metadata.io/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://metadata.io/developers/tools/
- group: start
  title: ''
  type: GettingStarted
  url: https://metadata.io/developers/quickstart.html
- group: operate
  title: ''
  type: StatusPage
  url: https://metadata.io/developers/status.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metadata-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/metadata-well-known.yml
created: '2026-07-17'
description: 'Metadata (metadata.io) is a B2B marketing automation and demand-generation platform that uses AI agents to plan, execute, and optimize paid advertising campaigns across LinkedIn, Meta (Facebook and Instagram), Google Search and Display, Reddit, and Bing. Its core products are Metadata Campaigns (automated full-funnel paid campaign execution), Metadata Audiences with the patented MetaMatch B2B audience engine for precision targeting, and Metadata Insights for real-time, revenue-focused performance analytics. The platform connects to ad channels, CRMs (Salesforce, HubSpot), and marketing automation platforms (Marketo, Pardot) to run multivariate campaign testing at scale and optimize for pipeline and revenue rather than lead volume. Backed by 500 Global and Partech. Metadata publishes no public REST API. Its developer surface is MCP-native: the MetadataONE MCP server at mcp-server.metadata.io/mcp exposes 141 documented tools across audiences, campaigns, creatives, offers, keywords,
  ad extensions, analytics and integrations, so an agent can build an audience, generate on-brand creative, assemble a campaign and launch real paid spend without a REST client or an SDK. Developer docs, a quickstart, an authentication and scopes reference and the full tool catalog are published at metadata.io/developers/.'
image: https://metadata.io/wp-content/uploads/2025/06/IMG-20250618-WA0007.webp
layout: provider
mcp_servers:
- description: ''
  name: Metadata MCP Server (MetadataONE)
  slug: metadata-mcp-server-metadataone
modified: '2026-08-12'
name: Metadata
nav: Providers
network: true
overview: 'Metadata publishes 2 APIs on the [APIs.io](https://apis.io/) network: Health API and MCP API. Tagged areas include Company, Marketing, Marketing Automation, Demand Generation, and Advertising.


  Metadata''s developer surface includes support, engineering blog, pricing, documentation, API reference, getting-started guide, and 14 more developer resources.'
plans:
- name: Metadata Plans Pricing
  plan_count: 0
  slug: metadata-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Metadata Rate Limits
  slug: metadata-rate-limits
scopes:
- name: Metadata Scopes
  scope_count: 0
  slug: metadata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 41.5
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 43.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metadata/refs/heads/main/screenshots/metadata-2026-08-07T172641.png
security:
- kind: authentication
  name: Metadata Authentication
  slug: metadata-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Metadata Domain Security
  slug: metadata-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Metadata Trust Center
  slug: metadata-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701, GDPR, CCPA, CSA STAR
slug: metadata
tags:
- Company
- Marketing
- Marketing Automation
- Demand Generation
- Advertising
- B2B
- Artificial Intelligence
- MCP
- AI Agents
- Paid Media
- Account Based Marketing
website: https://metadata.io
---
