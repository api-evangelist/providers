---
aid: postman
url: https://raw.githubusercontent.com/api-evangelist/postman/refs/heads/main/apis.yml
apis:
- aid: postman:postman
  name: Postman
  tags:
  - Automation
  - Client
  - Collections
  - Discovery
  - Mocking
  - Network
  - Platform
  - Testing
  - Workflows
  humanURL: https://www.postman.com/
  properties:
  - url: https://www.postman.com/
    type: Documentation
  - url: https://learning.postman.com/docs/developer/postman-api/intro-api/
    type: GettingStarted
  - url: https://learning.postman.com/docs/developer/postman-api/authentication/
    type: Authentication
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: PostmanCollection
  - url: asyncapi/postman-webhooks-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/postman-collection-schema.json
    type: JSONSchema
  - url: json-schema/postman-environment-schema.json
    type: JSONSchema
  - url: json-schema/postman-workspace-schema.json
    type: JSONSchema
  - url: json-ld/postman-context.yml
    type: JSON-LD
  description: Postman is your single platform for collaborative API development. Join 35+ million devs building great APIs together, across the entire API lifecycle.
- aid: postman:collections-api
  name: Postman Collections API
  tags:
  - API Management
  - Automation
  - Collections
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-collections-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: Use the Collections APIs to manage your Postman collections and simplify collection-related workflows, with endpoints to add, delete, or update your collections.
- aid: postman:workspaces-api
  name: Postman Workspaces API
  tags:
  - API Management
  - Collaboration
  - Workspaces
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-workspaces-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: Use the Workspaces APIs to manage your Postman workspaces, with endpoints that enable you to create, update, and delete workspaces programmatically.
- aid: postman:environments-api
  name: Postman Environments API
  tags:
  - Configuration
  - Environments
  - Variables
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-environments-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Environments API enables you to programmatically manage your Postman environments and global variables, scoping your work to different environments.
- aid: postman:mock-servers-api
  name: Postman Mock Servers API
  tags:
  - API Development
  - Mocking
  - Simulation
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-mock-servers-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Mock Servers API enables you to perform CRUD operations on mock servers and manage mock server responses for simulating API behavior during development.
- aid: postman:monitors-api
  name: Postman Monitors API
  tags:
  - Automation
  - Monitoring
  - Scheduling
  - Testing
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-monitors-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Monitors API enables you to programmatically run collections on a schedule, manage webhooks, and access metrics for API monitoring instances.
- aid: postman:apis-api
  name: Postman APIs API
  tags:
  - API Builder
  - API Design
  - Specifications
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-apis-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: Use the APIs endpoints to manage your API definitions in Postman, including creating, updating, and managing API versions and specifications.
- aid: postman:private-api-network-api
  name: Postman Private API Network API
  tags:
  - API Network
  - Discovery
  - Governance
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-private-api-network-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Private API Network API enables you to programmatically manage your private API network, automate management of internal documentation, and integrate with CI/CD pipelines.
- aid: postman:webhooks-api
  name: Postman Webhooks API
  tags:
  - Automation
  - Events
  - Integrations
  - Webhooks
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-webhooks-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/postman-webhooks-asyncapi.yml
    type: AsyncAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Webhooks API enables you to create webhooks that trigger collection runs with custom payloads. Webhooks provide a way to integrate Postman with external systems and automate workflows based on incoming events.
- aid: postman:collection-runs-api
  name: Postman Collection Runs API
  tags:
  - Automation
  - CI/CD
  - Collection Runner
  - Testing
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-collection-runs-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Collection Runs API enables you to programmatically run collections, schedule runs, and retrieve results for continuous integration and delivery pipelines.
- aid: postman:tags-api
  name: Postman Tags API
  tags:
  - Governance
  - Metadata
  - Organization
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-tags-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Tags API enables you to manage tags on APIs, collections, and workspaces for governance and organization. Tags help categorize and discover API assets across your team.
- aid: postman:audit-logs-api
  name: Postman Audit Logs API
  tags:
  - Audit Logs
  - Compliance
  - Governance
  - Security
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-audit-logs-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Audit Logs API provides access to team audit logs for compliance and governance. Track user actions, configuration changes, and security events across your Postman organization.
- aid: postman:secret-scanner-api
  name: Postman Secret Scanner API
  tags:
  - Compliance
  - Governance
  - Secret Scanning
  - Security
  humanURL: https://learning.postman.com/docs/developer/postman-api/intro-api/
  baseURL: https://api.getpostman.com
  properties:
  - url: openapi/postman-secret-scanner-api-openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/postman/postman-public-workspace/documentation/i2uqzpp/postman-api
    type: Documentation
  description: The Secret Scanner API enables you to manage detected secrets and resolve leaked credentials found in your Postman collections, environments, and other API assets.
