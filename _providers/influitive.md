---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.influitive.com
  baseurl_source: declared
  description: The Events API from Influitive — 1 operation(s) for events.
  name: Influitive Events API
  slug: influitive-events-api
artifact_total: 6
asyncapis:
- description: ''
  name: Influitive Webhooks
  slug: influitive-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: do-not-delete Events API
  slug: open-influitive-events-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/influitive-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/influitive-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/influitive-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/influitive-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/influitive-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/influitive-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/influitive-events-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/influitive-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/influitive-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/influitive-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/influitive-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/influitive-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://influitive.readme.io
- group: docs
  title: ''
  type: Documentation
  url: https://influitive.readme.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://influitive.readme.io/reference/events
- group: operate
  title: ''
  type: Support
  url: https://support.influitive.com
- group: company
  title: ''
  type: Blog
  url: https://influitive.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://influitive.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://influitive.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://influitive.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://influitive.com/request-a-demo/
- group: company
  title: ''
  type: Website
  url: https://influitive.com
created: '2026-07-17'
description: Influitive is a Toronto-based SaaS company that provides a customer advocacy, community, and engagement platform (historically branded AdvocateHub) that helps B2B companies discover, mobilize, and reward their customer advocates. The platform runs gamified challenges, guided customer journeys, referral and reference programs, reviews and social amplification, discussions, ideation, and loyalty rewards. Influitive exposes a small public HTTP API — the Events endpoint — that lets external systems log an event or act of advocacy and award points to an advocate, plus a catalog of outbound webhooks that notify integrations when advocacy, challenge, reward, referral, discussion, and profile events occur inside a hub. Developer documentation is published on a ReadMe-hosted portal at influitive.readme.io.
image: https://influitive.com/wp-content/uploads/2021/05/influitive-logo.png
layout: provider
modified: '2026-07-19'
name: Influitive
nav: Providers
network: true
overview: 'Influitive publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Company, Customer Advocacy, Customer Community, Customer Engagement, and Advocacy Marketing.


  The Influitive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Influitive''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 64.4
    developer_ergonomics: 33.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 41.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/influitive/refs/heads/main/screenshots/influitive-2026-07-25T222413.png
security:
- kind: authentication
  name: Influitive Authentication
  slug: influitive-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Influitive Domain Security
  slug: influitive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: influitive
tags:
- Company
- Customer Advocacy
- Customer Community
- Customer Engagement
- Advocacy Marketing
- Referral Marketing
- Customer Loyalty
- Gamification
- Webhook
- Software-as-a-Service
website: https://influitive.com
---
