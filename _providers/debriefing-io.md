---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Debriefing Io Agentic Access
  operation_count: 9
  slug: debriefing-io-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- description: Read competitors, signals, digests, and battlecards for one workspace.
  name: Debriefing Read API
  slug: debriefing-read-api
- baseURL: https://debriefing.io
  baseurl_source: declared
  description: Generated battlecards for this workspace.
  name: Debriefing Battlecards API
  slug: debriefing-io-battlecards-api
- baseURL: https://debriefing.io
  baseurl_source: declared
  description: Competitors this workspace tracks.
  name: Debriefing Competitors API
  slug: debriefing-io-competitors-api
- baseURL: https://debriefing.io
  baseurl_source: declared
  description: Generated digests for this workspace.
  name: Debriefing Digests API
  slug: debriefing-io-digests-api
- baseURL: https://debriefing.io
  baseurl_source: declared
  description: Evidence-backed competitor moves.
  name: Debriefing Signals API
  slug: debriefing-io-signals-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/debriefing-io/agentic-access/debriefing-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/debriefing-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/debriefing-io/plans/debriefing-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/debriefing-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/debriefing-io/rules/debriefing-io-rules.yml
  title: ''
  type: Spectral
  url: rules/debriefing-io-rules.yml
- group: design
  href: https://artifacts.apis.io/debriefing-io/json-ld/debriefing-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/debriefing-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/debriefing-io/vocabulary/debriefing-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/debriefing-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/debriefing-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/debriefing-io/data-model/debriefing-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/debriefing-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/debriefing-io/authentication/debriefing-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/debriefing-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/debriefing-io/errors/debriefing-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/debriefing-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/debriefing-io/conformance/debriefing-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/debriefing-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/debriefing-io/llms/debriefing-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/debriefing-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/debriefing-io/mcp/debriefing-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/debriefing-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/debriefing-io/well-known/debriefing-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/debriefing-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/debriefing-io/hosts/debriefing-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/debriefing-io-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://debriefing.io/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://debriefing.io/guides/getting-started-with-competitive-intel
- group: auth
  href: https://artifacts.apis.io/debriefing-io/security/debriefing-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/debriefing-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://debriefing.io/
- group: docs
  title: ''
  type: Documentation
  url: https://debriefing.io/developers.md
- group: docs
  title: ''
  type: APIReference
  url: https://debriefing.io/developers/openapi.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://debriefing.io/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://debriefing.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://debriefing.io/privacy_policy
- group: operate
  title: ''
  type: Support
  url: https://debriefing.io/contact
created: '2026-11-05'
description: Debriefing provides competitive intelligence for small to mid-sized companies (20‑249 employees) across any industry. It monitors competitor pricing, product launches, hiring, positioning, and market pages, turning source‑backed evidence into concise briefs with recommended actions. Users receive briefings via email, Slack, or a dashboard, and can request free or paid briefs through the platform. The service includes paid plans with advanced monitoring, a free trial, and a clear refund policy.
image: https://debriefing.io/icon-light.png
jsonld:
- class_count: 11
  name: Debriefing Io Context
  property_count: 76
  slug: debriefing-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at debriefing.io.
  name: Debriefing MCP Server
  slug: debriefing-io-mcp-yml
modified: '2026-11-05'
name: Debriefing
nav: Providers
network: true
overview: 'Debriefing publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Read API, Battlecards API, Competitors API, and 2 more. Tagged areas include Competitive Intelligence, Software-as-a-Service, B2B, Monitoring, and Small Business.


  The Debriefing catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Debriefing''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, support, and 18 more developer resources.'
plans:
- name: Debriefing Io Plans Pricing
  plan_count: 4
  slug: debriefing-io-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Debriefing API Rules
  rule_count: 63
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 1
  slug: debriefing-io-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 59.0
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Debriefing Io Authentication
  slug: debriefing-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Debriefing Io Domain Security
  slug: debriefing-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: debriefing-io-api
  slug: debriefing-io-api
slug: debriefing-io
tags:
- Competitive Intelligence
- Software-as-a-Service
- B2B
- Monitoring
- Small Business
website: https://debriefing.io/
---
