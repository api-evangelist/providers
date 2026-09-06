---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  band: agent-aware
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
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Voyc's integration API, monitored on the public status page as "Voyc API v3" (Data Export) alongside "Voyc API" (Conversation Uploads & Reporting). The production host is api.app.voyc.ai, confirmed li
  name: Voyc API v3
  slug: voyc-api-v3
artifact_total: 8
asyncapis:
- description: ''
  name: Voyc Webhooks
  slug: voyc-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/voyc-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://voyc.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.voyc.ai/en/
- group: operate
  title: ''
  type: Support
  url: https://www.voyc.ai/contact/
- group: company
  title: ''
  type: Blog
  url: https://voyc.ai/voyc-ai-blog-articles-case-studies-and-whitepapers/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.voyc.ai/en/collections/2918818-getting-started-with-voyc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.voyc.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voyc.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voyc.ai/gdpr-privacy-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voyc-ai
- group: start
  title: ''
  type: Login
  url: https://app.voyc.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.voyc.ai/
- group: auth
  title: ''
  type: Security
  url: https://trust.voyc.ai/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/voyc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voyc-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voyc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voyc-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/voyc-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voyc-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/voyc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voyc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voyc-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/voyc-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/voyc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voyc-rate-limits.yml
coverage:
  checked: '2026-08-14'
  detail: Voyc runs a real production API at api.app.voyc.ai — /v3/organisation/ answers a live 403 not_authenticated — but ships no public reference, OpenAPI, portal or SDK anywhere; the integration documentation is handed to customers during onboarding, so the only public trace of the API is a component name on the incident.io status page.
  evidence:
  - status: 403
    url: https://api.app.voyc.ai/v3/organisation/
  - status: 404
    url: https://api.app.voyc.ai/openapi.json
  - status: 404
    url: https://voyc.ai/api/
  - status: 404
    url: https://voyc.ai/developers/
  - status: 200
    url: https://help.voyc.ai/en/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Voyc is a conversation intelligence and compliance monitoring platform for regulated industries such as financial services and insurance. The platform automatically monitors 100% of contact centre interactions using speech analytics AI, flagging high-risk cases, complaints, and vulnerable customers in near real time, automating QA review, and producing the management information firms need to evidence regulatory compliance (including FCA Consumer Duty). Calls reach Voyc from telephony platforms like Twilio, Genesys, Five9, RingCentral, Aircall, Amazon Connect, and Talkdesk via SFTP or API, and a Voyc API (v3) supports conversation uploads and data export alongside webhooks.
image: https://github.com/voyc-ai.png
layout: provider
modified: '2026-08-14'
name: Voyc
nav: Providers
network: true
overview: 'Voyc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversation Intelligence, Compliance, Call Monitoring, and Speech Analytics.


  The Voyc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Voyc''s developer surface includes documentation, support, engineering blog, getting-started guide, authentication, and 20 more developer resources.'
plans:
- name: Voyc Plans Pricing
  plan_count: 0
  slug: voyc-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Voyc Rate Limits
  slug: voyc-rate-limits
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 41.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voyc/refs/heads/main/screenshots/voyc-2026-08-17T082827.png
security:
- kind: authentication
  name: Voyc Authentication
  slug: voyc-authentication
  summary_line: cookie-session/api-token · 2 schemes
- kind: domain-security
  name: Voyc Domain Security
  slug: voyc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Voyc Vulnerability Disclosure
  slug: voyc-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Voyc Trust Center
  slug: voyc-trust-center
  summary_line: SOC 2
slug: voyc
tags:
- Company
- Conversation Intelligence
- Compliance
- Call Monitoring
- Speech Analytics
- Contact Centers
- Financial-Services
- Artificial Intelligence
website: https://voyc.ai/
---
