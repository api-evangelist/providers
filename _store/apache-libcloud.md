---
aid: apache-libcloud
name: Apache Libcloud
description: Apache Libcloud is a Python library for interacting with many popular cloud service providers using a unified API. It supports over 30 providers for compute, object storage, DNS, load balancers, and container services under the Apache 2.0 license.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Abstraction Layer
  - Cloud
  - Multi-Cloud
  - Open Source
  - Python
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-libcloud/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-libcloud:compute-api
    name: Apache Libcloud Compute API
    description: The Libcloud Compute API provides a unified Python interface for managing virtual machine instances, images, sizes, and networks across AWS EC2, Azure, GCP, DigitalOcean, Linode, and 25+ other providers.
    humanURL: https://libcloud.readthedocs.io/en/stable/compute/
    tags:
      - Cloud
      - Compute
      - Python
      - VM Management
    properties:
      - type: Documentation
        url: https://libcloud.readthedocs.io/en/stable/compute/
      - type: SDK
        url: https://pypi.org/project/apache-libcloud/
  - aid: apache-libcloud:storage-api
    name: Apache Libcloud Storage API
    description: The Libcloud Storage API provides a unified Python interface for object storage operations across AWS S3, Azure Blob Storage, GCP Cloud Storage, Rackspace Cloud Files, and OpenStack Swift.
    humanURL: https://libcloud.readthedocs.io/en/stable/storage/
    tags:
      - Cloud
      - Object Storage
      - Python
    properties:
      - type: Documentation
        url: https://libcloud.readthedocs.io/en/stable/storage/
  - aid: apache-libcloud:dns-api
    name: Apache Libcloud DNS API
    description: The Libcloud DNS API provides a unified Python interface for managing DNS zones and records across Route53, Azure DNS, Google Cloud DNS, and other providers.
    humanURL: https://libcloud.readthedocs.io/en/stable/dns/
    tags:
      - Cloud
      - DNS
      - Python
    properties:
      - type: Documentation
        url: https://libcloud.readthedocs.io/en/stable/dns/
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/libcloud
  - type: Documentation
    url: https://libcloud.readthedocs.io/
  - type: GettingStarted
    url: https://libcloud.readthedocs.io/en/stable/getting_started.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://libcloud.readthedocs.io/en/stable/changelog.html
  - type: SDK
    url: https://pypi.org/project/apache-libcloud/
  - type: Features
    data:
      - name: Multi-Cloud Portability
        description: Unified Python API across 30+ cloud providers with no vendor lock-in.
      - name: Compute Management
        description: Create, delete, and manage VMs and images across cloud providers.
      - name: Object Storage
        description: Unified blob/object storage API across all major cloud storage providers.
      - name: DNS Management
        description: Manage DNS zones and records across cloud DNS providers.
      - name: Load Balancer API
        description: Unified load balancer management across cloud providers.
      - name: Container API
        description: Docker container management via Libcloud container API.
  - type: UseCases
    data:
      - name: Multi-Cloud Infrastructure
        description: Manage cloud infrastructure across multiple providers from a single Python codebase.
      - name: Cloud Provider Migration
        description: Migrate cloud workloads between providers with minimal code changes.
      - name: Infrastructure Automation
        description: Automate VM provisioning, storage, and DNS across cloud providers.
  - type: Integrations
    data:
      - name: Amazon Web Services
        description: EC2 compute, S3 storage, Route53 DNS, and ELB load balancer support.
      - name: Microsoft Azure
        description: Azure Compute, Blob Storage, and Azure DNS integration.
      - name: Google Cloud Platform
        description: GCP Compute Engine, Cloud Storage, and Cloud DNS support.
      - name: OpenStack
        description: Full OpenStack Nova, Swift, and Neutron integration.
      - name: DigitalOcean
        description: DigitalOcean Droplets, Spaces, and DNS support.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
