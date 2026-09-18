---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Drupal Agentic Access
  operation_count: 33
  slug: drupal-agentic-access
  summary_line: 33 operations · 17 acting
api_count: 2
apis:
- description: The read-only REST API the Drupal Association operates on drupal.org itself, exposing Drupal.org’s own nodes, users, comments and taxonomy terms as JSON or XML. This is the only Drupal API served from
  name: Drupal.org REST API
  slug: drupalorg-api
- description: The Drupal GraphQL module is a contributed module that enables developers to craft and expose a GraphQL schema for Drupal 10 and 11, allowing client applications to query Drupal content and entities u
  name: Drupal GraphQL API
  slug: graphql
- baseURL: https://example.com
  baseurl_source: declared
  description: Comment resources for reading and managing comments attached to content entities in Drupal.
  name: drupal Comments API
  slug: drupal-comments-api
- baseURL: https://example.com
  baseurl_source: declared
  description: JSON:API endpoints for file entities and file upload operations.
  name: drupal Files API
  slug: drupal-files-api
- baseURL: https://example.com
  baseurl_source: declared
  description: JSON:API endpoints for article content nodes. The bundle slug varies by Drupal installation; article is shown as an example bundle name.
  name: drupal Node Articles API
  slug: drupal-node-articles-api
- baseURL: https://example.com
  baseurl_source: declared
  description: JSON:API endpoints for basic page content nodes. The bundle slug varies by Drupal installation.
  name: drupal Node Pages API
  slug: drupal-node-pages-api
- baseURL: https://example.com
  baseurl_source: declared
  description: Content node resources representing structured content items of any type (article, page, etc.) stored in Drupal's content management system.
  name: drupal Nodes API
  slug: drupal-nodes-api
- baseURL: https://example.com
  baseurl_source: declared
  description: JSON:API endpoints for taxonomy term entities across all configured vocabularies.
  name: drupal Taxonomy Terms API
  slug: drupal-taxonomy-terms-api
- baseURL: https://example.com
  baseurl_source: declared
  description: Taxonomy vocabulary resources representing the container configurations that organize sets of taxonomy terms.
  name: drupal Taxonomy Vocabularies API
  slug: drupal-taxonomy-vocabularies-api
- baseURL: https://example.com
  baseurl_source: declared
  description: JSON:API endpoints for Drupal user entities. Config entities are read-only via JSON:API and require authentication.
  name: drupal Users API
  slug: drupal-users-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Drupal JSON: Comments API'
  slug: open-drupal-comments-api
- collection_type: open
  name: 'Drupal JSON: Comments Files API'
  slug: open-drupal-files-api
- collection_type: open
  name: Drupal JSON:API
  slug: open-drupal-jsonapi
- collection_type: open
  name: 'Drupal JSON: Comments Node Articles API'
  slug: open-drupal-node-articles-api
- collection_type: open
  name: 'Drupal JSON: Comments Node Pages API'
  slug: open-drupal-node-pages-api
- collection_type: open
  name: 'Drupal JSON: Comments Nodes API'
  slug: open-drupal-nodes-api
- collection_type: open
  name: Drupal REST API
  slug: open-drupal-rest-api
- collection_type: open
  name: 'Drupal JSON: Comments Taxonomy Terms API'
  slug: open-drupal-taxonomy-terms-api
- collection_type: open
  name: 'Drupal JSON: Comments Taxonomy Vocabularies API'
  slug: open-drupal-taxonomy-vocabularies-api
- collection_type: open
  name: 'Drupal JSON: Comments Users API'
  slug: open-drupal-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://drupal.org
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/agentic-access/drupal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drupal-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/security/drupal-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drupal-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/security/drupal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drupal-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/authentication/drupal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drupal-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/scopes/drupal-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/drupal-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drupal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drupal-project
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/json-ld/drupal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/drupal-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/json-schema/drupal-node-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/drupal-node-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.drupal.org/planet/rss.xml
- group: docs
  title: ''
  type: Documentation
  url: https://www.drupal.org/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.drupal.org/docs/develop
