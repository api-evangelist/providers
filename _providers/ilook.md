---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 16.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ilook Agentic Access
  operation_count: 1
  slug: ilook-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Subjective face‑shape, face score, Golden Ratio and focused measurement API.
  name: iLook Face Analysis API
  slug: ilook-face-analysis-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/ilook/agentic-access/ilook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ilook-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ilook/plans/ilook-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ilook-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ilook/rules/ilook-rules.yml
  title: ''
  type: Spectral
  url: rules/ilook-rules.yml
- group: auth
  href: https://artifacts.apis.io/ilook/authentication/ilook-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ilook-authentication.yml
- group: design
  href: https://artifacts.apis.io/ilook/conformance/ilook-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ilook-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ilook/llms/ilook-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ilook-llms.txt
- group: other
  href: https://artifacts.apis.io/ilook/a2a/ilook-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ilook-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ilook/mcp/ilook-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ilook-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ilook/well-known/ilook-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ilook-well-known.yml
- group: other
  href: https://artifacts.apis.io/ilook/hosts/ilook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ilook-hosts.yml
- group: other
  href: https://artifacts.apis.io/ilook/vendors/ilook-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ilook-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ilook.fit/pricing.md
- group: company
  title: ''
  type: Newsroom
  url: https://www.ilook.fit/press
- group: auth
  href: https://artifacts.apis.io/ilook/security/ilook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ilook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ilook.fit/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ilook.fit/api/docs
- group: company
  title: ''
  type: Blog
  url: https://www.ilook.fit/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ilook.fit/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ilook.fit/privacy
created: '2026-10-17'
description: iLook AI Face Analysis, operated by Arctan Technologies Private Limited, offers a free AI-powered facial analysis service that evaluates face shape, symmetry, and a subjective 0–100 score across five signals. Users can upload a single adult photo to receive detailed feedback, including Golden Ratio context and styling suggestions. The platform provides REST, MCP, and A2A APIs for developers and AI agents, with API keys required for access. Documentation, pricing, and privacy policies are publicly available on the website.
image: https://www.ilook.fit/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.ilook.fit.
  name: iLook AI Face Analysis (Wallic Technologies) MCP Server
  slug: ilook-mcp-yml
modified: '2026-10-17'
name: iLook AI Face Analysis (Wallic Technologies)
nav: Providers
network: true
overview: 'iLook AI Face Analysis (Wallic Technologies) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, FaceAnalysis, Image Processing, and Biometrics.


  The iLook AI Face Analysis (Wallic Technologies) catalog on APIs.io includes 1 Spectral governance ruleset.


  iLook AI Face Analysis (Wallic Technologies)''s developer surface includes authentication, pricing, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Ilook Plans Pricing
  plan_count: 2
  slug: ilook-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: iLook AI Face Analysis (Wallic Technologies) API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: ilook-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 24.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ilook Authentication
  slug: ilook-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ilook Domain Security
  slug: ilook-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ilook
tags:
- Company
- Artificial Intelligence
- FaceAnalysis
- Image Processing
- Biometrics
website: https://www.ilook.fit/
---
