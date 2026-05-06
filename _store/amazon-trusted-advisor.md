---
aid: amazon-trusted-advisor
name: Amazon Trusted Advisor
description: AWS Trusted Advisor provides real-time guidance to help you provision your resources following AWS best practices. It inspects your AWS environment and makes recommendations for saving money, improving system performance and reliability, and closing security gaps across cost optimization, performance, security, fault tolerance, and service limits.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Best Practices
  - Cloud Optimization
  - Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-trusted-advisor/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-trusted-advisor:aws-support-api
    name: AWS Trusted Advisor API
    description: The AWS Support API provides programmatic access to AWS Trusted Advisor checks, results, and recommendations. It enables retrieving check summaries, refreshing checks, and accessing detailed results for cost optimization, performance, security, fault tolerance, and service limits.
    humanURL: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
    baseURL: https://support.us-east-1.amazonaws.com
    tags:
      - AWS
      - Best Practices
      - Cloud Optimization
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html
      - type: APIReference
        url: https://docs.aws.amazon.com/awssupport/latest/APIReference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html
      - type: Pricing
        url: https://aws.amazon.com/premiumsupport/plans/
      - type: FAQ
        url: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
  - type: Documentation
    url: https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html
  - type: Console
    url: https://console.aws.amazon.com/trustedadvisor/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-trusted-advisor/refs/heads/main/rules/amazon-trusted-advisor-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-trusted-advisor/refs/heads/main/vocabulary/amazon-trusted-advisor-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-trusted-advisor/refs/heads/main/capabilities/amazon-trusted-advisor-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon Trusted Advisor.
      - name: API Access
        description: Programmatic access to Amazon Trusted Advisor resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon Trusted Advisor to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
