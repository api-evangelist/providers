---
aid: opensearch
name: OpenSearch
description: OpenSearch is the open source, community-driven search, analytics, and observability suite (forked from Elasticsearch and Kibana) maintained under the Linux Foundation's OpenSearch Software Foundation. The platform exposes REST APIs across the search engine, the OpenSearch Dashboards UI, and a set of plugins. The Security plugin REST API lets administrators programmatically create and manage internal users, roles, role mappings, action groups, tenants, security configuration, audit log configuration, and SSL certificates.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Search
  - Analytics
  - Observability
  - Open Source
  - Security
created: '2025-01-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/opensearch/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: opensearch:opensearch-security-api
    name: OpenSearch Security Plugin REST API
    description: The Security plugin REST API lets administrators programmatically create and manage internal users, roles, role mappings, action groups, tenants, security configuration, audit log configuration, allowlists, node DN entries, and SSL certificates. Endpoints are exposed under /_plugins/_security/api on the OpenSearch cluster and require authentication.
    humanURL: https://docs.opensearch.org/latest/security/access-control/api/
    baseURL: https://{cluster-host}:9200
    tags:
      - Security
      - Access Control
      - Roles
      - Authentication
    properties:
      - type: Documentation
        url: https://docs.opensearch.org/latest/security/access-control/api/
      - type: Documentation
        url: https://docs.opensearch.org/latest/security/access-control/index/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/opensearch/refs/heads/main/openapi/opensearch-security-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/opensearch/refs/heads/main/json-schema/opensearch-role-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/opensearch/refs/heads/main/json-ld/opensearch-context.jsonld
  - aid: opensearch:opensearch-search-api
    name: OpenSearch Search and Indexing REST API
    description: The core OpenSearch REST API for indexing documents, performing search queries (full text, vector, hybrid), aggregations, and managing indices, mappings, templates, aliases, and snapshots.
    humanURL: https://docs.opensearch.org/latest/api-reference/
    baseURL: https://{cluster-host}:9200
    tags:
      - Search
      - Indexing
      - Vector Search
      - Aggregations
    properties:
      - type: Documentation
        url: https://docs.opensearch.org/latest/api-reference/
      - type: Documentation
        url: https://docs.opensearch.org/latest/search-plugins/
      - type: Reference
        url: https://docs.opensearch.org/latest/api-reference/search/
common:
  - url: https://opensearch.org/
    name: OpenSearch
    type: Website
  - url: https://docs.opensearch.org/
    name: Documentation Portal
    type: Portal
  - url: https://docs.opensearch.org/latest/api-reference/
    name: API Reference
    type: Documentation
  - url: https://docs.opensearch.org/latest/getting-started/
    name: Getting Started
    type: GettingStarted
  - url: https://opensearch.org/community/
    name: Community
    type: Community
  - url: https://forum.opensearch.org/
    name: Discussion Forum
    type: Forum
  - url: https://opensearch.org/blog/
    name: Blog
    type: Blog
  - url: https://github.com/opensearch-project
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/opensearch-project/security
    name: Security Plugin Source
    type: GitHubRepository
  - url: https://github.com/opensearch-project/OpenSearch
    name: OpenSearch Core Source
    type: GitHubRepository
  - url: https://opensearch.org/downloads/
    name: Downloads
    type: Download
  - url: https://opensearch.org/license.html
    name: License (Apache 2.0)
    type: License
  - url: https://opensearch.org/security
    name: Security Advisories
    type: Security
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
