---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dumpstercontrols Io Agentic Access
  operation_count: 8
  slug: dumpstercontrols-io-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://gcwyoiihrupbfqqlcurh.supabase.co/functions/v1/api-v1/v1
  baseurl_source: declared
  description: The Customers API from Dumpster Controls — 1 operation(s) for customers.
  name: Dumpster Controls Customers API
  slug: dumpstercontrols-io-customers-api
- baseURL: https://gcwyoiihrupbfqqlcurh.supabase.co/functions/v1/api-v1/v1
  baseurl_source: declared
  description: The Estimates API from Dumpster Controls — 1 operation(s) for estimates.
  name: Dumpster Controls Estimates API
  slug: dumpstercontrols-io-estimates-api
- baseURL: https://gcwyoiihrupbfqqlcurh.supabase.co/functions/v1/api-v1/v1
  baseurl_source: declared
  description: The Junk Jobs API from Dumpster Controls — 1 operation(s) for junk jobs.
  name: Dumpster Controls Junk Jobs API
  slug: dumpstercontrols-io-junk-jobs-api
- baseURL: https://gcwyoiihrupbfqqlcurh.supabase.co/functions/v1/api-v1/v1
  baseurl_source: declared
  description: The Leads API from Dumpster Controls — 1 operation(s) for leads.
  name: Dumpster Controls Leads API
  slug: dumpstercontrols-io-leads-api
- baseURL: https://gcwyoiihrupbfqqlcurh.supabase.co/functions/v1/api-v1/v1
  baseurl_source: declared
  description: The Orders API from Dumpster Controls — 2 operation(s) for orders.
  name: Dumpster Controls Orders API
  slug: dumpstercontrols-io-orders-api
- baseURL: https://gcwyoiihrupbfqqlcurh.supabase.co/functions/v1/api-v1/v1
  baseurl_source: declared
  description: The Sizes API from Dumpster Controls — 1 operation(s) for sizes.
  name: Dumpster Controls Sizes API
  slug: dumpstercontrols-io-sizes-api
artifact_total: 20
common:
- group: docs
  title: ''
  type: APIReference
  url: https://dumpstercontrols.io/llms.txt
- group: agent
  href: https://artifacts.apis.io/dumpstercontrols-io/agentic-access/dumpstercontrols-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dumpstercontrols-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dumpstercontrols-io/plans/dumpstercontrols-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dumpstercontrols-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dumpstercontrols-io/rules/dumpstercontrols-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dumpstercontrols-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dumpstercontrols-io/json-ld/dumpstercontrols-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dumpstercontrols-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dumpstercontrols-io/vocabulary/dumpstercontrols-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dumpstercontrols-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dumpstercontrols-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dumpstercontrols-io/data-model/dumpstercontrols-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dumpstercontrols-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dumpstercontrols.io/security
- group: design
  href: https://artifacts.apis.io/dumpstercontrols-io/errors/dumpstercontrols-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dumpstercontrols-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dumpstercontrols-io/conformance/dumpstercontrols-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dumpstercontrols-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dumpstercontrols-io/llms/dumpstercontrols-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dumpstercontrols-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/dumpstercontrols-io/well-known/dumpstercontrols-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dumpstercontrols-io-security.txt
- group: agent
  href: https://artifacts.apis.io/dumpstercontrols-io/well-known/dumpstercontrols-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dumpstercontrols-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dumpstercontrols-io/hosts/dumpstercontrols-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dumpstercontrols-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dumpstercontrols-io/vendors/dumpstercontrols-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dumpstercontrols-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://dumpstercontrols.io/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dumpstercontrols.io/developers
- group: auth
  href: https://artifacts.apis.io/dumpstercontrols-io/authentication/dumpstercontrols-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dumpstercontrols-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dumpstercontrols-io/security/dumpstercontrols-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dumpstercontrols-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dumpstercontrols-io/security/dumpstercontrols-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dumpstercontrols-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dumpstercontrols-io/security/dumpstercontrols-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dumpstercontrols-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dumpstercontrols.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dumpstercontrols.io/help
- group: start
  title: ''
  type: GettingStarted
  url: https://dumpstercontrols.io/help/getting-started
- group: company
  title: ''
  type: Blog
  url: https://dumpstercontrols.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dumpstercontrols.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dumpstercontrols.io/login?signup=true
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dumpstercontrols.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dumpstercontrols.io/privacy
created: '2026-11-06'
description: Dumpster Controls provides free dumpster rental and junk removal software for haulage companies across the United States and Canada. Founded in 2020 in Florida, the platform offers dispatch, online booking, driver apps for iOS and Android, invoicing, AI‑driven order creation, and a public REST API. It serves over 500 hauling firms, tracks more than 3,800 dumpsters, and includes a marketplace of 1,750 landfills. The service is free with optional card‑processing fees, and the company publishes extensive documentation, blog articles, and pricing guides.
image: https://dumpstercontrols.io/og-image.png
json_schemas:
- name: Customer
  property_count: 15
  slug: dumpstercontrols-io-customer
- name: JunkJob
  property_count: 12
  slug: dumpstercontrols-io-junk-job
- name: Lead
  property_count: 10
  slug: dumpstercontrols-io-lead
- name: Order
  property_count: 16
  slug: dumpstercontrols-io-order
- name: Size
  property_count: 7
  slug: dumpstercontrols-io-size
jsonld:
- class_count: 6
  name: Dumpstercontrols Io Context
  property_count: 47
  slug: dumpstercontrols-io-context
layout: provider
modified: '2026-11-06'
name: Dumpster Controls
nav: Providers
network: true
overview: 'Dumpster Controls publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customers API, Estimates API, Junk Jobs API, and 3 more. Tagged areas include Dumpster Controls, Waste Management, Software-as-a-Service, Logistics, and FreeSoftware.


  The Dumpster Controls catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dumpster Controls'' developer surface includes API reference, authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Dumpstercontrols Io Plans Pricing
  plan_count: 3
  slug: dumpstercontrols-io-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Dumpster Controls API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: dumpstercontrols-io-rules
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 60.1
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dumpstercontrols Io Authentication
  slug: dumpstercontrols-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dumpstercontrols Io Domain Security
  slug: dumpstercontrols-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dumpstercontrols Io Vulnerability Disclosure
  slug: dumpstercontrols-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dumpstercontrols Io Trust Center
  slug: dumpstercontrols-io-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
skill_count: 1
skills:
- name: dumpstercontrols-io-create-lead
  slug: dumpstercontrols-io-create-lead
slug: dumpstercontrols-io
tags:
- Dumpster Controls
- Waste Management
- Software-as-a-Service
- Logistics
- FreeSoftware
website: https://dumpstercontrols.io/
---
