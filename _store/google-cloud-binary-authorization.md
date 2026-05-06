---
aid: google-cloud-binary-authorization
name: Google Cloud Binary Authorization
description: Google Cloud Binary Authorization is a deploy-time security control that ensures only trusted container images are deployed on Google Kubernetes Engine (GKE), Cloud Run, and Anthos clusters. It uses attestation-based policies to validate that container images have been signed by trusted authorities before allowing deployment, helping enforce software supply chain security.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-binary-authorization/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Attestation
  - Container Security
  - DevSecOps
  - Kubernetes
  - Policy Enforcement
  - Supply Chain Security
apis:
  - name: Binary Authorization API
    description: The Binary Authorization API provides programmatic access to manage deploy-time security policies for container images. Developers can use the API to create and manage attestors, attestations, and policies that control which container images are allowed to be deployed. The API integrates with GKE, Cloud Run, and Anthos to enforce that only verified and trusted container images are deployed to production environments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/binary-authorization/docs
    baseURL: https://binaryauthorization.googleapis.com
    tags:
      - Attestations
      - Attestors
      - Container Images
      - Policies
    properties:
      - type: Documentation
        url: https://cloud.google.com/binary-authorization/docs/reference/rest
      - type: OpenAPI
        url: openapi/binary-authorization-api-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/binary-authorization/docs/reference/rest#authentication
      - type: JSONSchema
        url: json-schema/google-cloud-binary-authorization-policy-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/binary-authorization
  - type: Getting Started
    url: https://cloud.google.com/binary-authorization/docs/getting-started-cli
  - type: Documentation
    url: https://cloud.google.com/binary-authorization/docs
  - type: Authentication
    url: https://cloud.google.com/binary-authorization/docs/reference/rest#authentication
  - type: Pricing
    url: https://cloud.google.com/binary-authorization/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com
  - type: Support
    url: https://cloud.google.com/binary-authorization/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-binary-authorization-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
