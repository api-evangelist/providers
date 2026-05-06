---
aid: auth0
name: Auth0
description: |
  Auth0 (now part of Okta) is a leading identity and access management platform providing secure authentication and authorization for applications, APIs, and devices. It implements OpenID Connect, OAuth 2.0, and SAML 2.0 protocols and offers a Management API, Authentication API, My Account API, and My Organization API for programmatic control over identity infrastructure.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity Management
  - OAuth
  - Okta
  - OpenID Connect
  - SAML
  - Security
url: https://raw.githubusercontent.com/api-evangelist/auth0/refs/heads/main/apis.yml
created: '2024-04-14'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: auth0:auth0-management-api
    name: Auth0 Management API
    description: The Auth0 Management API enables programmatic management of your Auth0 tenant, including users, connections, applications, rules, and logs.
    humanURL: https://auth0.com/docs/api/management/v2
    baseURL: https://your-tenant.auth0.com/api/v2
    tags:
      - Authentication
      - Identity
      - User Management
    properties:
      - type: Documentation
        url: https://auth0.com/docs/api/management/v2
      - type: GettingStarted
        url: https://auth0.com/docs/get-started
      - type: Authentication
        url: https://auth0.com/docs/secure/tokens
      - type: OpenAPI
        url: openapi/auth0-api-openapi.yml
  - aid: auth0:auth0-authentication-api
    name: Auth0 Authentication API
    description: The Auth0 Authentication API implements OpenID Connect and OAuth 2.0 protocols for authentication and authorization.
    humanURL: https://auth0.com/docs/api/authentication
    baseURL: https://your-tenant.auth0.com
    tags:
      - Authentication
      - OAuth
      - OpenID Connect
    properties:
      - type: Documentation
        url: https://auth0.com/docs/api/authentication
      - type: APIReference
        url: https://auth0.com/docs/api/authentication
  - aid: auth0:auth0-my-account-api
    name: Auth0 My Account API
    description: |
      The Auth0 My Account API provides user self-service endpoints for managing authentication factors, authentication methods, and account settings.
    humanURL: https://auth0.com/docs/api/myaccount
    baseURL: https://your-tenant.auth0.com
    tags:
      - Account Management
      - Authentication
      - MFA
      - Self-Service
    properties:
      - type: Documentation
        url: https://auth0.com/docs/api/myaccount
  - aid: auth0:auth0-my-organization-api
    name: Auth0 My Organization API
    description: |
      The Auth0 My Organization API provides organization-scoped endpoints for business customers to manage their own Organizations, including IdP configuration, SCIM, and Home Realm Discovery.
    humanURL: https://auth0.com/docs/api/myorganization
    baseURL: https://your-tenant.auth0.com
    tags:
      - Authentication
      - B2B
      - Identity
      - Organizations
    properties:
      - type: Documentation
        url: https://auth0.com/docs/api/myorganization
common:
  - type: Website
    url: https://auth0.com/
  - type: Documentation
    url: https://auth0.com/docs/
  - type: Getting Started
    url: https://auth0.com/docs/get-started
  - type: Blog
    url: https://auth0.com/blog/
  - type: Sign Up
    url: https://auth0.com/signup
  - type: Login
    url: https://manage.auth0.com/
  - type: Pricing
    url: https://auth0.com/pricing
  - type: GitHub Organization
    url: https://github.com/auth0
  - type: Status
    url: https://status.auth0.com/
  - type: Community
    url: https://community.auth0.com/
  - type: Support
    url: https://support.auth0.com/
  - type: Terms of Service
    url: https://auth0.com/legal/tos
  - type: Privacy Policy
    url: https://auth0.com/privacy
  - type: SDK
    url: https://auth0.com/docs/libraries
  - type: Features
    data:
      - 'Free: 25,000 MAUs, passwordless, social connections, SCIM'
      - 'Essentials: $35/mo (B2C) or $150/mo (B2B) starting at 500 MAUs'
      - 'Professional: $240/mo (B2C) or $800/mo (B2B)'
      - 'Enterprise custom: 99.99% SLA, private deployment'
      - Authentication API (OAuth/OIDC/SAML)
      - Management API for users, roles, connections
      - Auth0 for AI Agents add-on (50% of base)
      - M2M Tokens add-on
      - 'Authentication API: 100 RPS Free, 200 RPS Paid'
      - 'Management API: 2 RPS Free, 15 RPS Paid'
      - Universal Login + Lock customizable UI
      - Actions for custom auth pipeline logic
      - Tenant log streaming to SIEM
      - Bot Detection and Anomaly Detection
      - Organizations for B2B multi-tenancy
      - Self-Service SSO with SCIM provisioning
    sources:
      - https://auth0.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Customer Identity
        description: Add secure, scalable authentication to customer-facing web and mobile applications with social login and passwordless options.
      - name: Workforce Identity
        description: Federate with enterprise IdPs for employee authentication with SSO, MFA, and SCIM provisioning.
      - name: B2B Identity
        description: Provide multi-tenant identity for SaaS applications with per-customer organization management and custom login flows.
      - name: API Authorization
        description: Secure REST and GraphQL APIs using OAuth 2.0 access tokens with audience and scope validation.
      - name: Machine-to-Machine Auth
        description: Issue OAuth 2.0 client credentials tokens for service-to-service API authentication without user involvement.
  - type: Integrations
    data:
      - name: Okta
        description: Auth0 is now part of Okta, enabling combined workforce and customer identity capabilities.
      - name: Active Directory/LDAP
        description: Connect on-premises Active Directory and LDAP directories for enterprise user authentication.
      - name: Azure AD
        description: Federate with Azure Active Directory for Microsoft ecosystem authentication and SSO.
      - name: Salesforce
        description: Use Auth0 as identity provider for Salesforce apps and customer communities.
      - name: AWS
        description: Secure AWS API Gateway and Lambda functions with Auth0-issued JWT access tokens.
      - name: Twilio
        description: Send OTP and MFA verification codes via Twilio SMS and voice using Auth0 MFA integration.
  - type: Solutions
    data:
      - name: Customer Identity Access Management
        description: Comprehensive CIAM solution for customer-facing applications with self-service registration, social login, and adaptive MFA.
      - name: Workforce Identity
        description: Enterprise identity management for employees with federation, MFA, and SSO across all applications.
      - name: B2B SaaS Identity
        description: Multi-tenant identity infrastructure for SaaS platforms requiring per-customer branding, SSO, and user management.
  - type: RateLimits
    url: https://auth0.com/docs/troubleshoot/customer-support/operational-policies/rate-limit-policy
  - type: ChangeLog
    url: https://auth0.com/changelog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
