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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.monaire.ai/security
- group: agent
  href: https://artifacts.apis.io/monaire/llms/monaire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monaire-llms.txt
- group: other
  href: https://artifacts.apis.io/monaire/hosts/monaire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monaire-hosts.yml
- group: other
  href: https://artifacts.apis.io/monaire/vendors/monaire-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monaire-vendors.yml
- group: auth
  href: https://artifacts.apis.io/monaire/security/monaire-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/monaire-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/monaire/security/monaire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monaire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monaire.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.monaire.ai/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.monaire.ai/
- group: start
  title: ''
  type: Login
  url: https://app.monaire.ai/
- group: company
  title: ''
  type: Newsroom
  url: https://www.monaire.ai/press
- group: commercial
  title: ''
  type: Pricing
  url: https://www.monaire.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monaire.ai/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.monaire.ai/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.monaire.ai/
- group: operate
  title: ''
  type: Support
  url: https://support.monaire.ai/portal/en/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monaire.ai/terms-and-conditions
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.monaire.ai/
coverage:
  checked: '2026-10-29'
  detail: Docs pages return 403 when accessed via simple GET, requiring a browser render.
  evidence:
  - status: 403
    url: https://dev.monaire.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Monaire provides AI‑powered HVAC/R management for multi‑site operators, delivering real‑time equipment monitoring, runtime optimization, predictive issue detection, coordinated work orders, and energy‑saving analytics across restaurant, retail, fitness and convenience‑store portfolios. Their platform claims 10‑30% lower energy use, up to 30% repair savings and up to 95% reduced downtime, all accessible via a unified web interface and API.
image: https://framerusercontent.com/assets/zLqzsPjpKhrovQUEtAtLITkBo.webp
layout: provider
modified: '2026-10-29'
name: Monaire
nav: Providers
network: true
overview: 'Monaire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, HVAC, Energy Management, and Software-as-a-Service.


  Monaire''s developer surface includes engineering blog, pricing, support, and 15 more developer resources.'
plans:
- name: Monaire Plans Pricing
  plan_count: 0
  slug: monaire-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 30.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 56.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/monaire/monaire-2026-11-03T135818.png
security:
- kind: domain-security
  name: Monaire Domain Security
  slug: monaire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Monaire Trust Center
  slug: monaire-trust-center
  summary_line: SOC 2, ISO 27001
slug: monaire
tags:
- Company
- Artificial Intelligence
- HVAC
- Energy Management
- Software-as-a-Service
website: https://monaire.ai/
---
