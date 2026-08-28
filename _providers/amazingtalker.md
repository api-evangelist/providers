---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Pages API from AmazingTalker — 1 operation(s) for pages.
  name: AmazingTalker Pages API
  slug: amazingtalker-pages-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Find tutors plugin Pages API
  slug: open-amazingtalker-pages-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazingtalker-find-tutors-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazingtalker-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazingtalker-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazingtalker-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazingtalker-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazingtalker-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazingtalker-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmazingTalker
- group: company
  title: ''
  type: Blog
  url: https://en.amazingtalker.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.amazingtalker.com/privacy-and-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.amazingtalker.com/privacy-and-terms
- group: company
  title: ''
  type: Website
  url: https://en.amazingtalker.com
created: '2026-07-17'
description: AmazingTalker is an online tutoring marketplace, founded in 2016 and headquartered in Taipei, that connects students with vetted professional tutors for personalized 1-on-1 lessons in more than 60 languages plus academic, music, and lifestyle subjects. Learners browse tutor profiles, compare pricing and ratings, book trial and formal lessons on a flexible pay-as-you-go basis, and meet over Zoom. AmazingTalker publicly exposes a ChatGPT-plugin OpenAPI (findTeachers) that returns bookable tutors for a subject with price, learning-need, auxiliary-language, and location filters.
image: https://en.amazingtalker.com/.well-known/logo.png
layout: provider
mcp_servers:
- description: ''
  name: AmazingTalker MCP Server
  slug: amazingtalker-mcp-server
modified: '2026-07-17'
name: AmazingTalker
nav: Providers
network: true
overview: 'AmazingTalker publishes 1 API on the [APIs.io](https://apis.io/) network: Pages API. Tagged areas include Company, Education, Tutoring, Language Learning, and Marketplace.


  AmazingTalker''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 16.7
    contract_quality: 41.5
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 37.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazingtalker/refs/heads/main/screenshots/amazingtalker-2026-07-25T195910.png
security:
- kind: authentication
  name: Amazingtalker Authentication
  slug: amazingtalker-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Amazingtalker Domain Security
  slug: amazingtalker-domain-security
  summary_line: TLSv1.3
slug: amazingtalker
tags:
- Company
- Education
- Tutoring
- Language Learning
- Marketplace
- EdTech
- ChatGPT Plugin
website: https://en.amazingtalker.com
---
