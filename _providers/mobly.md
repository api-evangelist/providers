---
access_model:
  confidence: medium
  label: Sales gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://help.getmobly.com/api-reference/readme
  - https://www.getmobly.com/request-a-demo/
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Mobly Agentic Access
  operation_count: 27
  slug: mobly-agentic-access
  summary_line: 27 operations · 12 acting
api_count: 1
apis:
- baseURL: https://core-api.getmobly.com/api/v0
  baseurl_source: declared
  description: The Activations API from Mob.ly — 2 operation(s) for activations.
  name: Mob.ly Activations API
  slug: mobly-activations-api
- baseURL: https://core-api.getmobly.com/api/v0
  baseurl_source: declared
  description: The Events API from Mob.ly — 5 operation(s) for events.
  name: Mob.ly Events API
  slug: mobly-events-api
- baseURL: https://core-api.getmobly.com/api/v0
  baseurl_source: declared
  description: The IndustryEvents API from Mob.ly — 4 operation(s) for industryevents.
  name: Mob.ly Industry Events API
  slug: mobly-industryevents-api
- baseURL: https://core-api.getmobly.com/api/v0
  baseurl_source: declared
  description: The LeadActivityEvents API from Mob.ly — 2 operation(s) for leadactivityevents.
  name: Mob.ly Lead Activity Events API
  slug: mobly-leadactivityevents-api
- baseURL: https://core-api.getmobly.com/api/v0
  baseurl_source: declared
  description: The Leads API from Mob.ly — 2 operation(s) for leads.
  name: Mob.ly Leads API
  slug: mobly-leads-api
- baseURL: https://core-api.getmobly.com/api/v0
  baseurl_source: declared
  description: The Tag Groups API from Mob.ly — 2 operation(s) for tag groups.
  name: Mob.ly Tag Groups API
  slug: mobly-tag-groups-api
artifact_total: 18
asyncapis:
- description: ''
  name: Mobly Webhooks
  slug: mobly-webhooks
collections:
- collection_type: open
  name: Mobly REST API
  slug: open-mobly-rest-api-v0
common:
- group: other
  href: https://artifacts.apis.io/mobly/capabilities/mobly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mobly-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/mobly/overlays/mobly-rest-api-v0-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mobly-rest-api-v0-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mobly/agentic-access/mobly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mobly-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmobly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.getmobly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.getmobly.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://help.getmobly.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.getmobly.com/help-center/getting-started/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.getmobly.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.getmobly.com/resources/
- group: operate
  href: https://artifacts.apis.io/mobly/changelog/mobly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mobly-changelog.yml
- group: agent
  href: https://artifacts.apis.io/mobly/llms/mobly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mobly-llms.txt
- group: auth
  href: https://artifacts.apis.io/mobly/authentication/mobly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mobly-authentication.yml
- group: design
  href: https://artifacts.apis.io/mobly/conventions/mobly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mobly-conventions.yml
- group: operate
  href: https://artifacts.apis.io/mobly/rate-limits/mobly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mobly-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/mobly/errors/mobly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mobly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mobly/data-model/mobly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mobly-data-model.yml
- group: design
  href: https://artifacts.apis.io/mobly/lifecycle/mobly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mobly-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mobly/conformance/mobly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mobly-conformance.yml
- group: build
  href: https://artifacts.apis.io/mobly/packages/mobly-packages.yml
  title: ''
  type: Packages
  url: packages/mobly-packages.yml
- group: commercial
  href: https://artifacts.apis.io/mobly/plans/mobly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mobly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mobly/asyncapi/mobly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mobly-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/mobly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/mobly/security/mobly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mobly-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmobly.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getmobly.com/termsofuse
- group: start
  title: ''
  type: Login
  url: https://hub.getmobly.com/login
created: '2026-07-17'
description: Mob.ly (Mobly) is an AI-powered in-person go-to-market platform — "The Event Marketer's Operating System" — that helps B2B teams plan events, capture and enrich leads in person, engage prospects, and measure pipeline across trade shows and in-real-life (IRL) marketing experiences. Its product suite spans Capture (universal lead capture and OCR badge/business-card scanning), Host (self-run activations, registration pages and Stripe-backed ticketing), Insights (dashboards and reporting), Pulse (speed-to-lead sequences and lead routing) and Scout (event discovery), with native integrations into HubSpot, Salesforce, Pardot, Marketo, Pipedrive, Zoho, Slack, Calendly and generic webhook destinations. Mobly publishes a JSON REST API (v0) at core-api.getmobly.com covering events, leads, lead activity events, activations, tag groups and industry events, authenticated with an organization API key issued by its customer success team. Headquartered in Lehi, Utah and backed by Uncork Capital
  and Jump Capital.
finops:
- has_sources: true
  method: derived
  name: Mobly Finops
  primary_unit: ''
  service_category: ''
  slug: mobly-finops
  template: true
image: https://www.getmobly.com/images/webclip.png
layout: provider
modified: '2026-08-13'
name: Mob.ly
nav: Providers
network: true
overview: 'Mob.ly publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activations API, Events API, Industry Events API, and 3 more. Tagged areas include Company, Event, Event Marketing, Lead Capture, and Lead Enrichment.


  The Mob.ly catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mob.ly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 20 more developer resources.'
plans:
- name: Mobly Plans Pricing
  plan_count: 0
  slug: mobly-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Mobly Rate Limits
  slug: mobly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Mob.ly API Rules
  rule_count: 60
  severity_counts:
    error: 51
    hint: 0
    info: 5
    warn: 4
  slug: mobly-rules
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 65.7
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/mobly/mobly-2026-08-07T183858.png
security:
- kind: authentication
  name: Mobly Authentication
  slug: mobly-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mobly Domain Security
  slug: mobly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create a lead and attach it to an event
  slug: mobly-capture-and-qualify-lead
- name: Search and shortlist industry events with Scout
  slug: mobly-scout-industry-events
- name: Sync event leads out of Mobly
  slug: mobly-sync-event-leads
slug: mobly
tags:
- Company
- Event
- Event Marketing
- Lead Capture
- Lead Enrichment
- B2B
- Marketing
- Go-To-Market
- Artificial Intelligence
- CRM
- Marketing Automation
- Trade Shows
- Data Enrichment
website: https://www.getmobly.com/
---
