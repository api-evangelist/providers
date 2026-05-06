---
aid: gluu
name: Gluu
description: Gluu is a technology company that specializes in providing identity and access management solutions for businesses. Their platform allows organizations to centrally manage the authentication and authorization of users across various applications and systems, ensuring secure access to sensitive data and resources.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-08-14'
modified: '2026-04-28'
position: Consumer
tags:
  - Access Management
  - Authentication
  - Authorization
  - IAM
  - Identities
  - OAuth
  - OpenID Connect
url: https://raw.githubusercontent.com/api-evangelist/gluu/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: gluu:gluu-flex
    name: Gluu Flex
    description: Gluu Flex is the commercial, self-hosted enterprise distribution of the Linux Foundation Janssen Project. It provides a cloud-native digital identity platform with OAuth 2.0, OpenID Connect, FIDO, SCIM, and UMA capabilities, deployable via Helm charts with auto-scaling support.
    humanURL: https://gluu.org/flex/
    baseURL: https://docs.gluu.org/
    tags:
      - Authentication
      - Authorization
      - IAM
      - OAuth
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://docs.gluu.org/
      - type: Getting Started
        url: https://docs.gluu.org/head/admin-guide/quick-start/
      - type: GitHubRepository
        url: https://github.com/GluuFederation/flex
      - type: Pricing
        url: https://gluu.org/pricing/
  - aid: gluu:janssen-project
    name: Janssen Project
    description: The Janssen Project is the upstream Linux Foundation open-source identity platform that powers Gluu Flex. It implements OAuth 2.0, OpenID Connect, FIDO 2.0, SCIM, UMA, and CIBA, providing a federated identity provider, authorization server, and FIDO server.
    humanURL: https://jans.io/
    baseURL: https://docs.jans.io/
    tags:
      - Authentication
      - Authorization
      - Linux Foundation
      - OAuth
      - Open Source
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://docs.jans.io/
      - type: GitHubRepository
        url: https://github.com/JanssenProject/jans
      - type: Reference
        url: https://docs.jans.io/head/admin/reference/
  - aid: gluu:cedarling
    name: Cedarling
    description: Cedarling is an embeddable Policy Decision Point (PDP) built in Rust that runs anywhere and returns authorization decisions in under 50 microseconds based on declarative Cedar access policies. It validates JWT tokens and applies policies to deliver fine-grained authorization.
    humanURL: https://gluu.org/cedarling/
    tags:
      - Authorization
      - Cedar
      - PDP
      - Policy
      - Rust
    properties:
      - type: Documentation
        url: https://docs.jans.io/head/cedarling/cedarling-overview/
      - type: GitHubRepository
        url: https://github.com/JanssenProject/jans/tree/main/jans-cedarling
  - aid: gluu:agama-lab
    name: Agama Lab
    description: Agama Lab is a developer portal for authoring Cedar schema and policies, building authentication workflows using the Agama domain specific language, and managing hosted Gluu infrastructure.
    humanURL: https://gluu.org/agama-lab/
    tags:
      - Authentication
      - Developer Portal
      - DSL
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.gluu.org/agama-lab/
      - type: Portal
        url: https://cloud.gluu.org/agama-lab
common:
  - type: Website
    url: https://gluu.org/
  - type: Documentation
    url: https://docs.gluu.org/
  - type: Blog
    url: https://gluu.org/blog/
  - type: Support
    url: https://help.gluu.org/
  - type: GitHub Organization
    url: https://github.com/GluuFederation
  - type: Pricing
    url: https://gluu.org/pricing/
  - type: Contact
    url: https://gluu.org/contact/
  - type: Community
    url: https://gluu.org/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
