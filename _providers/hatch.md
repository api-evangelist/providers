---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.usehatchapp.com
  baseurl_source: declared
  description: The contacts API from Hatch — 1 operation(s) for contacts.
  name: Hatch Contacts API
  slug: hatch-contacts-api
artifact_total: 10
asyncapis:
- description: ''
  name: Hatch Webhooks
  slug: hatch-webhooks
collections:
- collection_type: open
  name: Hatch contacts API
  slug: open-hatch-contacts-api
common:
- group: commercial
  href: https://artifacts.apis.io/hatch/plans/hatch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hatch-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/hatch/capabilities/hatch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hatch-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/hatch/mcp/hatch-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hatch-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.usehatchapp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usehatchapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usehatchapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usehatchapp.com/integrations/hatch-api/hatch-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usehatchapp.com/getting-started/intro-to-hatch/what-is-hatch
- group: operate
  title: ''
  type: Support
  url: https://docs.usehatchapp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.usehatchapp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usehatchapp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.usehatchapp.com/
- group: start
  title: ''
  type: Login
  url: https://app.usehatchapp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usehatchapp.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usehatchapp.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usehatchapp.com
- group: docs
  href: https://artifacts.apis.io/hatch/openapi/_original/hatch-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/hatch-openapi-original.json
- group: auth
  href: https://artifacts.apis.io/hatch/authentication/hatch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hatch-authentication.yml
- group: design
  href: https://artifacts.apis.io/hatch/errors/hatch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hatch-problem-types.yml
- group: other
  href: https://artifacts.apis.io/hatch/overlays/hatch-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hatch-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/hatch/conventions/hatch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hatch-conventions.yml
- group: design
  href: https://artifacts.apis.io/hatch/lifecycle/hatch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hatch-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/hatch/rate-limits/hatch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hatch-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hatch/asyncapi/hatch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hatch-webhooks.yml
- group: design
  href: https://artifacts.apis.io/hatch/conformance/hatch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hatch-conformance.yml
- group: design
  href: https://artifacts.apis.io/hatch/data-model/hatch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hatch-data-model.yml
- group: auth
  href: https://artifacts.apis.io/hatch/security/hatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hatch-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/hatch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hatch/llms/hatch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hatch-llms.txt
created: '2026-07-17'
description: Hatch is an AI-powered customer communication platform for service businesses, unifying voice, SMS, and email into a single system with custom AI agents (AI CSRs) that text and call leads and customers to qualify them, book appointments, and drive bottom-line growth without adding headcount. Products include Voice AI, Messaging AI, Journey Builder for multi-channel campaigns, a Knowledge Engine, and a Command Center for performance tracking. For developers, Hatch exposes a public REST API (bearer-token auth) whose primary operation upserts contacts into campaigns, a Bulk Export API for BI/analytics, and an outbound webhook surface (11 event types, EdDSA-signed) for pushing events to downstream systems and Zapier. Backed by Bessemer Venture Partners and True Ventures. Added to the API Evangelist network and enriched from the provider's own public developer surface.
finops:
- has_sources: true
  method: derived
  name: Hatch Finops
  primary_unit: ''
  service_category: ''
  slug: hatch-finops
  template: true
image: https://cdn.prod.website-files.com/6979136a27d403634304b470/69c2be9beb7874c215169569_hatch-homepage-og-image.png
layout: provider
modified: '2026-07-19'
name: Hatch
nav: Providers
network: true
overview: 'Hatch publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Contacts API. Tagged areas include Company, Vertical Software, Customer Communication, Conversational AI, and SMS.


  The Hatch catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hatch''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Hatch Plans Pricing
  plan_count: 3
  slug: hatch-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Hatch Rate Limits
  slug: hatch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Hatch API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: hatch-rules
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 44.7
  previous_composite: 59.0
  provenance:
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
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/hatch/hatch-2026-07-25T220750.png
security:
- kind: authentication
  name: Hatch Authentication
  slug: hatch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hatch Domain Security
  slug: hatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Upsert a contact into Hatch
  slug: hatch-upsert-contact
slug: hatch
tags:
- Company
- Vertical Software
- Customer Communication
- Conversational AI
- SMS
- Voice
- Email
- Marketing
- Home Services
- Contact Center
website: https://www.usehatchapp.com/
---
