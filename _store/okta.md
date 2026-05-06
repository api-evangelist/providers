---
aid: okta
name: Okta
description: Okta connects any person with any application on any device. It's an enterprise-grade, identity management service, built for the cloud, but compatible with many on-premises applications. With Okta, IT can manage any employee's access to any application or device. Okta runs in the cloud, on a secure, reliable, extensively audited platform, which integrates deeply with on-premises applications, directories, and identity management systems.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity
  - Platform
  - Single Sign-On
url: https://raw.githubusercontent.com/api-evangelist/okta/refs/heads/main/apis.yml
created: '2023-11-20'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: okta:okta-api
    name: Okta API
    description: The Okta API is a unified identity and access management interface that allows developers to integrate authentication, authorization, user management, group management, application provisioning, policies, sessions, hooks, logs, and more into their applications. It provides programmatic access to the full Okta Identity Cloud platform for managing identity lifecycle and security across enterprise systems.
    humanURL: https://developer.okta.com/docs/reference/
    baseURL: https://your-subdomain.okta.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Authentication
      - Authorization
      - Identity
    properties:
      - type: Documentation
        url: https://developer.okta.com/docs/reference/
      - type: OpenAPI
        url: openapi/okta-openapi-original.yml
common:
  - type: Website
    url: https://www.okta.com/
  - type: Portal
    url: https://developer.okta.com/
  - type: Documentation
    url: https://developer.okta.com/docs/reference/
  - type: Authentication
    url: https://developer.okta.com/docs/reference/api/authn/
  - type: GitHubOrganization
    url: https://github.com/okta
  - type: Status
    url: https://status.okta.com/
  - type: Support
    url: https://support.okta.com/
  - type: Concepts
    url: https://developer.okta.com/docs/concepts/
  - type: Guides
    url: https://developer.okta.com/docs/guides/
  - type: SDKs
    url: https://developer.okta.com/code/
  - type: Change Log
    url: https://developer.okta.com/docs/release-notes/
  - type: Login
    url: https://developer.okta.com/login/
  - type: Sign Up
    url: https://developer.okta.com/signup/
  - type: Blog
    url: https://developer.okta.com/blog/
  - type: Plans
    url: https://www.okta.com/pricing/
  - type: Forum
    url: https://devforum.okta.com/
  - type: Terms of Service
    url: https://developer.okta.com/terms/
  - type: Privacy Policy
    url: https://www.okta.com/privacy-policy/
  - type: Features
    data:
      - 'Starter at $6/user/mo: SSO + MFA + Universal Directory'
      - 'Core Essentials at $14/user/mo: Adaptive MFA, PAM, Lifecycle Mgmt'
      - 'Essentials at $17/user/mo: 50 Workflows'
      - 'Professional: Device Access, ITP, ISPM, unlimited Workflows'
      - 'Enterprise: API Access Management, Access Gateway, M2M Tokens'
      - 'REST APIs: Authentication, Authorization, Users, Groups, Apps, Policies'
      - Default rate limits 600 req/min on most endpoints
      - OAuth /token at 1,000 req/min
      - Logs endpoint capped at 120 req/min
      - OIDC, SAML, WS-Fed protocols
      - Universal Directory with custom attributes
      - Workflows for no-code automation
      - Lifecycle Management for provisioning
      - Adaptive MFA with risk-based policies
      - Identity Threat Protection (Professional+)
      - API Access Management (Enterprise) with OAuth as a Service
    sources:
      - https://www.okta.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
