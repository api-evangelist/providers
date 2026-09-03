---
access_model:
  confidence: high
  label: Free trial · Self-serve signup
  onboarding: self-serve
  pricing: free-trial
  public: false
  source:
  - plans
  trial: true
  try_now: true
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
  score: 7.9
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://textla.com
- group: other
  title: ''
  type: Product
  url: https://www.textla.com/product
- group: commercial
  title: ''
  type: Pricing
  url: https://www.textla.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.textla.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.textla.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.textla.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.textla.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.textla.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.textla.com/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/textla-inc-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.textla.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.textla.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.textla.com/en/collections/3372929-get-started-with-textla
- group: agent
  title: ''
  type: WellKnown
  url: well-known/textla-inc-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/textla-inc-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/textla-inc-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/textla-inc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/textla-inc-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/textla-inc-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/textla-inc-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Textla ships only an end-user web app — every spec path (/openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt) 404s on www.textla.com and app.textla.com, its own api.textla.com DNS record answers Cloudflare 1016 "origin DNS error" with nothing behind it, and the one live GraphQL endpoint (portal-api.textla.com/graphql) is the undocumented internal backend for app.textla.com with introspection disabled.
  evidence:
  - status: 404
    url: https://www.textla.com/openapi.json
  - status: 530
    url: https://api.textla.com/openapi.json
  - status: 404
    url: https://app.textla.com/llms.txt
  - status: 400
    url: https://portal-api.textla.com/graphql
  - status: 200
    url: https://auth.textla.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Textla is a business texting platform for sending bulk SMS marketing campaigns and two-way conversational messages to customers. It provides contact list segmentation, message scheduling and personalization, a shared team inbox for direct/two-way replies, contact management with CSV import, and real-time delivery verification and analytics, backed by US-based human support via phone, email, and live chat. The company promotes low per-message rates and reports 2B+ messages sent for 21K+ businesses. Textla is a Zapier partner for no-code automation; as of this profile it does not publish a public developer API, SDKs, or developer documentation.
image: https://cdn.prod.website-files.com/6621259acbeea8020086d69d/66460f7a6c72efba3794bea2_Textla%20OG%20Image.png
layout: provider
modified: '2026-08-13'
name: Textla Inc.
nav: Providers
network: true
overview: 'Textla Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, Text Messaging, Business Messaging, and Bulk SMS.


  Textla Inc.''s developer surface includes pricing, engineering blog, support, signup flow, documentation, getting-started guide, authentication, and 13 more developer resources.'
plans:
- name: Textla Inc Plans Pricing
  plan_count: 3
  slug: textla-inc-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Textla Inc Rate Limits
  slug: textla-inc-rate-limits
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 33.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/textla-inc/refs/heads/main/screenshots/textla-inc-2026-09-02T163313.png
security:
- kind: authentication
  name: Textla Inc Authentication
  slug: textla-inc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Textla Inc Domain Security
  slug: textla-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: textla-inc
tags:
- Company
- SMS
- Text Messaging
- Business Messaging
- Bulk SMS
- Communications
- Marketing
- Customer Engagement
website: https://textla.com
---
