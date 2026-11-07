---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Larridin Agentic Access
  operation_count: 41
  slug: larridin-agentic-access
  summary_line: 41 operations
api_count: 1
apis:
- baseURL: https://scout-api.larridin.com/api/v1
  baseurl_source: declared
  description: Organization- and department-level AI adoption metrics.
  name: Larridin Adoption API
  slug: larridin-adoption-api
- baseURL: https://scout-api.larridin.com/api/v1
  baseurl_source: declared
  description: AI proficiency scoring, prompt categories, and conversation metrics. Period-based selection.
  name: Larridin Proficiency API
  slug: larridin-proficiency-api
- baseURL: https://scout-api.larridin.com/api/v1
  baseurl_source: declared
  description: Survey campaigns, questions, options, and responses.
  name: Larridin Surveys API
  slug: larridin-surveys-api
- baseURL: https://scout-api.larridin.com/api/v1
  baseurl_source: declared
  description: Browser and desktop AI tool adoption, policy enforcement, and unapproved tool discovery.
  name: Larridin Tools API
  slug: larridin-tools-api
- baseURL: https://scout-api.larridin.com/api/v1
  baseurl_source: declared
  description: Clustered workflow analysis, friction, recommendations, and tool verdicts.
  name: Larridin Workflow Intelligence API
  slug: larridin-workflow-intelligence-api
artifact_total: 24
collections:
- collection_type: open
  name: Larridin Scout Adoption API
  slug: open-larridin-adoption-api
- collection_type: open
  name: Larridin Scout Adoption Proficiency API
  slug: open-larridin-proficiency-api
- collection_type: open
  name: Larridin Scout Adoption Surveys API
  slug: open-larridin-surveys-api
- collection_type: open
  name: Larridin Scout Adoption Tools API
  slug: open-larridin-tools-api
- collection_type: open
  name: Larridin Scout Adoption Workflow Intelligence API
  slug: open-larridin-workflow-intelligence-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://larridin.com/router/
- group: commercial
  href: https://artifacts.apis.io/larridin/plans/larridin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/larridin-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/larridin/capabilities/larridin-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/larridin-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/larridin/agentic-access/larridin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/larridin-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/larridin/security/larridin-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/larridin-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://larridin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.larridin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.larridin.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.larridin.com/api/scout-api-v1-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.larridin.com/get-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.larridin.com/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://larridin.com/contact
- group: company
  title: ''
  type: Blog
  url: https://larridin.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://larridin.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/larridin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://larridin.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://larridin.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.larridin.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.larridin.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.larridin.com/
- group: agent
  href: https://artifacts.apis.io/larridin/mcp/larridin-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/larridin-mcp.yml
- group: agent
  href: https://artifacts.apis.io/larridin/llms/larridin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/larridin-llms.txt
- group: agent
  href: https://artifacts.apis.io/larridin/well-known/larridin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/larridin-well-known.yml
- group: auth
  href: https://artifacts.apis.io/larridin/authentication/larridin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/larridin-authentication.yml
- group: auth
  href: https://artifacts.apis.io/larridin/scopes/larridin-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/larridin-scopes.yml
- group: design
  href: https://artifacts.apis.io/larridin/conventions/larridin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/larridin-conventions.yml
- group: design
  href: https://artifacts.apis.io/larridin/conformance/larridin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/larridin-conformance.yml
- group: design
  href: https://artifacts.apis.io/larridin/lifecycle/larridin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/larridin-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/larridin/errors/larridin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/larridin-problem-types.yml
- group: design
  href: https://artifacts.apis.io/larridin/data-model/larridin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/larridin-data-model.yml
- group: auth
  href: https://artifacts.apis.io/larridin/security/larridin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/larridin-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/larridin/security/larridin-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/larridin-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/larridin/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/larridin/overlays/larridin-scout-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/larridin-scout-overlay.yaml
created: '2026-07-17'
description: Larridin is an enterprise AI intelligence platform that measures whether an organization's investment in AI is actually paying off across both its human and agent workforce. Its Scout product instruments AI usage through a managed browser extension and desktop agent, then joins that telemetry with source control, coding-assistant, incident, and work-tracking systems to report on AI adoption, AI fluency (proficiency), AI governance and shadow-tool risk, token spend, workflow intelligence, and Developer Intelligence — covering AI code share, velocity, quality, CI/CD delivery, reliability, agent effectiveness, agent readiness, and developer sentiment. Larridin exposes this data through the read-only Scout API v1 and a beta Model Context Protocol server for agents.
finops:
- has_sources: true
  method: derived
  name: Larridin Finops
  primary_unit: ''
  service_category: ''
  slug: larridin-finops
  template: true
image: https://larridin.com/assets/img/logo-header.webp
layout: provider
mcp_servers:
- description: 'Larridin publishes an official Model Context Protocol server that connects AI assistants and agents to Scout. It is enabled per organization: additional tools may be enabled for an organization and ac'
  name: Larridin MCP Server
  slug: larridin
modified: '2026-07-19'
name: Larridin
nav: Providers
network: true
overview: 'Larridin publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Adoption API, Proficiency API, Surveys API, and 2 more. Tagged areas include Company, Artificial Intelligence, AI Adoption, AI Governance, and Analytics.


  The Larridin catalog on APIs.io includes 1 Spectral governance ruleset.


  Larridin''s developer surface includes pricing, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 27 more developer resources.'
plans:
- name: Larridin Plans Pricing
  plan_count: 1
  slug: larridin-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Larridin API Rules
  rule_count: 65
  severity_counts:
    error: 61
    hint: 0
    info: 2
    warn: 2
  slug: larridin-rules
scopes:
- name: Larridin Scopes
  scope_count: 4
  slug: larridin-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 69.7
    contract_governance: 31.8
    contract_quality: 50.0
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/larridin/larridin-2026-07-25T224539.png
security:
- kind: authentication
  name: Larridin Authentication
  slug: larridin-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Larridin Domain Security
  slug: larridin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Larridin Vulnerability Disclosure
  slug: larridin-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Larridin Trust Center
  slug: larridin-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 4
skills:
- name: Report AI adoption across the organization
  slug: larridin-ai-adoption-report
- name: Measure AI fluency and pair it with survey sentiment
  slug: larridin-ai-fluency-and-sentiment
- name: Audit shadow AI and policy enforcement
  slug: larridin-shadow-ai-governance-audit
- name: Review workflow friction and tool impact
  slug: larridin-workflow-friction-review
slug: larridin
tags:
- Company
- Artificial Intelligence
- AI Adoption
- AI Governance
- Analytics
- Developer Productivity
- Developer Intelligence
- Workflow Intelligence
- Enterprise Software
- Observability
website: https://larridin.com/
---