name: Postman
tags:
- AI Agent Builder
- API Development
- API Documentation
- API Governance
- API Monitoring
- API Testing
- Automation
- Client
- Clients
- Collaboration
- Collections
- Discovery
- Environments
- MCP
- Mock Servers
- Mocking
- Network
- Platform
- Testing
- Workflows
- Workspaces
type: Index
image: https://www.postman.com/assets/logos/postman-logo-horizontal-orange.svg
access: 3rd-Party
common:
- url: https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode
  name: VSCode Extension
  type: VSCodeExtension
- url: https://www.youtube.com/c/Postman
  name: Youtube
  type: Youtube
- url: https://www.postman.com/
  name: Postman API Platform
  type: Website
  description: 'null'
- url: https://www.postman.com/pricing/
  name: Plans & Pricing | Postman API Platform
  type: Pricing
  description: 'null'
- url: https://www.postman.com/learn/
  name: Learn APIs with Postman | Docs, courses, guides, videos - all free.
  type: Knowledgebase
  description: 'null'
- url: https://blog.postman.com/
  name: 'All Things API: News, Tutorials & More | Postman Blog'
  type: Blog
  description: 'null'
- url: https://www.postman.com/templates/
  name: Postman Templates | Postman
  type: Templates
  description: 'null'
- url: https://support.postman.com/hc/en-us
  name: Postman
  type: Support
  description: 'null'
- url: https://www.postman.com/release-notes/
  name: Release Notes | Postman
  type: ChangeLog
  description: 'null'
- url: https://status.postman.com/
  name: Postman Status
  type: Status
  description: 'null'
- url: https://www.postman.com/events/
  name: Postman Events | Postman
  type: Events
  description: 'null'
- url: https://learning.postman.com/docs/postman-cli/postman-cli-installation/
  name: Install the Postman CLI | Postman Docs
  type: CLI
  description: 'null'
- url: https://www.postman.com/partner-program/
  name: The Postman Partner Program
  type: Partners
  description: 'null'
- url: https://www.postman.com/case-studies/
  name: API Case Studies | Postman API Platform
  type: Customers
  description: 'null'
- url: https://www.postman.com/case-studies/
  name: API Case Studies | Postman API Platform
  type: Customers
  description: 'null'
- url: https://www.postman.com/legal/terms/
  name: Terms of Service | Postman
  type: TermsOfService
  description: 'null'
- url: https://www.postman.com/legal/privacy-policy/
  name: Privacy Policy | Postman
  type: PrivacyPolicy
  description: 'null'
- url: https://www.postman.com/legal/trademark-policy/
  name: Trademark Policy | Postman
  type: Trademark
  description: 'null'
- url: https://www.postman.com/trust/
  name: Trust Center | Postman
  type: Trust
  description: 'null'
- url: https://www.postman.com/use-cases/
  data:
  - name: API-first development
  - name: Application development
  - name: Developer onboarding
  - name: Developer portals
  - name: API Testing
  name: Use Cases
  type: UseCases
