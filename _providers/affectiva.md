---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-09-16'
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
artifact_total: 18
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/security/affectiva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affectiva-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/authentication/affectiva-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/packages/affectiva-packages.yml
  title: ''
  type: Packages
  url: packages/affectiva-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/packages/affectiva-packages.yml
  title: ''
  type: SDKs
  url: packages/affectiva-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/llms/affectiva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affectiva-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/mcp/affectiva-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/affectiva-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/conformance/affectiva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affectiva-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/errors/affectiva-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/affectiva-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/lifecycle/affectiva-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/affectiva-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/conventions/affectiva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/affectiva-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/data-model/affectiva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/affectiva-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/plans/affectiva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affectiva-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/rate-limits/affectiva-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/affectiva-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-data_collection_projects-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-data_collection_projects-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-entries-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-entries-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-event_configs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-event_configs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-event_instances-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-event_instances-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-frame_sampling_jobs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-frame_sampling_jobs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-jobs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-jobs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-labeling_job_annotations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-labeling_job_annotations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-labeling_jobs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-labeling_jobs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-labeling_tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-labeling_tasks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-representation_storages-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-representation_storages-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-representations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-representations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-video_frames-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/affectiva-eaas-video_frames-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/affectiva/refs/heads/main/overlays/affectiva-eaas-video_segments-overlay.yaml
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
overview: 'Affectiva publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, data collection projects API, Entries API, and 11 more. Tagged areas include Company, Emotion AI, Artificial Intelligence, Machine-Learning, and Computer-Vision.


  Affectiva''s developer surface includes authentication, API reference, documentation, support, engineering blog, and 31 more developer resources.'
plans:
- name: Affectiva Plans Pricing
  plan_count: 0
  slug: affectiva-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Affectiva Rate Limits
  slug: affectiva-rate-limits
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 48.4
    developer_ergonomics: 44.6
    discoverability: 74.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Affectiva Authentication
  slug: affectiva-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Affectiva Domain Security
  slug: affectiva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affectiva
tags:
- Company
- Emotion AI
- Artificial Intelligence
- Machine-Learning
- Computer-Vision
- Facial Coding
- Facial Expression Analysis
- Media Analytics
- Market Research
- Automotive
- Driver Monitoring
- Video Analysis
- Affective Computing
website: https://www.affectiva.com/
---
