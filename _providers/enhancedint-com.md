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
  band_gated_from: agent-native
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Enhancedint Com Agentic Access
  operation_count: 7
  slug: enhancedint-com-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://book.enhancedint.com/enhanced-intelligence
  baseurl_source: declared
  description: The Agent API from enhancedint-com — 6 operation(s) for agent.
  name: enhancedint-com Agent API
  slug: enhancedint-com-agent-api
- baseURL: https://book.enhancedint.com/enhanced-intelligence
  baseurl_source: declared
  description: The Mcp API from enhancedint-com — 1 operation(s) for mcp.
  name: enhancedint-com MCP API
  slug: enhancedint-com-mcp-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: Security
  url: https://example.com/security/disclosure-policy
- group: agent
  href: https://artifacts.apis.io/enhancedint-com/agentic-access/enhancedint-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enhancedint-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/enhancedint-com/rules/enhancedint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/enhancedint-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/enhancedint-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/enhancedint-com/conventions/enhancedint-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/enhancedint-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/enhancedint-com/conventions/enhancedint-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/enhancedint-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/enhancedint-com/authentication/enhancedint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/enhancedint-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/enhancedint-com/errors/enhancedint-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/enhancedint-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/enhancedint-com/conformance/enhancedint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enhancedint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/enhancedint-com/llms/enhancedint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enhancedint-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/enhancedint-com/well-known/enhancedint-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/enhancedint-com-security.txt
- group: auth
  href: https://artifacts.apis.io/enhancedint-com/well-known/enhancedint-com-enhancedint-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/enhancedint-com-enhancedint-security.txt
- group: agent
  href: https://artifacts.apis.io/enhancedint-com/well-known/enhancedint-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enhancedint-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/enhancedint-com/hosts/enhancedint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enhancedint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/enhancedint-com/vendors/enhancedint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enhancedint-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.enhancedint.com/get-started
- group: auth
  href: https://artifacts.apis.io/enhancedint-com/security/enhancedint-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/enhancedint-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/enhancedint-com/security/enhancedint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enhancedint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enhancedint.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.enhancedint.com/book
- group: operate
  title: ''
  type: Support
  url: https://www.enhancedint.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.enhancedint.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enhancedint.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enhancedint.com/terms
created: '2026-10-29'
description: Enhanced Intelligence provides AI-powered websites and receptionist services for local businesses, enabling automated booking, pricing display, and phone call handling. Their platform integrates a Cortex app that consolidates client information, scheduling, and invoicing, while AI agents answer calls and guide customers through services. The company showcases case studies across industries such as mobile detailing and dog training, emphasizing AI-driven customer engagement and streamlined operations.
image: https://www.enhancedint.com/og-image.png
layout: provider
modified: '2026-10-29'
name: enhancedint-com
nav: Providers
network: true
overview: 'enhancedint-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent API and MCP API. Tagged areas include Artificial Intelligence, Websites, Receptionist, Booking, and Local Business.


  The enhancedint-com catalog on APIs.io includes 1 Spectral governance ruleset.


  enhancedint-com''s developer surface includes authentication, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: enhancedint-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: enhancedint-com-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 47.7
    developer_ergonomics: 26.8
    discoverability: 73.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/enhancedint-com/enhancedint-com-2026-11-03T131652.png
security:
- kind: authentication
  name: Enhancedint Com Authentication
  slug: enhancedint-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Enhancedint Com Domain Security
  slug: enhancedint-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enhancedint Com Vulnerability Disclosure
  slug: enhancedint-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: enhancedint-com-book-appointment
  slug: enhancedint-com-book-appointment
slug: enhancedint-com
tags:
- Artificial Intelligence
- Websites
- Receptionist
- Booking
- Local Business
- Automation
website: https://www.enhancedint.com/
---
