---
aid: cloudability
url: https://raw.githubusercontent.com/api-evangelist/cloudability/refs/heads/main/apis.yml
name: Cloudability
created: '2026-03-27'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - Cloud Cost Management
  - Cost Optimization
  - FinOps
  - Multi-Cloud
  - Recommendations
  - Reporting
description: Cloudability (an IBM Apptio product) is a cloud cost management and FinOps platform providing cost visibility, optimization recommendations, anomaly detection, and governance across AWS, Azure, Google Cloud, and other multi-cloud environments. The Cloudability API v3 is REST-oriented with JSON responses, HTTP basic authentication using an API token, cursor-style limit/offset pagination, and operations for reporting, business mappings, rightsizing recommendations, anomalies, vendor credentials, and views.
apis:
  - aid: cloudability:api-v3
    name: Cloudability API v3
    tags:
      - Cloud Cost Management
      - FinOps
      - Recommendations
      - Reporting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudability.com/v3
    humanURL: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas?topic=api-getting-started-cloudability-v3
    properties:
      - url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas?topic=api-getting-started-cloudability-v3
        type: Documentation
      - url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas?topic=api-getting-started-cloudability-v3
        type: Getting Started
    description: The Cloudability v3 API is the modern REST interface for the platform. It exposes resource-oriented endpoints for reporting, dimensions and metrics, business mappings, anomalies, rightsizing recommendations, vendor credentials, views, dashboards, and budgets. Responses default to JSON (CSV available via Accept header), pagination uses limit and offset together, and sort accepts +attribute / -attribute syntax. Authentication uses HTTP basic auth with an API token issued from the Cloudability portal.
  - aid: cloudability:api-v1
    name: Cloudability API v1 (Legacy)
    tags:
      - Cloud Cost Management
      - FinOps
      - Legacy
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://app.cloudability.com/api/v1
    humanURL: https://community.ibm.com/community/user/discussion/apis-getting-started-with-cloudability-apis
    properties:
      - url: https://community.ibm.com/community/user/discussion/apis-getting-started-with-cloudability-apis
        type: Documentation
    description: The legacy v1 API remains available for older integrations covering cost reporting and dimensions. Apptio recommends migrating to v3 for new integrations. v1 uses an api_key query parameter for authentication.
  - aid: cloudability:reporting
    name: Cloudability Reporting API
    tags:
      - Cost Reporting
      - Dimensions
      - FinOps
      - Metrics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudability.com/v3/reporting
    humanURL: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
    properties:
      - url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
        type: Documentation
    description: The Reporting endpoints under v3 build cost-and-usage queries against Cloudability's normalized billing dataset. Callers select metrics (unblended cost, amortized cost, usage_quantity), dimensions (vendor, account_id, service_name, business_mapping, region), filters, and date ranges to produce tabular results that can be exported as JSON or CSV.
  - aid: cloudability:business-mappings
    name: Cloudability Business Mappings API
    tags:
      - Allocation
      - Business Mappings
      - Showback
      - Tagging
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudability.com/v3/business-mappings
    humanURL: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
    properties:
      - url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
        type: Documentation
    description: Business Mappings define rule-based dimensions that allocate spend to cost centers, products, environments, or applications. The API lets callers list, create, update and delete mappings, manage rule order and statements, and preview the resulting allocation against billing data.
  - aid: cloudability:rightsizing
    name: Cloudability Rightsizing Recommendations API
    tags:
      - Cost Optimization
      - Recommendations
      - Rightsizing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudability.com/v3/rightsizing
    humanURL: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
    properties:
      - url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
        type: Documentation
    description: The Rightsizing API surfaces machine-learning generated downsizing, modernization and termination recommendations for AWS EC2, RDS, EBS, Azure VMs and disks, and Google Compute Engine instances, including estimated savings, confidence, and supporting utilization metrics.
  - aid: cloudability:anomalies
    name: Cloudability Anomaly Detection API
    tags:
      - Alerts
      - Anomaly Detection
      - Cost Optimization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudability.com/v3/anomalies
    humanURL: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
    properties:
      - url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
        type: Documentation
    description: The Anomalies API exposes detected cost anomalies on dimensions such as service, account, and business mapping. Callers can query open anomalies, retrieve baseline / actual cost deltas, classify anomalies, and acknowledge them through the API.
  - aid: cloudability:vendor-credentials
    name: Cloudability Vendor Credentials API
    tags:
      - AWS
      - Azure
      - GCP
      - Onboarding
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cloudability.com/v3/vendors
    humanURL: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
    properties:
      - url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
        type: Documentation
    description: The Vendor Credentials API manages connections to AWS payer accounts, Azure billing scopes, GCP billing projects, OCI tenancies and other cloud vendors. It supports listing existing credentials, validating connectivity, rotating secrets, and onboarding new accounts.
common:
  - type: Website
    url: https://www.apptio.com/products/cloudability/
  - type: Portal
    url: https://www.ibm.com/products/cloudability
  - type: Documentation
    url: https://www.ibm.com/docs/en/cloudability-commercial/cloudability-premium/saas
  - type: GitHub
    url: https://github.com/cloudability
  - type: Training
    url: https://education.apptio.com/courses/ibm-cloudability-api
  - type: JSON-LD
    url: json-ld/cloudability-context.jsonld
  - type: Spectral
    url: rules/cloudability-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cloud-cost-finops.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
