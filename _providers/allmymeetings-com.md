---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://allmymeetings.com
  baseurl_source: declared
  description: Calendar sync platform MCP and webhook surfaces.
  name: AllMyMeetings API
  slug: allmymeetings-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/allmymeetings-com/plans/allmymeetings-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allmymeetings-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/allmymeetings-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/allmymeetings-com/conformance/allmymeetings-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allmymeetings-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allmymeetings-com/llms/allmymeetings-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allmymeetings-com-llms.txt
- group: other
  href: https://artifacts.apis.io/allmymeetings-com/a2a/allmymeetings-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/allmymeetings-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/allmymeetings-com/mcp/allmymeetings-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/allmymeetings-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/allmymeetings-com/well-known/allmymeetings-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allmymeetings-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/allmymeetings-com/hosts/allmymeetings-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allmymeetings-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/allmymeetings-com/vendors/allmymeetings-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allmymeetings-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://allmymeetings.com/security
- group: start
  title: ''
  type: Login
  url: https://allmymeetings.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://allmymeetings.com/changelog
- group: auth
  href: https://artifacts.apis.io/allmymeetings-com/security/allmymeetings-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/allmymeetings-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/allmymeetings-com/security/allmymeetings-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allmymeetings-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allmymeetings.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://allmymeetings.com/developers
- group: operate
  title: ''
  type: Support
  url: https://allmymeetings.com/support
- group: company
  title: ''
  type: Blog
  url: https://allmymeetings.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://allmymeetings.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allmymeetings.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allmymeetings.com/privacy
created: '2026-11-01'
description: AllMyMeetings provides calendar synchronization across Google Calendar, Microsoft Outlook, and Apple iCloud, enabling users to avoid double‑bookings and keep personal and work schedules aligned. Founded in early 2026 by Conrad Southworth of Wolfgang Solutions, the service offers a free tier with AI‑compatible MCP server integration, allowing assistants like Claude to manage events via OAuth. The platform includes bidirectional sync, scheduling pages, webhooks for real‑time updates, and a transparent pricing model for individuals and professionals.
image: https://allmymeetings.com/images/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at allmymeetings.com.
  name: AllMyMeetings MCP Server
  slug: allmymeetings-com-mcp-yml
modified: '2026-11-01'
name: AllMyMeetings
nav: Providers
network: true
overview: 'AllMyMeetings is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar, Sync, Artificial Intelligence, Productivity, and Software-as-a-Service.


  AllMyMeetings'' developer surface includes changelog, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Allmymeetings Com Plans Pricing
  plan_count: 1
  slug: allmymeetings-com-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 37.6
    developer_ergonomics: 10.1
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 38.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Allmymeetings Com Domain Security
  slug: allmymeetings-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Allmymeetings Com Vulnerability Disclosure
  slug: allmymeetings-com-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: sync-calendar
  slug: allmymeetings-com-sync-calendar
slug: allmymeetings-com
tags:
- Calendar
- Sync
- Artificial Intelligence
- Productivity
- Software-as-a-Service
website: https://allmymeetings.com/
---
