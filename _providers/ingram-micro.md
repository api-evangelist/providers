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
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ingram Micro Agentic Access
  operation_count: 8
  slug: ingram-micro-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.ingrammicro.com
  baseurl_source: declared
  description: Product catalog operations
  name: ingram-micro Catalog API
  slug: ingram-micro-catalog-api
- baseURL: https://api.ingrammicro.com
  baseurl_source: declared
  description: Inventory management operations
  name: ingram-micro Inventory API
  slug: ingram-micro-inventory-api
- baseURL: https://api.ingrammicro.com
  baseurl_source: declared
  description: Order management operations
  name: ingram-micro Orders API
  slug: ingram-micro-orders-api
- baseURL: https://api.ingrammicro.com
  baseurl_source: declared
  description: Pricing and availability operations
  name: ingram-micro Pricing API
  slug: ingram-micro-pricing-api
- baseURL: https://api.ingrammicro.com
  baseurl_source: declared
  description: Shipment tracking operations
  name: ingram-micro Shipments API
  slug: ingram-micro-shipments-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ingram Micro Reseller Catalog API
  slug: open-ingram-micro-catalog-api
- collection_type: open
  name: Ingram Micro Reseller Catalog Inventory API
  slug: open-ingram-micro-inventory-api
- collection_type: open
  name: Ingram Micro Reseller Catalog Orders API
  slug: open-ingram-micro-orders-api
- collection_type: open
  name: Ingram Micro Reseller Catalog Pricing API
  slug: open-ingram-micro-pricing-api
- collection_type: open
  name: Ingram Micro Reseller API
  slug: open-ingram-micro-reseller-api
- collection_type: open
  name: Ingram Micro Reseller Catalog Shipments API
  slug: open-ingram-micro-shipments-api
- collection_type: open
  name: Ingram Micro Vendor API
  slug: open-ingram-micro-vendor-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ingram-micro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ingram-micro-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ingrammicro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ingram-micro
description: © 2025 - All Rights Reserved. Ingram Micro Inc. - Privacy Policy | Terms of Use.
finops:
- name: Ingram Micro Finops
  service_category: API
  slug: ingram-micro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ingram-micro.png
layout: provider
modified: '2026-05-19'
name: Ingram Micro
nav: Providers
network: true
overview: Ingram Micro publishes 5 APIs on the [APIs.io](https://apis.io/) network, including ingram-micro Catalog API, ingram-micro Inventory API, ingram-micro Orders API, and 2 more. Tagged areas include Fortune 100.
plans:
- name: Ingram Micro Plans Pricing
  plan_count: 3
  slug: ingram-micro-plans-pricing
press:
- date: '2026-05-25'
  title: Press Releases
  url: https://ingrammicrosaudi.com/press-releases/
- date: '2026-05-25'
  title: Ingram Micro expands AI automation and digital technology
  url: https://www.digitalcommerce360.com/2026/03/05/ingram-micro-ai-automation-sales-q4-2025/
- date: '2026-05-25'
  title: 'Sales Briefing Assistant: Ingram Micro''s Agentic AI Boosts ...'
  url: https://www.channelpronetwork.com/2025/11/03/how-msps-benefit-from-sales-briefing-assistant-ingram-micros-new-agentic-ai/
- date: '2026-05-25'
  title: Press Releases | Ingram Micro United Kingdom
  url: https://uk.ingrammicro.eu/imagine-next-hub/press-releases
- date: '2026-05-25'
  title: Ingram Micro Announces Agentic AI Capabilities, Adds ...
  url: https://www.businesswire.com/news/home/20251028908276/en/Ingram-Micro-Announces-Agentic-AI-Capabilities-Adds-Googles-Gemini-Models-to-Xvantage-AI-Factory
random_paper: 3
rate_limits:
- limit_count: 5
  name: Ingram Micro Rate Limits
  slug: ingram-micro-rate-limits
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 9.5
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 23.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ingram-micro/refs/heads/main/screenshots/ingram-micro-2026-06-20T183355.png
security:
- kind: domain-security
  name: Ingram Micro Domain Security
  slug: ingram-micro-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ingram-micro
tags:
- Fortune 100
---
