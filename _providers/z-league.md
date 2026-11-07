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
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Z League Agentic Access
  operation_count: 7
  slug: z-league-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://app.gomega.ai
  baseurl_source: declared
  description: The Leads API from Z League — 2 operation(s) for leads.
  name: Z League Leads API
  slug: z-league-leads-api
- baseURL: https://app.gomega.ai
  baseurl_source: declared
  description: The Webhooks API from Z League — 2 operation(s) for webhooks.
  name: Z League Webhooks API
  slug: z-league-webhooks-api
arazzos:
- description: Register a lead.created webhook, then create a lead. Real inserts fire the webhook so your endpoint is notified. Uses an Idempotency-Key so the create is retry-safe.
  name: MEGA CRM — capture lead and register webhook
  slug: z-league-capture-and-notify
- description: 'Poll the MEGA CRM for leads with stable keyset cursor pagination: fetch the first page sorted by updated_at ascending, then follow next_cursor to fetch the next page.'
  name: MEGA CRM — incremental lead sync
  slug: z-league-incremental-lead-sync
artifact_total: 19
asyncapis:
- description: Outbound webhook event surface for the MEGA public CRM Lead API. MEGA POSTs a signed `lead.created` event to a subscriber-registered public HTTPS endpoint whenever a genuine new lead is created. Deliv
  name: MEGA Public CRM Lead Webhooks
  slug: z-league-lead-webhooks-asyncapi
- description: ''
  name: Z League Lead Webhooks
  slug: z-league-lead-webhooks
collections:
- collection_type: open
  name: MEGA Public CRM Lead Leads API
  slug: open-z-league-leads-api
- collection_type: open
  name: MEGA Public CRM Lead Leads Webhooks API
  slug: open-z-league-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/z-league/plans/z-league-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/z-league-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/z-league/capabilities/z-league-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/z-league-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/z-league/mcp/z-league-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/z-league-mcp.yml
- group: other
  href: https://artifacts.apis.io/z-league/overlays/z-league-crm-lead-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/z-league-crm-lead-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gomega.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gomega.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gomega.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gomega.ai/quickstart
- group: company
  title: ''
  type: Website
  url: https://www.gomega.ai
- group: company
  title: ''
  type: Blog
  url: https://www.gomega.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gomega.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.gomega.ai/megapricing
- group: start
  title: ''
  type: Login
  url: https://app.gomega.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gomega.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gomega.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@gomega.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zleague
- group: operate
  href: https://artifacts.apis.io/z-league/changelog/z-league-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/z-league-changelog.yml
- group: design
  href: https://artifacts.apis.io/z-league/lifecycle/z-league-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/z-league-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/z-league/rate-limits/z-league-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/z-league-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/z-league/llms/z-league-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/z-league-llms.txt
- group: auth
  href: https://artifacts.apis.io/z-league/security/z-league-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/z-league-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/z-league/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/z-league/arazzo/z-league-incremental-lead-sync.yml
  title: ''
  type: Arazzo
  url: arazzo/z-league-incremental-lead-sync.yml
- group: design
  href: https://artifacts.apis.io/z-league/arazzo/z-league-capture-and-notify.yml
  title: ''
  type: Arazzo
  url: arazzo/z-league-capture-and-notify.yml
created: '2026-07-17'
description: 'Z League is an a16z-backed startup that operates the MEGA platform (gomega.ai) — a suite of AI marketing agents that autonomously manage SEO, paid advertising, and website/growth optimization for businesses at a fraction of traditional agency cost. MEGA also ships a built-in CRM, and exposes the MEGA public CRM Lead API: a server-to-server REST API to pull/search leads with cursor pagination, push leads one-at-a-time or in bulk (up to 500) with idempotency and email/phone de-duplication, and register HMAC-signed `lead.created` webhooks. Authentication is an admin-issued, customer-locked, scoped Personal Access Token (Bearer `mega_...`) plus an `x-customer-id` header. The API is documented with an OpenAPI 3.1 spec and a Mintlify developer portal published from the company''s public GitHub org (github.com/zleague).'
finops:
- has_sources: true
  method: derived
  name: Z League Finops
  primary_unit: ''
  service_category: ''
  slug: z-league-finops
  template: true
image: https://raw.githubusercontent.com/api-evangelist/z-league/refs/heads/main/openapi/z-league-crm-lead-openapi.json
layout: provider
modified: '2026-07-21'
name: Z League
nav: Providers
network: true
overview: 'Z League publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Leads API and Webhooks API. Tagged areas include Company, CRM, Leads, Marketing, and AI Agents.


  The Z League catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Z League''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 18 more developer resources.'
plans:
- name: Z League Plans Pricing
  plan_count: 3
  slug: z-league-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Z League Rate Limits
  slug: z-league-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Z League API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: z-league-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 60.6
    developer_ergonomics: 20.8
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 48.2
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
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/z-league/z-league-2026-08-17T083228.png
security:
- kind: authentication
  name: Z League Authentication
  slug: z-league-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Z League Domain Security
  slug: z-league-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Bulk-import leads
  slug: z-league-bulk-import
- name: Push a lead safely (idempotent)
  slug: z-league-push-lead
- name: Register and verify a lead.created webhook
  slug: z-league-register-webhook
- name: Incrementally sync leads
  slug: z-league-sync-leads
slug: z-league
tags:
- Company
- CRM
- Leads
- Marketing
- AI Agents
- SEO
- Advertising
- Webhook
- Gaming
website: https://www.gomega.ai
---
