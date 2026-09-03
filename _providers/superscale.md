---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://docs.superscale.ai/billing/plans
  - https://superscale.ai/pricing
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: The product Model Context Protocol server. Lets an external agent runtime (Claude and similar MCP clients) drive Superscale's creative engine — generating statics, UGC video and scripts from context t
  name: Superscale MCP Server
  slug: superscale-mcp-server
- description: An anonymous Model Context Protocol server served from Superscale's own documentation host, providing search and retrieval over the published Superscale knowledge base. Introspected live on 2026-08-12
  name: Superscale Documentation MCP Server
  slug: superscale-documentation-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.superscale.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superscale.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superscale.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superscale.ai/getting-started/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://superscale.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://superscale.ai/signup
- group: start
  title: ''
  type: Login
  url: https://superscale.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superscale.ai/data/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superscale.ai/data/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://superscale.ai/news
- group: operate
  title: ''
  type: Support
  url: mailto:support@superscale.ai
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.superscale.ai/resources/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superscale-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superscale.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.superscale.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/superscale-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superscale-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superscale-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superscale-docs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/superscale-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/superscale-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/superscale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/superscale-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superscale-domain-security.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/superscale-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superscale-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superscale-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/superscale-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superscale-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superscale-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/superscale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/superscale-rate-limits.yml
created: '2026-07-17'
description: 'Superscale is an autonomous AI marketing agent for performance advertising. A user gives it a product URL (App Store, Shopify, website, or Lovable project) and a brief; the agent then researches competitor ads in the niche, writes copy and scripts, produces AI UGC videos and static image ads, adds captions and finishing touches, resizes every asset to the required aspect ratios, and — where ad accounts are connected — builds and publishes campaigns on Meta, Google and TikTok behind a blocking human approval step. It serves mobile-app marketers, e-commerce brands, SaaS companies, agencies and growth teams. Superscale is Europe-based and backed by Interface Capital, S16VC, Creandum, Lovable and ElevenLabs. Its machine-readable surface is agent-native rather than REST: an OAuth-gated Model Context Protocol server at mcp.superscale.ai (included from the Pro plan upward), an anonymous documentation MCP server, a conformant A2A agent card, and a published Agent Skill — with no OpenAPI.'
image: https://superscale.ai/images/og-images/default-og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Superscale MCP Server
  slug: superscale-mcp-server
modified: '2026-08-12'
name: Superscale
nav: Providers
network: true
overview: 'Superscale publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketing, Advertising, and Generative AI.


  Superscale''s developer surface includes documentation, getting-started guide, pricing, signup flow, engineering blog, support, changelog, and 26 more developer resources.'
plans:
- name: Superscale Plans Pricing
  plan_count: 6
  slug: superscale-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 8
  name: Superscale Rate Limits
  slug: superscale-rate-limits
scopes:
- name: Superscale Scopes
  scope_count: 7
  slug: superscale-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 38.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superscale/refs/heads/main/screenshots/superscale-2026-08-17T082204.png
security:
- kind: authentication
  name: Superscale Authentication
  slug: superscale-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Superscale Domain Security
  slug: superscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Superscale Vulnerability Disclosure
  slug: superscale-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: superscale
tags:
- Company
- Artificial Intelligence
- Marketing
- Advertising
- Generative AI
- Creative
- AdTech
- Software-as-a-Service
- Agents
- MCP
- A2A
- Agent Skills
- Advertising Technology
- Video Generation
- Media Buying
website: https://www.superscale.ai/
---
