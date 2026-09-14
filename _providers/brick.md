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
api_count: 1
apis:
- description: The BRICK ontology v1.4.4 defines a standardized vocabulary of building system concepts, relationships, and data model for smart building analytics. Available as RDF/OWL files, BRICK describes sensors
  name: BRICK Ontology
  slug: ontology
- baseURL: https://{brick-server-host}/brickapi/v1
  baseurl_source: declared
  description: The Brick Example Server is the BrickSchema organisation's self-hostable HTTP contract, documented at docs.brickschema.org as "demonstrating how a Brick model can be abstracted by an HTTP API". OpenAP
  name: Brick Example Server
  slug: server
artifact_total: 7
common:
- group: auth
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
  title: ''
  type: Vocabulary
  url: vocabulary/brick-vocabulary.yml
- group: build
  title: ''
  type: Packages
  url: packages/brick-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brick-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/brick-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brick-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brick-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brick-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brick-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brick-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brick-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brick-llms.txt
- group: agent
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
- name: Brick Finops
  service_category: API
  slug: brick-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brick.png
layout: provider
modified: '2026-09-04'
name: BRICK Schema
nav: Providers
network: true
overview: 'BRICK Schema publishes 1 API on the [APIs.io](https://apis.io/) network: Brick Example Server. Tagged areas include Building Information Modeling, BIM, Smart Buildings, Ontology, and Semantic Web.


  BRICK Schema''s developer surface includes authentication, documentation, CLI, changelog, API reference, getting-started guide, and 21 more developer resources.'
plans:
- name: Brick Plans Pricing
  plan_count: 0
  slug: brick-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Brick Rate Limits
  slug: brick-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/brick/refs/heads/main/screenshots/brick-2026-06-20T173653.png
security:
- kind: authentication
  name: Brick Authentication
  slug: brick-authentication
  summary_line: http · 1 scheme
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
