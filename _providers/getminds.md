---
agent_readiness:
  band: agent-native
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
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.7
  scored_at: '2026-09-25'
api_count: 2
apis:
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: REST v1 API for Minds (AI personas), Audiences, Studies, knowledge, chat, research runs, analytics and exports. JSON over HTTPS, bearer API-key auth (minds_ prefix), durable async jobs with polling, a
  name: Minds Public API
  slug: minds-public-api
- description: Hosted, agent-native MCP server (streamable-http) exposing 23 published tools for creating grounded Audiences, planning and running multi-question Studies, asking standalone questions, heatmaps, summa
  name: Minds MCP Server
  slug: minds-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://getminds.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getminds.ai/docs/api/overview
- group: docs
  title: ''
  type: Documentation
  url: https://getminds.ai/docs/api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://getminds.ai/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://getminds.ai/docs/api/overview
- group: operate
  title: ''
  type: Support
  url: https://getminds.ai/guide
- group: company
  title: ''
  type: Blog
  url: https://getminds.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://getminds.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://getminds.ai/settings/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getminds.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getminds.ai/legal/dataprivacy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/lifecycle/getminds-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/getminds-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/mcp/getminds-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getminds-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/mcp/getminds-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/getminds-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/scopes/getminds-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/getminds-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/llms/getminds-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getminds-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/well-known/getminds-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getminds-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/authentication/getminds-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getminds-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/conventions/getminds-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getminds-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/conventions/getminds-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/getminds-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/conformance/getminds-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getminds-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/errors/getminds-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getminds-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/data-model/getminds-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getminds-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/lifecycle/getminds-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getminds-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/security/getminds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getminds-domain-security.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/rate-limits/getminds-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getminds-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/plans/getminds-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getminds-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/packages/getminds-packages.yml
  title: ''
  type: Packages
  url: packages/getminds-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/regulatory/getminds-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/getminds-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/regulatory/getminds-regulatory-posture.yml
  title: ''
  type: DataResidency
  url: regulatory/getminds-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getminds/refs/heads/main/regulatory/getminds-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/getminds-regulatory-posture.yml
created: '2026-09-20'
description: Minds (getminds.ai) is an end-to-end platform for commercial synthetic market research. Brand, agency, product and insights teams build reusable AI Audiences grounded in their own research and public sources, then run in-depth interviews, questionnaires, concept and message tests, MaxDiff/conjoint methods, and segment comparisons in a single Study — from audience creation through analysis and export. Minds ships a public v1 REST API (OpenAPI 3.1.0, 103 operations), a hosted MCP server (23 published tools, OAuth 2.0 / API key), and an agent integration guide. Operated by Art of X UG (Berlin, Germany) with EU (Frankfurt/ Stockholm) data residency and a full GDPR posture.
image: https://getminds.ai/images/preview.webp
layout: provider
mcp_servers:
- description: Build synthetic Audiences and run Studies for concept testing, message testing, and segment comparison.
  name: Minds MCP Server
  slug: minds-mcp-server
- description: ''
  name: Minds MCP Server
  slug: minds-mcp-server-2
modified: '2026-09-20'
name: Minds
nav: Providers
network: true
overview: 'Minds publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Public API, and 1 more. Tagged areas include Synthetic Research, Market Research, Surveys, User Research, and Marketing Analytics.


  Minds'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Getminds Plans Pricing
  plan_count: 4
  slug: getminds-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Getminds Rate Limits
  slug: getminds-rate-limits
scopes:
- name: Getminds Scopes
  scope_count: 0
  slug: getminds-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.3
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 48.7
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 54.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 46.1
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Getminds Authentication
  slug: getminds-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Getminds Domain Security
  slug: getminds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getminds
tags:
- Synthetic Research
- Market Research
- Surveys
- User Research
- Marketing Analytics
- ai-personas
- MCP
- Agent-Native
- GDPR
website: https://getminds.ai
---