- group: docs
  title: ''
  type: APIReference
  url: https://www.drupal.org/docs/develop/drupal-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.drupal.org/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.drupal.org/community
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drupal.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drupal.org/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.drupal.org/user/register
- group: auth
  title: ''
  type: Security
  url: https://www.drupal.org/security
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/packages/drupal-packages.yml
  title: ''
  type: Packages
  url: packages/drupal-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/cli/drupal-cli.yml
  title: ''
  type: CLI
  url: cli/drupal-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/mcp/drupal-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/drupal-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/mcp/drupal-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/drupal-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/llms/drupal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drupal-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/conformance/drupal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drupal-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/errors/drupal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drupal-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/lifecycle/drupal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/drupal-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.drupal.org/about/core/policies/core-change-policies/drupal-deprecation-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/changelog/drupal-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/drupal-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/conventions/drupal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drupal-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/data-model/drupal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drupal-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/well-known/drupal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drupal-well-known.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/rate-limits/drupal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/drupal-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/rules/drupal-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/drupal-jsonschema-spectral-rules.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/finops/drupal-finops.yml
  title: ''
  type: FinOps
  url: finops/drupal-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/overlays/drupal-node-articles-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/drupal-node-articles-api-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://www.drupal.org/about/licensing
created: '2026-05-04'
description: 'Drupal is an open-source content management system written in PHP, used to build websites, applications and digital experiences for individuals, organizations, governments and enterprises worldwide. It is self-hosted software rather than a hosted service: Drupal core ships a JSON:API v1.0 surface and a RESTful Web Services surface that run on the operator’s own domain, and contributed modules add GraphQL and an MCP server. The Drupal Association itself operates one public read-only API, the Drupal.org REST API at https://www.drupal.org/api-d7, alongside a machine-readable release-history feed and a Composer package repository.'
finops:
- name: Drupal Finops
  service_category: API
  slug: drupal-finops
graphqls:
- description: The Drupal GraphQL module is a contributed module that enables developers to craft and expose a GraphQL schema for Drupal 10 and 11, allowing client applications to query Drupal content and entities u
  name: drupal GraphQL API
  slug: drupal-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drupal.png
json_schemas:
- name: Drupal JSON:API Resource
  property_count: 6
  slug: drupal-jsonapi-resource
- name: Drupal Node
  property_count: 22
  slug: drupal-node
jsonld:
- class_count: 0
  name: Drupal Context
  property_count: 8
  slug: drupal-context
layout: provider
mcp_servers:
- description: ''
  name: Drupal MCP Server
  slug: drupal-mcp-server
modified: '2026-09-17'
name: Drupal
nav: Providers
network: true
overview: 'Drupal publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Files API, Node Articles API, and 5 more. Tagged areas include Content Management, CMS, Open-Source, JSON:API, and GraphQL.


  The Drupal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Drupal''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, signup flow, and 32 more developer resources.'
plans:
- name: Drupal Plans Pricing
  plan_count: 0
  slug: drupal-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Drupal Rate Limits
  slug: drupal-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Drupal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: drupal-jsonschema-spectral-rules
scopes:
- name: Drupal Scopes
  scope_count: 2
  slug: drupal-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.3
    catalog_earned_first_party: 8.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.6
  facets:
    access_clarity: 42.1
    contract_governance: 14.4
    contract_quality: 65.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/screenshots/drupal-2026-06-20T180306.png
security:
- kind: authentication
  name: Drupal Authentication
  slug: drupal-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Drupal Domain Security
  slug: drupal-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Drupal Vulnerability Disclosure
  slug: drupal-vulnerability-disclosure
  summary_line: disclosure policy published
slug: drupal
tags:
- Content Management
- CMS
- Open-Source
- JSON:API
- GraphQL
- Headless
- PHP
- Self-Hosted
- Publishing
- Digital Experience
website: https://drupal.org
---
