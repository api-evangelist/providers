---
aid: secure-code-warrior
url: https://raw.githubusercontent.com/api-evangelist/secure-code-warrior/refs/heads/main/apis.yml
apis:
  - aid: secure-code-warrior:secure-code-warrior-portal-api
    name: Secure Code Warrior Portal API
    tags:
      - Security Training
      - Application Security
      - Developer Training
      - Reporting
      - User Management
    humanURL: https://portal-api.securecodewarrior.com/api/docs/v2/
    baseURL: https://portal-api.securecodewarrior.com/api/v2
    properties:
      - url: openapi/secure-code-warrior-portal-openapi.yml
        type: OpenAPI
      - url: https://portal-api.securecodewarrior.com/api/docs/v2/
        type: Documentation
      - url: https://help.securecodewarrior.com/hc/en-us/sections/360006026452-API
        type: Documentation
    description: The Secure Code Warrior Portal API provides programmatic access to the Secure Code Warrior developer security training platform. The API enables user management, team administration, training progress reporting, assessment management, tournament administration, course assignments, and audit logging. It supports multiple API key types including Report, Admin, and Team keys for granular access control, with separate server instances for US and EU regions.
  - aid: secure-code-warrior:secure-code-warrior-direct-linking-api
    name: Secure Code Warrior Direct Linking API
    tags:
      - Security Training
      - Application Security
      - CWE
      - OWASP
      - GitHub Integration
    humanURL: https://help.securecodewarrior.com/hc/en-us/articles/900005309583-Direct-Linking-API-Documentation
    properties:
      - url: https://help.securecodewarrior.com/hc/en-us/articles/900005309583-Direct-Linking-API-Documentation
        type: Documentation
    description: The Secure Code Warrior Direct Linking API is a RESTful JSON service that allows partners to retrieve application security training material including links to explainer videos and training exercises in over 50 programming languages and frameworks. The API maps Common Weakness Enumeration (CWE) and OWASP vulnerability references to contextually relevant training content, enabling integration with GitHub, SARIF code scanning alerts, and other developer workflow tools.
name: Secure Code Warrior
tags:
  - Application Security
  - Developer Training
  - Security Education
  - AppSec
  - Secure Coding
  - DevSecOps
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-02'
modified: '2026-05-02'
position: Consuming
description: Secure Code Warrior is a developer-first security platform that provides security training, coaching, and assessments to help developers write secure code from the start. The platform offers over 50 programming language and framework combinations, covering OWASP Top 10 and CWE vulnerability categories through interactive challenges, assessments, tournaments, and guided learning courses. Secure Code Warrior exposes a REST API supporting user management, training progress reporting, assessment assignment and tracking, tournament management, metrics, and audit logging, with GitHub and CI/CD pipeline integrations for contextual in-workflow security coaching.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Website
    url: https://www.securecodewarrior.com
    type: Website
  - name: Portal API Documentation
    url: https://portal-api.securecodewarrior.com/api/docs/v2/
    type: Documentation
  - name: Help Center API Section
    url: https://help.securecodewarrior.com/hc/en-us/sections/360006026452-API
    type: Documentation
  - name: Direct Linking API
    url: https://help.securecodewarrior.com/hc/en-us/articles/900005309583-Direct-Linking-API-Documentation
    type: Documentation
  - name: GitHub Organization
    url: https://github.com/SecureCodeWarrior
    type: GitHubOrganization
  - name: GitHub App
    url: https://github.com/marketplace/secure-code-warrior-for-github
    type: GitHubApp
  - name: How to Enable API Access
    url: https://help.securecodewarrior.com/hc/en-us/articles/360036036512-How-to-enable-API-access
    type: GettingStarted
  - url: json-schema/secure-code-warrior-user-schema.json
    type: JSONSchema
  - url: json-structure/secure-code-warrior-training-structure.json
    type: JSONStructure
  - url: json-ld/secure-code-warrior-context.jsonld
    type: JSONLDContext
  - url: examples/secure-code-warrior-get-leaderboard-example.json
    type: Example
  - url: rules/secure-code-warrior-rules.yml
    type: SpectralRuleset
  - url: capabilities/developer-security-training.yaml
    type: NaftikoCapability
  - url: vocabulary/secure-code-warrior-vocabulary.yml
    type: Vocabulary
---
