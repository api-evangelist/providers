---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - finops
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The BRICK ontology v1.4.4 defines a standardized vocabulary of building system concepts, relationships, and data model for smart building analytics. Available as RDF/OWL files, BRICK describes sensors
  name: BRICK Ontology
  slug: ontology
- baseURL: https://brickschema.org/schema/
  baseurl_source: declared
  description: The Actuation API from BRICK Schema — 1 operation(s) for actuation.
  name: BRICK Schema Actuation API
  slug: brick-actuation-api
- baseURL: https://brickschema.org/schema/
  baseurl_source: declared
  description: The Auth API from BRICK Schema — 5 operation(s) for auth.
  name: BRICK Schema Auth API
  slug: brick-auth-api
- baseURL: https://brickschema.org/schema/
  baseurl_source: declared
  description: The Brickapi API from BRICK Schema — 1 operation(s) for brickapi.
  name: BRICK Schema Brickapi API
  slug: brick-brickapi-api
- baseURL: https://brickschema.org/schema/
  baseurl_source: declared
  description: The Data API from BRICK Schema — 3 operation(s) for data.
  name: BRICK Schema Data API
  slug: brick-data-api
- baseURL: https://brickschema.org/schema/
  baseurl_source: declared
  description: The Entities API from BRICK Schema — 3 operation(s) for entities.
  name: BRICK Schema Entities API
  slug: brick-entities-api
- baseURL: https://brickschema.org/schema/
  baseurl_source: declared
  description: The Raw Queries API from BRICK Schema — 2 operation(s) for raw queries.
  name: BRICK Schema Raw Queries API
  slug: brick-raw-queries-api
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/brick/plans/brick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brick-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/brick/rate-limits/brick-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/brick-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/brick/finops/brick-finops.yml
  title: ''
  type: FinOps
  url: finops/brick-finops.yml
- group: other
  href: https://artifacts.apis.io/brick/overlays/brick-brick-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brick-brick-server-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/brick/authentication/brick-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brick-authentication.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/BrickSchema/Brick/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/BrickSchema/Brick/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/BrickSchema/Brick/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/BrickSchema/Brick/blob/master/LICENSE
- group: auth
  href: https://artifacts.apis.io/brick/security/brick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brickschema.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brickschema.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BrickSchema
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/BrickSchema/Brick
- group: other
  title: ''
  type: OntologyBrowser
  url: https://ontology.brickschema.org/
- group: operate
  title: ''
  type: Community
  url: https://groups.google.com/g/brickschema
- group: build
  title: ''
  type: PyPIPackage
  url: https://pypi.org/project/brickschema/
- group: design
  href: https://artifacts.apis.io/brick/vocabulary/brick-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brick-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/brick/packages/brick-packages.yml
  title: ''
  type: Packages
  url: packages/brick-packages.yml
- group: build
  href: https://artifacts.apis.io/brick/packages/brick-packages.yml
  title: ''
  type: SDKs
  url: packages/brick-packages.yml
- group: build
  href: https://artifacts.apis.io/brick/cli/brick-cli.yml
  title: ''
  type: CLI
  url: cli/brick-cli.yml
- group: design
  href: https://artifacts.apis.io/brick/conventions/brick-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brick-conventions.yml
- group: design
  href: https://artifacts.apis.io/brick/data-model/brick-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brick-data-model.yml
- group: design
  href: https://artifacts.apis.io/brick/errors/brick-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brick-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brick/lifecycle/brick-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brick-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/brick/changelog/brick-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brick-changelog.yml
- group: design
  href: https://artifacts.apis.io/brick/conformance/brick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brick-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brick/llms/brick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brick-llms.txt
- group: agent
  href: https://artifacts.apis.io/brick/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://brickschema.readthedocs.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brickschema.org/lifecycle/creation.html
created: '2025-02-17'
description: BRICK is an open-source community-driven ontology standard for standardizing semantic descriptions of physical, logical, and virtual assets in buildings and the relationships between them. Using Semantic Web (RDF/OWL) technology, BRICK v1.4.4 enables interoperability across building management systems, reducing the cost of deploying analytics and energy efficiency initiatives. It supports HVAC, lighting, fire, security, and other building subsystems under a unified extensible vocabulary with SHACL-based validation.
finops:
- has_sources: false
  method: generated
  name: Brick Finops
  primary_unit: request
  service_category: API
  slug: brick-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brick.png
layout: provider
modified: '2026-09-04'
name: BRICK Schema
nav: Providers
network: true
overview: 'BRICK Schema publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actuation API, Auth API, Brickapi API, and 4 more. Tagged areas include Building Information Modeling, BIM, Smart Buildings, Ontology, and Semantic Web.


  The BRICK Schema catalog on APIs.io includes 1 Spectral governance ruleset.


  BRICK Schema''s developer surface includes authentication, documentation, CLI, changelog, API reference, getting-started guide, and 25 more developer resources.'
plans:
- name: Brick Plans Pricing
  plan_count: 0
  slug: brick-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Brick Rate Limits
  slug: brick-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: BRICK Schema API Rules
  rule_count: 44
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 2
  slug: brick-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 40.7
    developer_ergonomics: 58.9
    discoverability: 71.7
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 36.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: third-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/brick/brick-2026-06-20T173653.png
security:
- kind: authentication
  name: Brick Authentication
  slug: brick-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brick Domain Security
  slug: brick-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: brick-actuation-safety
  slug: brick-actuation-safety
- name: brick-model-ingest-and-query
  slug: brick-model-ingest-and-query
- name: brick-ontology-lookup
  slug: brick-ontology-lookup
- name: brick-timeseries-access
  slug: brick-timeseries-access
slug: brick
tags:
- Building Information Modeling
- BIM
- Smart Buildings
- Ontology
- Semantic Web
- IoT
- HVAC
- Energy Management
website: https://brickschema.org/
---
