---
aid: apache-jclouds
name: Apache Jclouds
description: Apache jclouds is an open-source multi-cloud toolkit for the Java platform that provides a portable abstraction for cloud APIs. It supports over 30 cloud providers including AWS, Azure, GCP, Rackspace, and OpenStack for compute, blobstore, and DNS operations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Abstraction Layer
  - Cloud
  - Java
  - Multi-Cloud
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-jclouds/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-jclouds:compute-api
    name: Apache Jclouds Compute API
    description: The jclouds Compute API provides a unified Java interface for managing virtual machine instances, images, hardware profiles, and networking across 30+ cloud providers including AWS EC2, Azure Compute, GCP, DigitalOcean, and OpenStack.
    humanURL: https://jclouds.apache.org/start/compute/
    tags:
      - Cloud
      - Compute
      - Java
      - VM Management
    properties:
      - type: Documentation
        url: https://jclouds.apache.org/start/compute/
      - type: GettingStarted
        url: https://jclouds.apache.org/start/
  - aid: apache-jclouds:blobstore-api
    name: Apache Jclouds BlobStore API
    description: The jclouds BlobStore API provides a unified Java interface for object storage operations across AWS S3, Azure Blob Storage, GCP Cloud Storage, Rackspace Cloud Files, and OpenStack Swift.
    humanURL: https://jclouds.apache.org/start/blobstore/
    tags:
      - Blob Storage
      - Cloud
      - Java
      - Object Storage
    properties:
      - type: Documentation
        url: https://jclouds.apache.org/start/blobstore/
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/jclouds
  - type: Documentation
    url: https://jclouds.apache.org/documentation/
  - type: GettingStarted
    url: https://jclouds.apache.org/start/
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://jclouds.apache.org/releasenotes/
  - type: SDK
    url: https://search.maven.org/search?q=g:org.apache.jclouds
  - type: Features
    data:
      - name: Multi-Cloud Portability
        description: Write cloud code once and run it across 30+ providers without modification.
      - name: Compute API
        description: Unified API for VM lifecycle management across all supported cloud providers.
      - name: BlobStore API
        description: Unified object storage API across AWS S3, Azure, GCP, and OpenStack Swift.
      - name: Provider Abstraction
        description: Provider-specific APIs available alongside portable abstractions.
      - name: Async Support
        description: Asynchronous operations using Java Futures for non-blocking cloud calls.
  - type: UseCases
    data:
      - name: Multi-Cloud Deployments
        description: Deploy applications across multiple cloud providers with a single codebase.
      - name: Cloud Migration
        description: Migrate workloads between cloud providers using portable APIs.
      - name: Cloud Cost Optimization
        description: Switch cloud providers transparently based on pricing or availability.
  - type: Integrations
    data:
      - name: AWS EC2 and S3
        description: Full compute and object storage support for Amazon Web Services.
      - name: Microsoft Azure
        description: Azure Compute and Blob Storage integration.
      - name: Google Cloud Platform
        description: GCP Compute Engine and Cloud Storage integration.
      - name: OpenStack
        description: Full OpenStack Nova compute and Swift object storage support.
      - name: DigitalOcean
        description: DigitalOcean Droplets and Spaces support via jclouds provider.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
