---
aid: appwrite
name: Appwrite
description: Appwrite is an open-source backend server for building web and mobile applications. It provides a wide range of features including user authentication, file storage, database management, cloud functions, and messaging. With Appwrite, developers can easily set up a backend for their applications without writing code from scratch, offering a simple and intuitive API for seamless front-end integration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Applications
  - Backends
  - Mobile
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/appwrite/refs/heads/main/apis.yml
created: '2025-02-17'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: appwrite:appwrite-api
    name: Appwrite API
    tags:
      - Authentication
      - Database
      - Storage
      - Functions
      - Open Source
      - Backend-as-a-Service
    humanURL: https://appwrite.io/
    properties:
      - url: https://appwrite.io/docs
        type: Documentation
      - url: https://github.com/appwrite/appwrite
        type: GitHubRepository
      - url: openapi/appwrite-openapi.yaml
        type: OpenAPI
      - url: json-schema/user-schema.json
        type: JSONSchema
      - url: json-structure/user-structure.json
        type: JSONStructure
      - url: examples/user-example.json
        type: Example
      - url: json-ld/appwrite-context.jsonld
        type: JSONLD
      - url: rules/appwrite-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/appwrite-api.yaml
        type: NaftikoCapability
      - url: capabilities/mobile-backend.yaml
        type: NaftikoCapability
      - url: vocabulary/appwrite-vocabulary.yaml
        type: Vocabulary
    description: The Appwrite REST API provides programmatic access to authentication, databases, storage, functions, and messaging for building open source web and mobile application backends.
common:
  - type: Website
    url: https://appwrite.io/
  - type: Documentation
    url: https://appwrite.io/docs
  - type: Blog
    url: https://appwrite.io/blog
  - type: Community
    url: https://appwrite.io/community
  - type: Sign Up
    url: https://cloud.appwrite.io/register
  - type: Login
    url: https://cloud.appwrite.io/login
  - type: GitHub Organization
    url: https://github.com/appwrite
  - type: Pricing
    url: https://appwrite.io/pricing
  - type: Status
    url: https://status.appwrite.online/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
