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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for the Leiden University Scholarly Publications repository, an Islandora-based institutional repository providing open access to PhD theses, articles, journal
  name: Scholarly Publications OAI-PMH
  slug: scholarly-oai
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leiden-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.universiteitleiden.nl/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/LeidenUniversityLibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/leiden-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/leiden-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leiden-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leiden-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Leiden University (Universiteit Leiden) is the oldest university in the Netherlands, founded in 1575, and ranks #141 in the QS World University Rankings 2025. Its public, machine-accessible developer footprint is modest and centered on its libraries rather than a central developer portal. Leiden University Libraries operates an OAI-PMH metadata harvesting endpoint for its Scholarly Publications repository and maintains an active open-source GitHub organization (LeidenUniversityLibrary) with library, Islandora, and IIIF tooling. There is no centrally documented public REST API program; most institutional and student systems are gated behind SSO.'
finops:
- name: Leiden Finops
  service_category: Education
  slug: leiden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leiden.png
jsonld:
- class_count: 22
  name: Leiden Context
  property_count: 5
  slug: leiden-context
layout: provider
modified: '2026-06-03'
name: Leiden University
nav: Providers
network: true
overview: 'Leiden University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Netherlands, and Library.


  The Leiden University catalog on APIs.io includes 1 JSON-LD context.


  Leiden University''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Leiden Plans Pricing
  plan_count: 2
  slug: leiden-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Leiden Rate Limits
  slug: leiden-rate-limits
score:
  band: emerging
  composite: 23.6
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
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leiden/refs/heads/main/screenshots/leiden-2026-06-20T184415.png
security:
- kind: domain-security
  name: Leiden Domain Security
  slug: leiden-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: leiden
tags:
- Education
- Higher Education
- University
- Netherlands
- Library
- Open Access
- OAI-PMH
- Research
website: https://www.universiteitleiden.nl/en
---
