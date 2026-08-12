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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The jclouds Compute API provides a unified Java interface for managing virtual machine instances, images, hardware profiles, and networking across 30+ cloud providers including AWS EC2, Azure Compute,
  name: Apache Jclouds Compute API
  slug: compute-api
- description: The jclouds BlobStore API provides a unified Java interface for object storage operations across AWS S3, Azure Blob Storage, GCP Cloud Storage, Rackspace Cloud Files, and OpenStack Swift.
  name: Apache Jclouds BlobStore API
  slug: blobstore-api
artifact_total: 20
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/jclouds/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-jclouds-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-jclouds-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/jclouds
- group: docs
  title: ''
  type: Documentation
  url: https://jclouds.apache.org/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://jclouds.apache.org/start/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://jclouds.apache.org/releasenotes/
- group: build
  title: ''
  type: SDKs
  url: https://search.maven.org/search?q=g:org.apache.jclouds
- group: company
  title: ''
  type: Blog
  url: https://jclouds.apache.org/releasenotes/atom.xml
created: '2026-03-16'
description: Apache jclouds is an open-source multi-cloud toolkit for the Java platform that provides a portable abstraction for cloud APIs. It supports over 30 cloud providers including AWS, Azure, GCP, Rackspace, and OpenStack for compute, blobstore, and DNS operations.
features:
- description: Write cloud code once and run it across 30+ providers without modification.
  name: Multi-Cloud Portability
- description: Unified API for VM lifecycle management across all supported cloud providers.
  name: Compute API
- description: Unified object storage API across AWS S3, Azure, GCP, and OpenStack Swift.
  name: BlobStore API
- description: Provider-specific APIs available alongside portable abstractions.
  name: Provider Abstraction
- description: Asynchronous operations using Java Futures for non-blocking cloud calls.
  name: Async Support
finops:
- name: Apache Jclouds Finops
  service_category: API
  slug: apache-jclouds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-jclouds.png
integrations:
- description: Full compute and object storage support for Amazon Web Services.
  name: AWS EC2 and S3
- description: Azure Compute and Blob Storage integration.
  name: Microsoft Azure
- description: GCP Compute Engine and Cloud Storage integration.
  name: Google Cloud Platform
- description: Full OpenStack Nova compute and Swift object storage support.
  name: OpenStack
- description: DigitalOcean Droplets and Spaces support via jclouds provider.
  name: DigitalOcean
layout: provider
modified: '2026-04-19'
name: Apache Jclouds
nav: Providers
network: true
overview: 'Apache Jclouds publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Abstraction Layer, Cloud, Java, Multi-Cloud, and Open Source.


  Apache Jclouds'' developer surface includes documentation, getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Apache Jclouds Plans Pricing
  plan_count: 3
  slug: apache-jclouds-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Apache Jclouds Rate Limits
  slug: apache-jclouds-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: -7.8
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 28.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-jclouds/refs/heads/main/screenshots/apache-jclouds-2026-06-20T172111.png
security:
- kind: domain-security
  name: Apache Jclouds Domain Security
  slug: apache-jclouds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Jclouds Vulnerability Disclosure
  slug: apache-jclouds-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-jclouds
tags:
- Abstraction Layer
- Cloud
- Java
- Multi-Cloud
- Open Source
use_cases:
- description: Deploy applications across multiple cloud providers with a single codebase.
  name: Multi-Cloud Deployments
- description: Migrate workloads between cloud providers using portable APIs.
  name: Cloud Migration
- description: Switch cloud providers transparently based on pricing or availability.
  name: Cloud Cost Optimization
---
