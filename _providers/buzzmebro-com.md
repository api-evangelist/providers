---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Buzzmebro Com Agentic Access
  operation_count: 20
  slug: buzzmebro-com-agentic-access
  summary_line: 20 operations · 12 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://buzzmebro.com/api/partner/v1
  baseurl_source: declared
  description: The Applications API from BuzzMeBro — 5 operation(s) for applications.
  name: BuzzMeBro Applications API
  slug: buzzmebro-com-applications-api
- baseURL: https://buzzmebro.com/api/agent/v1
  baseurl_source: declared
  description: The Check API from BuzzMeBro — 1 operation(s) for check.
  name: BuzzMeBro Check API
  slug: buzzmebro-com-check-api
- baseURL: https://buzzmebro.com/api/partner/v1
  baseurl_source: declared
  description: The Info API from BuzzMeBro — 1 operation(s) for info.
  name: BuzzMeBro Info API
  slug: buzzmebro-com-info-api
- baseURL: https://buzzmebro.com/api/partner/v1
  baseurl_source: declared
  description: The Me API from BuzzMeBro — 7 operation(s) for me.
  name: BuzzMeBro Me API
  slug: buzzmebro-com-me-api
- baseURL: https://buzzmebro.com/api/agent/v1
  baseurl_source: declared
  description: The Setups API from BuzzMeBro — 5 operation(s) for setups.
  name: BuzzMeBro Setups API
  slug: buzzmebro-com-setups-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/buzzmebro-com/agentic-access/buzzmebro-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buzzmebro-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/buzzmebro-com/rules/buzzmebro-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buzzmebro-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/buzzmebro-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/buzzmebro-com/security/buzzmebro-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/buzzmebro-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/buzzmebro-com/errors/buzzmebro-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buzzmebro-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buzzmebro-com/conformance/buzzmebro-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buzzmebro-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buzzmebro-com/llms/buzzmebro-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buzzmebro-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/buzzmebro-com/mcp/buzzmebro-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buzzmebro-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/buzzmebro-com/well-known/buzzmebro-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buzzmebro-com-security.txt
- group: agent
  href: https://artifacts.apis.io/buzzmebro-com/well-known/buzzmebro-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buzzmebro-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buzzmebro-com/hosts/buzzmebro-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buzzmebro-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buzzmebro-com/vendors/buzzmebro-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buzzmebro-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buzzmebro.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buzzmebro.com/privacy
- group: start
  title: ''
  type: Login
  url: https://buzzmebro.com/signin
- group: company
  title: ''
  type: Blog
  url: https://buzzmebro.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://buzzmebro.com/blog/ai-assistant-buzzer-setup-for-roommates
- group: docs
  title: ''
  type: APIReference
  url: https://buzzmebro.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/buzzmebro-com/authentication/buzzmebro-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buzzmebro-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/buzzmebro-com/security/buzzmebro-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buzzmebro-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buzzmebro-com/security/buzzmebro-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buzzmebro-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buzzmebro.com/
created: '2026-11-03'
description: BuzzMeBro is a Toronto‑based service that expands apartment buzzer access to multiple roommates, eliminating reliance on a single person to answer the door. The platform lets any authorized resident open the door via their phone, offering a free first month and a subscription of $9.99 per month for the whole apartment. BuzzMeBro emphasizes privacy, never selling user data, and aims to simplify shared living security and convenience.
image: https://buzzmebro.com/brand/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at buzzmebro.com.
  name: BuzzMeBro MCP Server
  slug: buzzmebro-com-mcp-yml
modified: '2026-11-03'
name: BuzzMeBro
nav: Providers
network: true
overview: 'BuzzMeBro publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Check API, Info API, and 2 more. Tagged areas include Company, Buzzer, Apartments, Access, and Subscription.


  The BuzzMeBro catalog on APIs.io includes 1 Spectral governance ruleset.


  BuzzMeBro''s developer surface includes engineering blog, getting-started guide, API reference, authentication, and 18 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: BuzzMeBro API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: buzzmebro-com-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 50.4
    developer_ergonomics: 24.4
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Buzzmebro Com Authentication
  slug: buzzmebro-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Buzzmebro Com Domain Security
  slug: buzzmebro-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Buzzmebro Com Vulnerability Disclosure
  slug: buzzmebro-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: buzzmebro-com-setup-checkout
  slug: buzzmebro-com-setup-checkout
slug: buzzmebro-com
tags:
- Company
- Buzzer
- Apartments
- Access
- Subscription
- Toronto
website: https://buzzmebro.com/
---
