---
aid: cloudinary
url: https://raw.githubusercontent.com/api-evangelist/cloudinary/refs/heads/main/apis.yml
name: Cloudinary
created: '2024-11-13'
modified: '2026-05-04'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - Asset Management
  - Digital Asset Management
  - Image Processing
  - Image Transformation
  - Media
  - SaaS
  - Video Processing
description: Cloudinary is a cloud-based service that provides comprehensive solutions for managing digital media assets, including images and videos, for websites and mobile applications. The platform exposes REST APIs for uploading and transforming media, administering assets and product environments, provisioning users and accounts, and configuring granular permissions. APIs use Basic Authentication with API key and secret over HTTPS.
apis:
  - aid: cloudinary:upload
    name: Cloudinary Upload API
    tags:
      - Asset Upload
      - Image Processing
      - Media
      - Transformation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudinary.com/v1_1
    humanURL: https://cloudinary.com/documentation/image_upload_api_reference
    properties:
      - url: https://cloudinary.com/documentation/image_upload_api_reference
        type: Documentation
      - url: https://cloudinary.com/documentation/upload_images
        type: Getting Started
    description: The Upload API exposes methods for uploading and managing assets, including advanced upload options, CRUD operations on assets, metadata management, eager and on-the-fly transformations, signed and unsigned uploads, and creation of new asset variants from existing originals. Endpoints are versioned under /v1_1/:cloud_name/:resource_type and use HTTP Basic Auth with API key and secret.
  - aid: cloudinary:admin
    name: Cloudinary Admin API
    tags:
      - Administration
      - Asset Management
      - Folders
      - Metadata
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudinary.com/v1_1
    humanURL: https://cloudinary.com/documentation/admin_api
    properties:
      - url: https://cloudinary.com/documentation/admin_api
        type: Documentation
    description: The Admin API supports bulk asset management (search, retrieval, update, delete, restore), and CRUD management of folders, metadata fields, metadata rules, upload presets, transformations, streaming profiles, webhooks, mappings and product environment configuration. Authentication uses HTTP Basic Auth with API key and secret. EU and AP regional endpoints are available for enterprise customers (api-eu.cloudinary.com, api-ap.cloudinary.com).
  - aid: cloudinary:search
    name: Cloudinary Search API
    tags:
      - Asset Discovery
      - Search
      - Visual Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudinary.com/v1_1
    humanURL: https://cloudinary.com/documentation/search_api
    properties:
      - url: https://cloudinary.com/documentation/search_api
        type: Documentation
    description: The Search API exposes Lucene-style query expressions across asset metadata, tags, contextual metadata, structured metadata, and AI-derived tags. Supports sorting, aggregation, pagination via cursors, and saved searches. Visual search and similarity search use perceptual hashes and embeddings to find visually similar assets.
  - aid: cloudinary:provisioning
    name: Cloudinary Provisioning API
    tags:
      - Account Management
      - API Keys
      - Provisioning
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudinary.com/v1_1/provisioning
    humanURL: https://cloudinary.com/documentation/provisioning_api
    properties:
      - url: https://cloudinary.com/documentation/provisioning_api
        type: Documentation
    description: The Provisioning API enables enterprise account-level management of product environments (sub-accounts), users, user groups, and API keys. Authentication uses provisioning API key and secret. Useful for onboarding teams, rotating credentials, and automating environment lifecycle in multi-tenant deployments.
  - aid: cloudinary:permissions
    name: Cloudinary Permissions API
    tags:
      - Access Control
      - Permissions
      - RBAC
      - Roles
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudinary.com/v1_1
    humanURL: https://cloudinary.com/documentation/permissions_api
    properties:
      - url: https://cloudinary.com/documentation/permissions_api
        type: Documentation
    description: The Permissions API assigns granular permissions to principals (users, groups, API keys) by roles or directly. Supports folder-scoped, asset- scoped, and product-environment-scoped permission grants and listing.
  - aid: cloudinary:transformations
    name: Cloudinary Transformation URL API
    tags:
      - Delivery
      - Image Transformation
      - URL API
      - Video Transformation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://res.cloudinary.com
    humanURL: https://cloudinary.com/documentation/transformation_reference
    properties:
      - url: https://cloudinary.com/documentation/transformation_reference
        type: Documentation
    description: The Transformation URL API delivers and transforms images and videos by composing parameters into the delivery URL path (/{cloud_name}/{resource_type}/{type}/{transformations}/{public_id}). Supports resizing, cropping, color and effect transformations, format conversion, watermarks, overlays, AI-driven content-aware operations, and conditional transformations.
  - aid: cloudinary:notifications
    name: Cloudinary Notifications and Webhooks
    tags:
      - Events
      - Notifications
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloudinary.com/documentation/notifications
    properties:
      - url: https://cloudinary.com/documentation/notifications
        type: Documentation
    description: Cloudinary fires HTTP webhook notifications for upload completion, eager transformation completion, AI moderation outcomes, asset deletion, and backup events. Notifications include signatures for verification and can target multiple endpoints per product environment.
common:
  - type: Website
    url: https://cloudinary.com/
  - type: Portal
    url: https://console.cloudinary.com/
  - type: Documentation
    url: https://cloudinary.com/documentation
  - type: SignUp
    url: https://cloudinary.com/users/register_free
  - type: Pricing
    url: https://cloudinary.com/pricing
  - type: Status
    url: https://status.cloudinary.com/
  - type: GitHub
    url: https://github.com/cloudinary
  - type: Terms of Service
    url: https://cloudinary.com/tos
  - type: Privacy
    url: https://cloudinary.com/privacy
  - type: Features
    data:
      - 'Free: 25 monthly credits with all core features'
      - 'Plus at $99/mo: 225 credits, S3 backup, auto-tagging'
      - 'Advanced at $249/mo: 600 credits, custom domain, SSL'
      - 'Enterprise: custom credits, multi-CDN, dedicated CSM'
      - Credits = sum of transformations + storage + bandwidth
      - Image and video transformation API
      - URL-based on-the-fly transformations
      - Video transcoding and adaptive bitrate streaming
      - Upload API with auto-tagging
      - 'Admin API: 500 req/hr Free, 2K req/hr Paid'
      - Bulk delete up to 1,000 resources/request
      - AI-powered transformations (background removal, generative fill)
      - Auto-format and auto-quality for delivery
      - Programmable Media SDKs (JS, mobile, server)
      - Digital Asset Management (DAM) with workflows
      - Multi-CDN delivery (Akamai + Fastly + others on Enterprise)
    sources:
      - https://cloudinary.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
