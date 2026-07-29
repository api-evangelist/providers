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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Bump Sh Agentic Access
  operation_count: 15
  slug: bump-sh-agentic-access
  summary_line: 15 operations · 9 acting
api_count: 8
apis:
- description: Manage branches of a given documentation
  name: Bump.sh Branches API
  slug: bump-sh-branches-api
- description: The Diffs API from Bump.sh — 2 operation(s) for diffs.
  name: Bump.sh Diffs API
  slug: bump-sh-diffs-api
- description: The Hubs API from Bump.sh — 2 operation(s) for hubs.
  name: Bump.sh Hubs API
  slug: bump-sh-hubs-api
- description: The MCP servers API from Bump.sh — 1 operation(s) for mcp servers.
  name: Bump.sh MCP servers API
  slug: bump-sh-mcp-servers-api
- description: The Ping API from Bump.sh — 1 operation(s) for ping.
  name: Bump.sh Ping API
  slug: bump-sh-ping-api
- description: The Previews API from Bump.sh — 2 operation(s) for previews.
  name: Bump.sh Previews API
  slug: bump-sh-previews-api
- description: The Validations API from Bump.sh — 1 operation(s) for validations.
  name: Bump.sh Validations API
  slug: bump-sh-validations-api
- description: The Versions API from Bump.sh — 2 operation(s) for versions.
  name: Bump.sh Versions API
  slug: bump-sh-versions-api
artifact_total: 54
collections:
- collection_type: postman
  name: Bump.sh Api Branches API
  slug: postman-bump-sh-branches-api
- collection_type: postman
  name: Bump.sh Api Branches Diffs API
  slug: postman-bump-sh-diffs-api
- collection_type: postman
  name: Bump.sh Api Branches Hubs API
  slug: postman-bump-sh-hubs-api
- collection_type: postman
  name: Bump.sh Api Branches MCP servers API
  slug: postman-bump-sh-mcp-servers-api
- collection_type: postman
  name: Bump.sh Api Branches Ping API
  slug: postman-bump-sh-ping-api
- collection_type: postman
  name: Bump.sh Api Branches Previews API
  slug: postman-bump-sh-previews-api
- collection_type: postman
  name: Bump.sh Api Branches Validations API
  slug: postman-bump-sh-validations-api
- collection_type: postman
  name: Bump.sh Api Branches Versions API
  slug: postman-bump-sh-versions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bumpsh/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bump-sh-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bump-sh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bump-sh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bump-sh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bump.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bump.sh
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bump.sh
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.bump.sh/source.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bump-sh
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/cli
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/github-action
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/flower-spec
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/bump-ci-example
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/examples
- group: company
  title: ''
  type: Blog
  url: https://bump.sh/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bump.sh/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://bump.sh/changelog
- group: start
  title: ''
  type: Signup
  url: https://bump.sh/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://bump.sh/users/sign_in
- group: operate
  title: ''
  type: StatusPage
  url: https://bumpsh.statuspage.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bump-sh
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.bump.sh/llms.txt
created: '2026-03-16'
description: Bump.sh is "the modern API doc platform" — automatic, diff-aware documentation for OpenAPI and AsyncAPI specifications, plus a managed Model Context Protocol (MCP) platform that compiles Flower or Arazzo workflow documents into deterministic, observable MCP servers for AI agents. Customers include Aviobook, MongoDB, Elastic, Lightspeed, and BigID.
examples:
- key_count: 5
  name: Bump Sh Create Branch Example
  slug: bump-sh-create-branch-example
- key_count: 5
  name: Bump Sh Create Diff Example
  slug: bump-sh-create-diff-example
- key_count: 5
  name: Bump Sh Create Preview Example
  slug: bump-sh-create-preview-example
- key_count: 5
  name: Bump Sh Create Version Example
  slug: bump-sh-create-version-example
- key_count: 5
  name: Bump Sh Delete Branch Example
  slug: bump-sh-delete-branch-example
