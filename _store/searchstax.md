---
aid: searchstax
url: https://raw.githubusercontent.com/api-evangelist/searchstax/refs/heads/main/apis.yml
apis:
  - aid: searchstax:searchstax-provisioning-api
    name: SearchStax Provisioning API
    tags:
      - Provisioning
      - Solr
      - Deployments
      - Infrastructure
    humanURL: https://www.searchstax.com/docs/searchstax-cloud-apis-overview/
    baseURL: https://app.searchstax.com/api/rest/v2
    properties:
      - url: openapi/searchstax-provisioning-openapi.yml
        type: OpenAPI
      - url: https://www.searchstax.com/docs/searchstax-cloud-apis-overview/
        type: Documentation
      - url: https://www.searchstax.com/docs/searchstax-cloud-deployment-api/
        type: Documentation
    description: The SearchStax Provisioning API is a REST interface for creating and managing Solr deployments in the SearchStax Managed Search cloud. It supports deployment lifecycle management, backup and restore operations, node management, plan listing, usage reporting, authentication configuration, webhook management, and ZooKeeper configuration. Token-based authentication is used for most operations, with API key authentication available for a subset of deployment management functions.
  - aid: searchstax:searchstax-site-search-api
    name: SearchStax Site Search API
    tags:
      - Search
      - Site Search
      - Studio
      - Full-Text Search
    humanURL: https://www.searchstax.com/docs/searchstudio/searchstax-studio-search-api/
    baseURL: https://search.searchstax.com
    properties:
      - url: https://www.searchstax.com/docs/searchstudio/searchstax-studio-search-api/
        type: Documentation
    description: The SearchStax Site Search API returns JSON search results from a SearchStax Studio Site Search application. It provides real-time search via the /emselect endpoint, supporting faceted search, auto-suggest, popular searches, related searches, and search analytics tracking.
name: SearchStax
tags:
  - Search
  - Solr
  - Managed Search
  - Search Infrastructure
  - Full-Text Search
  - Site Search
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-02'
modified: '2026-05-02'
position: Consuming
description: SearchStax is a managed Solr search infrastructure company that provides cloud-hosted Apache Solr deployments and a Site Search platform. SearchStax eliminates the complexity of running and scaling Solr by offering fully managed dedicated and serverless deployments on AWS, Azure, and Google Cloud. The platform exposes a comprehensive REST Provisioning API for managing deployments, backup and restore, authentication, webhooks, and infrastructure configuration, along with a Site Search API for delivering search results from SearchStax Studio applications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Website
    url: https://www.searchstax.com
    type: Website
  - name: API Library Overview
    url: https://www.searchstax.com/docs/hc/searchstax-api-library/
    type: Documentation
  - name: Managed Search APIs Overview
    url: https://www.searchstax.com/docs/searchstax-cloud-apis-overview/
    type: Documentation
  - name: GitHub Organization
    url: https://github.com/searchstax
    type: GitHubOrganization
  - name: Deployment API Documentation
    url: https://www.searchstax.com/docs/searchstax-cloud-deployment-api/
    type: Documentation
  - name: Backup Restore API
    url: https://www.searchstax.com/docs/searchstax-cloud-backup-restore-api/
    type: Documentation
  - name: Authentication API
    url: https://www.searchstax.com/docs/searchstax-cloud-authentication-api/
    type: Documentation
  - url: json-schema/searchstax-deployment-schema.json
    type: JSONSchema
  - url: json-structure/searchstax-deployment-structure.json
    type: JSONStructure
  - url: json-ld/searchstax-context.jsonld
    type: JSONLDContext
  - url: examples/searchstax-list-deployments-example.json
    type: Example
  - url: rules/searchstax-rules.yml
    type: SpectralRuleset
  - url: capabilities/search-infrastructure-management.yaml
    type: NaftikoCapability
  - url: vocabulary/searchstax-vocabulary.yml
    type: Vocabulary
---
