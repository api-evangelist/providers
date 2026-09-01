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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: The Libcloud Compute API provides a unified Python interface for managing virtual machine instances, images, sizes, and networks across AWS EC2, Azure, GCP, DigitalOcean, Linode, and 25+ other provide
  name: Apache Libcloud Compute API
  slug: compute-api
- description: The Libcloud Storage API provides a unified Python interface for object storage operations across AWS S3, Azure Blob Storage, GCP Cloud Storage, Rackspace Cloud Files, and OpenStack Swift.
  name: Apache Libcloud Storage API
  slug: storage-api
- description: The Libcloud DNS API provides a unified Python interface for managing DNS zones and records across Route53, Azure DNS, Google Cloud DNS, and other providers.
  name: Apache Libcloud DNS API
  slug: dns-api
artifact_total: 21
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/libcloud/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/libcloud/blob/trunk/CONTRIBUTING.rst
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/libcloud/blob/trunk/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-libcloud-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-libcloud
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/libcloud
- group: docs
  title: ''
  type: Documentation
  url: https://libcloud.readthedocs.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://libcloud.readthedocs.io/en/stable/getting_started.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://libcloud.readthedocs.io/en/stable/changelog.html
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/apache-libcloud/
- group: company
  title: ''
  type: Blog
  url: https://libcloud.apache.org/blog/atom.xml
created: '2026-03-16'
description: Apache Libcloud is a Python library for interacting with many popular cloud service providers using a unified API. It supports over 30 providers for compute, object storage, DNS, load balancers, and container services under the Apache 2.0 license.
features:
- description: Unified Python API across 30+ cloud providers with no vendor lock-in.
  name: Multi-Cloud Portability
- description: Create, delete, and manage VMs and images across cloud providers.
  name: Compute Management
- description: Unified blob/object storage API across all major cloud storage providers.
  name: Object Storage
- description: Manage DNS zones and records across cloud DNS providers.
  name: DNS Management
- description: Unified load balancer management across cloud providers.
  name: Load Balancer API
- description: Docker container management via Libcloud container API.
  name: Container API
finops:
- name: Apache Libcloud Finops
  service_category: API
  slug: apache-libcloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-libcloud.png
integrations:
- description: EC2 compute, S3 storage, Route53 DNS, and ELB load balancer support.
  name: Amazon Web Services
- description: Azure Compute, Blob Storage, and Azure DNS integration.
  name: Microsoft Azure
- description: GCP Compute Engine, Cloud Storage, and Cloud DNS support.
  name: Google Cloud Platform
- description: Full OpenStack Nova, Swift, and Neutron integration.
  name: OpenStack
- description: DigitalOcean Droplets, Spaces, and DNS support.
  name: DigitalOcean
layout: provider
modified: '2026-04-19'
name: Apache Libcloud
nav: Providers
network: true
overview: 'Apache Libcloud publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Abstraction Layer, Cloud, Multi-Cloud, Open-Source, and Python.


  Apache Libcloud''s developer surface includes documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Apache Libcloud Plans Pricing
  plan_count: 3
  slug: apache-libcloud-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Apache Libcloud Rate Limits
  slug: apache-libcloud-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 23.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-libcloud/refs/heads/main/screenshots/apache-libcloud-2026-06-20T172117.png
security:
- kind: domain-security
  name: Apache Libcloud Domain Security
  slug: apache-libcloud-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apache-libcloud
tags:
- Abstraction Layer
- Cloud
- Multi-Cloud
- Open-Source
- Python
use_cases:
- description: Manage cloud infrastructure across multiple providers from a single Python codebase.
  name: Multi-Cloud Infrastructure
- description: Migrate cloud workloads between providers with minimal code changes.
  name: Cloud Provider Migration
- description: Automate VM provisioning, storage, and DNS across cloud providers.
  name: Infrastructure Automation
---
