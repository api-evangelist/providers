---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Read‑only MCP server provides tools for AI agents to access venue review forms, deadlines, LLM policies, and other data.
  name: ReviewPaper AI API
  slug: reviewpaper-ai-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/reviewpaper-ai/plans/reviewpaper-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reviewpaper-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/reviewpaper-ai/llms/reviewpaper-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reviewpaper-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/reviewpaper-ai/mcp/reviewpaper-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reviewpaper-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/reviewpaper-ai/well-known/reviewpaper-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reviewpaper-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/reviewpaper-ai/hosts/reviewpaper-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reviewpaper-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/reviewpaper-ai/vendors/reviewpaper-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reviewpaper-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://reviewpaper.ai/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://reviewpaper.ai/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://reviewpaper.ai/developers
- group: auth
  href: https://artifacts.apis.io/reviewpaper-ai/security/reviewpaper-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reviewpaper-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reviewpaper.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://reviewpaper.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reviewpaper.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reviewpaper.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reviewpaper-ai
coverage:
  checked: '2026-10-30'
  detail: Developer portal provides only a read‑only MCP server with no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://reviewpaper.ai/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: ReviewPaper.ai is an AI-powered platform that generates peer‑review style feedback for academic papers submitted to major conferences such as NeurIPS, ICLR, and ACL. By simulating the exact review format of each venue, it provides a predicted score, a ranked list of suggested improvements, and the ability to iteratively re‑review revised drafts or draft rebuttals. The service offers three free reviews per user and aims to help researchers strengthen their submissions before official review.
image: https://reviewpaper.ai/opengraph-image-pwu6ef?2656ec22fbde9d58
layout: provider
mcp_servers:
- description: Remote MCP server at reviewpaper.ai.
  name: reviewpaper-ai MCP Server
  slug: reviewpaper-ai-mcp-yml
modified: '2026-10-30'
name: reviewpaper-ai
nav: Providers
network: true
overview: 'reviewpaper-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Peer Review, Academic, NLP, and Research Tools.


  reviewpaper-ai''s developer surface includes documentation, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Reviewpaper Ai Plans Pricing
  plan_count: 3
  slug: reviewpaper-ai-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Reviewpaper Ai Authentication
  slug: reviewpaper-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Reviewpaper Ai Domain Security
  slug: reviewpaper-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: reviewpaper-ai
tags:
- AI
- Peer Review
- Academic
- NLP
- Research Tools
website: https://reviewpaper.ai/
---
