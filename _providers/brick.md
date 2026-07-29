---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The BRICK ontology v1.4.4 defines a standardized vocabulary of building system concepts, relationships, and data model for smart building analytics. Available as RDF/OWL files, BRICK describes sensors
  name: BRICK Ontology
  slug: ontology
artifact_total: 5
common:
- group: auth
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
created: '2025-02-17'
description: BRICK is an open-source community-driven ontology standard for standardizing semantic descriptions of physical, logical, and virtual assets in buildings and the relationships between them. Using Semantic Web (RDF/OWL) technology, BRICK v1.4.4 enables interoperability across building management systems, reducing the cost of deploying analytics and energy efficiency initiatives. It supports HVAC, lighting, fire, security, and other building subsystems under a unified extensible vocabulary with SHACL-based validation.
finops:
- name: Brick Finops
  service_category: API
  slug: brick-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brick.png
layout: provider
modified: '2026-04-21'
name: BRICK Schema
nav: Providers
network: true
overview: 'BRICK Schema publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Building Information Modeling, BIM, Smart Buildings, Ontology, and Semantic Web.


  BRICK Schema''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Brick Plans Pricing
  plan_count: 3
  slug: brick-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Brick Rate Limits
  slug: brick-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brick/refs/heads/main/screenshots/brick-2026-06-20T173653.png
security:
- kind: domain-security
  name: Brick Domain Security
  slug: brick-domain-security
  summary_line: TLSv1.3
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
