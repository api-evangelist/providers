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
- acting_count: 114
  human_in_the_loop: 0
  name: Cellarity Agentic Access
  operation_count: 167
  slug: cellarity-agentic-access
  summary_line: 167 operations · 114 acting
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Cellarity website at cellarity.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Cellarity Website (WordPress REST)
  slug: cellarity-com-website-wordpress-rest
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/cellarity/overlays/cellarity-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cellarity-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cellarity.com/
- group: company
  title: ''
  type: About
  url: https://cellarity.com/about/
- group: other
  title: ''
  type: Technology
  url: https://cellarity.com/platform/
- group: other
  title: ''
  type: Pipeline
  url: https://cellarity.com/pipeline/
- group: company
  title: ''
  type: News
  url: https://cellarity.com/news-events/
- group: operate
  title: ''
  type: Support
  url: https://cellarity.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://cellarity.com/life-at-cellarity/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cellarity.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cellarity.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cellarity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cellarity/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cellaritybio
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cellarity_stock/
- group: build
  href: https://artifacts.apis.io/cellarity/packages/cellarity-packages.yml
  title: ''
  type: Packages
  url: packages/cellarity-packages.yml
- group: agent
  href: https://artifacts.apis.io/cellarity/llms/cellarity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cellarity-llms.txt
- group: agent
  href: https://artifacts.apis.io/cellarity/well-known/cellarity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cellarity-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cellarity/authentication/cellarity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cellarity-authentication.yml
- group: design
  href: https://artifacts.apis.io/cellarity/conventions/cellarity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cellarity-conventions.yml
- group: design
  href: https://artifacts.apis.io/cellarity/conformance/cellarity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cellarity-conformance.yml
- group: design
  href: https://artifacts.apis.io/cellarity/lifecycle/cellarity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cellarity-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/cellarity/security/cellarity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellarity-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cellarity/agentic-access/cellarity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cellarity-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/cellarity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cellarity/data-model/cellarity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cellarity-data-model.yml
- group: design
  href: https://artifacts.apis.io/cellarity/errors/cellarity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cellarity-problem-types.yml
created: '2026-08-09'
description: Cellarity is a Somerville, Massachusetts based clinical-stage biotechnology company founded in 2017 inside Flagship Labs by Flagship Pioneering, which discovers medicines against the cell as a whole rather than a single molecular target. Its multi-omics, AI-powered platform is trained on tens of millions of single-cell transcriptomes to characterize disease as a shift in cell state and to design small molecules that course-correct that state back toward health. The company has raised roughly $294M across Series A, B and C rounds from Flagship Pioneering, BlackRock, The Baupost Group and Pictet Group, runs an active MASH collaboration with Novo Nordisk, and is advancing CLY-124 — a first-in-class globin-switching oral medicine for sickle cell disease — through a Phase 1 clinical study, alongside myelofibrosis and exploratory hematology programs. Cellarity publishes no product or developer API and runs no developer program; its only anonymously readable machine-readable surface
  is the WordPress REST API (wp/v2) that serves cellarity.com — news items, the drug-development pipeline, leadership and board profiles, event speakers, case studies, platform videos, media and site search — as JSON. Its scientific software is published as open-source research code in the github.com/Cellarity organization (DrugReflector, DILImap, MolRL), and its technical documentation site at docs.cellarity.com is a private Read the Docs Business instance behind SSO.
image: https://cellarity.com/wp-content/uploads/Logo-Icon-blue.svg
layout: provider
modified: '2026-08-09'
name: Cellarity
nav: Providers
network: true
overview: 'Cellarity is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Drug Discovery, Life Sciences, and Artificial Intelligence.


  Cellarity''s developer surface includes product news, support, authentication, and 23 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.9
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
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 17.9
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
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cellarity/cellarity-2026-09-02T145024.png
security:
- kind: authentication
  name: Cellarity Authentication
  slug: cellarity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cellarity Domain Security
  slug: cellarity-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Map Cellarity leadership, board and event speakers
  slug: cellarity-map-people
- name: Read the Cellarity drug-development pipeline
  slug: cellarity-read-pipeline
- name: Track the Cellarity newsroom
  slug: cellarity-track-newsroom
slug: cellarity
tags:
- Company
- Biotechnology
- Drug Discovery
- Life Sciences
- Artificial Intelligence
- Machine Learning
- Single Cell
- Transcriptomics
- Pharmaceuticals
- Clinical Trials
- Hematology
- Research
- Content
website: https://cellarity.com/
---
