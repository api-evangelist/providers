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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Metrobi Agentic Access
  operation_count: 5
  slug: metrobi-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://delivery-api.metrobi.com/api/
  baseurl_source: declared
  description: Create, read, list, estimate and cancel local courier deliveries.
  name: Metrobi Deliveries API
  slug: metrobi-deliveries-api
artifact_total: 7
asyncapis:
- description: ''
  name: Metrobi Delivery Webhooks
  slug: metrobi-delivery-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Metrobi Delivery Deliveries API
  slug: open-metrobi-deliveries-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/metrobi-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://metrobi.com/integrations/delivery-api/
- group: docs
  title: ''
  type: Documentation
  url: https://metrobi.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://metrobi.readme.io/reference/what-is-metrobi
- group: start
  title: ''
  type: GettingStarted
  url: https://metrobi.readme.io/reference/authentication
- group: start
  title: ''
  type: SignUp
  url: https://metrobi.com/register/
- group: start
  title: ''
  type: Login
  url: https://deliver.metrobi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://metrobi.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://metrobi.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://metrobi.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metrobi.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metrobi.com/privacy-policy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/metrobi-delivery-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/metrobi-delivery-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metrobi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metrobi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metrobi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metrobi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metrobi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metrobi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/metrobi-delivery-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/metrobi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metrobi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/metrobi-book-local-delivery.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/metrobi-manage-deliveries.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metrobi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metrobi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metrobi.com/
created: '2026-07-17'
description: Metrobi is a Boston-based local same-day delivery and courier platform for businesses — bakeries, caterers, florists, coffee roasters, meal-prep and wholesale food & beverage makers — covering the top 18 US metropolitan areas. Its fulfillment platform handles delivery management, route optimization, receiver notifications, live tracking and driver dispatch across a network of contractor drivers, plus tools for teams running their own in-house drivers. The Metrobi Delivery API lets platforms programmatically estimate, create, read, list and cancel local deliveries and receive real-time status updates via per-delivery webhooks.
image: https://metrobi.com/wp-content/uploads/2023/06/website-thumbnail.jpg
layout: provider
modified: '2026-07-20'
name: Metrobi
nav: Providers
network: true
overview: 'Metrobi publishes 1 API on the [APIs.io](https://apis.io/) network: Deliveries API. Tagged areas include Company, Delivery, Logistics, Couriers, and Last Mile Delivery.


  The Metrobi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Metrobi''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 21 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 63.1
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 42.8
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metrobi/refs/heads/main/screenshots/metrobi-2026-08-07T172751.png
security:
- kind: authentication
  name: Metrobi Authentication
  slug: metrobi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metrobi Domain Security
  slug: metrobi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metrobi
tags:
- Company
- Delivery
- Logistics
- Couriers
- Last Mile Delivery
- Route Optimization
- Fulfillment
- Local Delivery
- Webhook
website: https://metrobi.com/
---
