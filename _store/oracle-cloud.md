---
aid: oracle-cloud
url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/apis.yml
apis:
- name: Compute API
  description: Manage compute instances, images, and related resources.
  image: https://www.oracle.com/cloud/compute/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/
  baseURL: https://iaas.{region}.oraclecloud.com
  tags:
  - Compute
  - Instances
  - Virtual Machines
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/Compute/home.htm
  - type: X-pricing
    url: https://www.oracle.com/cloud/compute/pricing.html
- name: Object Storage API
  description: Store and retrieve large amounts of unstructured data.
  image: https://www.oracle.com/cloud/storage/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/objectstorage/latest/
  baseURL: https://objectstorage.{region}.oraclecloud.com
  tags:
  - Buckets
  - Object Storage
  - Storage
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/objectstorage/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/Object/home.htm
  - type: X-pricing
    url: https://www.oracle.com/cloud/storage/pricing.html
- name: Networking API
  description: Manage virtual cloud networks, subnets, and network resources.
  image: https://www.oracle.com/cloud/networking/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vcn/
  baseURL: https://iaas.{region}.oraclecloud.com
  tags:
  - Load Balancer
  - Networking
  - VCN
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm
- name: Database API
  description: Manage Oracle Database Cloud Services and Autonomous Databases.
  image: https://www.oracle.com/database/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/database/latest/
  baseURL: https://database.{region}.oraclecloud.com
  tags:
  - Autonomous Database
  - Database
  - DBaaS
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/database/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/Database/home.htm
  - type: X-pricing
    url: https://www.oracle.com/cloud/price-list.html#database
- name: Identity and Access Management API
  description: Manage users, groups, policies, and authentication.
  image: https://www.oracle.com/security/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/identity/latest/
  baseURL: https://identity.{region}.oraclecloud.com
  tags:
  - Authentication
  - Authorization
  - IAM
  - Security
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/identity/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/Identity/home.htm
- name: Container Engine for Kubernetes API
  description: Manage Kubernetes clusters and node pools.
  image: https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/containerengine/latest/
  baseURL: https://containerengine.{region}.oraclecloud.com
  tags:
  - Containers
  - Kubernetes
  - OKE
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/containerengine/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/ContEng/home.htm
- name: Functions API
  description: Serverless platform for building and running applications.
  image: https://www.oracle.com/cloud/cloud-native/functions/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/functions/latest/
  baseURL: https://functions.{region}.oraclecloud.com
  tags:
  - FaaS
  - Functions
  - Serverless
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/functions/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm
- name: Monitoring API
  description: Monitor cloud resources using metrics and alarms.
  image: https://www.oracle.com/cloud/monitoring/
  humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/monitoring/latest/
  baseURL: https://telemetry.{region}.oraclecloud.com
  tags:
  - Alarms
  - Metrics
  - Monitoring
  properties:
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/monitoring/latest/
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/Content/Monitoring/home.htm
name: Oracle Cloud Infrastructure
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of Oracle Cloud Infrastructure (OCI) REST APIs for managing cloud resources and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

