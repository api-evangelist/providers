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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Headless flow-execution API for iX Hello Customer v2. Starts a stateful conversational session against an authored flow, sends user turns into it, reads accumulated session variables, and terminates t
  name: iX Hello Customer v2 Universal Messaging API
  slug: ix-hello-customer-v2-universal-messaging-api
- description: Places outbound PSTN and SIP voice calls programmatically and runs an authored iX Hello flow on the call. Three result-delivery modes — synchronous (connection held to a 30 second gateway timeout), po
  name: iX Hello Customer v2 Outbound Calling API
  slug: ix-hello-customer-v2-outbound-calling-api
artifact_total: 7
asyncapis:
- description: ''
  name: Concentrix Ix Hello Webhooks
  slug: concentrix-ix-hello-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.concentrix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ixhello.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ixhello.com/ixhc2/integrations/outbound-calling-api-user-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ixhello.com/welcome-to-ix-hello
- group: operate
  title: ''
  type: Support
  url: https://docs.ixhello.com/ixhc2/administration/support
- group: operate
  title: ''
  type: StatusPage
  url: https://ixhellosidekick.statuspage.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/concentrix-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/concentrix-ixhello-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/concentrix-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/concentrix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/concentrix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/concentrix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/concentrix-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/concentrix-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/concentrix-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/concentrix-ix-hello-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/concentrix-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/concentrix-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/concentrix-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/concentrix-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/concentrix-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Concentrix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/concentrix
- group: company
  title: ''
  type: Newsroom
  url: https://www.concentrix.com/news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.concentrix.com/
- group: company
  title: ''
  type: Careers
  url: https://www.concentrix.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.concentrix.com/contact/
- group: company
  title: ''
  type: About
  url: https://www.concentrix.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.concentrix.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.concentrix.com/wp-content/uploads/2024/04/Concentrix-Website-Terms-of-Use.pdf
- group: start
  title: ''
  type: Login
  url: https://www.ixhello.com/
- group: company
  title: ''
  type: Blog
  url: https://www.concentrix.com/feed/
created: '2026-03-21'
description: 'Concentrix is a global technology and services company delivering customer experience management, digital transformation and technology consulting for roughly 2,000 brands. Its product line is the iX suite — iX Hello (customer- and employee-facing AI assistants), iX Hero (an agent desktop) and iX Hello Customer v2 (a flow-based conversational platform) — alongside Catalyst, its experience and engineering consultancy. iX Hello Customer v2 is the one genuinely callable surface: Concentrix publishes REST APIs on api.vnext.ixhello.com for headless flow execution, stateful conversational sessions and programmatic outbound PSTN/SIP calling, with signed webhook callbacks, documented at docs.ixhello.com. There is no OpenAPI, no SDK, no self-service signup and no published pricing — keys are issued per organization by the product team, so the API is real but sales-gated.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/concentrix.png
layout: provider
modified: '2026-09-05'
name: Concentrix
nav: Providers
network: true
overview: 'Concentrix publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Business Process Outsourcing, Consulting, Conversational AI, and Customer Experience.


  The Concentrix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Concentrix''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, engineering blog, and 25 more developer resources.'
plans:
- name: Concentrix Plans Pricing
  plan_count: 0
  slug: concentrix-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Concentrix Rate Limits
  slug: concentrix-rate-limits
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.2
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 5.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/concentrix/refs/heads/main/screenshots/concentrix-2026-06-20T174841.png
security:
- kind: authentication
  name: Concentrix Authentication
  slug: concentrix-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Concentrix Domain Security
  slug: concentrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: concentrix
tags:
- AI Agents
- Business Process Outsourcing
- Consulting
- Conversational AI
- Customer Experience
- Digital Transformation
- Enterprise Services
- Contact Center
- Voice
- Webhooks
- Fortune 500
website: https://www.concentrix.com
---
