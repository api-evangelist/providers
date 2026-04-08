---
aid: cloudformation
url: https://raw.githubusercontent.com/api-evangelist/cloudformation/refs/heads/main/apis.yml
apis:
- name: AWS CloudFormation API
  description: AWS CloudFormation gives you an easy way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles. It uses templates to define stacks of resources and provides API operations for creating, updating, and deleting stacks.
  image: https://aws.amazon.com/cloudformation/logo.png
  humanURL: https://aws.amazon.com/cloudformation/
  baseURL: https://cloudformation.{region}.amazonaws.com
  tags:
  - Infrastructure
  - Resources
  - Stacks
  - Templates
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudformation/
  - type: Reference
    url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html
  - type: OpenAPI
    url: openapi/cloudformation-api.yml
  - type: Pricing
    url: https://aws.amazon.com/cloudformation/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/cloudformation/getting-started/
  - type: Change Log
    url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/document-history.html
  - type: Client Libraries
    url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
  contact:
  - FN: AWS Support
    url: https://aws.amazon.com/contact-us/
    email: ''
- name: AWS Cloud Control API
  description: AWS Cloud Control API provides a uniform CRUDL (create, read, update, delete, list) interface for managing AWS and third-party resources. It offers a standardized way to access and provision resource types available in the CloudFormation Registry without needing to learn each individual service API.
  image: https://aws.amazon.com/cloudformation/logo.png
  humanURL: https://aws.amazon.com/cloudcontrolapi/
  baseURL: https://cloudcontrolapi.{region}.amazonaws.com
  tags:
  - Cloud Control
  - CRUDL
  - Provisioning
  - Resources
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html
  - type: OpenAPI
    url: openapi/cloud-control-api.yml
  - type: Reference
    url: https://docs.aws.amazon.com/cloudcontrolapi/index.html
  contact:
  - FN: AWS Support
    url: https://aws.amazon.com/contact-us/
    email: ''
name: AWS CloudFormation
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure as Code
- Stack Management
type: Contract
image: https://aws.amazon.com/cloudformation/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs provided by AWS for infrastructure as code provisioning and management of AWS and third-party resources using CloudFormation templates and the Cloud Control API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

