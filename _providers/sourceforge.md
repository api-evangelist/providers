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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Sourceforge Agentic Access
  operation_count: 28
  slug: sourceforge-agentic-access
  summary_line: 28 operations · 12 acting
api_count: 7
apis:
- description: Administrative operations including exports, tool installation, and webhooks
  name: SourceForge Admin API
  slug: sourceforge-admin-api
- description: Project blog post management
  name: SourceForge Blog API
  slug: sourceforge-blog-api
- description: Forum and discussion thread management
  name: SourceForge Discussion API
  slug: sourceforge-discussion-api
- description: Project creation, retrieval, and permission management
  name: SourceForge Projects API
  slug: sourceforge-projects-api
- description: Issue and ticket tracking
  name: SourceForge Tracker API
  slug: sourceforge-tracker-api
- description: User profile and authentication
  name: SourceForge Users API
  slug: sourceforge-users-api
- description: Project wiki page management
  name: SourceForge Wikis API
  slug: sourceforge-wikis-api
artifact_total: 37
collections:
- collection_type: postman
  name: SourceForge Allura Admin API
  slug: postman-sourceforge-admin-api
- collection_type: postman
  name: SourceForge Allura Admin Blog API
  slug: postman-sourceforge-blog-api
- collection_type: postman
  name: SourceForge Allura Admin Discussion API
  slug: postman-sourceforge-discussion-api
- collection_type: postman
  name: SourceForge Allura Admin Projects API
  slug: postman-sourceforge-projects-api
- collection_type: postman
  name: SourceForge Allura Admin Tracker API
  slug: postman-sourceforge-tracker-api
- collection_type: postman
  name: SourceForge Allura Admin Users API
  slug: postman-sourceforge-users-api
- collection_type: postman
  name: SourceForge Allura Admin Wikis API
  slug: postman-sourceforge-wikis-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SourceForge Allura Admin API
  slug: open-sourceforge-admin-api
- collection_type: open
  name: SourceForge Allura API
  slug: open-sourceforge-allura
- collection_type: open
  name: SourceForge Allura Admin Blog API
  slug: open-sourceforge-blog-api
- collection_type: open
  name: SourceForge Allura Admin Discussion API
  slug: open-sourceforge-discussion-api
- collection_type: open
  name: SourceForge Allura Admin Projects API
  slug: open-sourceforge-projects-api
- collection_type: open
  name: SourceForge Allura Admin Tracker API
  slug: open-sourceforge-tracker-api
- collection_type: open
  name: SourceForge Allura Admin Users API
  slug: open-sourceforge-users-api
- collection_type: open
  name: SourceForge Allura Admin Wikis API
  slug: open-sourceforge-wikis-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sourceforge/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sourceforge-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sourceforge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sourceforge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sourceforge-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sourceforge-net
- group: start
  title: ''
  type: Portal
  url: https://sourceforge.net/p/forge/documentation/API/
- group: docs
  title: ''
  type: Documentation
  url: https://sourceforge.net/p/forge/documentation/
- group: company
  title: ''
  type: Website
  url: https://sourceforge.net/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apache/allura
- group: docs
  title: ''
  type: API Documentation
  url: https://sourceforge.net/api-docs/
- group: start
  title: ''
  type: OAuth Portal
  url: https://sourceforge.net/auth/oauth/
- group: docs
  title: ''
  type: Webhooks Documentation
  url: https://forge-allura.apache.org/p/allura/wiki/Webhooks/
- group: operate
  title: ''
  type: Support
  url: https://sourceforge.net/p/forge/site-support/
- group: company
  title: ''
  type: Blog
  url: https://sourceforge.net/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://sourceforge.net/p/forge/site-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sourceforge.net/p/forge/documentation/Terms%20of%20Use/
- group: agent
  title: ''
  type: LlmsText
  url: https://sourceforge.net/llms.txt
created: '2026-03-16'
description: SourceForge is a web-based platform for hosting, managing, and distributing open source software projects. Built on the Apache Allura platform, SourceForge provides project management tools including wiki, issue tracking, discussion forums, blogs, file releases, code repositories (Git, SVN, Mercurial), and a REST API for programmatic access to all project resources.
examples:
- key_count: 2
  name: Sourceforge List Tickets Example
  slug: sourceforge-list-tickets-example
finops:
- name: Sourceforge Finops
  service_category: API
  slug: sourceforge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sourceforge.png
json_schemas:
- name: SourceForge Project
  property_count: 6
  slug: sourceforge-project
- name: SourceForge Ticket
  property_count: 9
  slug: sourceforge-ticket
json_structures:
- name: Sourceforge Ticket Structure
  property_count: 0
  slug: sourceforge-ticket-structure
jsonld:
- class_count: 6
  name: Sourceforge Context
  property_count: 12
  slug: sourceforge-context
layout: provider
modified: '2026-05-19'
name: SourceForge
nav: Providers
network: true
overview: 'SourceForge publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Blog API, Discussion API, and 4 more. Tagged areas include Open-Source, Developer Tools, Project Management, Code Hosting, and Collaboration.


  The SourceForge catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SourceForge''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 13 more developer resources.'
plans:
- name: Sourceforge Plans Pricing
  plan_count: 3
  slug: sourceforge-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Sourceforge Rate Limits
  slug: sourceforge-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SourceForge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sourceforge-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: SourceForge API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 7
  slug: sourceforge-rules
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 63.2
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sourceforge/refs/heads/main/screenshots/sourceforge-2026-06-20T194221.png
security:
- kind: authentication
  name: Sourceforge Authentication
  slug: sourceforge-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sourceforge Domain Security
  slug: sourceforge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sourceforge Vulnerability Disclosure
  slug: sourceforge-vulnerability-disclosure
  summary_line: disclosure policy published
slug: sourceforge
tags:
- Open-Source
- Developer Tools
- Project Management
- Code Hosting
- Collaboration
website: https://sourceforge.net/
---
