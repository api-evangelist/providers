---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 8
asyncapis:
- description: ''
  name: Homebot Events Webhooks
  slug: homebot-events-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/homebot/plans/homebot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/homebot-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://homebot.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://homebot.ai/open-api
- group: docs
  title: ''
  type: APIReference
  url: https://homebot.ai/open-api
- group: docs
  title: ''
  type: Documentation
  url: https://help.homebotapp.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.homebotapp.com/en/articles/10172778-quick-start-7-easy-steps-to-set-up-your-account-for-success
- group: operate
  title: ''
  type: Support
  url: https://help.homebotapp.com
- group: company
  title: ''
  type: Blog
  url: https://homebot.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/homebotapp
- group: commercial
  title: ''
  type: Pricing
  url: https://homebot.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://customer-admin.homebotapp.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://homebot.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://homebot.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.homebot.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://homebot.ai/trust-compliance
- group: auth
  title: ''
  type: Security
  url: https://homebot.ai/trust-compliance
- group: agent
  href: https://artifacts.apis.io/homebot/llms/homebot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/homebot-llms.txt
- group: design
  href: https://artifacts.apis.io/homebot/conformance/homebot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/homebot-conformance.yml
- group: auth
  href: https://artifacts.apis.io/homebot/security/homebot-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/homebot-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/homebot/security/homebot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/homebot-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/homebot/security/homebot-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/homebot-trust-center.yml
- group: design
  href: https://artifacts.apis.io/homebot/asyncapi/homebot-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/homebot-events-webhooks.yml
created: '2026-07-17'
description: Homebot is a homeownership platform that helps loan officers, real estate agents, banks, and credit unions engage clients with personalized home-finance insights and behavioral intelligence. It sends automated monthly digests covering home value, equity, and buying power, and surfaces high-intent "Motivated Client Alerts" so professionals can reach the right client at the right time. Homebot's Open API exposes 60+ client-activity events and equity/intent signals, and it integrates with CRMs (Salesforce, Total Expert, Follow Up Boss, Sierra Interactive), video (BombBomb), and automation (Zapier) to drive retention, referrals, and repeat business. The platform serves 10,000+ customers and 13 million homeowners. Backed by 500 Global.
finops:
- has_sources: true
  method: derived
  name: Homebot Finops
  primary_unit: subscription
  service_category: ''
  slug: homebot-finops
  template: false
image: https://assets.homebotapp.com/images/homebot-icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.homebot.ai over HTTP.
  name: Homebot MCP Server
  slug: homebot
modified: '2026-07-19'
name: Homebot
nav: Providers
network: true
overview: 'Homebot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Mortgage, PropTech, and Fintech.


  The Homebot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Homebot''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Homebot Plans Pricing
  plan_count: 5
  slug: homebot-plans-pricing
- name: Homebot Price Estimates
  plan_count: 0
  slug: homebot-price-estimates
random_paper: 6
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 45.2
    discoverability: 58.3
    operational_transparency: 21.1
  previous_composite: 50.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa-cpra
    - jurisdiction: US
      standard: glba
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/homebot/homebot-2026-07-25T221335.png
security:
- kind: domain-security
  name: Homebot Domain Security
  slug: homebot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Homebot Vulnerability Disclosure
  slug: homebot-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Homebot Trust Center
  slug: homebot-trust-center
  summary_line: SOC 2 Type 2
slug: homebot
tags:
- Company
- Real Estate
- Mortgage
- PropTech
- Fintech
- Homeownership
- Client Engagement
- CRM
- Lead Generation
- Webhook
website: https://homebot.ai
---
