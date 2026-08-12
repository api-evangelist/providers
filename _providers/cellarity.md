---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 114
  human_in_the_loop: 0
  name: Cellarity Agentic Access
  operation_count: 167
  slug: cellarity-agentic-access
  summary_line: 167 operations · 114 acting
api_count: 16
apis:
- description: The Case Studies API from Cellarity — 4 operation(s) for case studies.
  name: Cellarity Case Studies API
  slug: cellarity-case-studies-api
- description: The Comments API from Cellarity — 2 operation(s) for comments.
  name: Cellarity Comments API
  slug: cellarity-comments-api
- description: The Discovery API from Cellarity — 6 operation(s) for discovery.
  name: Cellarity Discovery API
  slug: cellarity-discovery-api
- description: The Events API from Cellarity — 2 operation(s) for events.
  name: Cellarity Events API
  slug: cellarity-events-api
- description: The Media API from Cellarity — 4 operation(s) for media.
  name: Cellarity Media API
  slug: cellarity-media-api
- description: The News API from Cellarity — 2 operation(s) for news.
  name: Cellarity News API
  slug: cellarity-news-api
- description: The Pages API from Cellarity — 2 operation(s) for pages.
  name: Cellarity Pages API
  slug: cellarity-pages-api
- description: The People API from Cellarity — 4 operation(s) for people.
  name: Cellarity People API
  slug: cellarity-people-api
- description: The Pipeline API from Cellarity — 4 operation(s) for pipeline.
  name: Cellarity Pipeline API
  slug: cellarity-pipeline-api
- description: The Posts API from Cellarity — 2 operation(s) for posts.
  name: Cellarity Posts API
  slug: cellarity-posts-api
- description: The Projects API from Cellarity — 6 operation(s) for projects.
  name: Cellarity Projects API
  slug: cellarity-projects-api
- description: The Search API from Cellarity — 1 operation(s) for search.
  name: Cellarity Search API
  slug: cellarity-search-api
- description: The Settings API from Cellarity — 1 operation(s) for settings.
  name: Cellarity Settings API
  slug: cellarity-settings-api
- description: The Taxonomy API from Cellarity — 8 operation(s) for taxonomy.
  name: Cellarity Taxonomy API
  slug: cellarity-taxonomy-api
- description: The Users API from Cellarity — 3 operation(s) for users.
  name: Cellarity Users API
  slug: cellarity-users-api
- description: The Video API from Cellarity — 4 operation(s) for video.
  name: Cellarity Video API
  slug: cellarity-video-api
artifact_total: 19
common:
- group: other
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
  title: ''
  type: Packages
  url: packages/cellarity-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cellarity-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cellarity-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cellarity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cellarity-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cellarity-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cellarity-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cellarity-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cellarity-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: Cellarity is a Somerville, Massachusetts based clinical-stage biotechnology company founded in 2017 inside Flagship Labs by Flagship Pioneering, which discovers medicines against the cell as a whole rather than a single molecular target. Its multi-omics, AI-powered platform is trained on tens of millions of single-cell transcriptomes to characterize disease as a shift in cell state and to design small molecules that course-correct that state back toward health. The company has raised roughly $294M across Series A, B and C rounds from Flagship Pioneering, BlackRock, The Baupost Group and Pictet Group, runs an active MASH collaboration with Novo Nordisk, and is advancing CLY-124 — a first-in-class globin-switching oral medicine for sickle cell disease — through a Phase 1 clinical study, alongside myelofibrosis and exploratory hematology programs. Cellarity publishes no product or developer API and runs no developer program; its only anonymously readable machine-readable surface
  is the WordPress REST API (wp/v2) that serves cellarity.com — news items, the drug-development pipeline, leadership and board profiles, event speakers, case studies, platform videos, media and site search — as JSON. Its scientific software is published as open-source research code in the github.com/Cellarity organization (DrugReflector, DILImap, MolRL), and its technical documentation site at docs.cellarity.com is a private Read the Docs Business instance behind SSO.
image: https://cellarity.com/wp-content/uploads/Logo-Icon-blue.svg
layout: provider
modified: '2026-08-09'
name: Cellarity
nav: Providers
network: true
overview: 'Cellarity publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Case Studies API, Comments API, Discovery API, and 13 more. Tagged areas include Company, Biotechnology, Drug Discovery, Life Sciences, and Artificial Intelligence.


  Cellarity''s developer surface includes product news, support, authentication, and 21 more developer resources.'
random_paper: 41
score:
  band: emerging
  composite: 22.9
  delta: -10.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 14.5
    developer_ergonomics: 16.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
security:
- kind: authentication
  name: Cellarity Authentication
  slug: cellarity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cellarity Domain Security
  slug: cellarity-domain-security
  summary_line: TLSv1.3 · DMARC
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
