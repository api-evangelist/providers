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
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Erechnung Konverter Agentic Access
  operation_count: 2
  slug: erechnung-konverter-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Validate German XRechnung and ZUGFeRD invoices via REST.
  name: E-Rechnung API
  slug: e-rechnung-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/erechnung-konverter/agentic-access/erechnung-konverter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/erechnung-konverter-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/erechnung-konverter/rules/erechnung-konverter-rules.yml
  title: ''
  type: Spectral
  url: rules/erechnung-konverter-rules.yml
- group: design
  href: https://artifacts.apis.io/erechnung-konverter/conformance/erechnung-konverter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/erechnung-konverter-conformance.yml
- group: other
  href: https://artifacts.apis.io/erechnung-konverter/hosts/erechnung-konverter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/erechnung-konverter-hosts.yml
- group: other
  href: https://artifacts.apis.io/erechnung-konverter/vendors/erechnung-konverter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/erechnung-konverter-vendors.yml
- group: auth
  href: https://artifacts.apis.io/erechnung-konverter/security/erechnung-konverter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/erechnung-konverter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://erechnung-konverter.vercel.app
- group: docs
  title: ''
  type: Documentation
  url: https://erechnung-konverter.vercel.app/e-rechnung-api
created: '2026-10-20'
description: The E‑Rechnung API provides a REST endpoint for validating German XRechnung (CII/UBL) and ZUGFeRD invoices against the official KoSIT Schematron rules. Users can POST an invoice file or PDF and receive JSON indicating validity, detected format, and detailed rule violations with IDs and German explanations. The service offers 50 free validations per month via an API key, with optional paid plans for higher volume.
layout: provider
modified: '2026-10-20'
name: E-Rechnung API (XRechnung & ZUGFeRD Validator)
nav: Providers
network: true
overview: 'E-Rechnung API (XRechnung & ZUGFeRD Validator) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Validation, German, Invoicing, and XRechnung.


  The E-Rechnung API (XRechnung & ZUGFeRD Validator) catalog on APIs.io includes 1 Spectral governance ruleset.


  E-Rechnung API (XRechnung & ZUGFeRD Validator)''s developer surface includes documentation and 7 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: E-Rechnung API (XRechnung & ZUGFeRD Validator) API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: erechnung-konverter-rules
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 9.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/erechnung-konverter/erechnung-konverter-2026-11-03T131612.png
security:
- kind: domain-security
  name: Erechnung Konverter Domain Security
  slug: erechnung-konverter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: erechnung-konverter
tags:
- Company
- Validation
- German
- Invoicing
- XRechnung
- ZUGFeRD
website: https://erechnung-konverter.vercel.app
---
