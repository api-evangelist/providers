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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: REST API and Python SDK for programmatically managing annotation projects, datasets, ontologies, labels, and workflows within the Encord Annotate platform. Supports creating and retrieving projects an
  name: Encord Annotate API
  slug: encord-annotate-api
- description: API for the Encord Active module, which provides model evaluation, data curation, and active learning capabilities. Allows importing model predictions, computing quality metrics, running embedding-bas
  name: Encord Active API
  slug: encord-active-api
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/encord-team/encord-client-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/encord-team/encord-client-python/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/encord-team/encord-client-python/blob/master/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/encord-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encord-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://encord.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.encord.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/encord-team
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encord-team
- group: other
  title: ''
  type: X
  url: https://x.com/encord_team
- group: company
  title: ''
  type: Blog
  url: https://encord.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://encord.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.encord.com/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/encord/refs/heads/main/plans/encord-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/encord/refs/heads/main/rate-limits/encord-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/encord/refs/heads/main/finops/encord-finops.yml
- group: company
  title: ''
  type: BlogCatalog
  url: https://raw.githubusercontent.com/api-evangelist/encord/refs/heads/main/blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/encord/refs/heads/main/json-ld/encord-context.jsonld
created: 2026-06-12
description: Encord is a computer vision data labeling and model evaluation platform that provides tools and APIs for managing datasets, annotation tasks, labels, and quality workflows at scale. The platform supports multimodal data including images, video, audio, DICOM, point clouds, and text. Encord exposes a REST API and a Python SDK (encord) for programmatically managing projects, datasets, ontologies, storage, and automated labeling workflows. Authentication is handled via SSH private key or service account credentials, with separate US and UK API endpoints available. Encord is used by AI teams in healthcare, autonomous systems, and other industries to accelerate model development by streamlining data curation, annotation, and evaluation pipelines.
finops:
- name: Encord Finops
  service_category: ''
  slug: encord-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encord.png
jsonld:
- class_count: 0
  name: Encord Context
  property_count: 0
  slug: encord-context
layout: provider
modified: 2026-06-12
name: Encord
nav: Providers
network: true
overview: 'Encord publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Computer-Vision, Data Labeling, Annotation, Machine-Learning, and Model Evaluation.


  The Encord catalog on APIs.io includes 1 JSON-LD context.


  Encord''s developer surface includes documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Encord Plans Pricing
  plan_count: 3
  slug: encord-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Encord Rate Limits
  slug: encord-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 65.8
  open_source:
    applies: true
    score: 25.0
  previous_composite: 31.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encord/refs/heads/main/screenshots/encord-2026-06-20T180648.png
security:
- kind: domain-security
  name: Encord Domain Security
  slug: encord-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Encord Trust Center
  slug: encord-trust-center
  summary_line: SOC 2, HIPAA
slug: encord
tags:
- Computer-Vision
- Data Labeling
- Annotation
- Machine-Learning
- Model Evaluation
- Dataset Management
- Artificial Intelligence
- Image Annotation
- Video Annotation
- DICOM
- Active Learning
- Quality Assurance
website: https://encord.com/
---
