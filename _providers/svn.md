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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Svn Agentic Access
  operation_count: 8
  slug: svn-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 7
apis:
- description: The Subversion C library provides the low-level API for building tools and integrations. It includes the libsvn_client, libsvn_ra, libsvn_wc, and libsvn_repos libraries for client operations, reposito
  name: SVN C Library API
  slug: svn-c-api
- description: Python bindings for Subversion C libraries, providing access to client and repository operations via pysvn and the official svn.client Python module.
  name: SVN Python Bindings
  slug: svn-python-bindings
- description: SVNKit is a pure Java Subversion client library providing full access to Subversion repository and working copy data. Used by major IDE plugins including IntelliJ IDEA and Eclipse Subclipse.
  name: SVNKit Java Library
  slug: svn-java-bindings
- description: Commit lifecycle — create transaction, stage changes, finalize
  name: Subversion Commits API
  slug: svn-commits-api
- description: File and directory content retrieval
  name: Subversion Files API
  slug: svn-files-api
- description: Log, blame, and revision history operations
  name: Subversion History API
  slug: svn-history-api
- description: Repository root and metadata operations
  name: Subversion Repository API
  slug: svn-repository-api
artifact_total: 23
collections:
- collection_type: open
  name: SVN WebDAV HTTP API
  slug: open-svn-webdav
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/svn-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/svn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/svn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/svn-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://subversion.apache.org/quick-start
- group: other
  title: ''
  type: Book
  url: https://svnbook.red-bean.com/
- group: other
  title: ''
  type: Downloads
  url: https://subversion.apache.org/download/
- group: auth
  title: ''
  type: Security
  url: https://subversion.apache.org/security/
- group: operate
  title: ''
  type: FAQ
  url: https://subversion.apache.org/faq.html
- group: operate
  title: ''
  type: Community
  url: https://subversion.apache.org/mailing-lists.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/apache/subversion
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: build
  title: ''
  type: Package
  url: https://packages.apache.org/subversion
created: '2024-01-01'
description: Apache Subversion (SVN) is a centralized version control system that tracks changes to files and directories over time. It supports atomic commits, directory versioning, cheap branching and tagging, merge tracking, and binary file handling. SVN is served over HTTP/HTTPS using the WebDAV/DeltaV protocol via mod_dav_svn, or over a custom protocol using svnserve.
examples:
- key_count: 2
  name: Svn Commit Example
  slug: svn-commit-example
- key_count: 3
  name: Svn Get File Example
  slug: svn-get-file-example
finops:
- name: Svn Finops
  service_category: API
  slug: svn-finops
image: https://subversion.apache.org/images/svn-square.jpg
json_schemas:
- name: SVN Commit
  property_count: 5
  slug: svn-commit
- name: SVN Repository
  property_count: 5
  slug: svn-repository
json_structures:
- name: Svn Repository Structure
  property_count: 0
  slug: svn-repository-structure
jsonld:
- class_count: 0
  name: Svn Context
  property_count: 26
  slug: svn-context
layout: provider
modified: '2026-05-19'
name: Subversion
nav: Providers
network: true
overview: 'Subversion publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Commits API, Files API, History API, and 1 more. Tagged areas include Apache, Open Source, Repository, Source Control, and Svn.


  The Subversion catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Subversion''s developer surface includes authentication, getting-started guide, FAQ, GitHub presence, and 9 more developer resources.'
plans:
- name: Svn Plans Pricing
  plan_count: 3
  slug: svn-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Svn Rate Limits
  slug: svn-rate-limits
rules:
- name: Subversion API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: svn-jsonschema-spectral-rules
- name: Subversion API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: svn-rules
score:
  band: developing
  composite: 53.5
  delta: 2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.4
    developer_ergonomics: 26.1
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 47.4
  previous_composite: 51.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/svn/refs/heads/main/screenshots/svn-2026-06-20T194747.png
security:
- kind: authentication
  name: Svn Authentication
  slug: svn-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Svn Domain Security
  slug: svn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Svn Vulnerability Disclosure
  slug: svn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: svn
tags:
- Apache
- Open Source
- Repository
- Source Control
- Svn
- Version Control
- Webdav
---
