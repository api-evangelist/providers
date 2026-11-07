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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Embedded PDF tools API documented on the developer portal, but no machine‑readable contract found.
  name: EasyPDF API
  slug: easypdf-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/easypdf-fr/plans/easypdf-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easypdf-fr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/easypdf-fr/conformance/easypdf-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easypdf-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/easypdf-fr/llms/easypdf-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easypdf-fr-llms.txt
- group: other
  href: https://artifacts.apis.io/easypdf-fr/hosts/easypdf-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easypdf-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/easypdf-fr/vendors/easypdf-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easypdf-fr-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.easypdf.fr/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.easypdf.fr/developers
- group: company
  title: ''
  type: Blog
  url: https://www.easypdf.fr/blog
- group: auth
  href: https://artifacts.apis.io/easypdf-fr/security/easypdf-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easypdf-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easypdf.fr/
coverage:
  checked: '2026-11-06'
  detail: Developer portal page renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.easypdf.fr/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: EasyPDF is a free AI‑powered online PDF editor offering text editing, summarisation, transformation, OCR, compression and conversion tools without sign‑up or watermarks. It supports multiple languages, integrates AI features for font recognition and data extraction, and provides a web‑based interface accessible from any browser. The service is offered by EasyPDF, a SaaS company focused on simplifying PDF workflows for individuals and businesses.
image: https://www.easypdf.fr/assets/og-image.png
layout: provider
modified: '2026-11-06'
name: EasyPDF
nav: Providers
network: true
overview: 'EasyPDF is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PDF, Artificial Intelligence, Editor, Software-as-a-Service, and Free.


  EasyPDF''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Easypdf Fr Plans Pricing
  plan_count: 3
  slug: easypdf-fr-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
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
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easypdf Fr Domain Security
  slug: easypdf-fr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: easypdf-fr
tags:
- PDF
- Artificial Intelligence
- Editor
- Software-as-a-Service
- Free
website: https://easypdf.fr/
---
