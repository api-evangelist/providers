---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Access Bloomberg index constituent data, returns, analytics, and historical data for the Bloomberg Global Aggregate, US Aggregate, Euro Aggregate, and other benchmark indices via BLPAPI and Data Licen
  name: Bloomberg Index Data API
  slug: index-data-api
- description: License Bloomberg indices for use in ETFs, mutual funds, structured products, and other financial instruments. BISL provides benchmark administration services compliant with EU Benchmark Regulation (B
  name: Bloomberg Index Licensing
  slug: index-licensing
artifact_total: 15
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-index-solutions-limited-bisl-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/solution/indices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Index Solutions Limited (BISL) is the entity that administers Bloomberg's fixed income and multi-asset indices, including the Bloomberg Global Aggregate Bond Index and other benchmark indices. BISL provides index data, calculations, and licensing for asset managers and financial institutions using Bloomberg indices as benchmarks or for financial product construction.
features:
- description: Daily constituent data including weights, yields, durations, and analytics.
  name: Index Constituents
- description: Daily, monthly, and historical total and excess returns for Bloomberg indices.
  name: Index Returns
- description: Duration, spread, yield, and risk analytics for fixed income indices.
  name: Index Analytics
- description: EU BMR-compliant benchmark administration and governance.
  name: Benchmark Administration
- description: Custom index design and calculation services for institutional clients.
  name: Custom Index Construction
finops:
- name: Bloomberg Index Solutions Limited Bisl Finops
  service_category: API
  slug: bloomberg-index-solutions-limited-bisl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-index-solutions-limited-bisl.png
layout: provider
modified: '2026-08-27'
name: Bloomberg Index Solutions Limited (BISL)
nav: Providers
network: true
overview: 'Bloomberg Index Solutions Limited (BISL) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Index, Fixed Income, Benchmarks, Multi-Asset, and Index Administration.


  Bloomberg Index Solutions Limited (BISL)''s developer surface includes developer portal, documentation, support, and 4 more developer resources.'
plans:
- name: Bloomberg Index Solutions Limited Bisl Plans Pricing
  plan_count: 3
  slug: bloomberg-index-solutions-limited-bisl-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Bloomberg Index Solutions Limited Bisl Rate Limits
  slug: bloomberg-index-solutions-limited-bisl-rate-limits
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-index-solutions-limited-bisl/refs/heads/main/screenshots/bloomberg-index-solutions-limited-bisl-2026-07-25T203402.png
security:
- kind: domain-security
  name: Bloomberg Index Solutions Limited Bisl Domain Security
  slug: bloomberg-index-solutions-limited-bisl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-index-solutions-limited-bisl
tags:
- Index
- Fixed Income
- Benchmarks
- Multi-Asset
- Index Administration
- Bloomberg
use_cases:
- description: Compare portfolio performance against Bloomberg benchmark indices.
  name: Benchmark Comparison
- description: Replicate Bloomberg indices for passive investment products.
  name: ETF and Fund Replication
- description: Attribute portfolio risk relative to Bloomberg index benchmarks.
  name: Risk Attribution
- description: Use Bloomberg indices as underlying benchmarks for structured products.
  name: Product Structuring
website: https://www.bloomberg.com/professional/
---
