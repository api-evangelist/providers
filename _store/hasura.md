---
aid: hasura
url: https://raw.githubusercontent.com/api-evangelist/hasura/refs/heads/main/apis.yml
apis:
  - aid: hasura:hasura-graphql-api
    name: Hasura GraphQL API
    tags:
      - GraphQL
      - Mutations
      - Queries
      - Realtime
      - Subscriptions
    humanURL: https://hasura.io/docs/2.0/api-reference/graphql-api/index/
    properties:
      - url: https://hasura.io/docs/2.0/api-reference/graphql-api/index/
        type: Documentation
      - url: https://hasura.io/docs/2.0/api-reference/overview/
        type: APIReference
      - url: https://hasura.io/docs/2.0/api-reference/restified/
        type: Documentation
      - url: https://hasura.io/docs/2.0/getting-started/overview/
        type: GettingStarted
    description: The Hasura GraphQL Engine v2 provides instant realtime GraphQL APIs on your data with fine-grained access control. Supports GraphQL queries, mutations, and subscriptions at the /v1/graphql endpoint, along with RESTified GraphQL endpoints, Relay API, metadata API, schema API, config API, health check API, PG dump API, and explain API.
  - aid: hasura:hasura-metadata-api
    name: Hasura Metadata API
    tags:
      - Configuration
      - Metadata
      - Schema
    humanURL: https://hasura.io/docs/2.0/api-reference/metadata-api/index/
    properties:
      - url: https://hasura.io/docs/2.0/api-reference/metadata-api/index/
        type: Documentation
      - url: https://hasura.io/docs/2.0/api-reference/overview/
        type: APIReference
    description: The Hasura Metadata API allows programmatic management of Hasura GraphQL Engine configuration. All requests are POST requests to the /v1/metadata endpoint, supporting operations for managing data sources, tables, relationships, permissions, remote schemas, actions, event triggers, and RESTified endpoints.
  - aid: hasura:hasura-ddn-graphql-api
    name: Hasura DDN GraphQL API
    tags:
      - Data Delivery Network
      - DDN
      - GraphQL
      - Realtime
      - Supergraph
    humanURL: https://hasura.io/docs/3.0/graphql-api/overview/
    properties:
      - url: https://hasura.io/docs/3.0/graphql-api/overview/
        type: Documentation
      - url: https://hasura.io/docs/3.0/index/
        type: Documentation
      - url: https://hasura.io/docs/3.0/graphql-api/mutations/
        type: Documentation
      - url: https://hasura.io/docs/3.0/graphql-api/subscriptions/
        type: Documentation
      - url: https://hasura.io/docs/3.0/basics/
        type: GettingStarted
      - url: https://hasura.io/docs/3.0/reference/cli/
        type: CLI
      - url: https://hasura.io/docs/3.0/reference/cli/installation/
        type: Installation
      - url: https://hasura.io/docs/3.0/reference/metadata-reference/graphql-config/
        type: APIReference
    description: The Hasura Data Delivery Network (DDN) is a metadata-driven API platform that generates instant GraphQL APIs on any data source. It provides queries, mutations, and subscriptions as root-level fields, with support for global IDs, API versioning, Apollo Federation, filtering, sorting, aggregation, and joins across multiple data connectors including PostgreSQL, MongoDB, ClickHouse, MySQL, Snowflake, Elasticsearch, and SQL Server.
  - aid: hasura:hasura-cloud-api
    name: Hasura Cloud API
    tags:
      - Cloud
      - Management
      - Projects
    humanURL: https://hasura.io/docs/2.0/api-reference/cloud-api-reference/
    properties:
      - url: https://hasura.io/docs/2.0/api-reference/cloud-api-reference/
        type: Documentation
      - url: https://hasura.io/docs/2.0/hasura-cloud/projects/index/
        type: Documentation
    description: The Hasura Cloud API provides a GraphQL endpoint at https://data.pro.hasura.io/v1/graphql to programmatically create and manage Hasura Cloud projects, tenants, collaborators, and configurations. Authentication uses Personal Access Tokens via the Authorization header.
  - aid: hasura:promptql-natural-language-api
    name: PromptQL Natural Language API
    tags:
      - AI
      - LLM
      - Natural Language
      - PromptQL
    humanURL: https://promptql.io/docs/promptql-apis/natural-language-api/
    properties:
      - url: https://promptql.io/docs/promptql-apis/natural-language-api/
        type: Documentation
      - url: https://promptql.io/docs/promptql-apis/execute-program-api/
        type: Documentation
      - url: https://hasura.io/docs/promptql/index/
        type: Documentation
      - url: https://hasura.io/docs/promptql/quickstart/
        type: GettingStarted
      - url: https://github.com/hasura/promptql-python-sdk
        type: PythonSDK
      - url: https://www.npmjs.com/package/@hasura/promptql
        type: NodeSDK
    description: The PromptQL Natural Language API allows interaction with Hasura PromptQL to send natural language messages and receive AI-powered responses with streaming support. It enables accurate AI by continuously learning the unique context of your business data, composing tool calls and LLM tasks for high explainability, accuracy, and repeatability. Available in v1 and v2 with Python and JavaScript SDKs.
