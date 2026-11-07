---
access_model:
  confidence: low
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for Cavyro, all endpoints under /api/v1
  name: Cavyro API
  slug: cavyro-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/cavyro-com/plans/cavyro-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cavyro-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cavyro-com/conformance/cavyro-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cavyro-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cavyro-com/llms/cavyro-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cavyro-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/cavyro-com/well-known/cavyro-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cavyro-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cavyro-com/well-known/cavyro-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cavyro-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cavyro-com/hosts/cavyro-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cavyro-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cavyro.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.cavyro.com
- group: auth
  title: ''
  type: Security
  url: https://cavyro.com/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://cavyro.com/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cavyro.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://cavyro.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.cavyro.com/auth/sign-in
- group: company
  title: ''
  type: Blog
  url: https://cavyro.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cavyro.com/getting-started/introduction/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cavyro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cavyro.do/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cavyro.com
- group: auth
  href: https://artifacts.apis.io/cavyro-com/security/cavyro-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cavyro-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cavyro-com/security/cavyro-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cavyro-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cavyro.com/
created: '2026-11-04'
description: Cavyro provides an agentic CRM platform built on Telegram, enabling sales teams to manage deals, meetings, automations and campaigns directly within the messaging app. The solution combines real‑time communication with CRM features, offering pricing tiers from $49 to $99 per month, and integrates with MCP for extended workflow automation. It targets teams seeking a conversational sales interface and leverages Telegram’s bot ecosystem to streamline customer interactions.
image: https://cavyro.com/og.png
layout: provider
modified: '2026-11-04'
name: Cavyro
nav: Providers
network: true
overview: 'Cavyro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Telegram, Sales, Automation, and MCP.


  Cavyro''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, API reference, and 15 more developer resources.'
plans:
- name: Cavyro Com Plans Pricing
  plan_count: 3
  slug: cavyro-com-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cavyro Com Domain Security
  slug: cavyro-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cavyro Com Vulnerability Disclosure
  slug: cavyro-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cavyro-com
tags:
- CRM
- Telegram
- Sales
- Automation
- MCP
website: https://cavyro.com/
---
