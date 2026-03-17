---
name: Amazon SNS
description: Amazon Simple Notification Service (SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. It enables pub/sub, SMS, email, and mobile push notifications.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
- messaging
- notifications
- pub/sub
- SMS
- push notifications
- email
- AWS
created: '2024-01-01'
modified: '2026-03-16'
url: https://aws.amazon.com/sns/
specificationVersion: '0.16'
apis:
- name: Amazon SNS API
  description: RESTful API for Amazon Simple Notification Service
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/sns/
  baseURL: https://sns.{region}.amazonaws.com
  tags:
  - messaging
  - notifications
  - AWS
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/sns/
  - type: OpenAPI
    url: openapi/amazon-sns-api-openapi.yml
  - type: AsyncAPI
    url: asyncapi/amazon-sns-notifications-asyncapi.yml
  - type: JSONSchema
    url: json-schema/amazon-sns-notification-schema.json
  - type: JSON-LD
    url: json-ld/amazon-sns-context.jsonld
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/sns/2010-03-31/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/sns/latest/api/welcome.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html
  - type: SDK - Python (Boto3)
    url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html
  - type: SDK - JavaScript
    url: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SNS.html
  - type: SDK - Java
    url: https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sns/package-summary.html
  - type: SDK - .NET
    url: https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/SNS/NSNS.html
  - type: Pricing
    url: https://aws.amazon.com/sns/pricing/
  - type: FAQ
    url: https://aws.amazon.com/sns/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/sns/sla/
  - type: Quotas
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-quotas.html
  - type: Features
    url: https://aws.amazon.com/sns/features/
  - type: Use Cases
    url: https://aws.amazon.com/sns/use-cases/
  - type: Best Practices
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-best-practices.html
  - type: API Actions Reference
    url: https://docs.aws.amazon.com/sns/latest/api/API_Operations.html
  - type: Developer Guide
    url: https://docs.aws.amazon.com/sns/latest/dg/welcome.html
  - type: SDK - Go
    url: https://docs.aws.amazon.com/sdk-for-go/api/service/sns/
  - type: SDK - Ruby
    url: https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SNS/Client.html
  - type: SDK - PHP
    url: https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Sns.SnsClient.html
  - type: FIFO Topics
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html
  - type: Message Filtering
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html
  - type: Dead-Letter Queues
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html
  - type: Logging and Monitoring
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-logging-monitoring.html
  - type: CloudWatch Monitoring
    url: https://docs.aws.amazon.com/sns/latest/dg/sns-monitoring-using-cloudwatch.html
  - type: CloudFormation
    url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html
  - type: Terraform
    url: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sns_topic
  - type: Code Examples
    url: https://github.com/awsdocs/aws-doc-sdk-examples
maintainers:
- FN: Kin Lane
  email: kin@apievangelist.com
  url: https://apievangelist.com
common:
- type: Blog
  url: https://aws.amazon.com/blogs/messaging-and-targeting/
- type: Status Dashboard
  url: https://health.aws.amazon.com/health/status
- type: Forum
  url: https://forums.aws.amazon.com/forum.jspa?forumID=72
- type: What's New
  url: https://aws.amazon.com/about-aws/whats-new/messaging/
- type: Authentication
  url: https://docs.aws.amazon.com/sns/latest/dg/sns-authentication-and-access-control.html
- type: Rate Limits
  url: https://docs.aws.amazon.com/sns/latest/dg/sns-quotas.html
- type: Console
  url: https://console.aws.amazon.com/sns/
- type: CLI Reference
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html
- type: Compliance
  url: https://aws.amazon.com/compliance/services-in-scope/
- type: Security
  url: https://docs.aws.amazon.com/sns/latest/dg/sns-security.html
- type: Knowledge Center
  url: https://aws.amazon.com/premiumsupport/knowledge-center/#Amazon_Simple_Notification_Service
- type: Partners
  url: https://aws.amazon.com/sns/partners/
- type: Support
  url: https://console.aws.amazon.com/support/home
- type: Documentation Overview
  url: https://aws.amazon.com/documentation-overview/sns/
- type: API Reference PDF
  url: https://docs.aws.amazon.com/pdfs/sns/latest/api/sns-api.pdf
- type: Developer Guide PDF
  url: https://docs.aws.amazon.com/pdfs/sns/latest/dg/sns-dg.pdf
- type: Developer Guide Source
  url: https://github.com/awsdocs/amazon-sns-developer-guide
- type: Sample Code
  url: https://github.com/aws-samples/aws-sns-samples
---