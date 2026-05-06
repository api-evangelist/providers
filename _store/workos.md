---
aid: workos
name: WorkOS
description: WorkOS is an authentication and identity platform providing enterprise SSO, directory sync (SCIM), and multi-factor authentication APIs for SaaS applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Identity Provider
url: https://raw.githubusercontent.com/api-evangelist/workos/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: workos:workos
    name: WorkOS
    description: WorkOS is an authentication and identity platform providing enterprise SSO, directory sync (SCIM), and multi-factor authentication APIs for SaaS applications.
    humanURL: https://workos.com
    tags:
      - Authentication
      - Identity Provider
    properties:
      - type: Documentation
        url: https://workos.com/docs
      - type: GitHub Repository
        url: https://github.com/workos
common:
  - type: Website
    url: https://workos.com
  - type: Documentation
    url: https://workos.com/docs
  - type: GitHub Organization
    url: https://github.com/workos
  - type: Features
    data:
      - 'AuthKit: free up to 1M MAU, then $2,500/mo per additional 1M'
      - 'Single Sign-On: tiered $50-$125 per active SAML/OIDC connection'
      - 'Directory Sync (SCIM): tiered $50-$125 per connection'
      - Audit Logs (separate pricing)
      - Magic Link, OAuth (Google/MS/Apple), MFA, Passwordless
      - Admin Portal (white-label B2B onboarding)
      - REST API at api.workos.com
      - Default 600 req/min, auth 60 req/min, Directory Sync 10/sec
      - Webhooks for user/org/directory events
      - OpenID Connect / SAML 2.0 / SCIM 2.0
      - Bearer token + organization-scoped API keys
      - Built-in support for 50+ identity providers (Okta, Azure AD, etc.)
      - MFA enrollment + verification API
      - Event streaming for SIEM integration
      - Self-service Admin Portal for end customers
      - SOC 2 Type 2 + GDPR + HIPAA-eligible
    sources:
      - https://workos.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
