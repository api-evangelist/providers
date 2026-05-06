---
aid: quay
name: Quay
description: Quay is a container image registry that enables you to build, store, distribute, and deploy container images with built-in security scanning, access controls, and automated build triggers. Available as a hosted service at Quay.io or as a self-hosted solution through Red Hat Quay.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Container Images
  - Containers
  - Red Hat
  - Registry
  - Security Scanning
url: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: quay:quay
    name: Quay
    description: Quay is a container image registry that enables you to build, store, distribute, and deploy container images with built-in security scanning, access controls, and automated build triggers.
    humanURL: https://quay.io/
    baseURL: https://quay.io/api/v1
    tags:
      - Container Images
      - Containers
      - Registry
      - Security Scanning
    properties:
      - type: Documentation
        url: https://docs.quay.io/
      - type: Getting Started
        url: https://docs.quay.io/guides/
      - type: Pricing
        url: https://quay.io/plans/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/openapi/quay-openapi.yml
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/json-ld/quay-context.jsonld
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/json-schema/quay-repository-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/json-schema/quay-tag-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/json-schema/quay-manifest-security-schema.json
common:
  - type: Website
    url: https://quay.io/
  - type: Documentation
    url: https://docs.quay.io/
  - type: Getting Started
    url: https://docs.quay.io/guides/
  - type: GitHub Organization
    url: https://github.com/quay
  - type: Pricing
    url: https://quay.io/plans/
  - type: Blog
    url: https://www.redhat.com/en/blog
  - type: Sign Up
    url: https://quay.io/signin/
  - type: Support
    url: https://access.redhat.com/products/red-hat-quay/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
