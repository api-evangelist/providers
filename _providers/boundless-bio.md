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
    agentic_access: derived
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Boundless Bio Agentic Access
  operation_count: 73
  slug: boundless-bio-agentic-access
  summary_line: 73 operations · 48 acting
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Boundless Bio website at boundlessbio.com: the route index of the site''s content management system, catalogued as one site surface rather than as separat'
  name: Boundless Bio Website (WordPress REST)
  slug: boundlessbio-com-website-wordpress-rest
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/boundless-bio/overlays/boundless-bio-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/boundless-bio-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/boundless-bio/security/boundless-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boundless-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boundlessbio.com/
- group: company
  title: ''
  type: About
  url: https://boundlessbio.com/why-we-are-here/
- group: other
  title: ''
  type: Technology
  url: https://boundlessbio.com/what-we-do/
- group: other
  title: ''
  type: Team
  url: https://boundlessbio.com/who-we-are/
- group: other
  title: ''
  type: Publications
  url: https://boundlessbio.com/publications/
- group: company
  title: ''
  type: Careers
  url: https://boundlessbio.com/work-with-us/
- group: operate
  title: ''
  type: Support
  url: https://boundlessbio.com/contact/
- group: company
  title: ''
  type: Investors
  url: https://investors.boundlessbio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boundlessbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boundlessbio.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boundlessbio
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/BoundlessBio
- group: build
  href: https://artifacts.apis.io/boundless-bio/packages/boundless-bio-packages.yml
  title: ''
  type: Packages
  url: packages/boundless-bio-packages.yml
- group: agent
  href: https://artifacts.apis.io/boundless-bio/llms/boundless-bio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boundless-bio-llms.txt
- group: agent
  href: https://artifacts.apis.io/boundless-bio/well-known/boundless-bio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boundless-bio-well-known.yml
- group: auth
  href: https://artifacts.apis.io/boundless-bio/authentication/boundless-bio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boundless-bio-authentication.yml
- group: design
  href: https://artifacts.apis.io/boundless-bio/conventions/boundless-bio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/boundless-bio-conventions.yml
- group: design
  href: https://artifacts.apis.io/boundless-bio/conformance/boundless-bio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boundless-bio-conformance.yml
- group: design
  href: https://artifacts.apis.io/boundless-bio/lifecycle/boundless-bio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/boundless-bio-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/boundless-bio/agentic-access/boundless-bio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boundless-bio-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/boundless-bio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/boundless-bio_stock/
- group: design
  href: https://artifacts.apis.io/boundless-bio/data-model/boundless-bio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boundless-bio-data-model.yml
- group: design
  href: https://artifacts.apis.io/boundless-bio/errors/boundless-bio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boundless-bio-problem-types.yml
created: '2026-08-08'
description: 'Boundless Bio (Nasdaq: BOLD) is a San Diego, California based clinical-stage, next-generation precision oncology company founded in 2018 to target extrachromosomal DNA (ecDNA) — circular, centromere-free DNA that carries high copy-number oncogene amplifications and is observed in roughly 17% of cancer patients, driving tumor heterogeneity and resistance to targeted therapy. Its proprietary Spyglass discovery platform, built on a suite of ecDNA+/- tumor models plus molecular analytics and imaging, identifies targets essential to ecDNA function, which the company drugs with small-molecule ecDNA-directed therapies (ecDTx). The clinical pipeline is led by BBI-940, a kinesin inhibitor targeting ecDNA segregation, in the Phase 1 KOMODO-1 trial in ER+/HER2- and TNBC-LAR breast cancer opened in February 2026, with earlier CHK1 (replication stress) and RNR (DNA assembly and repair) programs behind it; ECHO, its ecDNA diagnostic algorithm, reads ecDNA off routine clinical next-generation
  sequencing and is described by the company as the first ecDNA diagnostic used in clinical trials. Boundless Bio raised a $100M Series C co-led by Leaps by Bayer and RA Capital and listed on Nasdaq in 2024. It publishes no developer program, no product API, no SDKs and no API documentation of any kind; the only machine-readable surface on boundlessbio.com is the WordPress REST API (wp/v2), anonymously readable, which serves the corporate pages, the Leadership directory and the media library as JSON.'
image: https://boundlessbio.com/wp-content/uploads/2019/09/logo-boundless-bio.png
layout: provider
modified: '2026-08-08'
name: Boundless Bio
nav: Providers
network: true
overview: 'Boundless Bio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Oncology, Precision Medicine, and Drug Discovery.


  Boundless Bio''s developer surface includes support, authentication, and 24 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 23.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 17.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/boundless-bio/boundless-bio-2026-09-02T144938.png
security:
- kind: authentication
  name: Boundless Bio Authentication
  slug: boundless-bio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Boundless Bio Domain Security
  slug: boundless-bio-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Harvest Boundless Bio scientific posters and media
  slug: boundless-bio-harvest-scientific-media
- name: Read Boundless Bio corporate pages (the acf.modules trap)
  slug: boundless-bio-read-corporate-pages
- name: Read the Boundless Bio leadership directory
  slug: boundless-bio-read-leadership-directory
slug: boundless-bio
tags:
- Company
- Biotechnology
- Oncology
- Precision Medicine
- Drug Discovery
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Genomics
- Diagnostics
- Research
- Content
website: https://boundlessbio.com/
---
