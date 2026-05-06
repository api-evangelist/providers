---
aid: apollo-graphql
url: https://raw.githubusercontent.com/api-evangelist/apollo-graphql/refs/heads/main/apis.yml
apis:
  - aid: apollo-graphql:apollo-graphql
    name: Apollo GraphQL
    tags:
      - Clients
      - Connectors
      - Federation
      - Graph
      - GraphQL
    humanURL: ' https://www.apollographql.com/'
    properties:
      - url: ' https://www.apollographql.com/'
        type: Documentation
    description: Whether your team is new to GraphQL, or seasoned experts, learn why Apollo is the fastest and safest way to build and scale your APIs.
  - aid: apollo-graphql:apollo-graphos-platform-api
    name: Apollo GraphOS Platform API
    tags:
      - API Management
      - Federation
      - GraphQL
      - Platform
      - Schema Registry
    humanURL: https://www.apollographql.com/docs/graphos/platform/platform-api
    properties:
      - url: https://www.apollographql.com/docs/graphos/platform/platform-api
        type: Documentation
      - url: https://www.apollographql.com/docs/graphos/platform
        type: GettingStarted
      - url: https://www.apollographql.com/docs/graphos/platform/security/overview
        type: Security
      - url: https://www.apollographql.com/docs/graphos/platform/schema-management
        type: SchemaManagement
    description: The GraphOS Platform API enables programmatic management of Apollo GraphOS, including publishing schemas, running schema checks, managing proposals, handling API keys, and accessing operation and field insights data.
  - aid: apollo-graphql:apollo-server
    name: Apollo Server
    tags:
      - GraphQL
      - JavaScript
      - Node.js
      - Server
      - TypeScript
    humanURL: https://www.apollographql.com/docs/apollo-server
    properties:
      - url: https://www.apollographql.com/docs/apollo-server
        type: Documentation
      - url: https://www.apollographql.com/docs/apollo-server/api/apollo-server
        type: APIReference
      - url: https://github.com/apollographql/apollo-server
        type: GitHubRepository
      - url: https://www.npmjs.com/package/@apollo/server
        type: PackageManager
      - url: https://github.com/apollographql/apollo-server/blob/main/packages/server/CHANGELOG.md
        type: Changelog
    description: Apollo Server is an open-source, spec-compliant GraphQL server compatible with any GraphQL client. It is the recommended way to build a production-ready, self-documenting GraphQL API that can use data from any source.
  - aid: apollo-graphql:apollo-client-web
    name: Apollo Client (Web)
    tags:
      - Client
      - GraphQL
      - JavaScript
      - React
      - State Management
      - TypeScript
    humanURL: https://www.apollographql.com/docs/react
    properties:
      - url: https://www.apollographql.com/docs/react
        type: Documentation
      - url: https://www.apollographql.com/docs/react/get-started
        type: GettingStarted
      - url: https://www.apollographql.com/docs/react/api/core/ApolloClient
        type: APIReference
      - url: https://github.com/apollographql/apollo-client
        type: GitHubRepository
      - url: https://www.npmjs.com/package/@apollo/client
        type: PackageManager
      - url: https://github.com/apollographql/apollo-client/blob/main/CHANGELOG.md
        type: Changelog
    description: Apollo Client is a comprehensive state management library for JavaScript and TypeScript applications. It is the industry-leading GraphQL client for React, Vue, Angular, and more, with powerful caching, intuitive APIs, and comprehensive developer tools.
  - aid: apollo-graphql:apollo-client-ios
    name: Apollo Client (iOS)
    tags:
      - Client
      - GraphQL
      - iOS
      - Mobile
      - Swift
    humanURL: https://www.apollographql.com/docs/ios
    properties:
      - url: https://www.apollographql.com/docs/ios
        type: Documentation
      - url: https://github.com/apollographql/apollo-ios
        type: GitHubRepository
      - url: https://github.com/apollographql/apollo-ios/blob/main/CHANGELOG.md
        type: Changelog
    description: Apollo iOS is a Swift-first, open-source GraphQL client for native iOS applications. It executes queries and mutations using a GraphQL server and returns results as operation-specific Swift types, with built-in caching mechanisms for GraphQL data.
  - aid: apollo-graphql:apollo-client-kotlin
    name: Apollo Client (Kotlin)
    tags:
      - Android
      - Client
      - GraphQL
      - JVM
      - Kotlin
      - Mobile
    humanURL: https://www.apollographql.com/docs/kotlin
    properties:
      - url: https://www.apollographql.com/docs/kotlin
        type: Documentation
      - url: https://github.com/apollographql/apollo-kotlin
        type: GitHubRepository
      - url: https://github.com/apollographql/apollo-kotlin/releases
        type: Changelog
    description: Apollo Kotlin is a strongly-typed, caching GraphQL client for the JVM, Android, and Kotlin multiplatform. It generates Kotlin models for GraphQL operations and executes them against a GraphQL server, returning results as operation-specific Kotlin types.
  - aid: apollo-graphql:apollo-router
    name: Apollo Router
    tags:
      - Federation
      - Gateway
      - GraphQL
      - Router
      - Rust
    humanURL: https://www.apollographql.com/docs/graphos/routing
    properties:
      - url: https://www.apollographql.com/docs/graphos/routing
        type: Documentation
      - url: https://www.apollographql.com/docs/graphos/routing/configuration/overview
        type: Configuration
      - url: https://github.com/apollographql/router
        type: GitHubRepository
      - url: https://github.com/apollographql/router/releases
        type: Changelog
      - url: https://www.apollographql.com/docs/graphos/routing/security/jwt
        type: Security
    description: Apollo Router is a high-performance graph router written in Rust for running federated supergraphs using Apollo Federation 2. It serves as the execution engine for graph-based API orchestration, sitting in front of existing REST and GraphQL APIs.
  - aid: apollo-graphql:apollo-connectors
    name: Apollo Connectors
    tags:
      - Connectors
      - Federation
      - GraphQL
      - Integration
      - REST
    humanURL: https://www.apollographql.com/docs/graphos/connectors
    properties:
      - url: https://www.apollographql.com/docs/graphos/connectors
        type: Documentation
      - url: https://www.apollographql.com/docs/graphos/connectors/getting-started
        type: GettingStarted
      - url: https://www.apollographql.com/docs/graphos/connectors/getting-started/requirements
        type: Requirements
      - url: https://www.apollographql.com/graphos/apollo-connectors
        type: ProductPage
    description: Apollo Connectors simplify REST API orchestration in graphs, replacing unmaintainable procedural code with scalable, declarative schema directives. They provide a declarative language for connecting REST APIs directly to a graph without writing a separate GraphQL server.
  - aid: apollo-graphql:rover-cli
    name: Rover CLI
    tags:
      - CI/CD
      - CLI
      - Federation
      - GraphQL
      - Schema Management
    humanURL: https://www.apollographql.com/docs/rover
    properties:
      - url: https://www.apollographql.com/docs/rover
        type: Documentation
      - url: https://www.apollographql.com/docs/rover/getting-started
        type: GettingStarted
      - url: https://www.apollographql.com/docs/rover/commands/graphs
        type: CommandReference
      - url: https://www.apollographql.com/docs/rover/ci-cd
        type: CICDIntegration
      - url: https://github.com/apollographql/rover
        type: GitHubRepository
      - url: https://github.com/apollographql/rover/blob/main/CHANGELOG.md
        type: Changelog
    description: Rover is the command-line interface for managing and maintaining graphs with Apollo GraphOS. It supports publishing subgraph schemas, running a supergraph router locally, fetching schemas via introspection, composing federated supergraph schemas, and running schema checks.
  - aid: apollo-graphql:apollo-federation
    name: Apollo Federation
    tags:
      - Distributed
      - Federation
      - GraphQL
      - Microservices
      - Supergraph
    humanURL: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/federation
    properties:
      - url: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/federation
        type: Documentation
      - url: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives
        type: DirectivesReference
      - url: https://github.com/apollographql/federation
        type: GitHubRepository
      - url: https://www.apollographql.com/docs/graphos/reference/federation/versions
        type: Changelog
    description: Apollo Federation enables declarative composition of multiple APIs into a single federated GraphQL API. It serves as an API orchestration layer where clients make a single GraphQL request and the router coordinates multiple API calls to return a unified response.
  - aid: apollo-graphql:apollo-mcp-server
    name: Apollo MCP Server
    tags:
      - AI
      - GraphQL
      - MCP
      - Model Context Protocol
    humanURL: https://www.apollographql.com/docs/apollo-mcp-server
    properties:
      - url: https://www.apollographql.com/docs/apollo-mcp-server
        type: Documentation
      - url: https://github.com/apollographql/apollo-mcp-server/releases
        type: Changelog
    description: Apollo MCP Server provides Model Context Protocol integration for Apollo GraphQL, enabling AI agents and large language models to interact with GraphQL APIs through the MCP standard.
