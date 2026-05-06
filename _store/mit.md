---
aid: mit
name: MIT
description: The Massachusetts Institute of Technology (MIT) operates an internal developer portal that exposes APIs for the institution's information systems. The MIT developer environment publishes APIs such as the Roles API for managing institutional roles and authorizations. Access to the developer portal and most APIs requires MIT authentication via Shibboleth / Touchstone single sign-on, making the catalog primarily available to community members, partners, and authorized integrators rather than to the general public.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/mit/refs/heads/main/apis.yml
tags:
  - Education
  - Higher Education
  - Identity
  - Research
  - Roles
  - University
created: '2025-02-08'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mit:roles
    name: MIT Roles API
    description: The MIT Roles API provides programmatic access to institutional role and authorization data, enabling MIT applications and authorized integrators to query, manage, and synchronize roles assigned to people and groups across MIT systems. The Roles API is published through MIT's developer portal and is gated behind MIT Touchstone / Shibboleth authentication.
    humanURL: https://developers-dev.mit.edu/
    tags:
      - Authorization
      - Identity
      - Roles
    properties:
      - type: Documentation
        url: https://developers-dev.mit.edu/
      - type: SignUp
        url: https://developers-dev.mit.edu/
common:
  - type: Website
    url: https://www.mit.edu/
  - type: DeveloperPortal
    url: https://developers.mit.edu/
  - type: Authentication
    url: https://ist.mit.edu/touchstone
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
