---
aid: google-cloud-binary-authorization
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-binary-authorization/refs/heads/main/apis.yml
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
name: Google Cloud Binary Authorization
tags:
- Attestation
- Container Security
- DevSecOps
- Kubernetes
- Policy Enforcement
- Supply Chain Security
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Binary Authorization is a deploy-time security control that ensures only trusted container images are deployed on Google Kubernetes Engine (GKE), Cloud Run, and Anthos clusters. It uses attestation-based policies to validate that container images have been signed by trusted authorities before allowing deployment, helping enforce software supply chain security.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

