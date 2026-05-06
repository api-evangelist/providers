---
aid: backblaze
url: https://raw.githubusercontent.com/api-evangelist/backblaze/refs/heads/main/apis.yml
apis:
  - aid: backblaze:backblaze-b2-cloud-storage-api
    name: Backblaze B2 Cloud Storage API
    tags:
      - Cloud Storage
      - Object Storage
      - Storage
    humanURL: https://www.backblaze.com/b2/cloud-storage.html
    properties:
      - type: Documentation
        url: https://www.backblaze.com/apidocs/introduction-to-the-b2-native-api
      - type: GettingStarted
        url: https://www.backblaze.com/docs/cloud-storage-native-api
      - type: OpenAPI
        url: openapi/backblaze-b2-native-api.yaml
    description: The Backblaze B2 Native API provides programmatic access to all B2 Cloud Storage functions including account authorization, bucket management, file upload and download, large file multi-part uploads, application key management, lifecycle rules, replication, and event notifications. Uses HTTP Basic authentication to obtain authorization tokens for subsequent API calls. API v4 is the current stable version.
  - aid: backblaze:backblaze-s3-compatible-api
    name: Backblaze S3-Compatible API
    tags:
      - Cloud Storage
      - Object Storage
      - S3 Compatible
    humanURL: https://www.backblaze.com/apidocs/introduction-to-the-s3-compatible-api
    properties:
      - type: Documentation
        url: https://www.backblaze.com/apidocs/introduction-to-the-s3-compatible-api
      - type: APIReference
        url: https://www.backblaze.com/docs/cloud-storage-call-the-s3-compatible-api
    description: The Backblaze S3-Compatible API allows existing applications built for Amazon S3 to work with Backblaze B2 Cloud Storage with minimal code changes. Supports S3 authentication (AWS Signature V4) and S3 API operations for bucket and object management. Endpoint URLs follow the pattern s3.<region>.backblazeb2.com.
name: Backblaze
tags:
  - Cloud Storage
  - Object Storage
  - Storage
  - Backup
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - type: Website
    url: https://www.backblaze.com
  - type: Portal
    url: https://www.backblaze.com/docs
  - type: Documentation
    url: https://www.backblaze.com/apidocs/
  - type: GettingStarted
    url: https://www.backblaze.com/docs/cloud-storage-native-api
  - type: Pricing
    url: https://www.backblaze.com/cloud-storage/pricing
  - type: SignUp
    url: https://www.backblaze.com/b2/sign-up.html
  - type: Blog
    url: https://www.backblaze.com/blog/
  - type: StatusPage
    url: https://status.backblaze.com
  - type: Support
    url: https://help.backblaze.com
  - type: TermsOfService
    url: https://www.backblaze.com/company/terms-of-service
  - type: PrivacyPolicy
    url: https://www.backblaze.com/company/privacy.html
  - type: GitHubOrganization
    url: https://github.com/Backblaze
  - type: GitHubRepository
    url: https://github.com/Backblaze/b2-sdk-python
  - type: SDK
    url: https://pypi.org/project/b2/
    title: Python SDK (B2 CLI & SDK)
  - type: SDK
    url: https://github.com/Backblaze/b2-sdk-java
    title: Java SDK
  - type: SDK
    url: https://github.com/Backblaze/blazer
    title: Go SDK
  - type: CLI
    url: https://github.com/Backblaze/B2_Command_Line_Tool
    title: B2 Command Line Tool
  - type: Tools
    url: https://github.com/Backblaze/terraform-provider-b2
    title: Terraform Provider
  - type: SpectralRules
    url: rules/backblaze-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/backblaze-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/cloud-storage-management.yaml
  - name: Features
    type: Features
    data:
      - name: Object Storage
        description: Store and retrieve any amount of data with a simple flat namespace and unique file IDs.
      - name: S3-Compatible API
        description: Use existing S3 tools and libraries without modification via the S3-compatible API endpoint.
      - name: Large File Multi-Part Upload
        description: Upload files larger than 5GB using the multi-part upload API (b2_start_large_file / b2_upload_part / b2_finish_large_file).
      - name: Application Key Management
        description: Create and manage scoped application keys with per-bucket and per-prefix restrictions.
      - name: Lifecycle Rules
        description: Automatically delete or hide files after a specified number of days using lifecycle rules.
      - name: File Versioning
        description: Keep multiple versions of files; older versions are preserved and accessible by file ID.
      - name: Event Notifications
        description: Configure webhook-based event notifications when objects are created, modified, or deleted.
      - name: Object Lock
        description: Protect files from deletion or modification for a specified retention period using object lock.
      - name: Cross-Region Replication
        description: Replicate buckets to other regions or accounts for disaster recovery and data locality.
      - name: Server-Side Encryption
        description: Encrypt data at rest using Backblaze-managed or customer-managed keys.
      - name: Cloudflare Bandwidth Alliance
        description: Zero egress fees when serving B2 data through Cloudflare CDN.
  - name: UseCases
    type: UseCases
    data:
      - name: Application Data Storage
        description: Store application data, user-uploaded content, and media files in the cloud.
      - name: Backup and Disaster Recovery
        description: Use Backblaze B2 as the storage backend for backup tools like Arq, MSP360, and Veeam.
      - name: Media Hosting and Delivery
        description: Host images, videos, and other media files and serve them via CDN integration.
      - name: Archival Storage
        description: Store infrequently accessed archival data at low cost with lifecycle-based management.
      - name: Data Migration
        description: Migrate data from S3 or other cloud storage providers using the S3-compatible API.
      - name: CI/CD Artifact Storage
        description: Store build artifacts, logs, and deployment packages in B2 buckets.
  - name: Integrations
    type: Integrations
    data:
      - name: Cloudflare
        description: Zero egress bandwidth alliance for CDN delivery of B2 content.
      - name: Arq Backup
        description: Popular Mac and Windows backup application with native B2 support.
      - name: Synology
        description: Synology NAS Hyper Backup integration for cloud backup.
      - name: Veeam
        description: Enterprise backup and replication solution with B2 support.
      - name: MSP360
        description: Managed backup service with native B2 storage support.
      - name: Terraform
        description: Infrastructure as code support via the official Terraform provider.
      - name: rclone
        description: Command-line sync tool with native B2 Native and S3-compatible API support.
created: '2025-03-01'
modified: '2026-04-19'
position: Consumer
description: Backblaze is a cloud storage and data backup provider offering B2 Cloud Storage - a low-cost, S3-compatible object storage service. Backblaze provides both a native B2 API and an S3-compatible API, enabling developers to build applications that store unlimited data at a fraction of major cloud provider costs. Features include file versioning, lifecycle rules, event notifications, object lock, cross-region replication, and a Cloudflare bandwidth alliance for zero-egress CDN delivery.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
