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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Apache Software Foundation hosts 300+ open source projects spanning big data, cloud, messaging, databases, build tools, and more. The ASF provides infrastructure, governance, and community support
  name: Apache Software Foundation
  slug: apache-software-foundation
artifact_total: 21
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apache/refs/heads/main/plans/apache-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apache-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apache/refs/heads/main/rate-limits/apache-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apache-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apache/refs/heads/main/finops/apache-finops.yml
  title: ''
  type: FinOps
  url: finops/apache-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apache/refs/heads/main/security/apache-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apache/refs/heads/main/security/apache-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apache-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-apache-software-foundation
- group: company
  title: ''
  type: Website
  url: https://www.apache.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: docs
  title: ''
  type: Documentation
  url: https://www.apache.org/dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://community.apache.org/newcomers/
- group: company
  title: ''
  type: Blog
  url: https://news.apache.org
- group: operate
  title: ''
  type: Support
  url: https://www.apache.org/foundation/mailinglists.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/apache/nutch/blob/c16be5f0c5f6132bc229dcd6820c4c09d952655f/.spectral.yaml
created: '2025-01-01'
description: The Apache Software Foundation (ASF) is a 501(c)(3) nonprofit organization that provides open source software for the public good. Home to more than 300 open source projects maintained by a global community of over 9,900 committers and 1,190 members, the ASF operates under the principle of community over code. Projects span big data, cloud infrastructure, messaging, web frameworks, databases, build tooling, machine learning, and more — all released under the Apache License.
features:
- description: Home to over 300 open source projects spanning big data, cloud infrastructure, messaging, databases, web frameworks, and more.
  name: 300+ Open Source Projects
- description: All ASF software is released under the Apache License 2.0, a permissive open source license compatible with most ecosystems.
  name: Apache License
- description: Maintained by 9,900+ committers and 1,190+ members from around the world operating under the principle of community over code.
  name: Global Community
- description: The Apache Incubator provides mentorship and infrastructure for new open source projects seeking to join the ASF ecosystem.
  name: Project Incubator
- description: The ASF manages 1,300+ software releases with formal release voting and cryptographic signing processes ensuring software integrity.
  name: Release Management
finops:
- has_sources: false
  method: generated
  name: Apache Finops
  primary_unit: ''
  service_category: API
  slug: apache-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache.png
integrations:
- description: Apache projects integrate with AWS, Azure, and Google Cloud for cloud-native deployments and managed service offerings.
  name: Cloud Platforms
- description: Many ASF projects support Kubernetes deployments via Helm charts and Kubernetes operators for containerized workloads.
  name: Kubernetes
- description: Deep integration with the Java ecosystem including Maven, Gradle, and major JVM frameworks and runtime environments.
  name: Java Ecosystem
- description: Apache projects like Airflow, Arrow, and Superset provide first-class Python support and PyPI packages.
  name: Python Ecosystem
layout: provider
modified: '2026-04-19'
name: Apache Software Foundation
nav: Providers
network: true
overview: 'Apache Software Foundation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source, Apache, Foundations, Software, and Fortune 500.


  The Apache Software Foundation catalog on APIs.io includes 1 Spectral governance ruleset.


  Apache Software Foundation''s developer surface includes documentation, getting-started guide, engineering blog, support, and 10 more developer resources.'
plans:
- name: Apache Plans Pricing
  plan_count: 3
  slug: apache-plans-pricing
press:
- date: ''
  title: The Apache Software Foundation Launches $10M ...
  url: https://news.apache.org/foundation/entry/the-apache-software-foundation-launches-10m-responsible-ai-initiative-with-initial-1-75m-donation
- date: ''
  title: Press Releases
  url: https://www.dremio.com/press-releases/
- date: ''
  title: Press Room
  url: https://www.alibabacloud.com/en/press-room?_p_lc=1
- date: ''
  title: Commvault Delivers Industry-First Cyber Resilience for AI ...
  url: https://www.prnewswire.com/news-releases/commvault-delivers-industry-first-cyber-resilience-for-ai-data-lakehouses-on-aws-with-support-for-apache-iceberg-tables-302570244.html
- date: ''
  title: The Apache Software Foundation Launches Responsible ...
  url: https://www.hpcwire.com/aiwire/2026/04/10/the-apache-software-foundation-launches-responsible-ai-initiative/
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apache Rate Limits
  slug: apache-rate-limits
rules:
- authorship: provider
  effective_rule_count: 0
  extends:
  - '@ibm-cloud/openapi-ruleset'
  name: Apache Software Foundation — nutch rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: apache-nutch-spectral-rules
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/apache/refs/heads/main/screenshots/apache-2026-06-20T172036.png
security:
- kind: domain-security
  name: Apache Domain Security
  slug: apache-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Vulnerability Disclosure
  slug: apache-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache
tags:
- Open Source
- Apache
- Foundations
- Software
- Fortune 500
use_cases:
- description: Process and analyze large-scale datasets using Apache Hadoop, Spark, Flink, Kafka, Arrow, and related ecosystem tools.
  name: Big Data Processing
- description: Route and manage API traffic with Apache APISIX and other gateway projects from the Apache ecosystem.
  name: API Gateway and Traffic Management
- description: Schedule and monitor data pipelines and workflows using Apache Airflow, Oozie, and related orchestration tools.
  name: Workflow Orchestration
- description: Build event-driven architectures using Apache Kafka, ActiveMQ, and Pulsar for high-throughput message streaming.
  name: Message Streaming
- description: Store and query data with Apache Cassandra, HBase, Accumulo, CouchDB, and other distributed database projects.
  name: Database and Storage
website: https://www.apache.org
---