- key_count: 5
  name: Bump Sh Deploy Mcp Server Example
  slug: bump-sh-deploy-mcp-server-example
- key_count: 4
  name: Bump Sh Doc Change Webhook Example
  slug: bump-sh-doc-change-webhook-example
- key_count: 5
  name: Bump Sh Fetch Diff Example
  slug: bump-sh-fetch-diff-example
- key_count: 5
  name: Bump Sh Fetch Hub Example
  slug: bump-sh-fetch-hub-example
- key_count: 5
  name: Bump Sh Fetch Version Example
  slug: bump-sh-fetch-version-example
- key_count: 5
  name: Bump Sh List Branches Example
  slug: bump-sh-list-branches-example
- key_count: 5
  name: Bump Sh List Hubs Example
  slug: bump-sh-list-hubs-example
- key_count: 5
  name: Bump Sh Ping Example
  slug: bump-sh-ping-example
- key_count: 5
  name: Bump Sh Promote Branch Example
  slug: bump-sh-promote-branch-example
- key_count: 5
  name: Bump Sh Update Preview Example
  slug: bump-sh-update-preview-example
- key_count: 5
  name: Bump Sh Validate Example
  slug: bump-sh-validate-example
finops:
- name: Bump Sh Finops
  service_category: API
  slug: bump-sh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bump-sh.png
json_schemas:
- name: Branch
  property_count: 4
  slug: bump-sh-branch
- name: Diff
  property_count: 9
  slug: bump-sh-diff
- name: DocStructureChangeEvent
  property_count: 4
  slug: bump-sh-doc-change-event
- name: Hub
  property_count: 6
  slug: bump-sh-hub
- name: McpDeployment
  property_count: 4
  slug: bump-sh-mcp-deployment
- name: Preview
  property_count: 3
  slug: bump-sh-preview
- name: Validation
  property_count: 3
  slug: bump-sh-validation
- name: Version
  property_count: 7
  slug: bump-sh-version
json_structures:
- name: Bump Sh Diff Structure
  property_count: 6
  slug: bump-sh-diff-structure
- name: Bump Sh Hub Structure
  property_count: 6
  slug: bump-sh-hub-structure
- name: Bump Sh Mcp Deployment Structure
  property_count: 4
  slug: bump-sh-mcp-deployment-structure
- name: Bump Sh Version Structure
  property_count: 7
  slug: bump-sh-version-structure
jsonld:
- class_count: 23
  name: Bump Sh Context
  property_count: 8
  slug: bump-sh-context
layout: provider
modified: '2026-05-22'
name: Bump.sh
nav: Providers
network: true
overview: 'Bump.sh publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Diffs API, Hubs API, and 5 more. Tagged areas include API Changelog, API Documentation, API Hub, API Governance, and Arazzo.


  The Bump.sh catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bump.sh''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, changelog, signup flow, and 16 more developer resources.'
plans:
- name: Bump Sh Plans Pricing
  plan_count: 4
  slug: bump-sh-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Bump Sh Rate Limits
  slug: bump-sh-rate-limits
rules:
- name: Bump.sh API Rules
  rule_count: 12
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 7
  slug: bump-sh-api-rules
- name: Bump.sh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bump-sh-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.8
  delta: -3.5
  facets:
    commercial_clarity: 63.2
    contract_quality: 62.5
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 68.4
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bump-sh/refs/heads/main/screenshots/bump-sh-2026-06-20T173758.png
security:
- kind: authentication
  name: Bump Sh Authentication
  slug: bump-sh-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Bump Sh Domain Security
  slug: bump-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bump Sh Vulnerability Disclosure
  slug: bump-sh-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bump-sh
tags:
- API Changelog
- API Documentation
- API Hub
- API Governance
- Arazzo
- AsyncAPI
- CI/CD
- Flower
- MCP
- OpenAPI
- Workflows
website: https://bump.sh
---
