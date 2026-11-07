---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dealerslip Com Agentic Access
  operation_count: 2
  slug: dealerslip-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://dealerslip.com
  baseurl_source: declared
  description: The Invoices API from DealerSlip — 1 operation(s) for invoices.
  name: DealerSlip Invoices API
  slug: dealerslip-com-invoices-api
- baseURL: https://dealerslip.com
  baseurl_source: declared
  description: The Schema API from DealerSlip — 1 operation(s) for schema.
  name: DealerSlip Schema API
  slug: dealerslip-com-schema-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/dealerslip-com/agentic-access/dealerslip-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dealerslip-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dealerslip-com/rules/dealerslip-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dealerslip-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/dealerslip-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dealerslip-com/errors/dealerslip-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dealerslip-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dealerslip-com/conformance/dealerslip-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealerslip-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dealerslip-com/hosts/dealerslip-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealerslip-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealerslip-com/vendors/dealerslip-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealerslip-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealerslip.com/privacy.html
- group: auth
  href: https://artifacts.apis.io/dealerslip-com/security/dealerslip-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealerslip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealerslip.com/
created: '2026-11-05'
description: 'dealerslip-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://dealerslip.com/dealerslip-demo-poster.jpg
layout: provider
modified: '2026-11-05'
name: DealerSlip
nav: Providers
network: true
overview: 'DealerSlip publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Invoices API and Schema API. Tagged areas include Invoicing, Car Sales, and UK Dealers.


  The DealerSlip catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: DealerSlip API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: dealerslip-com-rules
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 1.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dealerslip Com Domain Security
  slug: dealerslip-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: dealerslip-com-prepare-invoice
  slug: dealerslip-com-prepare-invoice
slug: dealerslip-com
tags:
- Invoicing
- Car Sales
- UK Dealers
website: https://dealerslip.com/
---
