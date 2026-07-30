---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Vagrant Agentic Access
  operation_count: 33
  slug: vagrant-agentic-access
  summary_line: 33 operations · 20 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: An official Ruby library that wraps the Vagrant Cloud API, providing a convenient interface for managing boxes, versions, and providers programmatically.
  name: Vagrant Cloud Ruby Client
  slug: vagrant-cloud-ruby-client
- description: The Vagrant Plugin SDK enables developers to build plugins that extend Vagrant with custom commands, providers, provisioners, guests, and host capabilities using Go or Ruby.
  name: Vagrant Plugin SDK
  slug: vagrant-plugin-sdk
- description: Endpoints for creating, reading, updating, and deleting Vagrant boxes in the Vagrant Cloud registry.
  name: Vagrant Boxes API
  slug: vagrant-boxes-api
- description: Endpoints for managing providers within a box version, including creating providers and uploading box files.
  name: Vagrant Providers API
  slug: vagrant-providers-api
- description: Endpoints for managing Vagrant box registries. A registry is a namespace that holds boxes and forms the first segment of a box tag such as hashicorp in hashicorp/vagrant.
  name: Vagrant Registries API
  slug: vagrant-registries-api
- description: Endpoints for searching the public Vagrant box catalog by query, provider, and other filters.
  name: Vagrant Search API
  slug: vagrant-search-api
- description: Endpoints for managing versions of a Vagrant box, including creating new versions and releasing them for consumption.
  name: Vagrant Versions API
  slug: vagrant-versions-api
artifact_total: 27
collections:
- collection_type: postman
  name: Vagrant Cloud Boxes API
  slug: postman-vagrant-boxes-api
- collection_type: postman
  name: Vagrant Cloud Boxes Providers API
  slug: postman-vagrant-providers-api
- collection_type: postman
  name: Vagrant Cloud Boxes Registries API
  slug: postman-vagrant-registries-api
- collection_type: postman
  name: Vagrant Cloud Boxes Search API
  slug: postman-vagrant-search-api
- collection_type: postman
  name: Vagrant Cloud Boxes Versions API
  slug: postman-vagrant-versions-api
- collection_type: open
  name: Vagrant Cloud API
  slug: open-vagrant-cloud-api
- collection_type: open
  name: HCP Vagrant Box Registry API
  slug: open-vagrant-hcp-vagrant-box-registry
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vagrant/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vagrant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vagrant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vagrant-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.hashicorp.com/vagrant
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/vagrant/docs
- group: company
  title: ''
  type: Website
  url: https://www.vagrantup.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hashicorp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hashicorp.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.hashicorp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.vagrantup.com/session/new
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hashicorp/vagrant
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/json-schema/vagrant-box-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/json-ld/vagrant-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/rules/vagrant-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/vocabulary/vagrant-vocabulary.yml
created: '2026-03-20'
description: Vagrant, by HashiCorp, is a tool for building and managing virtualized development environments. Their developer platform provides APIs and SDKs for interacting with Vagrant Cloud and the HCP Vagrant Box Registry, enabling automation of box lifecycle management, plugin development, and integration with CI/CD pipelines.
examples:
- key_count: 2
  name: Vagrant Create Box Example
  slug: vagrant-create-box-example
- key_count: 2
  name: Vagrant List Boxes Example
  slug: vagrant-list-boxes-example
finops:
- name: Vagrant Finops
  service_category: API
  slug: vagrant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vagrant.png
json_schemas:
- name: Vagrant Box
  property_count: 11
  slug: vagrant-box
json_structures:
- name: Vagrant Box Structure
  property_count: 0
  slug: vagrant-box-structure
jsonld:
- class_count: 0
  name: Vagrant Context
  property_count: 4
  slug: vagrant-context
layout: provider
modified: '2026-05-19'
name: Vagrant
nav: Providers
network: true
overview: 'Vagrant publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Boxes API, Providers API, Registries API, and 2 more. Tagged areas include DevOps, Virtualization, Development Environments, Boxes, and Cloud.


  The Vagrant catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vagrant''s developer surface includes authentication, developer portal, documentation, support, engineering blog, GitHub presence, and 11 more developer resources.'
plans:
- name: Vagrant Plans Pricing
  plan_count: 3
  slug: vagrant-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Vagrant Rate Limits
  slug: vagrant-rate-limits
rules:
- name: Vagrant API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vagrant-jsonschema-spectral-rules
- name: Vagrant API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 5
  slug: vagrant-rules
score:
  band: strong
  composite: 57.9
  delta: -3.2
  facets:
    commercial_clarity: 73.7
    contract_quality: 63.4
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vagrant/refs/heads/main/screenshots/vagrant-2026-06-20T200805.png
security:
- kind: authentication
  name: Vagrant Authentication
  slug: vagrant-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vagrant Domain Security
  slug: vagrant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vagrant
tags:
- DevOps
- Virtualization
- Development Environments
- Boxes
- Cloud
- HashiCorp
- Infrastructure
website: https://www.vagrantup.com/
---
