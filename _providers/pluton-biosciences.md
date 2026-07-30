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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
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
random_paper: 74
rate_limits:
- limit_count: 2
  name: Pluton Biosciences Rate Limits
  slug: pluton-biosciences-rate-limits
score:
  band: emerging
  composite: 15.4
  delta: -2.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.8
  schema_version: 0.6
  scored_at: '2026-07-28'
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
