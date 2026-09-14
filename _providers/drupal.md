---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Drupal Agentic Access
  operation_count: 33
  slug: drupal-agentic-access
  summary_line: 33 operations · 17 acting
api_count: 2
apis:
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
artifact_total: 33
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drupal-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drupal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drupal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drupal-authentication.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/drupal-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/drupal-node-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.drupal.org/planet/rss.xml
description: Drupal is an open-source content management system written in PHP and used to build websites, applications, and digital experiences for individuals, organizations, and enterprises worldwide.
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
modified: '2026-05-19'
name: Drupal
nav: Providers
network: true
overview: 'Drupal publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Files API, Node Articles API, and 5 more.


  The Drupal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Drupal''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Drupal Plans Pricing
  plan_count: 3
  slug: drupal-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
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
---
