---
aid: replit
name: Replit
description: Replit is a cloud-based development platform that lets you create, run, and deploy software directly from your browser. It provides instant, containerized environments for many programming languages, real-time multiplayer collaboration, an integrated editor and terminal, built-in package management, version control, and AI coding assistance. Use the Replit API to manage Repls, deployments, and users programmatically.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Code
  - Compiling
  - Development Environment
  - Programming Languages
  - Version Control
url: https://raw.githubusercontent.com/api-evangelist/replit/refs/heads/main/apis.yml
created: '2026-01-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: replit:replit
    name: Replit
    description: Replit is a cloud-based development platform that lets you create, run, and deploy software directly from your browser. The Replit API provides programmatic access to manage Repls (coding environments), deployments, and user profiles.
    humanURL: https://replit.com/
    tags:
      - Code
      - Development Environment
      - Deployments
      - Programming Languages
      - Repls
      - Users
      - Version Control
    properties:
      - url: https://docs.replit.com/api
        type: Documentation
      - url: openapi/replit-openapi.yml
        type: OpenAPI
      - url: rules/replit-rules.yml
        type: SpectralRuleset
      - url: capabilities/development-workflow.yaml
        type: NaftikoCapability
      - url: vocabulary/replit-vocabulary.yml
        type: Vocabulary
common:
  - type: Website
    url: https://replit.com
  - type: Documentation
    url: https://docs.replit.com
  - type: API Documentation
    url: https://docs.replit.com/api
  - type: Pricing
    url: https://replit.com/pricing
  - type: Blog
    url: https://blog.replit.com
  - type: TermsOfService
    url: https://replit.com/site/terms
  - type: PrivacyPolicy
    url: https://replit.com/site/privacy
  - type: SignUp
    url: https://replit.com/signup
  - type: Login
    url: https://replit.com/login
  - type: GitHub Organization
    url: https://github.com/replit
  - type: Python SDK
    url: https://github.com/replit/replit-py
  - type: Discord
    url: https://discord.gg/replit
  - type: Status
    url: https://status.replit.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
