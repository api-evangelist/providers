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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 187
  human_in_the_loop: 4
  name: Emory Agentic Access
  operation_count: 344
  slug: emory-agentic-access
  summary_line: 344 operations · 187 acting · 4 human-in-the-loop
api_count: 1
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
artifact_total: 69
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation API
  slug: open-emory-annotation-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation api_key API
  slug: open-emory-api-key-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation assetstore API
  slug: open-emory-assetstore-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation collection API
  slug: open-emory-collection-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation dicomweb_assetstore API
  slug: open-emory-dicomweb-assetstore-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation file API
  slug: open-emory-file-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation files API
  slug: open-emory-files-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation folder API
  slug: open-emory-folder-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation group API
  slug: open-emory-group-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation histomicsui API
  slug: open-emory-histomicsui-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation homepage API
  slug: open-emory-homepage-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation item API
  slug: open-emory-item-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation job API
  slug: open-emory-job-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation large_image API
  slug: open-emory-large-image-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation notification API
  slug: open-emory-notification-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation resource API
  slug: open-emory-resource-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation slicer_cli_web API
  slug: open-emory-slicer-cli-web-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation system API
  slug: open-emory-system-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation tcga API
  slug: open-emory-tcga-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation token API
  slug: open-emory-token-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation user API
  slug: open-emory-user-api
- collection_type: open
  name: Girder REST API (Emory Digital Slide Archive) annotation worker API
  slug: open-emory-worker-api
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
random_paper: 10
rate_limits:
- limit_count: 1
  name: Emory Rate Limits
  slug: emory-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Emory University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: emory-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Emory University API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: emory-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 58.7
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
