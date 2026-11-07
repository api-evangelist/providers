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
  band: human-only
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
    mcp_server: false
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
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Mathematical planning aid over published compound reference data.
  name: DosePlot Agent API
  slug: doseplot-agent-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/doseplot-com/plans/doseplot-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doseplot-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/doseplot-com/conformance/doseplot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doseplot-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doseplot-com/llms/doseplot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doseplot-com-llms.txt
- group: other
  href: https://artifacts.apis.io/doseplot-com/hosts/doseplot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doseplot-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doseplot-com/vendors/doseplot-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doseplot-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doseplot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doseplot.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.doseplot.com/
- group: auth
  href: https://artifacts.apis.io/doseplot-com/security/doseplot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doseplot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doseplot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doseplot.com/features
- group: commercial
  title: ''
  type: Pricing
  url: https://doseplot.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://doseplot.com/learn
- group: operate
  title: ''
  type: Support
  url: https://doseplot.com/faq
created: '2026-11-05'
description: DosePlot provides a web-based tool to simulate blood levels for over 270 compounds including peptides, TRT, and GLP‑1 medications. Users can track dosing cycles, manage inventory, and access AI‑assisted recommendations. Free tier offers basic calculations, while premium plans add reminders, site rotation, lab integrations, and advanced analytics.
image: https://doseplot.com/opengraph-image?189c4a683035b01b
layout: provider
modified: '2026-11-05'
name: DosePlot
nav: Providers
network: true
overview: 'DosePlot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Pharmacology, Dosage Calculator, and Peptide Tracker.


  DosePlot''s developer surface includes documentation, pricing, getting-started guide, support, and 10 more developer resources.'
plans:
- name: Doseplot Com Plans Pricing
  plan_count: 4
  slug: doseplot-com-plans-pricing
random_paper: 14
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doseplot Com Domain Security
  slug: doseplot-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doseplot-com
tags:
- Health
- Pharmacology
- Dosage Calculator
- Peptide Tracker
website: https://doseplot.com/
---
