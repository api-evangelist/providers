---
aid: cloudhealth
url: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/apis.yml
name: CloudHealth
tags:
  - Cloud Cost
  - Cloud Governance
  - Cloud Management
  - Cost Optimization
  - FinOps
  - Multi-Cloud
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-16'
modified: '2026-04-26'
position: Consumer
x-type: company
x-company: Broadcom (formerly VMware / Tanzu)
description: CloudHealth (now VMware Tanzu CloudHealth, owned by Broadcom) is a multi-cloud financial and operational management platform. It provides cost visibility, optimization recommendations, asset inventory, custom perspectives (groupings), policies, governance, and partner/MSP billing workflows across AWS, Azure, GCP, Oracle, and data center environments. The platform exposes both a REST API and a GraphQL API for programmatic access to reports, assets, accounts, perspectives, tags, metrics, and partner customer provisioning.
apis:
  - aid: cloudhealth:cloudhealth-rest-api
    name: CloudHealth REST API
    tags:
      - Assets
      - Cost Optimization
      - Perspectives
      - Reports
    humanURL: https://apidocs.cloudhealthtech.com/
    properties:
      - url: https://apidocs.cloudhealthtech.com/
        type: Documentation
      - url: https://apidocs.cloudhealthtech.com/#documentation_authenticating-api-requests
        type: Authentication
    description: REST API at https://chapi.cloudhealthtech.com for managing AWS/Azure accounts, generating OLAP cost and usage reports, querying assets, managing perspectives (groupings), tagging, metrics ingest/query, policies, and partner-tenant provisioning. Authentication uses Bearer tokens issued from the CloudHealth UI.
  - aid: cloudhealth:cloudhealth-graphql-api
    name: CloudHealth GraphQL API
    tags:
      - GraphQL
      - Reports
    humanURL: https://apidocs.cloudhealthtech.com/
    properties:
      - url: https://apidocs.cloudhealthtech.com/
        type: Documentation
    description: GraphQL API exposed in the CloudHealth UI under Setup > Admin > GraphQL Explorer for programmatic interaction with the platform's reporting and asset data model.
  - aid: cloudhealth:cloudhealth-partner-api
    name: CloudHealth Partner API
    tags:
      - MSP
      - Partner
      - Provisioning
    humanURL: https://apidocs.cloudhealthtech.com/#partner
    properties:
      - url: https://apidocs.cloudhealthtech.com/#partner
        type: Documentation
    description: Partner-specific REST endpoints for MSPs to provision customers, assign AWS/Azure accounts, manage custom price books, billing rules, and customer statements at scale.
common:
  - type: Website
    url: https://www.vmware.com/products/cloud-infrastructure/tanzu-cloudhealth
  - type: Documentation
    url: https://apidocs.cloudhealthtech.com/
  - type: Product Documentation
    url: https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/tnz-cloudhealth/index.html
  - type: Authentication
    url: https://apidocs.cloudhealthtech.com/#documentation_authenticating-api-requests
  - type: Privacy Policy
    url: https://www.broadcom.com/company/legal/privacy/policy
  - type: JSON-LD
    url: json-ld/cloudhealth-context.jsonld
  - type: Spectral
    url: rules/cloudhealth-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cloudhealth-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
