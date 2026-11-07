---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentrenderapi Com Agentic Access
  operation_count: 10
  slug: agentrenderapi-com-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: Agent-native URL rendering API for screenshots, PDFs, and data extraction.
  name: AgentRender API
  slug: agentrender-api
- baseURL: https://agentreliability.dev
  baseurl_source: declared
  description: 'The knowledge itself: objects, their index and the evidence behind them.'
  name: AgentRender Corpus API
  slug: agentrenderapi-com-corpus-api
- baseURL: https://agentreliability.dev
  baseurl_source: declared
  description: 'What this deployment is and what it serves: manifests, versions, this document.'
  name: AgentRender Deployment API
  slug: agentrenderapi-com-deployment-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/agentrenderapi-com/agentic-access/agentrenderapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentrenderapi-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentrenderapi-com/rules/agentrenderapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentrenderapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentrenderapi-com/vocabulary/agentrenderapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentrenderapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentrenderapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentrenderapi-com/errors/agentrenderapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentrenderapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentrenderapi-com/conformance/agentrenderapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentrenderapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentrenderapi-com/well-known/agentrenderapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentrenderapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentrenderapi-com/hosts/agentrenderapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentrenderapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentrenderapi-com/vendors/agentrenderapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentrenderapi-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentrenderapi-com/security/agentrenderapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrenderapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentrenderapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.agentrenderapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://agentrenderapi.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentrenderapi.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentrenderapi.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/corbinvachal48/agentrender-mcp
created: '2026-11-01'
description: AgentRender provides a read‑only remote MCP (Multi‑Channel Platform) that captures, screenshots, PDFs and extracts structured data from public webpages. Integrated with ChatGPT, it lets users embed visual QA, competitive analysis, and research briefs directly in AI workflows. The service offers free tier limits, paid plans via Stripe, and open‑source client libraries for Python and other environments. It emphasizes privacy, with no logging of user data, and includes public API documentation and SDKs.
image: https://agentrenderapi.com/og-image.png
layout: provider
modified: '2026-11-01'
name: AgentRender
nav: Providers
network: true
overview: 'AgentRender publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Corpus API, Deployment API, and 1 more. Tagged areas include Artificial Intelligence, Automation, Screenshots, PDF, and Data Extraction.


  The AgentRender catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentRender''s developer surface includes documentation, pricing, and 14 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AgentRender API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: agentrenderapi-com-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 44.7
    developer_ergonomics: 11.2
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentrenderapi Com Domain Security
  slug: agentrenderapi-com-domain-security
  summary_line: TLSv1.3
slug: agentrenderapi-com
tags:
- Artificial Intelligence
- Automation
- Screenshots
- PDF
- Data Extraction
- ChatGPT
website: https://agentrenderapi.com/
---
