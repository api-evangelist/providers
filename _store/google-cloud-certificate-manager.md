---
aid: google-cloud-certificate-manager
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-certificate-manager/refs/heads/main/apis.yml
apis:
- name: Certificate Manager API
  description: The Certificate Manager API enables developers to programmatically manage TLS certificates, certificate maps, certificate map entries, and DNS authorizations for Google Cloud resources. It supports creating and managing Google-managed certificates with automatic provisioning and renewal, as well as uploading self-managed certificates. The API allows mapping certificates to hostnames and associating them with load balancer configurations.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/certificate-manager/docs
  baseURL: https://certificatemanager.googleapis.com
  tags:
  - Certificate Maps
  - Certificates
  - DNS Authorization
  - TLS
  properties:
  - type: Documentation
    url: https://cloud.google.com/certificate-manager/docs/reference/rest
  - type: OpenAPI
    url: openapi/certificate-manager-api-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/certificate-manager/docs/reference/rest#authentication
  - type: JSONSchema
    url: json-schema/google-cloud-certificate-manager-certificate-schema.json
name: Google Cloud Certificate Manager
tags:
- Certificate Management
- Certificates
- Load Balancing
- Security
- SSL
- TLS
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Certificate Manager is a service that lets you acquire and manage TLS (SSL) certificates for use with Google Cloud load balancers and other Google Cloud services. It supports provisioning, renewing, and deploying both Google-managed and self-managed certificates, simplifying certificate lifecycle management at scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

