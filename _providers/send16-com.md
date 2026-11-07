---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Email, SMS and marketing automation API as documented at Send16 developer portal.
  name: Send16 API
  slug: send16-api
artifact_total: 6
asyncapis:
- description: ''
  name: Send16 Com Webhooks
  slug: send16-com-webhooks
common:
- group: operate
  title: ''
  type: Support
  url: https://help.send16.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.send16.com/
- group: commercial
  href: https://artifacts.apis.io/send16-com/plans/send16-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/send16-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/send16-com/asyncapi/send16-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/send16-com-webhooks.yml
- group: auth
  title: ''
  type: Compliance
  url: https://send16.com/security
- group: agent
  href: https://artifacts.apis.io/send16-com/llms/send16-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/send16-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/send16-com/well-known/send16-com-ws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/send16-com-ws-security.txt
- group: auth
  href: https://artifacts.apis.io/send16-com/well-known/send16-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/send16-com-security.txt
- group: auth
  href: https://artifacts.apis.io/send16-com/well-known/send16-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/send16-com-help-security.txt
- group: auth
  href: https://artifacts.apis.io/send16-com/well-known/send16-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/send16-com-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/send16-com/well-known/send16-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/send16-com-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/send16-com/well-known/send16-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/send16-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/send16-com/well-known/send16-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/send16-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/send16-com/hosts/send16-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/send16-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/send16-com/vendors/send16-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/send16-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://send16.com/security
- group: start
  title: ''
  type: Login
  url: https://app.send16.com/login
- group: auth
  href: https://artifacts.apis.io/send16-com/security/send16-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/send16-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/send16-com/security/send16-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/send16-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/send16-com/security/send16-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/send16-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://send16.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://send16.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://send16.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://send16.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://send16.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://send16.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://send16.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://send16.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/send16/workspace
coverage:
  checked: '2026-10-31'
  detail: API documentation provides a base URL but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: error
    url: https://api.send16.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Send16 provides email, SMS, and marketing automation services powered by Claude AI. It offers a unified platform for transactional and marketing communications, featuring customizable templates, automation workflows, and AI‑assisted content creation. Plans range from a free tier with 5,000 emails per month to enterprise options, and the service includes a developer portal with API documentation, SDKs, and MCP integration.
image: https://send16.com/opengraph-image
layout: provider
modified: '2026-10-31'
name: send16-com
nav: Providers
network: true
overview: 'send16-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Marketing, Automation, Artificial Intelligence, and Software-as-a-Service.


  The send16-com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  send16-com''s developer surface includes support, engineering blog, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
plans:
- name: Send16 Com Plans Pricing
  plan_count: 4
  slug: send16-com-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 49.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/send16-com/send16-com-2026-11-03T143012.png
security:
- kind: domain-security
  name: Send16 Com Domain Security
  slug: send16-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Send16 Com Vulnerability Disclosure
  slug: send16-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Send16 Com Trust Center
  slug: send16-com-trust-center
  summary_line: SOC 2, GDPR
slug: send16-com
tags:
- Email
- Marketing
- Automation
- Artificial Intelligence
- Software-as-a-Service
website: https://send16.com/
---