name: Hasura
tags:
  - Data Access
  - GraphQL
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/hasura
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://hasura.io/
    name: 'Hasura: Meet PromptQL - Reliable AI on your data'
    type: Website
    description: We've spent years perfecting products that make it effortless to access and use data.
  - url: https://hasura.io/pricing
    name: Pricing that scales with your needs - Hasura
    type: Plans
    description: 'null'
  - url: https://hasura.io/docs/2.0/getting-started/use-case/overview/
    name: Hasura use cases overview | Hasura GraphQL Docs
    type: UseCases
    description: 'null'
  - url: https://hasura.io/docs/2.0/auth/overview/
    name: Authentication and Authorization Overview | Hasura GraphQL Docs
    type: Authentication
    description: 'null'
  - url: https://hasura.io/docs/2.0/getting-started/overview/
    name: Get started with Hasura Overview | Hasura GraphQL Docs
    type: GettingStarted
    description: 'null'
  - url: https://hasura.io/docs/2.0/getting-started/overview/
    name: Get started with Hasura Overview | Hasura GraphQL Docs
    type: GettingStarted
    description: 'null'
  - url: https://hasura.io/docs/2.0/security/overview/
    name: 'Cloud & Enterprise Edition: API Security | Hasura GraphQL Docs'
    type: Security
    description: 'null'
  - url: https://hasura.io/docs/2.0/hasura-cli/overview/
    name: Hasura CLI | Hasura GraphQL Docs
    type: CLI
    description: 'null'
  - url: https://hasura.io/docs/2.0/cloud-ci-cd/index/
    name: Continuous Integration and Continuous Deployment with Hasura Cloud | Hasura GraphQL Docs
    type: CI/CD
    description: 'null'
  - url: https://hasura.io/docs/2.0/get-support/
    name: Troubleshooting Hasura GraphQL Engine errors | Hasura GraphQL Docs
    type: Support
    description: 'null'
  - url: https://hasura.io/docs/2.0/faq/index/
    name: FAQs | Hasura GraphQL Docs
    type: FAQ
    description: 'null'
  - url: https://discord.com/invite/hasura
    name: Discord
    type: Discord
    description: 'null'
  - url: https://hasura.io/docs/2.0/glossary/index/
    name: Glossary | Hasura GraphQL Docs
    type: Glossary
    description: 'null'
  - url: https://hasura.io/blog
    name: 'The Hasura Blog: The latest best from Hasura! - Hasura GraphQL Engine Blog'
    type: Blog
    description: 'null'
  - url: https://hasura.io/pricing
    name: Pricing that scales with your needs - Hasura
    type: Pricing
    description: 'null'
  - url: https://hasura.io/customers
    name: 'Hasura Customers: Case Studies & Community Stories'
    type: Customers
    description: 'null'
  - url: https://hasura.io/events?category=Webinar#wall-section
    name: Hasura Events | Hasura GraphQL Engine
    type: Webinars
    description: 'null'
  - url: https://hasura.io/graphql/
    name: A Comprehensive Guide to GraphQL with Hasura
    type: Hub
    description: 'null'
  - url: https://hasura.io/events
    name: Hasura Events | Hasura GraphQL Engine
    type: Events
    description: 'null'
  - url: https://hasura.io/resources
    name: Hasura Whitepapers
    type: WhitePapers
    description: 'null'
  - url: https://cloud.hasura.io/signup
    name: Login | Signup - Hasura Cloud
    type: Login
    description: 'null'
  - url: https://cloud.hasura.io/signup/new_user
    name: Hasura Cloud
    type: SignUp
    description: 'null'
  - url: https://hasura.io/legal/hasura-cloud-terms-of-service
    name: 'Hasura, Inc.: Hasura Cloud Terms of Service'
    type: TermsOfService
    description: 'null'
  - url: https://hasura.io/connectors#connectors-list
    name: Connector Hub | Explore Hasura Features & Integration
    type: Integrations
    description: 'null'
  - url: https://hasura.io/learn/
    data:
      - name: (MotherDuck) DuckDB
      - name: (Turso) SQLite
      - name: AlloyDB PostgreSQL
      - name: Apache Phoenix
      - name: Athena
      - name: AWS Aurora PostgreSQL
      - name: Azure Cosmos DB for NoSQL
      - name: Azure Cosmos DB for PostgreSQL
      - name: Azure Database for PostgreSQL
      - name: BigQuery
      - name: Cassandra
      - name: Citus PostgreSQL
      - name: ClickHouse
      - name: CockroachDB PostgreSQL
      - name: Coming Soon
      - name: Databricks
      - name: DuckDuckAPI
      - name: DynamoDB
      - name: Elasticsearch
      - name: GCP Cloud SQL PostgreSQL
      - name: GraphQL
      - name: HTTP
      - name: IBM DB2
      - name: MariaDB
      - name: MongoDB
      - name: MySQL
      - name: MySQL PromptQL
      - name: Neo4j
      - name: Neon PostgreSQL
      - name: NodeJS Lambda
      - name: OpenAPI Lambda
      - name: Oracle
      - name: Oracle PromptQL
      - name: Postgres PromptQL
      - name: PostgreSQL
      - name: Prometheus Data
      - name: Qdrant Data
      - name: Redshift
      - name: SingleStore Data
      - name: Snowflake
      - name: SQL Server
      - name: Storage Data
      - name: Stripe
      - name: Timescale PostgreSQL
      - name: Trino
      - name: Weaviate
      - name: YugabyteDB PostgreSQL
    name: Fullstack GraphQL Tutorial Series | Learn GraphQL & Hasura
    type: Tutorials
  - url: https://hasura.io/learn/#learn-faq
    name: Fullstack GraphQL Tutorial Series | Learn GraphQL & Hasura
    type: FAQ
    description: 'null'
  - data:
      - name: Build GraphQL APIs
      - name: Deploy GraphQL APIs
      - name: Run GraphQL APIs
      - name: Govern GraphQL APIs
      - name: Evolve GraphQL APIs
      - name: Scale GraphQL APIs
      - name: GraphQL API
      - name: Relay API
      - name: Nested filtering
      - name: Nested aggregations
      - name: Nested pagination
      - name: Nested sorting
      - name: API versioning
      - name: Field & entity level
      - name: authorization
      - name: API requests/month
      - name: Concurrent API users
      - name: Autoscaling
      - name: Zero cold-start
      - name: Global Edge network
      - name: Intelligent geo routing
      - name: DDoS protection
      - name: Database connectors
      - name: Code connectors
      - name: API connectors
      - name: Supergraph Explorer
      - name: Supergraph Registry
      - name: Query Plan
      - name: Trace Viewer
      - name: Model Usage Statistics
      - name: Field Usage Statistics
      - name: CI/CD
      - name: Breaking change detection
      - name: Immutable builds & build URLs
      - name: Local development
      - name: Self-hosting with
      - name: v3 graphql-engine
      - name: Schema registry
      - name: Schema changelog
      - name: Independent subgraph development
      - name: Number of supergraph developers
      - name: Multi-repo CI/CD
      - name: Traces Retention time
      - name: API performance metrics
      - name: Model Usage Statistics
      - name: Field Usage Statistics
      - name: Dedicated VPC
      - name: Choice of cloud
      - name: Choice of Regions
      - name: VPC peering
      - name: PrivateLink/Private
      - name: Service Connect
      - name: Private/Internal-only
      - name: GraphQL API endpoints
      - name: Custom firewall rules
      - name: Audit logs
      - name: Single sign-on (SSO)
      - name: SOC2 Type 2
      - name: GDPR Compliance
      - name: Data processing agreement
      - name: Business associate agreement
      - name: HIPAA compliance
    name: Features
    type: Features
  - data:
      - name: Use Cases
      - name: GraphQL backend
      - name: Data Access Layer
      - name: API gateway
    name: Features
    type: Features
  - url: https://hasura.io/about/
    name: About Hasura
    type: AboutPage
    description: Hasura makes data access easy, fast, secure and scalable, with offices in San Francisco and Bangalore.
  - url: https://status.hasura.io/
    name: Hasura Status
    type: StatusPage
    description: 'null'
  - url: https://hasura.io/changelog
    name: Hasura Changelog
    type: Changelog
    description: 'null'
  - url: https://github.com/hasura/graphql-engine
    name: Hasura GraphQL Engine GitHub Repository
    type: GitHubRepository
    description: 'null'
  - url: https://github.com/hasura/graphql-engine/discussions
    name: Hasura GitHub Discussions
    type: GitHubDiscussions
    description: 'null'
  - url: https://github.com/hasura/graphql-engine/releases
    name: Hasura GraphQL Engine Releases
    type: GitHubReleases
    description: 'null'
  - url: https://twitter.com/hasurahq
    name: Hasura on Twitter
    type: Twitter
    description: 'null'
  - url: https://www.linkedin.com/company/hasura/
    name: Hasura on LinkedIn
    type: LinkedIn
    description: 'null'
  - url: https://www.youtube.com/channel/UCZo1ciR8pZvdD3Wxp9aSNhQ
    name: Hasura on YouTube
    type: YouTube
    description: 'null'
  - url: https://www.reddit.com/r/Hasura/
    name: Hasura on Reddit
    type: Reddit
    description: 'null'
  - url: https://stackoverflow.com/questions/tagged/hasura
    name: Hasura on Stack Overflow
    type: StackOverflow
    description: 'null'
  - url: https://hasura.io/legal/hasura-privacy-policy
    name: Hasura Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://hasura.io/legal/website-terms-of-use
    name: Hasura Terms of Use
    type: TermsOfUse
    description: 'null'
  - url: https://hasura.io/contact-us
    name: Contact Hasura
    type: Contact
    description: 'null'
  - url: https://hasura.io/help/
    name: Get Help from the Hasura Team
    type: Help
    description: 'null'
  - url: https://hasura.io/community
    name: Hasura Community
    type: Community
    description: 'null'
  - url: https://hasura.io/ddn
    name: Hasura Data Delivery Network
    type: ProductPage
    description: Metadata-driven API platform for building, deploying, governing, and evolving high-quality API layers on all your data.
  - url: https://hasura.io/docs/2.0/api-reference/overview/
    name: Hasura v2 API Reference Overview
    type: APIReference
    description: 'null'
  - url: https://hasura.io/docs/3.0/index/
    name: Hasura DDN Documentation
    type: Documentation
    description: 'null'
  - url: https://hasura.io/user-stories/
    name: Hasura User Stories and Case Studies
    type: CaseStudies
    description: 'null'
  - url: https://hasura.io/legal
    name: Hasura Legal
    type: Legal
    description: 'null'
  - url: https://hasura.io/docs/2.0/enterprise/release-notes/
    name: Hasura Enterprise Edition Release Notes
    type: ReleaseNotes
    description: 'null'
  - url: https://hasura.io/learn-more
    name: Hasura Data API Platform Overview
    type: ProductPage
    description: 'null'
created: '2025-06-10T00:00:00.000Z'
modified: '2026-04-28'
position: Consumer
segments:
  - Gateways
  - ProCode_API_Composition
description: We've spent years perfecting products that make it effortless to access and use data.PromptQL for AIAccurate AI by continuously learning the unique context of your business.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
