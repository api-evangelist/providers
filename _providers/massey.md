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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata-harvesting interface for Massey Research Online (MRO), the DSpace institutional repository providing free full-text access to Massey University research outputs, theses, and disse
  name: Massey Research Online OAI-PMH
  slug: mro-oai-pmh
- description: HAL/JSON REST API for Massey Research Online, running DSpace 8.3. Exposes hypermedia (HATEOAS) endpoints for communities, collections, items, bundles, bitstreams, and metadata, enabling programmatic d
  name: Massey Research Online DSpace REST API
  slug: mro-rest
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/massey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.massey.ac.nz/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/massey-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/massey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/massey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/massey-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Massey University is a public research university in New Zealand with campuses in Palmerston North, Wellington, and Auckland, ranked #239 in the QS World University Rankings 2025. Its public, machine-readable footprint is centered on Massey Research Online (MRO), the institutional repository built on DSpace 8.3, which exposes a standards-based OAI-PMH 2.0 metadata-harvesting interface and a HAL/JSON DSpace REST API. The university''s former M-API WebService is now a legacy service and is no longer available. There is no broadly published general-purpose developer portal; most institutional API access (the historical M-API) was gated behind an ITS Service Desk developer-key request.'
finops:
- name: Massey Finops
  service_category: Education
  slug: massey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/massey.png
jsonld:
- class_count: 14
  name: Massey Context
  property_count: 2
  slug: massey-context
layout: provider
modified: '2026-06-03'
name: Massey University
nav: Providers
network: true
overview: 'Massey University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Massey University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Massey Plans Pricing
  plan_count: 2
  slug: massey-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Massey Rate Limits
  slug: massey-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/massey/refs/heads/main/screenshots/massey-2026-06-20T185021.png
security:
- kind: domain-security
  name: Massey Domain Security
  slug: massey-domain-security
  summary_line: TLSv1.3 · DMARC
slug: massey
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- New Zealand
website: https://www.massey.ac.nz/
---
