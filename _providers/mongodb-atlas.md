---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
  score: 32.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Mongodb Atlas Agentic Access
  operation_count: 16
  slug: mongodb-atlas-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 4
apis:
- description: The Clusters API from MongoDB Atlas — 2 operation(s) for clusters.
  name: MongoDB Atlas Clusters API
  slug: mongodb-atlas-clusters-api
- description: The Database Users API from MongoDB Atlas — 2 operation(s) for database users.
  name: MongoDB Atlas Database Users API
  slug: mongodb-atlas-database-users-api
- description: The Organizations API from MongoDB Atlas — 2 operation(s) for organizations.
  name: MongoDB Atlas Organizations API
  slug: mongodb-atlas-organizations-api
- description: The Projects API from MongoDB Atlas — 2 operation(s) for projects.
  name: MongoDB Atlas Projects API
  slug: mongodb-atlas-projects-api
artifact_total: 18
collections:
- collection_type: open
  name: MongoDB Atlas Administration API
  slug: open-mongodb-atlas
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mongodb-atlas-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mongodb-atlas-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mongodb-atlas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mongodb-atlas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mongodb-atlas-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/mongodb/agent-skills
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mongodb
- group: company
  title: ''
  type: Website
  url: https://www.mongodb.com/products/platform/atlas-database
- group: docs
  title: ''
  type: Documentation
  url: https://www.mongodb.com/docs/atlas/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mongodb.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.mongodb.com/cloud/atlas/register
- group: company
  title: ''
  type: Blog
  url: https://www.mongodb.com/blog/rss
created: '2026-05-11'
description: MongoDB Atlas is a fully managed cloud database service for MongoDB, available on AWS, Google Cloud, and Microsoft Azure, with global clusters, automated backups, security, and integrated search, vector, and stream processing capabilities. The Atlas Administration API provides programmatic control over projects, clusters, users, network access, backups, and billing, and is paired with a Data API and Resource Policy APIs for full lifecycle management using HTTP Digest, API keys, or service account OAuth tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mongodb-atlas.png
layout: provider
modified: '2026-05-11'
name: MongoDB Atlas
nav: Providers
network: true
overview: 'MongoDB Atlas publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Database Users API, Organizations API, and 1 more. Tagged areas include Database, Document Database, NoSQL, MongoDB, and Cloud Database.


  MongoDB Atlas'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 85
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 58.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mongodb-atlas/refs/heads/main/screenshots/mongodb-atlas-2026-06-20T185729.png
security:
- kind: authentication
  name: Mongodb Atlas Authentication
  slug: mongodb-atlas-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Mongodb Atlas Domain Security
  slug: mongodb-atlas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mongodb Atlas Vulnerability Disclosure
  slug: mongodb-atlas-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Mongodb Atlas Trust Center
  slug: mongodb-atlas-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
skill_count: 8
skills:
- name: mongodb-atlas-stream-processing
  slug: mongodb-atlas-stream-processing
- name: mongodb-connection
  slug: mongodb-connection
- name: mongodb-mcp-setup
  slug: mongodb-mcp-setup
- name: mongodb-natural-language-querying
  slug: mongodb-natural-language-querying
- name: mongodb-query-optimizer
  slug: mongodb-query-optimizer
- name: mongodb-schema-design
  slug: mongodb-schema-design
- name: mongodb-search-and-ai
  slug: mongodb-search-and-ai
- name: review-skill
  slug: review-skill
slug: mongodb-atlas
tags:
- Database
- Document Database
- NoSQL
- MongoDB
- Cloud Database
- DBaaS
- Vector Search
- Atlas
website: https://www.mongodb.com/products/platform/atlas-database
---
