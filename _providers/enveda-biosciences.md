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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 78
  human_in_the_loop: 0
  name: Enveda Biosciences Agentic Access
  operation_count: 115
  slug: enveda-biosciences-agentic-access
  summary_line: 115 operations · 78 acting
api_count: 2
apis:
- description: A Model Context Protocol server endpoint advertised in the enveda.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The endpoint is live b
  name: Enveda MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Enveda website at enveda.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Enveda Website (WordPress REST)
  slug: enveda-com-website-wordpress-rest
artifact_total: 9
common:
- group: other
  href: https://artifacts.apis.io/enveda-biosciences/overlays/enveda-biosciences-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/enveda-biosciences-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://enveda.com/
- group: company
  title: ''
  type: About
  url: https://enveda.com/purpose/
- group: company
  title: ''
  type: Blog
  url: https://enveda.com/in-veda/
- group: company
  title: ''
  type: BlogRSS
  url: https://enveda.com/feed/
- group: company
  title: ''
  type: News
  url: https://enveda.com/news/
- group: company
  title: ''
  type: Press
  url: https://enveda.com/press/
- group: operate
  title: ''
  type: Support
  url: https://enveda.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://enveda.com/careers/
- group: other
  title: ''
  type: Team
  url: https://enveda.com/people/
- group: other
  title: ''
  type: Technology
  url: https://enveda.com/platform/
- group: other
  title: ''
  type: Pipeline
  url: https://enveda.com/pipeline/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enveda.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enveda.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enveda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envedabio
- group: build
  href: https://artifacts.apis.io/enveda-biosciences/packages/enveda-biosciences-packages.yml
  title: ''
  type: Packages
  url: packages/enveda-biosciences-packages.yml
- group: agent
  href: https://artifacts.apis.io/enveda-biosciences/llms/enveda-biosciences-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enveda-biosciences-llms.txt
- group: agent
  href: https://artifacts.apis.io/enveda-biosciences/well-known/enveda-biosciences-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enveda-biosciences-well-known.yml
- group: auth
  href: https://artifacts.apis.io/enveda-biosciences/authentication/enveda-biosciences-authentication.yml
  title: ''
  type: Authentication
  url: authentication/enveda-biosciences-authentication.yml
- group: design
  href: https://artifacts.apis.io/enveda-biosciences/conventions/enveda-biosciences-conventions.yml
  title: ''
  type: Conventions
  url: conventions/enveda-biosciences-conventions.yml
- group: design
  href: https://artifacts.apis.io/enveda-biosciences/conformance/enveda-biosciences-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enveda-biosciences-conformance.yml
- group: design
  href: https://artifacts.apis.io/enveda-biosciences/lifecycle/enveda-biosciences-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/enveda-biosciences-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/enveda-biosciences/security/enveda-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enveda-biosciences-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/enveda-biosciences/agentic-access/enveda-biosciences-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enveda-biosciences-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/enveda-biosciences/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/enveda-biosciences_stock/
- group: company
  title: ''
  type: Website
  url: https://www.enveda.com/
- group: design
  href: https://artifacts.apis.io/enveda-biosciences/data-model/enveda-biosciences-data-model.yml
  title: ''
  type: DataModel
  url: data-model/enveda-biosciences-data-model.yml
- group: design
  href: https://artifacts.apis.io/enveda-biosciences/errors/enveda-biosciences-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/enveda-biosciences-problem-types.yml
created: '2026-08-04'
description: Enveda (Enveda Biosciences) is a Boulder, Colorado based clinical-stage biotechnology company founded in 2019 that discovers medicines by decoding the chemistry of the natural world. It combines high-throughput mass spectrometry, metabolomics, robotics and machine learning — including PRISM, a foundation model trained on more than a billion small- molecule mass spectra — to build a searchable library of plant-derived molecules and translate them into drug candidates. Enveda has raised over $360M across Series B, C and D rounds from Premji Invest, Kinnevik, Lux Capital, Dimension and Sanofi, reached unicorn status in 2026, and runs FDA-cleared clinical programs including ENV-294 (atopic dermatitis and asthma), ENV-308 (obesity) and ENV-6946 (inflammatory bowel disease). Enveda publishes no product or developer API; the machine-readable surface on enveda.com is a published llms.txt plus the WordPress REST API (wp/v2) that serves the company newsroom, In-Veda blog, leadership profiles,
  clinical-trial site directory and media library as JSON, alongside a WordPress MCP Adapter endpoint that is present but authentication-gated. Its open science is published as research code and data in the github.com/enveda organization.
image: https://enveda.com/wp-content/uploads/2026/06/cropped-enveda-favicon.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at enveda.com over HTTP.
  name: Enveda MCP Server
  slug: mcp-adapter-default-server
modified: '2026-08-04'
name: Enveda
nav: Providers
network: true
overview: 'Enveda is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Drug Discovery, Life Sciences, and Artificial Intelligence.


  Enveda''s developer surface includes engineering blog, product news, support, authentication, and 26 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 20
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
    developer_ergonomics: 25.6
    discoverability: 68.3
    operational_transparency: 2.6
  previous_composite: 19.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: site-plugin
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
screenshot: https://apis.io/screenshots/enveda-biosciences/enveda-biosciences-2026-08-07T164935.png
security:
- kind: authentication
  name: Enveda Biosciences Authentication
  slug: enveda-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Enveda Biosciences Domain Security
  slug: enveda-biosciences-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: Read the Enveda newsroom
  slug: enveda-biosciences-read-newsroom
- name: Search enveda.com and resolve people
  slug: enveda-biosciences-search-and-people
- name: List Enveda clinical-trial sites and trial pages
  slug: enveda-biosciences-trial-sites
slug: enveda-biosciences
tags:
- Company
- Biotechnology
- Drug Discovery
- Life Sciences
- Artificial Intelligence
- Machine Learning
- Metabolomics
- Natural Products
- Pharmaceuticals
- Clinical Trials
- Research
- Content
website: https://enveda.com/
---
