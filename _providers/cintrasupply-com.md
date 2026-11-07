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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cintrasupply Com Agentic Access
  operation_count: 1
  slug: cintrasupply-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Submit a bill of materials to receive a priced quote via email.
  name: Quote Desk
  slug: quote-desk
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/cintrasupply-com/agentic-access/cintrasupply-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cintrasupply-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cintrasupply-com/rules/cintrasupply-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cintrasupply-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cintrasupply-com/errors/cintrasupply-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cintrasupply-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cintrasupply-com/conformance/cintrasupply-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cintrasupply-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cintrasupply-com/llms/cintrasupply-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cintrasupply-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cintrasupply-com/hosts/cintrasupply-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cintrasupply-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cintrasupply-com/vendors/cintrasupply-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cintrasupply-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cintrasupply.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cintrasupply.com/privacy
- group: auth
  href: https://artifacts.apis.io/cintrasupply-com/security/cintrasupply-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cintrasupply-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cintrasupply.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cintrasupply.com/journal
- group: operate
  title: ''
  type: Contact
  url: https://www.cintrasupply.com/contact
- group: other
  title: ''
  type: Government
  url: https://www.cintrasupply.com/government
created: '2026-11-03'
description: Cintra Supply is a US wholesale distributor of industrial and operational supplies, offering multi‑category B2B products such as MRO, janitorial, packaging, safety, electrical, datacom, IT hardware, batteries, backup power, and HVAC. They provide quotes in minutes with nationwide delivery and no minimum order requirements, serving customers across the United States.
image: https://www.cintrasupply.com/static/og-card.png
layout: provider
modified: '2026-11-03'
name: Cintra Supply
nav: Providers
network: true
overview: 'Cintra Supply is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wholesale, Industrial Supplies, B2B, and Quote Service.


  The Cintra Supply catalog on APIs.io includes 1 Spectral governance ruleset.


  Cintra Supply''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Cintra Supply API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: cintrasupply-com-rules
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
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
  name: Cintrasupply Com Domain Security
  slug: cintrasupply-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cintrasupply-com
tags:
- Company
- Wholesale
- Industrial Supplies
- B2B
- Quote Service
website: https://www.cintrasupply.com/
---
