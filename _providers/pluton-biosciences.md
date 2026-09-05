---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
- description: Internal high-throughput microbial discovery platform that screens soil microbiomes and uses computational analysis to identify naturally occurring microbial consortia for agriculture and carbon seque
  name: Pluton Discovery Platform
  slug: discovery-platform
- description: Sun-powered, soil-surface biological nutrient delivery system in which photosynthetic microbial consortia fix atmospheric nitrogen and mobilize phosphorus. Field-validated and in active development; n
  name: Biological Nitrogen System
  slug: biological-nitrogen-system
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pluton-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plutonbio.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.plutonbio.com/contact-us
- group: other
  title: ''
  type: Email
  url: mailto:contact@plutonbio.com
- group: agent
  title: ''
  type: LlmsText
  url: https://plutonbio.com/llms.txt
created: '2026-05-23'
description: 'Pluton Biosciences is a microbial discovery company that uses a proprietary Discovery Platform - high-throughput soil microbiome screening combined with computational analysis - to find naturally occurring microbial consortia for agriculture and carbon sequestration. Its lead product is a Biological Nitrogen System: photosynthetic microbial consortia that operate at the soil surface to fix atmospheric nitrogen and mobilize phosphorus. Pluton is a research-and-product company, not an API company; it has no public developer portal. Partnership and licensing inquiries are handled directly.'
finops:
- name: Pluton Biosciences Finops
  service_category: API
  slug: pluton-biosciences-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pluton-biosciences.png
layout: provider
modified: '2026-05-23'
name: Pluton Biosciences
nav: Providers
network: true
overview: Pluton Biosciences publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Biotech, Microbials, and Soil Carbon.
plans:
- name: Pluton Biosciences Plans Pricing
  plan_count: 1
  slug: pluton-biosciences-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Pluton Biosciences Rate Limits
  slug: pluton-biosciences-rate-limits
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pluton-biosciences/refs/heads/main/screenshots/pluton-biosciences-2026-06-20T191815.png
security:
- kind: domain-security
  name: Pluton Biosciences Domain Security
  slug: pluton-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pluton-biosciences
tags:
- Agriculture
- AgTech
- Biotech
- Microbials
- Soil Carbon
- Discovery Platform
website: https://www.plutonbio.com/
---
