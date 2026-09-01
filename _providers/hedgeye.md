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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hedgeye-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://app.hedgeye.com
created: '2026-07-17'
description: Hedgeye Risk Management is an independent investment-research and financial-media firm founded in 2008 by Keith McCullough and headquartered in Stamford, Connecticut. Hedgeye sells subscription research and market analysis to investors across macroeconomics, sector/vertical coverage, and individual securities, delivered through daily notes, models, and its Hedgeye TV video platform, newsletters, and live events. The company is best known for its data-driven, process-oriented "GIP" (growth, inflation, policy) macro framework and its independent, no-conflicts positioning relative to traditional Wall Street sell-side research. As surfaced in the API Evangelist network, Hedgeye operates a consumer/subscriber web application at app.hedgeye.com but does not publish a public developer program, API, SDK, or machine-readable discovery surface; this profile captures the identity and domain-security posture that could be verified without authenticated access.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hedgeye.png
layout: provider
modified: '2026-07-19'
name: Hedgeye
nav: Providers
network: true
overview: Hedgeye is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Investment Research, Market Analysis, and Financial Media.
random_paper: 17
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hedgeye/refs/heads/main/screenshots/hedgeye-2026-07-25T220902.png
security:
- kind: domain-security
  name: Hedgeye Domain Security
  slug: hedgeye-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: hedgeye
tags:
- Company
- Financial-Services
- Investment Research
- Market Analysis
- Financial Media
- Macroeconomics
- Subscription
website: https://app.hedgeye.com
---
