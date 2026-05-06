---
aid: aws-cognito
name: Amazon Cognito
description: 'Amazon Cognito is an AWS service that provides authentication, authorization, and user management for web and mobile applications. It supports OAuth2, OIDC, SAML federation, and social identity providers. Cognito has two main components: User Pools for user authentication and app integration, and Federated Identities for granting temporary AWS credentials to authenticated users. It includes multi-factor authentication, advanced security features, and customizable authentication flows.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - AWS
  - Identity
  - Identity Provider
  - OAuth2
  - OIDC
url: https://raw.githubusercontent.com/api-evangelist/aws-cognito/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-cognito:aws-cognito-identity-provider
    name: Amazon Cognito Identity Provider
    description: Control plane API for managing Cognito user pools, app clients, users, groups, identity providers, and resource servers. Supports user authentication flows including SRP, custom, and hosted UI authentication.
    humanURL: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html
    baseURL: https://cognito-idp.{region}.amazonaws.com
    tags:
      - Authentication
      - AWS
      - Identity Provider
      - OAuth2
      - User Pools
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html
      - type: APIReference
        url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/cognito/latest/developerguide/security-iam.html
      - type: OpenAPI
        url: openapi/aws-cognito-identity-provider-openapi.yaml
  - aid: aws-cognito:aws-cognito-identity
    name: Amazon Cognito Identity (Federated Identities)
    description: Federated identity service that issues temporary AWS credentials to authenticated and unauthenticated users from Cognito user pools, social identity providers (Facebook, Google, Apple), and SAML-based enterprise IdPs.
    humanURL: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html
    baseURL: https://cognito-identity.{region}.amazonaws.com
    tags:
      - AWS
      - Credentials
      - Federation
      - Identity
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html
      - type: APIReference
        url: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/aws-cognito-identity-openapi.yaml
common:
  - type: Website
    url: https://aws.amazon.com/cognito/
  - type: Documentation
    url: https://docs.aws.amazon.com/cognito/
  - type: GettingStarted
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-cognito-user-pools.html
  - type: Pricing
    url: https://aws.amazon.com/cognito/pricing/
  - type: FAQ
    url: https://aws.amazon.com/cognito/faqs/
  - type: GitHubOrganization
    url: https://github.com/aws-amplify
  - type: Console
    url: https://console.aws.amazon.com/cognito/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/amazon-cognito/
  - type: SpectralRules
    url: rules/aws-cognito-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-cognito-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/identity-management-workflow.yaml
  - type: Features
    data:
      - name: User Pools
        description: Fully managed user directories with sign-up, sign-in, and user profile management.
      - name: OAuth2 and OIDC
        description: Standards-based OAuth2 authorization server and OpenID Connect identity provider for apps.
      - name: SAML Federation
        description: Integrate enterprise identity providers via SAML 2.0 for single sign-on.
      - name: Social Identity Providers
        description: Sign in with Google, Facebook, Apple, and Amazon without custom backend code.
      - name: Multi-Factor Authentication
        description: Built-in MFA with SMS, TOTP, and email verification options.
      - name: Customizable Auth Flows
        description: Lambda triggers for custom authentication challenges, pre-signup validation, and post-confirmation.
      - name: Advanced Security Features
        description: Risk-based adaptive authentication with compromised credential detection and device tracking.
      - name: Federated Identities
        description: Grant temporary AWS credentials to users authenticated via user pools or social providers.
      - name: Hosted UI
        description: Pre-built customizable sign-in/sign-up pages with OAuth2 endpoint support.
      - name: Fine-Grained Authorization
        description: Attribute-based access control with group-based IAM role assignment.
  - type: UseCases
    data:
      - name: Web and Mobile App Authentication
        description: Add user registration, login, and session management to web and mobile applications.
      - name: Enterprise SSO Integration
        description: Connect enterprise SAML identity providers for single sign-on to AWS-hosted applications.
      - name: API Authorization
        description: Use Cognito JWT tokens to authorize access to API Gateway, AppSync, and custom APIs.
      - name: B2C Identity Management
        description: Manage consumer user accounts with self-service registration and profile management.
      - name: Temporary AWS Credentials
        description: Issue scoped AWS credentials to authenticated users for direct service access.
  - type: Integrations
    data:
      - name: Amazon API Gateway
        description: Validate Cognito JWTs for API Gateway authorizer integration.
      - name: AWS Amplify
        description: Pre-built Amplify Auth library for easy Cognito integration in React, Vue, and mobile apps.
      - name: AWS Lambda
        description: Trigger Lambda functions for custom authentication logic and user data enrichment.
      - name: Amazon DynamoDB
        description: Use Cognito identity IDs as DynamoDB partition keys for per-user data isolation.
      - name: AWS IAM
        description: Map Cognito groups to IAM roles for role-based access control to AWS services.
      - name: AWS AppSync
        description: Use Cognito user pools as authorization mode for GraphQL API access control.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
