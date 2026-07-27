---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Hadoop Agentic Access
  operation_count: 17
  slug: hadoop-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 6
apis:
- description: REST API for accessing MapReduce job history and statistics.
  name: MapReduce History Server REST API
  slug: mapreduce-history-server-api
- description: HTTP REST API gateway supporting both webhdfs and httpfs operations for HDFS access.
  name: HttpFS REST API
  slug: httpfs-rest-api
- description: HDFS filesystem REST operations under /webhdfs/v1.
  name: Apache Hadoop WebHDFS API
  slug: hadoop-webhdfs-api
- description: Application listing, submission, and lifecycle.
  name: Apache Hadoop YARN Applications API
  slug: hadoop-yarn-applications-api
- description: Cluster information and metrics.
  name: Apache Hadoop YARN Cluster API
  slug: hadoop-yarn-cluster-api
- description: Cluster node listing and resource updates.
  name: Apache Hadoop YARN Nodes API
  slug: hadoop-yarn-nodes-api
artifact_total: 13
collections:
- collection_type: open
  name: Apache Hadoop REST APIs
  slug: open-hadoop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hadoop-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hadoop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hadoop-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/hadoop
- group: company
  title: ''
  type: Website
  url: https://hadoop.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://hadoop.apache.org/docs/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/hadoop
- group: operate
  title: ''
  type: Community
  url: https://hadoop.apache.org/mailing_lists.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://hadoop.apache.org/releases.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2024-01-15'
description: Apache Hadoop is an open-source framework for distributed storage and processing of large datasets across clusters of computers using simple programming models. It includes HDFS for distributed storage, YARN for resource management, and MapReduce for parallel data processing.
finops:
- name: Hadoop Finops
  service_category: API
  slug: hadoop-finops
image: https://hadoop.apache.org/hadoop-logo.jpg
layout: provider
modified: '2026-05-19'
name: Apache Hadoop
nav: Providers
network: true
overview: 'Apache Hadoop publishes 4 APIs on the [APIs.io](https://apis.io/) network, including WebHDFS API, YARN Applications API, YARN Cluster API, and 1 more. Tagged areas include Big Data, Data Processing, Distributed Computing, HDFS, and MapReduce.


  Apache Hadoop''s developer surface includes documentation, getting-started guide, changelog, and 8 more developer resources.'
plans:
- name: Hadoop Plans Pricing
  plan_count: 3
  slug: hadoop-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Hadoop Rate Limits
  slug: hadoop-rate-limits
score:
  band: thin
  composite: 41.5
  delta: 2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 44.7
    developer_ergonomics: 23.9
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 39.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hadoop/refs/heads/main/screenshots/hadoop-2026-06-20T182452.png
security:
- kind: domain-security
  name: Hadoop Domain Security
  slug: hadoop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hadoop Vulnerability Disclosure
  slug: hadoop-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hadoop
tags:
- Big Data
- Data Processing
- Distributed Computing
- HDFS
- MapReduce
- Open Source
website: https://hadoop.apache.org/
---
