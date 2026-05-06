---
aid: secureworks
url: https://raw.githubusercontent.com/api-evangelist/secureworks/refs/heads/main/apis.yml
apis:
  - aid: secureworks:secureworks-taegis-xdr-api
    name: Secureworks Taegis XDR API
    tags:
      - XDR
      - Threat Detection
      - Security Operations
      - GraphQL
      - Incident Response
    humanURL: https://docs.taegis.secureworks.com/apis/using_xdr_apis/
    baseURL: https://api.ctpx.secureworks.com
    properties:
      - url: openapi/secureworks-taegis-xdr-openapi.yml
        type: OpenAPI
      - url: https://docs.taegis.secureworks.com/apis/using_xdr_apis/
        type: Documentation
      - url: https://docs.taegis.secureworks.com/apis/api_authenticate/
        type: Authentication
    description: The Secureworks Taegis XDR API provides GraphQL-based programmatic access to the Taegis extended detection and response platform. The API supports alerts, investigations, endpoint assets, identities, threat intelligence, collectors, connectors, playbooks, and audit operations. Authentication uses OAuth2 client credentials flow with bearer token authorization. The platform is available across multiple regions in the US and EU, with each region served by a dedicated API endpoint.
name: Secureworks
tags:
  - Cybersecurity
  - XDR
  - Threat Detection
  - Security Operations
  - Incident Response
  - MDR
  - Threat Intelligence
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-02'
modified: '2026-05-02'
position: Consuming
description: Secureworks is a cybersecurity company that provides the Taegis XDR (Extended Detection and Response) platform, offering threat detection, investigation, and response capabilities backed by 20 years of security intelligence. Taegis ingests and correlates telemetry across endpoints, network, cloud, and identity sources to detect threats and automate response workflows. The Taegis XDR API exposes GraphQL APIs for alerts, investigations, endpoint assets, identities, threat intelligence, connectors, collectors, playbooks, and users, with OAuth2 client credentials authentication and multi-region deployment support.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Website
    url: https://www.secureworks.com
    type: Website
  - name: Taegis API Documentation
    url: https://docs.taegis.secureworks.com/apis/using_xdr_apis/
    type: Documentation
  - name: API Authentication
    url: https://docs.taegis.secureworks.com/apis/api_authenticate/
    type: Authentication
  - name: GitHub Organization
    url: https://github.com/secureworks
    type: GitHubOrganization
  - name: Taegis Python SDK
    url: https://github.com/secureworks/taegis-sdk-python
    type: SDK
  - name: VDR API Documentation
    url: https://us2.vdr.secureworks.com/api/v2/spec
    type: Documentation
  - name: API Blog Post
    url: https://www.secureworks.com/blog/show-me-the-apis
    type: Blog
  - url: json-schema/secureworks-alert-schema.json
    type: JSONSchema
  - url: json-structure/secureworks-investigation-structure.json
    type: JSONStructure
  - url: json-ld/secureworks-context.jsonld
    type: JSONLDContext
  - url: examples/secureworks-query-alerts-example.json
    type: Example
  - url: rules/secureworks-rules.yml
    type: SpectralRuleset
  - url: capabilities/threat-detection-response.yaml
    type: NaftikoCapability
  - url: vocabulary/secureworks-vocabulary.yml
    type: Vocabulary
---
