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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: auth
  title: ''
  type: DomainSecurity
  url: https://raw.githubusercontent.com/api-evangelist/vlocity/refs/heads/main/security/vlocity-domain-security.yml
created: '2026-07-17'
description: Vlocity was an industry-cloud software company founded in 2014 (by David Schmaier and team) that built vertical CRM applications on the Salesforce Platform for communications, media, energy, insurance, health, and the public sector, along with the OmniStudio low-code toolset (OmniScript, FlexCards, DataRaptor, Integration Procedures). Backed by Bessemer Venture Partners, Accel, Sutter Hill Ventures, and Salesforce Ventures, Vlocity was acquired by Salesforce in 2020 and folded into Salesforce Industries; the platform now ships as Salesforce OmniStudio. Vlocity no longer exists as an independent company and publishes no independent developer portal or public API — its domain (vlocity.com) is defunct (HTTP 503) and is now operated by Salesforce (confirmed via SPF/DMARC delegation to salesforce.com and a Salesforce, Inc. TLS certificate). Any API surface lives under Salesforce OmniStudio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vlocity.png
layout: provider
modified: '2026-08-21'
name: Vlocity
nav: Providers
network: true
overview: Vlocity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, CRM, Industry Cloud, and Low-Code.
random_paper: 1
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Vlocity Domain Security
  slug: vlocity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vlocity
tags:
- Company
- Cloud
- CRM
- Industry Cloud
- Low-Code
- Salesforce
- Acquired
---
