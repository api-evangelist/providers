---
aid: amazon-parallel-computing-service
name: Amazon Parallel Computing Service
description: AWS Parallel Computing Service (PCS) is a managed service that makes it easy to create and manage high performance computing (HPC) clusters on AWS. It provides familiar scheduler interfaces, integrates with existing HPC tools, and scales automatically to handle demanding workloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - High Performance Computing
  - HPC
  - Parallel Computing
  - Scientific Computing
url: https://raw.githubusercontent.com/api-evangelist/amazon-parallel-computing-service/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-parallel-computing-service:aws-pcs-api
    name: AWS Parallel Computing Service API
    description: The AWS Parallel Computing Service API provides programmatic access to create and manage HPC clusters, compute node groups, queues, and job scheduling for high performance computing workloads.
    humanURL: https://aws.amazon.com/pcs/
    baseURL: https://pcs.amazonaws.com
    tags:
      - High Performance Computing
      - HPC
      - Parallel Computing
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/pcs/latest/APIReference/Welcome.html
      - type: APIReference
        url: https://docs.aws.amazon.com/pcs/latest/APIReference/Welcome.html
      - type: Getting Started
        url: https://aws.amazon.com/pcs/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/pcs/pricing/
      - type: FAQ
        url: https://aws.amazon.com/pcs/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/pcs/
  - type: Website
    url: https://aws.amazon.com/pcs/
  - type: Documentation
    url: https://docs.aws.amazon.com/pcs/
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/hpc/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/pcs/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-parallel-computing-service-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-parallel-computing-service-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-parallel-computing-service-workflow.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
