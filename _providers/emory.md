---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 187
  human_in_the_loop: 4
  name: Emory Agentic Access
  operation_count: 344
  slug: emory-agentic-access
  summary_line: 344 operations · 187 acting · 4 human-in-the-loop
api_count: 25
apis:
- description: Emory's instance of the Instructure Canvas learning management system exposes the standard Canvas LMS REST API. Access requires an Emory Canvas account and developer keys / API access tokens; the refe
  name: Emory Canvas LMS REST API
  slug: canvas-lms
- description: 'Emory operates a federated Shibboleth identity provider for SAML-based single sign-on across institutional and partner services (InCommon federation). The IdP metadata endpoint is publicly reachable; '
  name: Emory Identity (Shibboleth / SAML)
  slug: shibboleth
- description: Emory Libraries (Library Technology and Digital Strategies) maintains a large public open-source GitHub organization with ~120 repositories, including the dlp-curate preservation workbench, TheKeep ar
  name: Emory Libraries Digital Repository Software
  slug: libraries-github
- description: annotation resource
  name: Emory University annotation API
  slug: emory-annotation-api
- description: api_key resource
  name: Emory University api_key API
  slug: emory-api-key-api
- description: assetstore resource
  name: Emory University assetstore API
  slug: emory-assetstore-api
- description: collection resource
  name: Emory University collection API
  slug: emory-collection-api
- description: dicomweb_assetstore resource
  name: Emory University dicomweb_assetstore API
  slug: emory-dicomweb-assetstore-api
- description: file resource
  name: Emory University file API
  slug: emory-file-api
- description: files resource
  name: Emory University files API
  slug: emory-files-api
- description: folder resource
  name: Emory University folder API
  slug: emory-folder-api
- description: group resource
  name: Emory University group API
  slug: emory-group-api
- description: histomicsui resource
  name: Emory University histomicsui API
  slug: emory-histomicsui-api
- description: homepage resource
  name: Emory University homepage API
  slug: emory-homepage-api
- description: item resource
  name: Emory University item API
  slug: emory-item-api
- description: job resource
  name: Emory University job API
  slug: emory-job-api
- description: large_image resource
  name: Emory University large_image API
  slug: emory-large-image-api
- description: notification resource
  name: Emory University notification API
  slug: emory-notification-api
- description: resource resource
  name: Emory University resource API
  slug: emory-resource-api
- description: slicer_cli_web resource
  name: Emory University slicer_cli_web API
  slug: emory-slicer-cli-web-api
- description: system resource
  name: Emory University system API
  slug: emory-system-api
- description: tcga resource
  name: Emory University tcga API
  slug: emory-tcga-api
- description: token resource
  name: Emory University token API
  slug: emory-token-api
- description: user resource
  name: Emory University user API
  slug: emory-user-api
- description: worker resource
  name: Emory University worker API
  slug: emory-worker-api
artifact_total: 46
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/emory-libraries/dlp-curate/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/emory-libraries/dlp-curate/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emory-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emory-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.emory.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://it.emory.edu/catalog/index.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/emory-libraries
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/emory-libraries/dlp-curate
- group: auth
  title: ''
  type: Authentication
  url: https://login.emory.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/emory-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/emory-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emory-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/emory-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Emory University is a private research university in Atlanta, Georgia, United States, ranked #196 in the QS World University Rankings 2025. Its public developer and API footprint is modest and largely tied to the libraries and research-computing units rather than a central developer portal. The most visible programmatic surfaces are the Emory Libraries open-source GitHub organization (digital-repository software built on the Samvera/Hyrax stack), a public Digital Slide Archive REST API operated by Emory''s biomedical imaging group, federated Shibboleth/SAML identity, and the Instructure Canvas LMS REST API exposed at the institution''s Canvas instance. Most institutional systems (OPUS student information, Course Atlas) are gated, browser-based applications without documented public APIs.'
examples:
- key_count: 2
  name: Emory Get Item Example
  slug: emory-get-item-example
- key_count: 2
  name: Emory List Annotations Example
  slug: emory-list-annotations-example
- key_count: 2
  name: Emory List Collections Example
  slug: emory-list-collections-example
- key_count: 2
  name: Emory List Folders Example
  slug: emory-list-folders-example
finops:
- name: Emory Finops
  service_category: Education
  slug: emory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emory.png
json_schemas:
- name: Girder Annotation
  property_count: 14
  slug: emory-annotation
- name: Girder Collection
  property_count: 10
  slug: emory-collection
- name: Girder Folder
  property_count: 15
  slug: emory-folder
- name: Girder Item
  property_count: 13
  slug: emory-item
json_structures:
- name: Emory Annotation Structure
  property_count: 14
  slug: emory-annotation-structure
- name: Emory Collection Structure
  property_count: 10
  slug: emory-collection-structure
- name: Emory Folder Structure
  property_count: 15
  slug: emory-folder-structure
- name: Emory Item Structure
  property_count: 13
  slug: emory-item-structure
jsonld:
- class_count: 13
  name: Emory Context
  property_count: 9
  slug: emory-context
layout: provider
modified: '2026-06-03'
name: Emory University
nav: Providers
network: true
overview: 'Emory University publishes 22 APIs on the [APIs.io](https://apis.io/) network, including annotation API, api_key API, assetstore API, and 19 more. Tagged areas include Education, Higher Education, University, Research, and Libraries.


  The Emory University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Emory University''s developer surface includes authentication, GitHub presence, and 13 more developer resources.'
plans:
- name: Emory Plans Pricing
  plan_count: 2
  slug: emory-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 1
  name: Emory Rate Limits
  slug: emory-rate-limits
rules:
- name: Emory University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: emory-jsonschema-spectral-rules
- name: Emory University API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: emory-rules
score:
  band: developing
  composite: 44.3
  delta: 1.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.8
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emory/refs/heads/main/screenshots/emory-2026-07-25T213244.png
security:
- kind: authentication
  name: Emory Authentication
  slug: emory-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Emory Domain Security
  slug: emory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emory
tags:
- Education
- Higher Education
- University
- Research
- Libraries
- United States
- Atlanta
website: https://www.emory.edu/
---