name: Apollo GraphQL
tags:
  - API Orchestration
  - Clients
  - Connectors
  - Federation
  - Graph
  - GraphQL
  - Router
  - Schema Registry
  - Supergraph
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.apollographql.com/
    name: Streamlining APIs, Databases, & Microservices | Apollo GraphQL
    type: Website
    description: 'null'
  - url: https://www.apollographql.com/pricing
    name: Apollo Pricing and Plans for GraphOS GraphQL Platform
    type: Pricing
    description: 'null'
  - url: https://www.apollographql.com/docs
    name: Documentation - Apollo GraphQL Docs
    type: Documentation
    description: 'null'
  - url: https://www.apollographql.com/tutorials/
    name: Learn with our GraphQL Tutorials, Examples, and Training - GraphQL Tutorials
    type: Tutorials
    description: 'null'
  - url: https://www.apollographql.com/tutorials/#certifications
    name: Learn with our GraphQL Tutorials, Examples, and Training - GraphQL Tutorials
    type: Certifications
    description: 'null'
  - url: https://www.apollographql.com/blog
    name: Apollo GraphQL Blog  latest insights and news on API and GraphQL solutions
    type: Blog
    description: 'null'
  - url: https://www.apollographql.com/developers
    name: Apollo Developer Hub
    type: Hub
    description: 'null'
  - url: https://community.apollographql.com/?_gl=1*1su9vuw*_gcl_au*Njc4MTcyOTc1LjE3NDk1ODk4Nzg.
    name: Apollo Community - Apollo GraphQL community
    type: Forums
    description: 'null'
  - url: https://www.apollographql.com/enterprise/support
    name: Enterprise Support
    type: Support
    description: 'null'
  - url: https://www.apollographql.com/professional-services
    name: Apollo GraphQL Professional Services
    type: ProfessionalServices
    description: 'null'
  - url: https://www.apollographql.com/events
    name: Apollo GraphQL Events
    type: Events
    description: 'null'
  - url: https://www.apollographql.com/resources
    name: Resources Hub | Apollo GraphQL
    type: Resources
    description: 'null'
  - url: https://www.apollographql.com/customers
    name: 'Customer Stories: Real Impact with Apollo GraphQL'
    type: Customers
    description: 'null'
  - url: https://www.apollographql.com/trust
    name: 'Trust @ Apollo: Build & Scale GraphQL Safely: Tech Talks, Best Practices & More'
    type: Trust
    description: 'null'
  - url: https://www.apollographql.com/partners
    name: Apollo GraphQL Partners
    type: Partners
    description: 'null'
  - url: https://support.apollographql.com/?_gl=1*hmmq01*_gcl_au*Njc4MTcyOTc1LjE3NDk1ODk4Nzg.
    name: Apollo Support
    type: Support
    description: 'null'
  - url: https://studio.apollographql.com/signup?_gl=1%2Ahmmq01%2A_gcl_au%2ANjc4MTcyOTc1LjE3NDk1ODk4Nzg.
    name: Studio
    type: SignUp
    description: 'null'
  - url: https://studio.apollographql.com/login?from=%2Fwelcome
    name: Studio
    type: Login
    description: 'null'
  - url: https://www.apollographql.com/leadership
    name: Apollo GraphQL Leadership Team
    type: AboutPage
    description: 'null'
  - url: https://www.apollographql.com/careers
    name: Careers at Apollo GraphQL
    type: Careers
    description: 'null'
  - url: https://www.apollographql.com/newsroom
    name: Apollo GraphQL Newsroom
    type: News
    description: 'null'
  - url: https://www.apollographql.com/contact-sales
    name: Contact Apollo GraphQL Sales
    type: Contact
    description: 'null'
  - url: https://www.apollographql.com/help-center
    name: Apollo GraphQL Help Center
    type: HelpCenter
    description: 'null'
  - url: https://www.apollographql.com/privacy-policy
    name: Apollo GraphQL Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.apollographql.com/Apollo-Website-Terms-of-Service.pdf
    name: Apollo GraphQL Website Terms of Service
    type: TermsOfService
    description: 'null'
  - url: https://www.apollographql.com/trust/legal-and-privacy
    name: Apollo GraphQL Legal and Privacy Resources
    type: Legal
    description: 'null'
  - url: https://www.apollographql.com/trust/compliance-and-security
    name: Apollo GraphQL Security and Compliance
    type: Security
    description: 'null'
  - url: https://www.apollographql.com/trust/graphos-data-privacy-and-compliance
    name: GraphOS Data Privacy and Compliance
    type: DataPrivacy
    description: 'null'
  - url: https://status.apollographql.com/
    name: Apollo GraphQL System Status
    type: StatusPage
    description: 'null'
  - url: https://www.apollographql.com/docs/graphos/resources/changelog
    name: Apollo Product Changelogs
    type: Changelog
    description: 'null'
  - url: https://www.apollographql.com/why-apollo
    name: Why Apollo GraphQL
    type: WhyChooseUs
    description: 'null'
  - url: https://www.apollographql.com/graphos
    name: Apollo GraphOS Platform
    type: Platform
    description: 'null'
  - url: https://www.apollographql.com/docs/quickstart
    name: Apollo GraphOS Quickstart
    type: GettingStarted
    description: 'null'
  - url: https://www.apollographql.com/docs/ide-support
    name: Apollo IDE Support for VS Code and JetBrains
    type: IDESupport
    description: 'null'
  - url: https://github.com/apollographql
    name: Apollo GraphQL GitHub Organization
    type: GitHubOrganization
    description: 'null'
  - url: https://twitter.com/apollographql
    name: Apollo GraphQL on Twitter
    type: Twitter
    description: 'null'
  - url: https://www.linkedin.com/company/apollo-graphql
    name: Apollo GraphQL on LinkedIn
    type: LinkedIn
    description: 'null'
  - url: https://www.youtube.com/c/ApolloGraphQL
    name: Apollo GraphQL on YouTube
    type: YouTube
    description: 'null'
  - name: Features
    type: Features
    data:
      - name: Build GraphQL APIs
      - name: Deploy GraphQL APIs
      - name: Scale  GraphQL APIs
      - name: GraphQL Clients
      - name: GraphQL SDKs
      - name: Schema Registry
      - name: Connectors
      - name: Studio
      - name: CLI
      - name: Router
      - name: Federation
      - name: Platform API
      - name: MCP Server
      - name: IDE Support
      - name: Kubernetes Operator
  - name: Use Cases
    type: UseCases
    data:
      - name: AI-driven Experiences
      - name: Developer Efficiency
      - name: Enhanced Customer Experience
      - name: Modernization
      - name: Mergers and Acquisitions
  - name: Integrations
    type: Integrations
    url: https://www.apollographql.com/graphos/apollo-connectors
    data:
      - name: Anthropic
      - name: OpenAI
      - name: OData
      - name: AWS DynamoDB
      - name: Stripe
      - name: AWS Lambda
      - name: Strapi
created: '2025-06-10T00:00:00.000Z'
modified: '2026-04-19'
position: Consumer
segments:
  - Clients
  - ProCode_API_Composition
description: Whether your team is new to GraphQL, or seasoned experts, learn why Apollo is the fastest and safest way to build and scale your APIs.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
