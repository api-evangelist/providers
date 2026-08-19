---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Datasets API from A-Alpha Bio — 9 operation(s) for datasets.
  name: A-Alpha Bio Datasets API
  slug: a-alpha-bio-datasets-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: A Alpha Bio Datasets API
  slug: open-a-alpha-bio-datasets-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/a-alpha-bio-atlas-datasets-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/A-Alpha-Bio/alphabind/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/A-Alpha-Bio/alphabind/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/a-alpha-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aalphabio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atlas.aalphabio.com/
- group: start
  title: ''
  type: SignUp
  url: https://atlas.aalphabio.com/
- group: start
  title: ''
  type: Login
  url: https://atlas.aalphabio.com/
- group: company
  title: ''
  type: Blog
  url: https://aalphabio.substack.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://aalphabio.substack.com/feed
- group: company
  title: ''
  type: News
  url: https://www.aalphabio.com/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/A-Alpha-Bio
- group: operate
  title: ''
  type: Support
  url: https://www.aalphabio.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aalphabio.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aalphabio.com/privacy-notice/
- group: company
  title: ''
  type: About
  url: https://www.aalphabio.com/about/
- group: company
  title: ''
  type: Careers
  url: https://www.aalphabio.com/careers/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AAlphaBio
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/aalphabio/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/A-Alpha-Bio/alphabind
- group: auth
  title: ''
  type: Authentication
  url: authentication/a-alpha-bio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/a-alpha-bio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/a-alpha-bio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/a-alpha-bio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/a-alpha-bio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/a-alpha-bio-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/a-alpha-bio-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/a-alpha-bio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/a-alpha-bio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: A-Alpha Bio is a Seattle biotechnology company, founded in 2017 out of the University of Washington's Institute for Protein Design and Center for Synthetic Biology, that measures, predicts and engineers protein-protein interactions. Its experimental platform AlphaSeq reprograms yeast mating to quantify millions of protein-protein binding affinities in a single experiment, and its computational platform AlphaBind is a domain-specific deep-learning model trained on hundreds of millions of those affinity measurements to predict and optimize antibody-antigen binding from sequence. In July 2026 the company launched Atlas, a web platform and data ecosystem that publishes ML-ready protein interaction "Data Blocks" for licensing, custom on-demand data generation, and a quarterly-release Atlas Consortium whose founding members include GSK, Boltz, Cradle and Dyno Therapeutics. Atlas is backed by a public HTTP API — the Data Product API at api.atlas.aalphabio.com — which serves dataset
  discovery, dataset metadata and structured Data Cards anonymously, and gates CSV data, CSV schemas and structure (.cif) files behind a bearer token issued through AWS Cognito sign-in.
examples:
- key_count: 3
  name: A Alpha Bio Get Dataset Datacard Response
  slug: a-alpha-bio-get-dataset-datacard-response
- key_count: 1
  name: A Alpha Bio Get Dataset Response
  slug: a-alpha-bio-get-dataset-response
- key_count: 1
  name: A Alpha Bio List Datasets Response
  slug: a-alpha-bio-list-datasets-response
image: https://www.aalphabio.com/icons/icon-512x512.png
json_schemas:
- name: DatacardResponse
  property_count: 3
  slug: a-alpha-bio-datacard
- name: DatasetItem
  property_count: 26
  slug: a-alpha-bio-dataset-item
- name: DatasetSchemaResponse
  property_count: 2
  slug: a-alpha-bio-dataset
layout: provider
mcp_servers:
- description: ''
  name: a-alpha-bio-mcp.yml
  slug: a-alpha-bio-mcpyml
modified: '2026-08-06'
name: A-Alpha Bio
nav: Providers
network: true
overview: 'A-Alpha Bio publishes 1 API on the [APIs.io](https://apis.io/) network: Datasets API. Tagged areas include protein-interactions, biotechnology, drug-discovery, antibody-engineering, and synthetic-biology.


  A-Alpha Bio''s developer surface includes signup flow, engineering blog, product news, support, authentication, CLI, and 24 more developer resources.'
random_paper: 125
score:
  band: thin
  composite: 37.9
  delta: -1.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 65.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 39.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/a-alpha-bio/refs/heads/main/screenshots/a-alpha-bio-2026-08-07T160731.png
security:
- kind: authentication
  name: A Alpha Bio Authentication
  slug: a-alpha-bio-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: A Alpha Bio Domain Security
  slug: a-alpha-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: a-alpha-bio
tags:
- protein-interactions
- biotechnology
- drug-discovery
- antibody-engineering
- synthetic-biology
- machine-learning
- training-data
- data-licensing
- life-sciences
- datasets
- protein-design
- bioinformatics
website: https://www.aalphabio.com/
---