- data:
  - name: 1 Day Collection Recovery
  - name: 100 Packages
  - name: 100,000 Mock Server Requests
  - name: 25 Collection Runs
  - name: 30 Day Collection Recovery
  - name: 50 Free Activities in Postbot
  - name: 90 Day Collection Recovery
  - name: Access Management
  - name: Access to Flows
  - name: Advanced Role-Based Access Control
  - name: API Admin
  - name: API Editor
  - name: API Governance Manager
  - name: API Monitoring
  - name: API Network Folder Manager
  - name: API Network Manager
  - name: API Viewer
  - name: Audit Logs
  - name: Basic Role-Based Access Control
  - name: Cloud-Based Integrations
  - name: Cloud-Based Integrations
  - name: Collection Editor
  - name: Collection Generation and Sync
  - name: Collection Recovery
  - name: Collection Viewer
  - name: Commenting & Annotations
  - name: Community Manager
  - name: Custom Domains
  - name: Customer Success
  - name: Define Governance Rules
  - name: Deployment Control
  - name: Desktop and Web Appside Extension (vs Code)
  - name: Element-Level Roles
  - name: Environment Editor
  - name: Environment Viewer
  - name: Graphql Client
  - name: Grpc Client
  - name: HTTP Client
  - name: Internal Workspaces
  - name: Internal Workspaces (Private)
  - name: Internal Workspaces (Private)
  - name: Live Preview
  - name: Mock Server Editor
  - name: Mock Server Viewer
  - name: Mock Servers
  - name: Monitor Editor
  - name: Monitor Viewer
  - name: Mqtt Client
  - name: Multi-Partner Workspaces
  - name: Newman CLI
  - name: Outline-Based Editing
  - name: Package Library
  - name: Partner (External)
  - name: Partner Editor
  - name: Partner Manager
  - name: Partner Viewer
  - name: Postman API Supportaudit Logs
  - name: Postman CLI
  - name: Postman Interceptor
  - name: Postman Proxy
  - name: Postman Public Docs
  - name: Postman Vault
  - name: Priority Email Support
  - name: Private API Documentation
  - name: Private API Network
  - name: Private API Network
  - name: Private APIs
  - name: Public API Documentation
  - name: Public API Network
  - name: Reporting & Analytics
  - name: Roles & Permissions
  - name: Saml
  - name: Secret Scanning
  - name: Single & Multi-Partner Workspaces
  - name: Single Partner Workspaces
  - name: Single Sign-on (SSO)
  - name: socket.io Client
  - name: SSO, Scim, & Saml
  - name: Super Admin Role
  - name: Team-Level Roles
  - name: Test Data Storage
  - name: Unlimited Collaborators
  - name: Unlimited Private & Public APIs
  - name: User Groups
  - name: User Groups
  - name: User Level Reporting & Analytics
  - name: User Provisioning (Scim)
  - name: View Syntax Errors
  - name: Websocket Client
  - name: Workspace Admin
  - name: Workspace Editor
  - name: Workspace Themes
  - name: Workspace Updates
  - name: Workspace Viewer
  - name: Workspace-Level Roles
  name: Features
  type: Features
- url: https://www.postman.com/product/integrations/
  data:
  - Name: 1PASSWORD Vault
  - Name: Aikido
  - Name: Amazon API Gateway
  - Name: Apigee
  - Name: Apimatic
  - Name: Apisec
  - Name: Appmap
  - Name: AWS Gateway for API Builder
  - Name: AWS Secrets Manager
  - Name: Azure API Management
  - Name: Azure Apim for API Builder
  - Name: Azure DevOps
  - Name: Azure Key Vault
  - Name: Bigpanda
  - Name: Bitbucket
  - Name: Bitbucket Pipelines
  - Name: Circleci
  - Name: Coralogix
  - Name: Datadog
  - Name: Dropbox
  - Name: Github
  - Name: Github Actions
  - Name: Gitlab
  - Name: Gitlab CI/CD
  - Name: Hashicorp Vault
  - Name: Helios
  - Name: Ilert
  - Name: Jenkins
  - Name: Jira
  - Name: Keen
  - Name: Liblab
  - Name: Microsoft Power Automate
  - Name: Microsoft Teams
  - Name: New Relic
  - Name: Open API
  - Name: Opsgenie
  - Name: Pagerduty
  - Name: Pynt
  - Name: Readme
  - Name: Slack
  - Name: Snyk
  - Name: Speedscale
  - Name: Splunk
  - Name: Splunk On-Call
  - Name: Stainless
  - Name: Statuspage
  - Name: Travis CI
  - Name: vs Code
  - Name: Workato
  name: Integrations
  type: Integrations
created: '2025-01-08T00:00:00.000Z'
modified: '2026-04-07'
position: Consumer
description: Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

