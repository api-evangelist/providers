---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
api_count: 13
apis:
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The annotations API from Affectiva — 2 operation(s) for annotations.
  name: Affectiva Annotations API
  slug: affectiva-annotations-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The data collection projects API from Affectiva — 2 operation(s) for data collection projects.
  name: Affectiva data collection projects API
  slug: affectiva-data-collection-projects-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The entries API from Affectiva — 3 operation(s) for entries.
  name: Affectiva Entries API
  slug: affectiva-entries-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The event configs API from Affectiva — 2 operation(s) for event configs.
  name: Affectiva event configs API
  slug: affectiva-event-configs-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The event instances API from Affectiva — 2 operation(s) for event instances.
  name: Affectiva event instances API
  slug: affectiva-event-instances-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The frame sampling jobs API from Affectiva — 1 operation(s) for frame sampling jobs.
  name: Affectiva frame sampling jobs API
  slug: affectiva-frame-sampling-jobs-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: Everything about your jobss
  name: Affectiva Jobs API
  slug: affectiva-jobs-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The labeling_job_annotations API from Affectiva — 1 operation(s) for labeling_job_annotations.
  name: Affectiva Labeling Job Annotations API
  slug: affectiva-labeling-job-annotations-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The labeling_jobs API from Affectiva — 2 operation(s) for labeling_jobs.
  name: Affectiva Labeling Jobs API
  slug: affectiva-labeling-jobs-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The labeling_tasks API from Affectiva — 2 operation(s) for labeling_tasks.
  name: Affectiva Labeling Tasks API
  slug: affectiva-labeling-tasks-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The representation storages API from Affectiva — 2 operation(s) for representation storages.
  name: Affectiva representation storages API
  slug: affectiva-representation-storages-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The representations API from Affectiva — 3 operation(s) for representations.
  name: Affectiva Representations API
  slug: affectiva-representations-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The video_frames API from Affectiva — 2 operation(s) for video_frames.
  name: Affectiva Video Frames API
  slug: affectiva-video-frames-api
- baseURL: https://index.affectiva.com
  baseurl_source: declared
  description: The video_segments API from Affectiva — 2 operation(s) for video_segments.
  name: Affectiva Video Segments API
  slug: affectiva-video-segments-api
artifact_total: 21
common:
- group: auth
  href: https://artifacts.apis.io/affectiva/security/affectiva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affectiva-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/affectiva/authentication/affectiva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/affectiva-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.affectiva.com/
- group: docs
  title: ''
  type: APIReference
  url: https://index.affectiva.com/swagger/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://imotions.com/support/document-library/affectiva-for-facial-expression-analysis/
- group: start
  title: ''
  type: Login
  url: https://index.affectiva.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: https://www.affectiva.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://blog.affectiva.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/affectiva
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.affectiva.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affectiva.com/privacy-policy/
- group: build
  href: https://artifacts.apis.io/affectiva/packages/affectiva-packages.yml
  title: ''
  type: Packages
  url: packages/affectiva-packages.yml
- group: build
  href: https://artifacts.apis.io/affectiva/packages/affectiva-packages.yml
  title: ''
  type: SDKs
  url: packages/affectiva-packages.yml
- group: agent
  href: https://artifacts.apis.io/affectiva/llms/affectiva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affectiva-llms.txt
- group: agent
  href: https://artifacts.apis.io/affectiva/mcp/affectiva-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/affectiva-mcp.yml
- group: design
  href: https://artifacts.apis.io/affectiva/conformance/affectiva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affectiva-conformance.yml
- group: design
  href: https://artifacts.apis.io/affectiva/errors/affectiva-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/affectiva-problem-types.yml
- group: design
  href: https://artifacts.apis.io/affectiva/lifecycle/affectiva-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/affectiva-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/affectiva/conventions/affectiva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/affectiva-conventions.yml
- group: design
  href: https://artifacts.apis.io/affectiva/data-model/affectiva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/affectiva-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/affectiva/plans/affectiva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affectiva-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/affectiva/rate-limits/affectiva-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/affectiva-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/affectiva/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-data_collection_projects-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-data_collection_projects-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-entries-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-entries-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-event_configs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-event_configs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-event_instances-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-event_instances-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-frame_sampling_jobs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-frame_sampling_jobs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-jobs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-jobs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-labeling_job_annotations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-labeling_job_annotations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-labeling_jobs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-labeling_jobs-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-labeling_tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-labeling_tasks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-representation_storages-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-representation_storages-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-representations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-representations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-video_frames-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-video_frames-overlay.yaml
- group: other
  href: https://artifacts.apis.io/affectiva/overlays/affectiva-eaas-video_segments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-video_segments-overlay.yaml
created: '2026-09-12'
description: Affectiva is an Emotion AI company founded out of the MIT Media Lab and headquartered in Boston, Massachusetts. Its AFFDEX science analyzes spontaneous facial expressions and speech to measure emotion, attention and cognitive state, trained on what the company describes as the world's largest emotion data set — 17.4M face videos and 8B facial frames gathered across 90 countries over 18 years. The technology is sold into media analytics (ad testing, entertainment content testing, qualitative research), in-cabin automotive sensing for driver and occupant monitoring, and academic behavioral research. Affectiva was acquired by Smart Eye AB in 2021 and its commercial product line has since been folded into the iMotions brand. Its developer surface is the Affectiva Facial Coding API — a cloud "EaaS" (Emotion as a Service) platform documented by thirteen Swagger 2.0 contracts at index.affectiva.com/swagger, plus the browser-side affdex.js Emotion SDK distributed from the company CDN
  and an Automotive SDK available on request.
image: https://www.affectiva.com/wp-content/uploads/2024/01/SoMe-Graphics-Zeus-Announcement.png
layout: provider
modified: '2026-09-12'
name: Affectiva
nav: Providers
network: true
overview: 'Affectiva publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Annotations API, data collection projects API, Entries API, and 11 more. Tagged areas include Company, Emotion AI, Artificial Intelligence, Machine Learning, and Computer Vision.


  The Affectiva catalog on APIs.io includes 1 Spectral governance ruleset.


  Affectiva''s developer surface includes authentication, API reference, documentation, support, engineering blog, and 31 more developer resources.'
plans:
- name: Affectiva Plans Pricing
  plan_count: 0
  slug: affectiva-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Affectiva Rate Limits
  slug: affectiva-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Affectiva API Rules
  rule_count: 45
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 5
  slug: affectiva-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 43.9
    developer_ergonomics: 44.6
    discoverability: 71.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/affectiva/affectiva-2026-10-11T093014.png
security:
- kind: authentication
  name: Affectiva Authentication
  slug: affectiva-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Affectiva Domain Security
  slug: affectiva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: affectiva-analyze-video
  slug: affectiva-analyze-video
- name: affectiva-label-video-data
  slug: affectiva-label-video-data
slug: affectiva
tags:
- Company
- Emotion AI
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Facial Coding
- Facial Expression Analysis
- Media Analytics
- Market Research
- Automotive
- Driver Monitoring
- Video Analysis
website: https://www.affectiva.com/
---
