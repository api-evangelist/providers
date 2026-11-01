---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Harmony Agentic Access
  operation_count: 9
  slug: harmony-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.harmony.io/service-desk
  baseurl_source: declared
  description: The tickets API from Harmony — 6 operation(s) for tickets.
  name: Harmony Tickets API
  slug: harmony-tickets-api
arazzos:
- description: Create a service-desk ticket, read it back, triage it, and audit the change.
  name: Harmony — create and triage an IT ticket
  slug: harmony-create-and-triage-ticket
artifact_total: 11
collections:
- collection_type: open
  name: service-desk tickets API
  slug: open-harmony-tickets-api
common:
- group: commercial
  href: https://artifacts.apis.io/harmony/plans/harmony-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/harmony-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/harmony/rate-limits/harmony-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/harmony-rate-limits.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://harmony.io/feed.xml
- group: other
  href: https://artifacts.apis.io/harmony/capabilities/harmony-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/harmony-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.harmony.io/
- group: agent
  href: https://artifacts.apis.io/harmony/mcp/harmony-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/harmony-mcp.yml
- group: other
  href: https://artifacts.apis.io/harmony/overlays/harmony-service-desk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/harmony-service-desk-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/harmony/security/harmony-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harmony-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.harmony.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.harmony.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.harmony.io/api-references/api-documentation/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.harmony.io/getting-started/welcome
- group: operate
  title: ''
  type: Support
  url: mailto:support@harmony.io
- group: company
  title: ''
  type: Blog
  url: https://harmony.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harmonyso
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harmony.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harmony.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harmony.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.harmony.io/
- group: agent
  href: https://artifacts.apis.io/harmony/llms/harmony-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/harmony-llms.txt
- group: design
  href: https://artifacts.apis.io/harmony/lifecycle/harmony-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/harmony-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/harmony/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/harmony/arazzo/harmony-create-and-triage-ticket.yml
  title: ''
  type: Arazzo
  url: arazzo/harmony-create-and-triage-ticket.yml
- group: agent
  href: https://artifacts.apis.io/harmony/agentic-access/harmony-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/harmony-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/harmony/authentication/harmony-authentication.yml
  title: ''
  type: Authentication
  url: authentication/harmony-authentication.yml
created: '2026-07-17'
description: Harmony is an agentic enterprise service management (ESM) platform that gives every employee an always-on AI expert for IT, HR, finance, procurement, and legal service requests inside Slack and Microsoft Teams. Its AI agents autonomously resolve requests — password and MFA resets, application access, device recovery, employee onboarding and offboarding — using a context graph that connects each employee's identity, devices, applications, and history, often resolving issues before a ticket is opened. Harmony exposes a public REST Service Desk API for programmatically listing, creating, updating, querying, and bulk-updating tickets along with their custom fields and activity history. Founded in 2025 by Nitzan Shapira and Ran Ribenzaft and backed by Lightspeed Venture Partners.
finops:
- has_sources: true
  method: derived
  name: Harmony Finops
  primary_unit: ''
  service_category: ''
  slug: harmony-finops
  template: true
image: https://harmony.io/favicon.ico
layout: provider
modified: '2026-10-06'
name: Harmony
nav: Providers
network: true
overview: 'Harmony publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Tickets API. Tagged areas include ITSM, Service Desk, Ticketing, Enterprise Service Management, and AI Agents.


  Harmony''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Harmony Plans Pricing
  plan_count: 1
  slug: harmony-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Harmony Rate Limits
  slug: harmony-rate-limits
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.2
  facets:
    access_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 49.0
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 42.1
  previous_composite: 44.6
  provenance:
    agentic_access: derived
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/harmony/harmony-2026-07-25T220731.png
security:
- kind: authentication
  name: Harmony Authentication
  slug: harmony-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Harmony Domain Security
  slug: harmony-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Create and triage an IT ticket
  slug: harmony-create-and-triage-ticket
- name: Query and bulk-update tickets
  slug: harmony-query-and-bulk-update-tickets
slug: harmony
tags:
- ITSM
- Service Desk
- Ticketing
- Enterprise Service Management
- AI Agents
- IT Automation
- Help Desk
- Identity
- Company
website: https://www.harmony.io/
---
