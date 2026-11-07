---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Churnlens Site Agentic Access
  operation_count: 7
  slug: churnlens-site-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://churnlens.site
  baseurl_source: declared
  description: Agent-facing discovery and query endpoints (MCP, A2A, NLWeb)
  name: ChurnLens Agent API
  slug: churnlens-site-agent-api
- baseURL: https://churnlens.site
  baseurl_source: declared
  description: Lead capture
  name: ChurnLens Funnel API
  slug: churnlens-site-funnel-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/churnlens-site/agentic-access/churnlens-site-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/churnlens-site-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/churnlens-site/plans/churnlens-site-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/churnlens-site-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/churnlens-site/rules/churnlens-site-rules.yml
  title: ''
  type: Spectral
  url: rules/churnlens-site-rules.yml
- group: design
  href: https://artifacts.apis.io/churnlens-site/vocabulary/churnlens-site-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/churnlens-site-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/churnlens-site/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/churnlens-site/security/churnlens-site-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/churnlens-site-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/churnlens-site/errors/churnlens-site-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/churnlens-site-problem-types.yml
- group: design
  href: https://artifacts.apis.io/churnlens-site/conformance/churnlens-site-conformance.yml
  title: ''
  type: Conformance
  url: conformance/churnlens-site-conformance.yml
- group: agent
  href: https://artifacts.apis.io/churnlens-site/llms/churnlens-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/churnlens-site-llms.txt
- group: other
  href: https://artifacts.apis.io/churnlens-site/a2a/churnlens-site-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/churnlens-site-a2a.yml
- group: agent
  href: https://artifacts.apis.io/churnlens-site/mcp/churnlens-site-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/churnlens-site-mcp.yml
- group: auth
  href: https://artifacts.apis.io/churnlens-site/well-known/churnlens-site-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/churnlens-site-security.txt
- group: agent
  href: https://artifacts.apis.io/churnlens-site/well-known/churnlens-site-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/churnlens-site-well-known.yml
- group: other
  href: https://artifacts.apis.io/churnlens-site/hosts/churnlens-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/churnlens-site-hosts.yml
- group: other
  href: https://artifacts.apis.io/churnlens-site/vendors/churnlens-site-vendors.yml
  title: ''
  type: Vendors
  url: vendors/churnlens-site-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://churnlens.site/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://churnlens.site/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kindrat86
- group: docs
  title: ''
  type: Documentation
  url: https://churnlens.site/guides
- group: auth
  href: https://artifacts.apis.io/churnlens-site/security/churnlens-site-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/churnlens-site-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/churnlens-site/security/churnlens-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/churnlens-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://churnlens.site/
- group: commercial
  title: ''
  type: Pricing
  url: https://churnlens.site/pricing
- group: company
  title: ''
  type: About
  url: https://churnlens.site/about
- group: operate
  title: ''
  type: Contact
  url: https://churnlens.site/contact
created: '2026-11-03'
description: ChurnLens provides buyer‑side SaaS due‑diligence tools. Users upload subscription CSVs and receive a human‑reviewed risk report exposing hidden churn, concentration risk, and revenue decay. The service helps investors and acquirers assess subscription‑based businesses before committing capital, delivering actionable insights to mitigate financial exposure and improve decision‑making.
image: https://churnlens.site/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at churnlens.site.
  name: ChurnLens MCP Server
  slug: churnlens-site-mcp-yml
modified: '2026-11-03'
name: ChurnLens
nav: Providers
network: true
overview: 'ChurnLens publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent API and Funnel API. Tagged areas include Software-as-a-Service, Due Diligence, Finance, Subscription, and Analytics.


  The ChurnLens catalog on APIs.io includes 1 Spectral governance ruleset.


  ChurnLens'' developer surface includes documentation, pricing, and 23 more developer resources.'
plans:
- name: Churnlens Site Plans Pricing
  plan_count: 6
  slug: churnlens-site-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: ChurnLens API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: churnlens-site-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 46.1
    developer_ergonomics: 6.5
    discoverability: 65.0
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Churnlens Site Domain Security
  slug: churnlens-site-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Churnlens Site Vulnerability Disclosure
  slug: churnlens-site-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-mcp-manifest
  slug: churnlens-site-get-mcp-manifest
slug: churnlens-site
tags:
- Software-as-a-Service
- Due Diligence
- Finance
- Subscription
- Analytics
website: https://churnlens.site/
---
