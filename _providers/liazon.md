---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liazon-domain-security.yml
created: '2026-07-17'
description: Liazon was a Buffalo, New York based operator of private benefits exchanges, best known for the Bright Choices Exchange, which helped small and mid-sized employers move to a defined-contribution benefits model and let their employees shop for health, dental, vision, life, and disability coverage through an online marketplace. Backed by Bain Capital Ventures and Bessemer Venture Partners, the company was acquired by Towers Watson — now WTW — and no longer operates as an independent business. As of a 2026-07-19 probe, liazon.com publishes no A record and serves no website over HTTP or HTTPS, while the domain's MX records resolve to willistowerswatson-com.mail.protection.outlook.com and the registration is held through MarkMonitor, indicating WTW retains the domain defensively rather than operating a product on it. There is no Liazon developer portal, documentation, API reference, SDK, or public API surface to catalog. This profile is retained as an acquired-company record; enrichment
  beyond domain-level DNS evidence is not applicable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liazon.png
layout: provider
modified: '2026-07-19'
name: Liazon
nav: Providers
network: true
overview: Liazon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Employee Benefits, Insurance, and Health Insurance.
random_paper: 2
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Liazon Domain Security
  slug: liazon-domain-security
  summary_line: DMARC
slug: liazon
tags:
- Company
- Commerce
- Employee Benefits
- Insurance
- Health Insurance
- Benefits Administration
- Private Benefits Exchange
- Acquired
- WTW
---
