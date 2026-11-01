---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/coffee-ai/plans/coffee-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coffee-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coffee.ai/security
- group: agent
  href: https://artifacts.apis.io/coffee-ai/llms/coffee-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coffee-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/coffee-ai/a2a/coffee-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coffee-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/coffee-ai/well-known/coffee-ai-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coffee-ai-help-security.txt
- group: agent
  href: https://artifacts.apis.io/coffee-ai/well-known/coffee-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coffee-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/coffee-ai/hosts/coffee-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coffee-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/coffee-ai/vendors/coffee-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coffee-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/coffee-ai/packages/coffee-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/coffee-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/coffee-ai/packages/coffee-ai-packages.yml
  title: ''
  type: Packages
  url: packages/coffee-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.coffee.ai/security
- group: start
  title: ''
  type: GettingStarted
  url: https://help.coffee.ai/en/articles/11891330-getting-started-with-your-coffee-account
- group: auth
  href: https://artifacts.apis.io/coffee-ai/security/coffee-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coffee-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coffee-ai/security/coffee-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coffee-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coffee.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.coffee.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coffee.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coffee.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coffee.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.coffee.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.coffee.ai/blog
created: '2026-10-22'
description: Coffee is an AI-powered CRM platform that helps sales teams automate data entry, pipeline intelligence, and meeting insights. By integrating with major CRMs like Salesforce and HubSpot, Coffee reduces manual effort, improves data quality, and boosts revenue. The service offers AI agents for lead generation, automatic data entry, and real‑time pipeline analytics, targeting sales organizations seeking to streamline workflows and increase productivity.
image: https://www.coffee.ai/og-image.jpg
layout: provider
modified: '2026-10-22'
name: Coffee
nav: Providers
network: true
overview: 'Coffee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, CRM, Sales, and Automation.


  Coffee''s developer surface includes getting-started guide, documentation, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Coffee Ai Plans Pricing
  plan_count: 3
  slug: coffee-ai-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coffee Ai Domain Security
  slug: coffee-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Coffee Ai Trust Center
  slug: coffee-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: coffee-ai
tags:
- Company
- AI
- CRM
- Sales
- Automation
website: https://www.coffee.ai/
---
