---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bayareamobiledogwash Com Agentic Access
  operation_count: 2
  slug: bayareamobiledogwash-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Check availability and request a mobile dog wash (the van comes to the customer's home; San Jose + nearby South Bay).
  name: Bay Area Mobile Dog Wash Booking API
  slug: bay-area-mobile-dog-wash-booking-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/bayareamobiledogwash-com/agentic-access/bayareamobiledogwash-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bayareamobiledogwash-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bayareamobiledogwash-com/plans/bayareamobiledogwash-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bayareamobiledogwash-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bayareamobiledogwash-com/rules/bayareamobiledogwash-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bayareamobiledogwash-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/bayareamobiledogwash-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bayareamobiledogwash-com/errors/bayareamobiledogwash-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bayareamobiledogwash-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bayareamobiledogwash-com/conformance/bayareamobiledogwash-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bayareamobiledogwash-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bayareamobiledogwash-com/llms/bayareamobiledogwash-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bayareamobiledogwash-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bayareamobiledogwash-com/mcp/bayareamobiledogwash-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bayareamobiledogwash-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/bayareamobiledogwash-com/hosts/bayareamobiledogwash-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bayareamobiledogwash-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bayareamobiledogwash-com/vendors/bayareamobiledogwash-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bayareamobiledogwash-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bayareamobiledogwash.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bayareamobiledogwash.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://bayareamobiledogwash.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://bayareamobiledogwash.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/bayareamobiledogwash-com/security/bayareamobiledogwash-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bayareamobiledogwash-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bayareamobiledogwash.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://bayareamobiledogwash.com/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://bayareamobiledogwash.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://bayareamobiledogwash.com/faq
created: '2026-11-02'
description: Bay Area Mobile Dog Wash provides on‑demand mobile dog grooming services throughout the San Jose and South Bay area. Customers can book a van‑based spa wash that includes bathing, brushing, nail trimming, de‑shedding and other treatments, all performed at the client’s curbside location. The business emphasizes personalized care, insurance coverage, and a limited‑client‑per‑day model to ensure quality service.
image: https://bayareamobiledogwash.com/opengraph-image.png?a9a6b45339db4230
layout: provider
mcp_servers:
- description: Remote MCP server at bayareamobiledogwash.com.
  name: Bay Area Mobile Dog Wash MCP Server
  slug: bayareamobiledogwash-com-mcp-yml
modified: '2026-11-02'
name: Bay Area Mobile Dog Wash
nav: Providers
network: true
overview: 'Bay Area Mobile Dog Wash is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Dog, Grooming, Bay Area, and Services.


  The Bay Area Mobile Dog Wash catalog on APIs.io includes 1 Spectral governance ruleset.


  Bay Area Mobile Dog Wash''s developer surface includes documentation, API reference, getting-started guide, pricing, support, and 14 more developer resources.'
plans:
- name: Bayareamobiledogwash Com Plans Pricing
  plan_count: 4
  slug: bayareamobiledogwash-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Bay Area Mobile Dog Wash API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: bayareamobiledogwash-com-rules
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bayareamobiledogwash Com Domain Security
  slug: bayareamobiledogwash-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bayareamobiledogwash-com
tags:
- Mobile
- Dog
- Grooming
- Bay Area
- Services
website: https://bayareamobiledogwash.com/
---
