---
aid: amazon-iam
name: Amazon IAM
description: Amazon Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users, groups, roles, and policies, and use permissions to allow and deny their access to AWS resources. IAM is a feature of your AWS account offered at no additional charge.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/amazon-iam/refs/heads/main/apis.yml
baseURL: https://iam.amazonaws.com
tags:
  - Access Management
  - Authentication
  - Authorization
  - AWS
  - Identity
  - Security
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iam:aws-iam-api
    name: AWS IAM API
    description: The AWS IAM API provides programmatic access to manage users, groups, roles, policies, and access keys for securing access to AWS services and resources.
    humanURL: https://aws.amazon.com/iam/
    baseURL: https://iam.amazonaws.com
    tags:
      - Access Management
      - Authentication
      - Authorization
      - Identity
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/IAM/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-iam-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/IAM/latest/APIReference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/iam/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iam/faqs/
      - type: JSONSchema
        url: json-schema/amazon-iam-user-schema.json
      - type: JSONStructure
        url: json-structure/amazon-iam-user-structure.json
      - type: Example
        url: examples/amazon-iam-user-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/iam/
  - type: Website
    url: https://aws.amazon.com/iam/
  - type: Documentation
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/iam/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-iam
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: JSONLD
    url: json-ld/amazon-iam-context.jsonld
  - type: SpectralRules
    url: rules/amazon-iam-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iam.yaml
  - type: NaftikoCapability
    url: capabilities/iam-access-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iam-vocabulary.yaml
  - type: Features
    data:
      - name: User Management
        description: Create, manage, and delete IAM users with fine-grained permissions.
      - name: Role-Based Access Control
        description: Define IAM roles that can be assumed by users, services, or applications.
      - name: Policy Management
        description: Create and attach identity-based and resource-based policies to control access.
      - name: Multi-Factor Authentication
        description: Enable MFA for IAM users to add an extra layer of security.
      - name: Access Key Management
        description: Programmatically manage AWS access keys for long-term credentials.
      - name: Permission Boundaries
        description: Use permission boundaries to define the maximum permissions an entity can have.
      - name: Service Control Policies
        description: Centrally control the maximum available permissions across AWS accounts.
  - type: UseCases
    data:
      - name: Least Privilege Access
        description: Grant only the permissions required for specific tasks to reduce the attack surface.
      - name: Cross-Account Access
        description: Enable users in one AWS account to assume roles in another account.
      - name: Service-to-Service Authorization
        description: Allow AWS services to access other services on your behalf through service roles.
      - name: Temporary Credentials
        description: Use STS to issue temporary security credentials for short-lived access.
      - name: Security Compliance
        description: Audit IAM configurations to ensure compliance with security policies and regulations.
  - type: Integrations
    data:
      - name: AWS Organizations
        description: Apply Service Control Policies across multiple AWS accounts in an organization.
      - name: AWS CloudTrail
        description: Log all IAM API calls for auditing and compliance tracking.
      - name: AWS Config
        description: Monitor IAM configuration changes and evaluate compliance with rules.
      - name: AWS Security Hub
        description: Centralize IAM security findings with other AWS security services.
      - name: Amazon Cognito
        description: Federate Cognito user pool identities with IAM roles for application access.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
