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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Kallyope website at kallyope.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Kallyope Website (WordPress REST)
  slug: kallyope-com-website-wordpress-rest
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/kallyope/mcp/kallyope-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kallyope-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kallyope/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://kallyope.com/
- group: company
  title: ''
  type: About
  url: https://kallyope.com/about/
- group: company
  title: ''
  type: Blog
  url: https://kallyope.com/news/
- group: operate
  title: ''
  type: Support
  url: https://kallyope.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://kallyope.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://kallyope.com/partnering/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kallyope/
- group: design
  href: https://artifacts.apis.io/kallyope/conformance/kallyope-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kallyope-conformance.yml
- group: auth
  href: https://artifacts.apis.io/kallyope/security/kallyope-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kallyope-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/kallyope/well-known/kallyope-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kallyope-well-known.yml
- group: agent
  href: https://artifacts.apis.io/kallyope/llms/kallyope-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kallyope-llms.txt
- group: design
  href: https://artifacts.apis.io/kallyope/json-ld/kallyope-organization.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kallyope-organization.jsonld
- group: auth
  href: https://artifacts.apis.io/kallyope/authentication/kallyope-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kallyope-authentication.yml
- group: design
  href: https://artifacts.apis.io/kallyope/conventions/kallyope-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kallyope-conventions.yml
- group: design
  href: https://artifacts.apis.io/kallyope/errors/kallyope-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kallyope-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kallyope/data-model/kallyope-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kallyope-data-model.yml
- group: design
  href: https://artifacts.apis.io/kallyope/lifecycle/kallyope-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kallyope-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/kallyope/mcp/kallyope-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kallyope-tool-crosswalk.yml
created: '2026-08-01'
description: 'Kallyope, Inc. is a New York City clinical-stage biotechnology company, founded in 2015 by Columbia University scientists Charles Zuker, Tom Maniatis and Richard Axel, that translates the biology of the gut-brain axis into medicines. It launched with a $44M Series A and has since raised a $66M Series B, a $112M Series C and a $236M Series D co-led by Mubadala Investment Company and The Column Group, with backers including Bill Gates, Lux Capital, Polaris Partners, Casdin Capital and Alexandria Real Estate Equities. Its proprietary Klarity platform integrates single-cell sequencing, pathway circuit mapping, optogenetics and chemogenetics, proprietary human genetics, mouse and human organoid systems, and small-molecule and peptide chemistry to map the neural circuits underlying migraine and metabolism; lead candidate elismetrep, a TRPM8 blocker, is in Phase 3 development for acute migraine. Kallyope publishes no developer portal, API reference, SDKs, CLI, status page or public
  GitHub organization, and no OpenAPI, AsyncAPI, GraphQL, MCP or A2A agent-card surface was found on any host. Enrichment probing did find one real, anonymous, read-only REST surface: kallyope.com runs WordPress and exposes the WordPress REST API publicly at https://kallyope.com/wp-json, carrying the company news feed, site pages, media library and a first-party "document" content type of scientific posters, presentations and publications classified by the custom program, event, content-type and document-type taxonomies.'
image: https://kallyope.com/wp-content/uploads/2022/06/Kallyope_og.jpg
jsonld:
- class_count: 0
  name: Kallyope Organization Context
  property_count: 0
  slug: kallyope-organization
layout: provider
modified: '2026-08-01'
name: Kallyope
nav: Providers
network: true
overview: 'Kallyope is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Drug Discovery.


  The Kallyope catalog on APIs.io includes 1 JSON-LD context.


  Kallyope''s developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 8.3
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 14.6
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
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kallyope/kallyope-2026-08-07T171056.png
security:
- kind: authentication
  name: Kallyope Authentication
  slug: kallyope-authentication
  summary_line: none/http · 3 schemes
- kind: domain-security
  name: Kallyope Domain Security
  slug: kallyope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Find the published science behind a Kallyope drug program
  slug: kallyope-find-program-science
- name: Track Kallyope company news and congress activity
  slug: kallyope-track-company-news
slug: kallyope
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Drug Discovery
- Neuroscience
- Gut-Brain Axis
- Migraine
- Metabolic Disease
- Clinical Trials
- Content
website: https://kallyope.com/
---
