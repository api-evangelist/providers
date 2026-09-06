---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The API host behind the Cockpit AI (formerly Kalendar AI) product. The root of https://api.oncockpit.ai returns HTTP 200 with {"name":"Cockpit AI API","status":"active"} and /health returns OK, and th
  name: Cockpit AI API
  slug: cockpit-ai-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goomp-inc-kalendar-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oncockpit.ai
- group: start
  title: ''
  type: SignUp
  url: https://oncockpit.ai/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oncockpit.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oncockpit.ai/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/goomp-inc-kalendar-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goomp-inc-kalendar-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/goomp-inc-kalendar-ai-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goomp-inc-kalendar-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goomp-inc-kalendar-ai-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/goomp-inc-kalendar-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goomp-inc-kalendar-ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goomp-inc-kalendar-ai-llms.txt
created: '2026-07-17'
description: Kalendar AI (Goomp Inc / Kalendar Inc, a Delaware corporation operating from New York) is an autonomous AI sales-agent platform that automates B2B outbound prospecting end to end. It sources ideal-customer prospects from a database of hundreds of millions of professionals and companies, generates and sends personalized outreach through dedicated AI-managed mailbox infrastructure, qualifies replies, and books meetings directly onto the user's calendar. As of the 2026-08-13 enrichment pass the company has rebranded to Cockpit AI and migrated to oncockpit.ai — kalendar.ai now 301-redirects site-wide, and the new site's robots.txt carries an explicit "Block legacy Kalendar.ai paths" section. The product is now framed as named AI workers you "hire" (Vinay for outbound, Amara), which research prospects, draft proposal documents, send from the customer's own email and LinkedIn accounts, and book meetings, with a human approval step before anything ships. Investors named on the site
  are 500 Global, Boost VC, Asymmetry Ventures and Village Global. The company runs a live API host (api.oncockpit.ai, which self-identifies as the "Cockpit AI API") and still serves a legacy ChatGPT plugin manifest at /.well-known/ai-plugin.json declaring OAuth with read/write scopes, but it publishes no developer portal, no API reference, no OpenAPI, no SDK, no webhook catalog, no MCP server and no pricing page.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goomp-inc-kalendar-ai.png
layout: provider
modified: '2026-08-13'
name: Goomp Inc, Kalendar AI
nav: Providers
network: true
overview: 'Goomp Inc, Kalendar AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, Sales Automation, and Outbound.


  Goomp Inc, Kalendar AI''s developer surface includes signup flow, authentication, and 11 more developer resources.'
plans:
- name: Goomp Inc Kalendar Ai Plans Pricing
  plan_count: 0
  slug: goomp-inc-kalendar-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Goomp Inc Kalendar Ai Rate Limits
  slug: goomp-inc-kalendar-ai-rate-limits
scopes:
- name: Goomp Inc Kalendar Ai Scopes
  scope_count: 0
  slug: goomp-inc-kalendar-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 9.8
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goomp-inc-kalendar-ai/refs/heads/main/screenshots/goomp-inc-kalendar-ai-2026-07-25T220105.png
security:
- kind: authentication
  name: Goomp Inc Kalendar Ai Authentication
  slug: goomp-inc-kalendar-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Goomp Inc Kalendar Ai Domain Security
  slug: goomp-inc-kalendar-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goomp-inc-kalendar-ai
tags:
- Company
- Artificial Intelligence
- Sales
- Sales Automation
- Outbound
- Lead Generation
- Scheduling
- Agents
- Email
- CRM
website: https://oncockpit.ai
---
