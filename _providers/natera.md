---
access_model:
  confidence: low
  gated_conflict: 'x-api-posture: private but 6 published API entries'
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Natera Agentic Access
  operation_count: 2
  slug: natera-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
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
- baseURL: https://www.natera.com
  baseurl_source: spec
  description: Test order submission (modeled on the documented order workflow).
  name: Natera Orders API
  slug: natera-orders-api
- baseURL: https://www.natera.com
  baseurl_source: spec
  description: Test results retrieval (modeled on the documented results workflow).
  name: Natera Results API
  slug: natera-results-api
artifact_total: 15
collections:
- collection_type: open
  name: Natera EMR Ordering and Results Integration Orders API
  slug: open-natera-orders-api
- collection_type: open
  name: Natera EMR Ordering and Integration Orders Results API
  slug: open-natera-results-api
- collection_type: open
  name: Natera
  slug: open-natera
common:
- group: company
  title: ''
  type: Blog
  url: https://www.natera.com/company/news/
- group: other
  href: https://artifacts.apis.io/natera/capabilities/natera-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/natera-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/natera/agentic-access/natera-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/natera-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/natera/security/natera-domain-security.yml
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
  href: https://artifacts.apis.io/natera/plans/natera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/natera-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/natera/rate-limits/natera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/natera-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/natera/finops/natera-finops.yml
  title: ''
  type: FinOps
  url: finops/natera-finops.yml
created: '2026-06-20'
description: Natera is a clinical genetic testing company spanning women's health, oncology, and organ health. Rather than a public developer REST API, Natera exposes integration surfaces - Epic Aura bidirectional order/results, OncoEMR (Flatiron) and other EHR connectivity over HL7, the Constellation cloud bioinformatics platform for partner labs, and clinician/patient portals plus a provider mobile app.
finops:
- has_sources: true
  method: generated
  name: Natera Finops
  primary_unit: ''
  service_category: Healthcare and Life Sciences
  slug: natera-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/natera.png
layout: provider
modified: '2026-10-06'
name: Natera
nav: Providers
network: true
overview: 'Natera publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Orders API, Results API, and 4 more. Tagged areas include Genetic Testing, Healthcare, Diagnostics, EHR Integration, and HL7.


  The Natera catalog on APIs.io includes 1 Spectral governance ruleset.


  Natera''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Natera Plans Pricing
  plan_count: 2
  slug: natera-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Natera Rate Limits
  slug: natera-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Natera API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: natera-rules
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 43.5
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 20.5
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
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/natera/natera-2026-06-20T185957.png
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
