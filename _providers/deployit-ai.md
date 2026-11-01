---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: Compliance
  url: https://deployit.ai/security
- group: agent
  href: https://artifacts.apis.io/deployit-ai/llms/deployit-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deployit-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/deployit-ai/mcp/deployit-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deployit-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/deployit-ai/well-known/deployit-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deployit-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/deployit-ai/hosts/deployit-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deployit-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/deployit-ai/vendors/deployit-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deployit-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://deployit.ai/security
- group: auth
  href: https://artifacts.apis.io/deployit-ai/security/deployit-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deployit-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deployit-ai/security/deployit-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deployit-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deployit.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://app.deployit.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.deployit.ai/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://app.deployit.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://app.deployit.ai/support
- group: company
  title: ''
  type: Blog
  url: https://deployit.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deployit
- group: commercial
  title: ''
  type: Pricing
  url: https://deployit.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deployit.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deployit.ai/privacy
coverage:
  checked: '2026-10-30'
  detail: Public website and app subdomains return HTML but no machine‑readable API specification or docs.
  evidence:
  - status: 200
    url: https://app.deployit.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: DeployIt provides a read‑only, AI‑enhanced analytics dashboard that connects to GitHub, GitLab, and Bitbucket to track developer and AI agent contributions, presenting weekly, monthly and quarterly dev‑day reports, highlighting blocked work, and offering a no‑code, quick‑setup solution for non‑technical founders and project leaders. The platform aggregates commit metadata, detects AI‑generated code, and delivers insights without installing any tools, ensuring GDPR‑compliant EU hosting and transparent privacy.
image: https://deployit.ai/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.deployit.ai.
  name: deployit-ai MCP Server
  slug: deployit-ai-mcp-yml
modified: '2026-10-30'
name: deployit-ai
nav: Providers
network: true
overview: 'deployit-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, DevOps, Analytics, and Dashboard.


  deployit-ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
random_paper: 17
scopes:
- name: Deployit Ai Scopes
  scope_count: 0
  slug: deployit-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.3
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deployit Ai Authentication
  slug: deployit-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Deployit Ai Domain Security
  slug: deployit-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Deployit Ai Trust Center
  slug: deployit-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: deployit-ai
tags:
- Company
- AI
- DevOps
- Analytics
- Dashboard
website: https://deployit.ai/
---
