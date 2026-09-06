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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Quay Agentic Access
  operation_count: 16
  slug: quay-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage Dockerfile builds, build logs, build triggers, and build configuration.
  name: Quay Build API
  slug: quay-build-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Inspect image manifests, manifest layers, and labels associated with a pushed image.
  name: Quay Manifest API
  slug: quay-manifest-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage Quay organizations, organization members, billing, application tokens, and organization-wide settings.
  name: Quay Organization API
  slug: quay-organization-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage user and team permissions on repositories.
  name: Quay Permission API
  slug: quay-permission-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage container image repositories including create, list, update, delete, visibility, descriptions, and metadata.
  name: Quay Repository API
  slug: quay-repository-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage robot accounts used for automated repository access including credentials and permissions.
  name: Quay Robot API
  slug: quay-robot-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Retrieve vulnerability scan results for repository images.
  name: Quay Security API
  slug: quay-security-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage repository image tags including listing, restoring, expiring, and deleting tags.
  name: Quay Tag API
  slug: quay-tag-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage organization teams, team membership, team roles, and team permissions on repositories.
  name: Quay Team API
  slug: quay-team-api
- baseURL: https://quay.io/api/v1
  baseurl_source: declared
  description: Manage Quay user accounts, profile, starred repositories, and personal OAuth tokens.
  name: Quay User API
  slug: quay-user-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quay Container Registry Build API
  slug: open-quay-build-api
- collection_type: open
  name: Quay Container Registry Build Manifest API
  slug: open-quay-manifest-api
- collection_type: open
  name: Quay Container Registry Build Organization API
  slug: open-quay-organization-api
- collection_type: open
  name: Quay Container Registry Build Permission API
  slug: open-quay-permission-api
- collection_type: open
  name: Quay Container Registry Build Repository API
  slug: open-quay-repository-api
- collection_type: open
  name: Quay Container Registry Build Robot API
  slug: open-quay-robot-api
- collection_type: open
  name: Quay Container Registry Build Security API
  slug: open-quay-security-api
- collection_type: open
  name: Quay Container Registry Build Tag API
  slug: open-quay-tag-api
- collection_type: open
  name: Quay Container Registry Build Team API
  slug: open-quay-team-api
- collection_type: open
  name: Quay Container Registry Build User API
  slug: open-quay-user-api
- collection_type: open
  name: Quay Container Registry API
  slug: open-quay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/quay-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://quay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quay.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quay.io/guides/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quay
- group: commercial
  title: ''
  type: Pricing
  url: https://quay.io/plans/
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog
- group: start
  title: ''
  type: Signup
  url: https://quay.io/signin/
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/products/red-hat-quay/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/quay/quay-mcp-server
created: '2026-03-26'
description: Quay is a container image registry that enables you to build, store, distribute, and deploy container images with built-in security scanning, access controls, and automated build triggers. Available as a hosted service at Quay.io or as a self-hosted solution through Red Hat Quay.
finops:
- name: Quay Finops
  service_category: API
  slug: quay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quay.png
json_schemas:
- name: Quay Manifest Security Scan
  property_count: 2
  slug: quay-manifest-security
- name: Quay Repository
  property_count: 11
  slug: quay-repository
- name: Quay Tag
  property_count: 9
  slug: quay-tag
jsonld:
- class_count: 5
  name: Quay Context
  property_count: 2
  slug: quay-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Quay
nav: Providers
network: true
overview: 'Quay publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Build API, Manifest API, Organization API, and 7 more. Tagged areas include Container Images, Containers, Red Hat, Registry, and Security Scanning.


  The Quay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Quay''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, support, and 6 more developer resources.'
plans:
- name: Quay Plans Pricing
  plan_count: 3
  slug: quay-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Quay Rate Limits
  slug: quay-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Quay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quay-jsonschema-spectral-rules
scopes:
- name: Quay Scopes
  scope_count: 6
  slug: quay-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 67.3
    catalog_earned_first_party: 0.0
    catalog_gap: 47.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/screenshots/quay-2026-06-20T192420.png
security:
- kind: authentication
  name: Quay Authentication
  slug: quay-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Quay Domain Security
  slug: quay-domain-security
  summary_line: TLSv1.3 · HSTS
slug: quay
tags:
- Container Images
- Containers
- Red Hat
- Registry
- Security Scanning
website: https://quay.io/
---
