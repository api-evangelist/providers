---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Natera Agentic Access
  operation_count: 2
  slug: natera-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 7
apis:
- description: Connect once to the Epic Aura (Order and Results Anywhere) hub for secure, HIPAA-compliant bidirectional order and results integration, transmitting order documentation (progress notes, pathology repo
  name: Natera Epic Aura Hub Integration
  slug: natera-epic-aura-hub
- description: Natera's oncology testing portfolio integrated into Flatiron Health's cloud-based OncoEMR platform for electronic ordering and results delivery inside the cancer-care clinical workflow.
  name: Natera OncoEMR (Flatiron) Integration
  slug: natera-oncoemr-integration
- description: Cloud-based platform giving partner laboratories programmatic access to Natera's cell-free DNA bioinformatic algorithms (e.g., Panorama NIPT) to run, monitor, and troubleshoot genetic analysis jobs. B
  name: Natera Constellation Bioinformatics Platform
  slug: natera-constellation-platform
- description: Web portal (Women's Health, Oncology, Organ Health, Rare Disease) for clinicians to order kits and supplies, check testing status and results, download and share reports, and schedule genetic counselo
  name: Natera Connect Clinician Portal
  slug: natera-connect-clinician-portal
- description: Provider-facing mobile application backed by Natera's private internal services for managing orders and results on the go. No public API surface is documented for the backend.
  name: Natera Provider Mobile App
  slug: natera-provider-mobile-app
- description: Test order submission (modeled on the documented order workflow).
  name: Natera Orders API
  slug: natera-orders-api
- description: Test results retrieval (modeled on the documented results workflow).
  name: Natera Results API
  slug: natera-results-api
artifact_total: 13
collections:
- collection_type: open
  name: Natera
  slug: open-natera
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/natera-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/natera-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/natera
- group: company
  title: ''
  type: Website
  url: https://www.natera.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.natera.com/emr/
- group: commercial
  title: ''
  type: Plans
  url: plans/natera-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/natera-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/natera-finops.yml
created: '2026-06-20'
description: Natera is a clinical genetic testing company spanning women's health, oncology, and organ health. Rather than a public developer REST API, Natera exposes integration surfaces - Epic Aura bidirectional order/results, OncoEMR (Flatiron) and other EHR connectivity over HL7, the Constellation cloud bioinformatics platform for partner labs, and clinician/patient portals plus a provider mobile app.
finops:
- name: Natera Finops
  service_category: Healthcare and Life Sciences
  slug: natera-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/natera.png
layout: provider
modified: '2026-06-20'
name: Natera
nav: Providers
network: true
overview: 'Natera publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Results API. Tagged areas include Genetic Testing, Healthcare, Diagnostics, EHR Integration, and HL7.


  Natera''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Natera Plans Pricing
  plan_count: 2
  slug: natera-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 2
  name: Natera Rate Limits
  slug: natera-rate-limits
score:
  band: emerging
  composite: 26.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/natera/refs/heads/main/screenshots/natera-2026-06-20T185957.png
security:
- kind: domain-security
  name: Natera Domain Security
  slug: natera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: natera
tags:
- Genetic Testing
- Healthcare
- Diagnostics
- EHR Integration
- HL7
website: https://www.natera.com
---
