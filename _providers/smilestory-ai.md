---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SmileStory builds technology for everyone — AI (WIA SOOM), publishing (WIA Book), news (The Korean Today) and accessibility tools, available in 88 languages. Founded in Seoul in 2009.
  name: SmileStory API
  slug: smilestory-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/smilestory-ai/llms/smilestory-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smilestory-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/smilestory-ai/mcp/smilestory-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/smilestory-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/smilestory-ai/well-known/smilestory-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smilestory-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/smilestory-ai/hosts/smilestory-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smilestory-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/smilestory-ai/packages/smilestory-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/smilestory-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/smilestory-ai/packages/smilestory-ai-packages.yml
  title: ''
  type: Packages
  url: packages/smilestory-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/smilestory-ai/security/smilestory-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smilestory-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smilestory.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smilestory.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smilestory.ai/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WIA-Official
coverage:
  checked: '2026-10-29'
  detail: Access to the API endpoint https://smilestory.ai/api/ returns HTTP 403 Forbidden, indicating a gated access wall.
  evidence:
  - status: 403
    url: https://smilestory.ai/api/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: SmileStory AI is a Korean AI-driven storytelling platform that offers REST API access for generating and managing personalized story content. The company provides tools for creators, integrates with large language models, and supports developers via a public API documented on its website. It operates under the SmileStory Group, with headquarters in Seoul, and maintains a GitHub organization for SDKs and examples.
image: https://smilestory.ai/smilestory_eng.png
layout: provider
mcp_servers:
- description: Remote MCP server at smilestory.ai.
  name: smilestory-ai MCP Server
  slug: smilestory-ai-mcp-yml
modified: '2026-10-29'
name: smilestory-ai
nav: Providers
network: true
overview: smilestory-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Storytelling, Korean, and Platform.
random_paper: 18
scopes:
- name: Smilestory Ai Scopes
  scope_count: 0
  slug: smilestory-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Smilestory Ai Authentication
  slug: smilestory-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Smilestory Ai Domain Security
  slug: smilestory-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: smilestory-ai
tags:
- Company
- Artificial Intelligence
- Storytelling
- Korean
- Platform
website: https://smilestory.ai/
---
