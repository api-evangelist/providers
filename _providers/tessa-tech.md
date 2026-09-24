---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tessa Tech Agentic Access
  operation_count: 51
  slug: tessa-tech-agentic-access
  summary_line: 51 operations · 12 acting
api_count: 1
apis:
- baseURL: https://aiagent.tessa.tech
  baseurl_source: declared
  description: 'FastAPI service behind aiagent.tessa.tech: the A2A agent card and JSON-RPC endpoint, per-service and per-tenant agent cards, the professional-services directory (firm cards and profiles, introduction '
  name: TESSA Agent Directory API
  slug: tessa-agent-directory-api
- description: 'Hosted, anonymous MCP server (Streamable HTTP at https://aiagent.tessa.tech/mcp/, serverInfo tessa-mcp-server 1.30.0, protocolVersion 2025-06-18) exposing ten tools: TESSA''s service catalog, case stud'
  name: TESSA MCP Server
  slug: tessa-mcp-server
- description: A2A agent (protocolVersion 0.3.0, JSONRPC) for TESSA Marketing & Technology with nine skills — services catalog, case studies, AI agent readiness assessment, professional-services firm search, WCAG au
  name: TESSA A2A Agent
  slug: tessa-a2a-agent
artifact_total: 11
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/security/tessa-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tessa-tech-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/agentic-access/tessa-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tessa-tech-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://tessa.tech/
- group: company
  title: ''
  type: Blog
  url: https://tessa.tech/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://tessa.tech/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://tessa.tech/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tessa.tech/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://tessa.tech/about/contact-us/
- group: company
  title: ''
  type: About
  url: https://tessa.tech/about/
- group: other
  title: ''
  type: Leadership
  url: https://tessa.tech/team/
- group: other
  title: ''
  type: CaseStudies
  url: https://tessa.tech/casestudies/
- group: docs
  title: ''
  type: Documentation
  url: https://aiagent.tessa.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aiagent.tessa.tech/redoc
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/llms/tessa-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tessa-tech-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://tessa.tech/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/a2a/tessa-tech-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tessa-tech-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/mcp/tessa-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tessa-tech-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/mcp/tessa-tech-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tessa-tech-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/well-known/tessa-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tessa-tech-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/authentication/tessa-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tessa-tech-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/scopes/tessa-tech-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tessa-tech-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/conventions/tessa-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tessa-tech-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/lifecycle/tessa-tech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tessa-tech-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/conformance/tessa-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tessa-tech-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/errors/tessa-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tessa-tech-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/data-model/tessa-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tessa-tech-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/overlays/tessa-tech-agent-directory-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tessa-tech-agent-directory-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/packages/tessa-tech-packages.yml
  title: ''
  type: Packages
  url: packages/tessa-tech-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/plans/tessa-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tessa-tech-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/rate-limits/tessa-tech-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tessa-tech-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tessa-tech/refs/heads/main/changelog/tessa-tech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tessa-tech-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://complianceregistry.net/extensions/tessa-professional-services/v1/changelog
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://tessa.tech/privacy-policy/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://tessa.tech/privacy-policy/
created: '2026-09-19'
description: 'TESSA Marketing & Technology is a McLean, Virginia digital marketing and web development agency (est. 2012) selling SEO, paid search and social advertising, generative engine optimization, WordPress and custom web/app development, WCAG 2.2 AA accessibility audits, AI website search and avatars, and an AI Agent Readiness service. It publishes an unusually complete agent surface for a services firm: an A2A agent card (protocolVersion 0.3.0, nine skills) and JSON-RPC endpoint on aiagent.tessa.tech, an anonymous hosted MCP server (Streamable HTTP, ten tools with published inputSchema) advertised through an MCP server.json and a did:web document, a 28-card per-service A2A fleet, a FastAPI OpenAPI for the directory service behind it, RFC 8414/9728 OAuth discovery for a second OAuth 2.1-gated WordPress MCP server, llms.txt, a Markdown pricing twin, and an AI-welcoming robots.txt. TESSA also operates two vertical A2A registries, complianceregistry.net and marketingregistry.org.'
image: https://tessa.tech/wp-content/uploads/2026/08/tessa-og-default-1200x630-1.png
layout: provider
mcp_servers:
- description: ''
  name: TESSA Marketing & Technology MCP Server
  slug: tessa-marketing-technology-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP)
  slug: mcp-endpoint-streamable-http
modified: '2026-09-19'
name: TESSA Marketing & Technology
nav: Providers
network: true
overview: 'TESSA Marketing & Technology publishes 1 API on the [APIs.io](https://apis.io/) network: TESSA Agent Directory API. Tagged areas include Digital Marketing, SEO, Web Development, Accessibility, and AI Agent Readiness.


  TESSA Marketing & Technology''s developer surface includes engineering blog, pricing, documentation, API reference, authentication, changelog, and 29 more developer resources.'
plans:
- name: Tessa Tech Plans Pricing
  plan_count: 0
  slug: tessa-tech-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Tessa Tech Rate Limits
  slug: tessa-tech-rate-limits
scopes:
- name: Tessa Tech Scopes
  scope_count: 1
  slug: tessa-tech-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 44.9
    developer_ergonomics: 32.7
    discoverability: 75.9
    operational_transparency: 15.8
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Tessa Tech Authentication
  slug: tessa-tech-authentication
  summary_line: none/oauth2/admin-token · 4 schemes
- kind: domain-security
  name: Tessa Tech Domain Security
  slug: tessa-tech-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tessa-tech
tags:
- Digital Marketing
- SEO
- Web Development
- Accessibility
- AI Agent Readiness
- Professional Services
- Agent Directory
- A2A
- MCP
- Agent-Native
- Company
website: https://tessa.tech/
---
