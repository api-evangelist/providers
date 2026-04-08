---
aid: cloud-custodian
url: https://raw.githubusercontent.com/api-evangelist/cloud-custodian/refs/heads/main/apis.yml
apis:
- aid: cloud-custodian:cloud-custodian
  name: Cloud Custodian
  tags:
  - Cloud Security
  - Policy as Code
  humanURL: https://cloudcustodian.io/
  properties:
  - url: https://cloudcustodian.io/docs/
    type: Documentation
  - url: https://cloudcustodian.io/docs/quickstart/index.html
    type: Getting Started
  - url: https://cloudcustodian.io/docs/overview/capabilities.html
    type: Reference
  - url: https://github.com/cloud-custodian/cloud-custodian
    type: GitHubRepository
  - type: JSONSchema
    url: json-schema/cloud-custodian-policy-schema.json
  description: Cloud Custodian provides rules-engine capabilities for managing cloud resources with security, compliance, and cost optimization policies.
- aid: cloud-custodian:cloud-custodian-aws
  name: Cloud Custodian AWS Provider
  description: The Cloud Custodian AWS provider enables policy-as-code management of Amazon Web Services resources including EC2, S3, IAM, RDS, Lambda, and hundreds of other AWS service resource types. Policies can be run in multiple execution modes including serverless Lambda functions, AWS Config rules, and scheduled CloudWatch Events.
  humanURL: https://cloudcustodian.io/docs/aws/gettingstarted.html
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - url: https://cloudcustodian.io/docs/aws/gettingstarted.html
    type: Getting Started
  - url: https://cloudcustodian.io/docs/aws/resources/index.html
    type: Reference
  - url: https://cloudcustodian.io/docs/aws/examples/index.html
    type: Documentation
  tags:
  - AWS
  - Cloud Security
  - Compliance
  - Policy as Code
- aid: cloud-custodian:cloud-custodian-azure
  name: Cloud Custodian Azure Provider
  description: The Cloud Custodian Azure provider enables policy-as-code management of Microsoft Azure resources including virtual machines, storage accounts, network security groups, and other Azure services. Policies can enforce security requirements, tagging standards, and cost controls across Azure subscriptions.
  humanURL: https://cloudcustodian.io/docs/azure/gettingstarted.html
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - url: https://cloudcustodian.io/docs/azure/gettingstarted.html
    type: Getting Started
  - url: https://cloudcustodian.io/docs/azure/policy/resources/index.html
    type: Reference
  tags:
  - Azure
  - Cloud Security
  - Compliance
  - Policy as Code
- aid: cloud-custodian:cloud-custodian-gcp
  name: Cloud Custodian GCP Provider
  description: The Cloud Custodian GCP provider enables policy-as-code management of Google Cloud Platform resources including Compute Engine instances, GCS buckets, Cloud SQL instances, and other GCP services. Policies can be used to enforce security, compliance, and cost governance standards across GCP projects.
  humanURL: https://cloudcustodian.io/docs/gcp/gettingstarted.html
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - url: https://cloudcustodian.io/docs/gcp/gettingstarted.html
    type: Getting Started
  - url: https://cloudcustodian.io/docs/gcp/resources/index.html
    type: Reference
  tags:
  - Cloud Security
  - Compliance
  - GCP
  - Policy as Code
- aid: cloud-custodian:cloud-custodian-c7n-org
  name: Cloud Custodian C7n-Org
  description: c7n-org is a Cloud Custodian tool for running policies across multiple cloud accounts, projects, or subscriptions in parallel. It uses an accounts configuration file with assumed roles to orchestrate Custodian execution at scale across AWS Organizations, Azure subscriptions, or GCP projects.
  humanURL: https://cloudcustodian.io/docs/tools/c7n-org.html
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - url: https://cloudcustodian.io/docs/tools/c7n-org.html
    type: Documentation
  tags:
  - Cloud Security
  - Multi-Account
  - Orchestration
- aid: cloud-custodian:cloud-custodian-c7n-mailer
  name: Cloud Custodian C7n-Mailer
  description: c7n-mailer is a Cloud Custodian notification tool that subscribes to an SQS queue populated by policy actions and sends notifications via SES email, Slack messages, or integrations with DataDog and Splunk. It enables teams to alert resource owners when Custodian policies detect policy violations.
  humanURL: https://cloudcustodian.io/docs/tools/c7n-mailer.html
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - url: https://cloudcustodian.io/docs/tools/c7n-mailer.html
    type: Documentation
  - type: AsyncAPI
    url: asyncapi/cloud-custodian-mailer-asyncapi.yml
  tags:
  - Alerting
  - Email
  - Notifications
  - Slack
name: Cloud Custodian
tags:
- Cloud Security
- Compliance
- Cost Optimization
- Multi-Cloud
- Policy as Code
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Cloud Custodian is a rules engine for cloud security, compliance, and cost optimization that enables users to define policies to manage cloud resources across AWS, Azure, and GCP. It helps organizations meet regulatory requirements and demonstrate accountability to stakeholders.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

