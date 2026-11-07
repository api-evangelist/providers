---
access_model:
  confidence: low
  gated_conflict: 'x-api-posture: private but 1 published API entry'
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the EDDA Technology website at www.eddatech.com: the route index of the site''s content management system, catalogued as one site surface rather than as separ'
  name: EDDA Technology Website (WordPress REST)
  slug: eddatech-com-website-wordpress-rest
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-edda-wordpress-rest-discovery
common:
- group: other
  href: https://artifacts.apis.io/edda/overlays/edda-wordpress-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edda-wordpress-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/edda/security/edda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eddatech.com/
- group: company
  title: ''
  type: About
  url: https://www.eddatech.com/about/
- group: other
  title: ''
  type: Products
  url: https://www.eddatech.com/products/
- group: company
  title: ''
  type: Blog
  url: https://www.eddatech.com/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.eddatech.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.eddatech.com/contact-us/
- group: other
  title: ''
  type: Events
  url: https://www.eddatech.com/events/
- group: company
  title: ''
  type: Careers
  url: https://www.eddatech.com/about/careers/
- group: other
  title: ''
  type: Team
  url: https://www.eddatech.com/about/management-team/
- group: other
  title: ''
  type: Publications
  url: https://www.eddatech.com/talks-publications/
- group: auth
  href: https://artifacts.apis.io/edda/authentication/edda-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edda-authentication.yml
- group: design
  href: https://artifacts.apis.io/edda/conventions/edda-conventions.yml
  title: ''
  type: Conventions
  url: conventions/edda-conventions.yml
- group: design
  href: https://artifacts.apis.io/edda/errors/edda-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/edda-problem-types.yml
- group: design
  href: https://artifacts.apis.io/edda/lifecycle/edda-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/edda-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/edda/conformance/edda-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edda-conformance.yml
- group: design
  href: https://artifacts.apis.io/edda/data-model/edda-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edda-data-model.yml
- group: agent
  href: https://artifacts.apis.io/edda/well-known/edda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edda-well-known.yml
- group: agent
  href: https://artifacts.apis.io/edda/mcp/edda-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/edda-mcp.yml
- group: agent
  href: https://artifacts.apis.io/edda/llms/edda-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edda-llms.txt
- group: agent
  href: https://artifacts.apis.io/edda/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: EDDA Technology, Inc. is a Princeton, New Jersey medical imaging software company behind the IQQA platform for computer-assisted radiology and surgery. IQQA delivers 3D quantitative image analysis, automated segmentation and volumetric measurement over CT and MR studies, supporting pre-surgical planning and simulation, intra-operative guidance and monitoring, post-operative follow-up evaluation, and clinical training across liver, lung, kidney and interventional oncology. Products include IQQA-BodyImaging, IQQA-Guide, IQQA-Chest, IQQA-Liver, IQQA-Liver Function, IQQA-eQMR and the IQQA-eFusion edge-AI surgical navigation system. The company is FDA cleared and CE marked under EU MDR 2017/745, and raised a US$150 million round led by SoftBank Vision Fund 2 with OrbiMed participation in April 2021. EDDA publishes no developer API for IQQA — it is regulated medical device software deployed on-premises in hospitals — so the only public API surface catalogued here is the WordPress
  REST API serving eddatech.com content.
image: https://www.eddatech.com/wp-content/uploads/2019/10/cropped-EDDA-Technology-Icon-192x192.png
layout: provider
modified: '2026-07-20'
name: EDDA Technology
nav: Providers
network: true
overview: 'EDDA Technology is listed with 1 API on the [APIs.io](https://apis.io/) network: Website (WordPress REST). Tagged areas include Company, Health Tech, Medical Imaging, Radiology, and Surgery.


  The EDDA Technology catalog on APIs.io includes 1 Spectral governance ruleset.


  EDDA Technology''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: EDDA Technology API Rules
  rule_count: 64
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 2
  slug: edda-rules
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 8.3
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 16.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/edda/edda-2026-07-25T212816.png
security:
- kind: authentication
  name: Edda Authentication
  slug: edda-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Edda Domain Security
  slug: edda-domain-security
  summary_line: TLSv1.2
skill_count: 2
skills:
- name: Explore the EDDA IQQA product catalog
  slug: edda-explore-iqqa-products
- name: Track EDDA Technology news and press releases
  slug: edda-track-news
slug: edda
tags:
- Company
- Health Tech
- Medical Imaging
- Radiology
- Surgery
- Oncology
- Artificial Intelligence
- Medical Devices
- Healthcare
- Clinical Software
website: https://www.eddatech.com/
---
