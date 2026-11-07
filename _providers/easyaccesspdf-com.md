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
  band: agent-aware
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides PDF accessibility services; see pricing page for details.
  name: EasyAccessPDF API
  slug: easyaccesspdf-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/easyaccesspdf-com/plans/easyaccesspdf-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easyaccesspdf-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/easyaccesspdf-com/llms/easyaccesspdf-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easyaccesspdf-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/easyaccesspdf-com/well-known/easyaccesspdf-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easyaccesspdf-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/easyaccesspdf-com/hosts/easyaccesspdf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easyaccesspdf-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/easyaccesspdf-com/vendors/easyaccesspdf-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easyaccesspdf-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/easyaccesspdf-com/security/easyaccesspdf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easyaccesspdf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easyaccesspdf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://easyaccesspdf.com/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://easyaccesspdf.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://easyaccesspdf.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easyaccesspdf.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easyaccesspdf.com/privacy-policy/
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on api.easyaccesspdf.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.easyaccesspdf.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: EasyAccessPDF provides an automated PDF accessibility service that tags PDFs for screen readers and validates them against PDF/UA (ISO 14289) using the open‑source veraPDF validator. It offers a flat‑rate per‑document pricing model, free compliance checks, and EU‑based processing, aiming to help businesses meet Section 508, ADA Title II/III, and the European Accessibility Act requirements. The platform also includes AI tools for diagram generation and various PDF conversion utilities, with membership plans for unlimited usage.
image: https://easyaccesspdf.com/wp-content/uploads/2026/09/eap-og-default.png
layout: provider
modified: '2026-11-06'
name: EasyAccessPDF
nav: Providers
network: true
overview: 'EasyAccessPDF is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PDF Accessibility, PDF Tagging, Compliance, Section 508, and ADA.


  EasyAccessPDF''s developer surface includes documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Easyaccesspdf Com Plans Pricing
  plan_count: 7
  slug: easyaccesspdf-com-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easyaccesspdf Com Domain Security
  slug: easyaccesspdf-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easyaccesspdf-com
tags:
- PDF Accessibility
- PDF Tagging
- Compliance
- Section 508
- ADA
- European Accessibility Act
- PDF/UA
website: https://easyaccesspdf.com/
---
