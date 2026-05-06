---
aid: chef
name: Chef
description: Chef (Progress Chef) provides infrastructure automation, compliance, and application delivery tooling. Chef exposes REST APIs for the Infra Server (managing nodes, cookbooks, roles, environments, and data bags), Chef Automate (visibility into convergence, compliance, and deployment), Habitat Builder (application packaging and delivery), and InSpec (a language and runner for security and compliance testing).
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chef/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Application Delivery
  - Automation
  - Compliance
  - Configuration Management
  - DevOps
  - DevSecOps
  - Habitat
  - Infrastructure as Code
  - InSpec
created: '2024-01-15'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chef:chef-infra-server-api
    name: Chef Infra Server API
    description: REST API for managing nodes, cookbooks, roles, environments, data bags, clients, and users on the Chef Infra Server. Authentication uses Chef signed-header authentication with an RSA client key.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.chef.io/server/api_chef_server/
    baseURL: https://chef.example.com/organizations/example
    tags:
      - Configuration Management
      - Infrastructure
    properties:
      - type: Documentation
        url: https://docs.chef.io/server/api_chef_server/
      - type: Authentication
        url: https://docs.chef.io/server/server_security/
      - type: OpenAPI
        url: openapi/chef-infra-server-api-openapi.yml
  - aid: chef:chef-automate-api
    name: Chef Automate API
    description: REST API for Chef Automate providing visibility into infrastructure convergence, compliance scans, and application deployment. Includes compliance profiles, scan jobs, reports, IAM, and configuration management endpoints.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.chef.io/automate/api/
    baseURL: https://automate.example.com/api/v0
    tags:
      - Automation
      - Compliance
      - Observability
    properties:
      - type: Documentation
        url: https://docs.chef.io/automate/api/
      - type: Reference
        url: https://docs.chef.io/automate/api_swagger/
      - type: Authentication
        url: https://docs.chef.io/automate/api_tokens/
      - type: OpenAPI
        url: openapi/chef-automate-api-openapi.yml
  - aid: chef:chef-habitat-builder-api
    name: Chef Habitat Builder API
    description: REST API for Chef Habitat Builder, the package management service for Habitat application packages. Manages origins, packages, channels, and deployment events.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.habitat.sh/docs/using-builder/
    baseURL: https://bldr.habitat.sh/v1
    tags:
      - Application Packaging
      - Deployment
      - Habitat
    properties:
      - type: Documentation
        url: https://docs.habitat.sh/docs/using-builder/
      - type: Authentication
        url: https://docs.habitat.sh/docs/using-builder/
      - type: OpenAPI
        url: openapi/chef-habitat-builder-api-openapi.yml
  - aid: chef:chef-inspec
    name: Chef InSpec
    description: InSpec is an open-source language and runner for security and compliance testing. It is consumed via the InSpec CLI and Ruby DSL, and surfaced inside Chef Automate as compliance profiles, scan jobs, and reports.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.chef.io/inspec/
    tags:
      - Compliance
      - Security
      - Testing
    properties:
      - type: Documentation
        url: https://docs.chef.io/inspec/
      - type: GitHub
        url: https://github.com/inspec/inspec
common:
  - type: Website
    url: https://www.chef.io/
  - type: Documentation
    url: https://docs.chef.io/
  - type: GettingStarted
    url: https://docs.chef.io/
  - type: Blog
    url: https://www.chef.io/blog
  - type: GitHub
    url: https://github.com/chef
  - type: Support
    url: https://www.chef.io/support
  - type: Training
    url: https://training.chef.io/
  - type: Community
    url: https://community.chef.io/
  - type: Status
    url: https://status.chef.io/
  - type: TermsOfService
    url: https://www.chef.io/terms-of-service
  - type: PrivacyPolicy
    url: https://www.chef.io/privacy-policy
  - type: JSONLD
    url: json-ld/chef-context.jsonld
  - type: JSONSchema
    url: json-schema/chef-node-schema.json
  - type: JSONSchema
    url: json-schema/chef-role-schema.json
  - type: JSONSchema
    url: json-schema/chef-compliance-profile-schema.json
  - type: Spectral
    url: spectral/chef-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/chef-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
