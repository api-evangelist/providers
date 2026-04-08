---
aid: amazon-cognito
url: https://raw.githubusercontent.com/api-evangelist/amazon-cognito/refs/heads/main/apis.yml
apis:
- name: Cognito User Pools API
  description: Amazon Cognito User Pools API provides user directory management, sign-up, sign-in, and token-based authentication for web and mobile applications. It supports multi-factor authentication, account recovery, and customizable authentication flows.
  baseURL: https://cognito-idp.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
  - type: OpenAPI
    url: openapi/amazon-cognito-user-pools-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cognito-idp/2016-04-18/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-cognito-user-pool-schema.json
  - type: JSONLD
    url: json-ld/amazon-cognito-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/cognito/pricing/
  - type: Getting Started
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-cognito-user-pools.html
  - type: FAQ
    url: https://aws.amazon.com/cognito/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html
  - type: API Reference
    url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/index.html
  - type: Security
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/security.html
- name: Cognito Identity Pools API
  description: Amazon Cognito Identity Pools (Federated Identities) API enables developers to create unique identities for users and federate them with identity providers. It provides temporary, limited-privilege AWS credentials to access AWS services.
  baseURL: https://cognito-identity.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cognito-identity/2014-06-30/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-cognito-user-pool-schema.json
  - type: JSONLD
    url: json-ld/amazon-cognito-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/cognito/pricing/
  - type: Getting Started
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html
  - type: FAQ
    url: https://aws.amazon.com/cognito/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html
  - type: API Reference
    url: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/cognito-identity/index.html
  - type: Security
    url: https://docs.aws.amazon.com/cognito/latest/developerguide/security.html
name: Amazon Cognito
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Cognito is a fully managed user identity and authentication service that enables developers to add sign-up, sign-in, and access control to web and mobile applications. It supports OAuth 2.0, SAML 2.0, and OpenID Connect standards, providing secure user directories that scale to millions of users. Cognito offers user pools for authentication and identity pools for authorization, allowing integration with social identity providers and enterprise identity systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

