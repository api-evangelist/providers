---
aid: elastic
name: Elastic
description: Elastic is a software company that builds search-powered solutions for observability, security, and search use cases. The Elastic Stack (Elasticsearch, Kibana, and related tools) lets organizations ingest, search, analyze, and visualize structured and unstructured data in real time. Elastic Cloud delivers managed Elasticsearch and Kibana deployments with REST APIs for both data operations and deployment management.
type: Index
position: Producer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Search
  - Analytics
  - Observability
  - Security
  - Visualization
  - Cloud
created: '2025-01-08'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/elastic/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: elastic:elasticsearch
    name: Elasticsearch REST API
    description: The Elasticsearch REST API powers indexing, search, and cluster administration for the Elasticsearch search and analytics engine. It exposes operations for indexing documents, running queries, managing indices and mappings, snapshots, security roles and API keys, and cluster health.
    humanURL: https://www.elastic.co/docs/api/doc/elasticsearch
    baseURL: https://api.elastic-cloud.com
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Search
      - Analytics
      - Indexing
      - Documents
      - Cluster
    properties:
      - type: Documentation
        url: https://www.elastic.co/docs/api/doc/elasticsearch
      - type: OpenAPI
        url: openapi/elastic-elasticsearch-openapi.yml
  - aid: elastic:kibana
    name: Kibana API
    description: The Kibana REST API manages Kibana resources including saved objects, data views, Spaces, connectors, and alerting rules. Calls are stateless and use the same authentication mechanisms as Elasticsearch.
    humanURL: https://www.elastic.co/docs/api/doc/kibana
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Visualization
      - Dashboards
      - SavedObjects
      - DataViews
    properties:
      - type: Documentation
        url: https://www.elastic.co/docs/api/doc/kibana
      - type: OpenAPI
        url: openapi/elastic-kibana-openapi.yml
  - aid: elastic:elastic-cloud
    name: Elastic Cloud API
    description: The Elastic Cloud API manages hosted Elasticsearch and Kibana deployments. It supports creating, updating, resizing, snapshotting, and deleting deployments, plus traffic filter and account-level operations.
    humanURL: https://www.elastic.co/docs/api/doc/cloud
    baseURL: https://api.elastic-cloud.com
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Cloud
      - Deployments
      - Provisioning
      - TrafficFilters
    properties:
      - type: Documentation
        url: https://www.elastic.co/docs/api/doc/cloud
      - type: OpenAPI
        url: openapi/elastic-cloud-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - name: Elastic Website
    url: https://www.elastic.co
    type: Website
  - name: Elastic Documentation
    url: https://www.elastic.co/guide/index.html
    type: Documentation
  - name: Elastic GitHub Organization
    url: https://github.com/elastic
    type: GitHub
  - name: Elastic Cloud Console
    url: https://cloud.elastic.co
    type: Console
  - name: Elastic Pricing
    url: https://www.elastic.co/pricing
    type: Pricing
  - name: Elastic License
    url: https://www.elastic.co/licensing/elastic-license
    type: License
  - type: Features
    data:
      - 'Elastic Cloud Hosted: resource-based with Standard/Gold/Platinum/Enterprise tiers'
      - 'Elastic Serverless: VCU + storage usage-based for Search/Observability/Security'
      - 'Self-managed: license-based for on-prem deployment'
      - 'Multi-cloud: AWS, GCP, Azure'
      - REST API for Elasticsearch, Kibana, APM
      - Bulk indexing API for high-throughput ingest
      - Throughput scales with cluster hardware
      - OAuth + API keys + JWT realm
      - Watcher for alerting on rules
      - ES|QL query language
      - Vector search with kNN
      - ELSER (Elastic Learned Sparse Encoder) for semantic search
      - Cross-cluster search/replication
      - Hot/Warm/Cold/Frozen data tiers
      - Index Lifecycle Management (ILM)
      - 'Compliance: SOC 2, HIPAA, FedRAMP (Enterprise)'
    sources:
      - https://www.elastic.co/pricing
    updated: '2026-05-04'
---
