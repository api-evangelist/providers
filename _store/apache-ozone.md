---
aid: apache-ozone
name: Apache Ozone
description: Apache Ozone is a scalable, redundant, and distributed object store optimized for big data workloads. It provides an S3-compatible interface and a Hadoop-compatible file system interface for seamless integration with existing big data tools.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Storage
  - Hadoop
  - Object Storage
  - S3-Compatible
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-ozone/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-ozone:apache-ozone
    name: Apache Ozone
    description: Ozone provides an S3-compatible REST API for object storage operations, a Hadoop-compatible File System API (o3fs, ofs), a Java client API for bucket and key management, and a Recon REST API for cluster monitoring.
    humanURL: https://ozone.apache.org/docs/current/
    tags:
      - Hadoop
      - Object Storage
      - REST
      - S3
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://ozone.apache.org/docs/current/
      - type: OpenAPI
        url: openapi/apache-ozone-s3-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/ozone
  - type: Documentation
    url: https://ozone.apache.org/
  - type: SpectralRules
    url: rules/apache-ozone-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-ozone-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ozone-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-ozone-context.jsonld
  - type: Features
    data:
      - name: S3-Compatible API
        description: Fully compatible with Amazon S3 API for object storage operations
      - name: HDFS-Compatible
        description: Hadoop-compatible file system interface (o3fs, ofs) for existing Hadoop workloads
      - name: Multi-Tenant
        description: Volume/bucket hierarchy with multi-tenant access controls
      - name: Replication
        description: Configurable replication for data durability
      - name: Erasure Coding
        description: Erasure coding support for storage efficiency
      - name: Scalability
        description: Scale to billions of files with petabytes of data
  - type: UseCases
    data:
      - name: Data Lake Storage
        description: Store raw data in a highly scalable and S3-compatible data lake
      - name: Hadoop Migration
        description: Replace HDFS with Ozone for petabyte-scale Hadoop clusters
      - name: Application Object Storage
        description: Use S3-compatible API for application file and media storage
      - name: Backup and Archive
        description: Cost-effective backup and long-term data archival
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Native HDFS-compatible file system integration
      - name: Apache Spark
        description: Direct Spark data source for reading and writing ORC/Parquet
      - name: Apache Hive
        description: Hive metastore integration for data lake querying
      - name: Amazon S3 SDK
        description: Compatible with AWS SDK for S3 operations
      - name: Kubernetes
        description: Container-native deployment with CSI driver support
---
