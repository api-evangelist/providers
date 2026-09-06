---
access_model:
  confidence: low
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: Route, type, taxonomy and status discovery documents.
  name: GRIN Therapeutics Discovery API
  slug: grin-therapeutics-discovery-api
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: Media library (174 attachments at harvest time).
  name: GRIN Therapeutics Media API
  slug: grin-therapeutics-media-api
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint for grintherapeutics.com URLs.
  name: GRIN Therapeutics Oembed API
  slug: grin-therapeutics-oembed-api
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: Corporate and clinical-programme pages (10 published at harvest time).
  name: GRIN Therapeutics Pages API
  slug: grin-therapeutics-pages-api
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: Blog/news post collection. Registered and reachable, but empty (X-WP-Total 0) — the News page is authored as a WPBakery page, not as posts.
  name: GRIN Therapeutics Posts API
  slug: grin-therapeutics-posts-api
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: Cross-content search across published objects.
  name: GRIN Therapeutics Search API
  slug: grin-therapeutics-search-api
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: Categories and tags. Registered by WordPress core; every term reports count 0 on this deployment.
  name: GRIN Therapeutics Taxonomy API
  slug: grin-therapeutics-taxonomy-api
- baseURL: https://grintherapeutics.com/wp-json
  baseurl_source: declared
  description: Public author records.
  name: GRIN Therapeutics Users API
  slug: grin-therapeutics-users-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GRIN Therapeutics Content Discovery API
  slug: open-grin-therapeutics-discovery-api
- collection_type: open
  name: GRIN Therapeutics Content Media API
  slug: open-grin-therapeutics-media-api
- collection_type: open
  name: GRIN Therapeutics Content Oembed API
  slug: open-grin-therapeutics-oembed-api
- collection_type: open
  name: GRIN Therapeutics Content Pages API
  slug: open-grin-therapeutics-pages-api
- collection_type: open
  name: GRIN Therapeutics Content Posts API
  slug: open-grin-therapeutics-posts-api
- collection_type: open
  name: GRIN Therapeutics Content Search API
  slug: open-grin-therapeutics-search-api
- collection_type: open
  name: GRIN Therapeutics Content Taxonomy API
  slug: open-grin-therapeutics-taxonomy-api
- collection_type: open
  name: GRIN Therapeutics Content Users API
  slug: open-grin-therapeutics-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/grin-therapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://grintherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://grintherapeutics.com/about-grin-therapeutics/
- group: other
  title: ''
  type: Science
  url: https://grintherapeutics.com/our-science/
- group: other
  title: ''
  type: DiseaseState
  url: https://grintherapeutics.com/disease-state/
- group: other
  title: ''
  type: PatientResources
  url: https://grintherapeutics.com/resources-for-patients-and-caregivers/
- group: company
  title: ''
  type: News
  url: https://grintherapeutics.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://grintherapeutics.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://grintherapeutics.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://grintherapeutics.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://grintherapeutics.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grintherapeutics.com/privacy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://grintherapeutics.com/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grin-therapeutics-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/GRIN_tx
- group: other
  title: ''
  type: ParentCompany
  url: https://neurvati.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/grin-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/grin-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/grin-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/grin-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/grin-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/grin-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/grin-therapeutics-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/grin-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grin-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/grin-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: GRIN Therapeutics, Inc. is a clinical-stage biotechnology company dedicated to the research and development of precision therapeutics for pediatric neurodevelopmental disorders caused by NMDA receptor dysfunction. It is an affiliate of Neurvati Neurosciences, a Blackstone Life Sciences portfolio company, and traces its founding to Dr. Pierandrea Muglia's attendance at the 2019 CFERV Conference on GRIN Variants at Emory University. Its lead investigational asset is radiprodil, an orally bioavailable selective negative allosteric modulator of the GluN2B subunit of the NMDA receptor, designed to fine-tune dysregulated receptor activity rather than fully block the channel. Radiprodil is in development for GRIN-related neurodevelopmental disorder (GRIN-NDD) arising from gain-of-function variants in GRIN1, GRIN2A, GRIN2B and GRIN2D, and for tuberous sclerosis complex (TSC) and focal cortical dysplasia (FCD) type II. The clinical programme comprises the completed Phase 1b/2a Honeycomb
  trial, the enrolling global Phase 3 Beeline registrational trial, the Phase 1b/2a Astroscape trial in TSC and FCD type II, and a GRIN-NDD natural history study; radiprodil carries FDA Breakthrough Therapy, Orphan Drug and Rare Pediatric Disease designations and EMA PRIME and Orphan Drug designations. In May 2025 GRIN Therapeutics entered an exclusive collaboration with Angelini Pharma to develop and commercialise radiprodil outside North America. GRIN Therapeutics runs no developer program and publishes no product API, no developer portal and no API documentation; the only machine-readable surface reachable without credentials is the WordPress REST content API behind grintherapeutics.com, catalogued here.
image: https://grintherapeutics.com/wp-content/uploads/2023/11/neurvati_grin_inline_fullcolor_rgb_6in@72ppi.png
layout: provider
modified: '2026-08-04'
name: GRIN Therapeutics
nav: Providers
network: true
overview: 'GRIN Therapeutics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Media API, Oembed API, and 5 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Neuroscience, and Rare Disease.


  GRIN Therapeutics'' developer surface includes product news, support, authentication, and 24 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 4.5
    contract_quality: 49.5
    developer_ergonomics: 18.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 30.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grin-therapeutics/refs/heads/main/screenshots/grin-therapeutics-2026-08-07T165843.png
security:
- kind: authentication
  name: Grin Therapeutics Authentication
  slug: grin-therapeutics-authentication
  summary_line: none/http · 3 schemes
- kind: domain-security
  name: Grin Therapeutics Domain Security
  slug: grin-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grin-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Neuroscience
- Rare Disease
- Precision Medicine
- Clinical Trials
- Pediatrics
- Epilepsy
- Life Sciences
- content-api
website: https://grintherapeutics.com/
---
