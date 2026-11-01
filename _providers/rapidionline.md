---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://myrapidi.com
  baseurl_source: declared
  description: 'Rapidi API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Rapidi API
  slug: rapidionline-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/rapidionline/plans/rapidionline-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rapidionline-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rapidionline/rules/rapidionline-rules.yml
  title: ''
  type: Spectral
  url: rules/rapidionline-rules.yml
- group: design
  href: https://artifacts.apis.io/rapidionline/vocabulary/rapidionline-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rapidionline-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rapidionline/conformance/rapidionline-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rapidionline-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rapidionline/llms/rapidionline-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rapidionline-llms.txt
- group: agent
  href: https://artifacts.apis.io/rapidionline/well-known/rapidionline-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rapidionline-well-known.yml
- group: other
  href: https://artifacts.apis.io/rapidionline/hosts/rapidionline-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rapidionline-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rapidionline.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rapidionline.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.rapidionline.com/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.rapidionline.com/en/product-updates/how-to-setup-transfers-in-myrapidi-a-step-by-step-guide
- group: auth
  href: https://artifacts.apis.io/rapidionline/security/rapidionline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rapidionline-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rapidionline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rapidionline.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rapidionline.com/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.rapidionline.com/en/support
- group: start
  title: ''
  type: Login
  url: https://www.myrapidi.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.myrapidi.com/mcp
  - status: 401
    url: https://www.rapidionline.com/mcp
  - status: 401
    url: https://www.myrapidi.com/mcp
  - status: 401
    url: https://api.rapidionline.com/mcp
  - status: 200
    url: https://rapidionline.com/
  reason: partner-login
  state: gated
created: '2026-10-21'
description: Rapidi provides pre‑built, no‑code integrations that keep ERP and CRM systems such as Microsoft Dynamics, Salesforce and HubSpot in sync. The platform offers a visual mapping interface, real‑time and scheduled sync options, error handling dashboards, and on‑premise connector capabilities, enabling businesses to automate data flows across multiple applications within weeks of deployment.
layout: provider
modified: '2026-10-21'
name: Rapidi
nav: Providers
network: true
overview: 'Rapidi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, ERP, CRM, and Automation.


  The Rapidi catalog on APIs.io includes 1 Spectral governance ruleset.


  Rapidi''s developer surface includes engineering blog, getting-started guide, documentation, pricing, support, and 12 more developer resources.'
plans:
- name: Rapidionline Plans Pricing
  plan_count: 4
  slug: rapidionline-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Rapidi API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: rapidionline-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 10.7
    developer_ergonomics: 28.6
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rapidionline Domain Security
  slug: rapidionline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rapidionline
tags:
- Company
- Integration
- ERP
- CRM
- Automation
website: https://rapidionline.com/
---
