---
aid: amazon-web-services
url: >-

  https://raw.githubusercontent.com/api-search/cloud/main/_apis/amazon-web-services/apis.md
apis:
  - aid: amazon-web-services:aws-certificate-manager
    name: AWS Certificate Manager
    tags:
      - Certificates
      - Options
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/certificate-manager/
    overlays:
      - url: overlays/acm-openapi-search.yml
        type: APIs.io Search
      - url: overlays/acm-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/certificate-manager/
        type: Documentation
      - url: openapi/acm-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/certificate-manager//pricing/
        type: Pricing
      - url: https://aws.amazon.com/certificate-manager//getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/certificate-manager//partners/
        type: Partners
      - url: https://aws.amazon.com/certificate-manager//events/
        type: Events
      - url: https://aws.amazon.com/certificate-manager/features/
        type: Features
      - url: https://aws.amazon.com/certificate-manager/resources/
        type: Resources
      - url: https://aws.amazon.com/certificate-manager/faqs/
        type: FAQ
    description: |-

      Utilize the AWS Certificate Manager (ACM) to effortlessly handle the
      provisioning, management, and deployment of SSL/TLS certificates for both
      public and private use with AWS services and internal connected resources.
      With ACM, the tedious tasks of purchasing, uploading, and renewing SSL/TLS
      certificates are streamlined and automated, saving you valuable time and
      effort.
  - aid: amazon-web-services:amazon-identity-and-access-management-access-analyzer
    name: Amazon Identity and Access Management Access Analyzer
    tags:
      - ARN
      - Access
      - Analyzed
      - Analyzer
      - Analyzers
      - Archive
      - Checks
      - Findings
      - Generated
      - Generation
      - Grants
      - Names
      - Policies
      - Previews
      - Resources
      - Rules
      - Scans
      - Untag
      - Validate
      - Validations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iam/access-analyzer/
    properties:
      - url: https://aws.amazon.com/iam/access-analyzer/
        type: Documentation
      - url: openapi/accessanalyzer-openapi-original.yml
        type: OpenAPI
    description: |-

      The API for IAM Access Analyzer offers users a variety of tools to
      effectively manage their Identity and Access Management policies. These
      tools include the ability to identify external and unused access, perform
      basic and custom policy checks, and create highly detailed policies.
  - aid: amazon-web-services:aws-migration-hub
    name: AWS Migration Hub
    tags:
      - Attributes
      - Migrations
      - Resources
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/migration-hub/
    overlays:
      - url: overlays/awsmigrationhub-openapi-search.yml
        type: APIs.io Search
      - url: overlays/awsmigrationhub-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/migration-hub/
        type: Documentation
      - url: openapi/awsmigrationhub-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/migration-hub/features/
        type: Features
      - url: https://aws.amazon.com/migration-hub/pricing/
        type: Pricing
      - url: https://aws.amazon.com/migration-hub/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/migration-hub/resources/
        type: Resources
      - url: https://aws.amazon.com/migration-hub/faqs/
        type: FAQ
      - url: https://aws.amazon.com/migration-hub/partners/
        type: Partners
    description: |-

      The AWS Migration Hub API provides users with the ability to view server
      and application migration progress and easily incorporate
      resource-specific migration tools through a code-based interface. To
      ensure smooth operation, it is crucial to specify your AWS Migration Hub
      home region before using any API functions to prevent encountering a
      HomeRegionNotSetException error. Furthermore, all API requests should
      originate from within your assigned home region for proper functioning.
  - aid: amazon-web-services:amazon-managed-service-for-prometheus
    name: Amazon Managed Service for Prometheus
    tags:
      - ARN
      - Alert  Management
      - Alerts
      - Ali
      - Alias
      - Configurations
      - Default
      - Definitions
      - Describe
      - Groups
      - Logging
      - Managers
      - Names
      - Namespaces
      - Resources
      - Rule  Groups  Namespaces
      - Rule Groups
      - Rules
      - Scraper  Configurations
      - Scraper Configurations
      - Scrapers
      - Untag
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/prometheus/
    overlays:
      - url: overlays/amp-openapi-search.yml
        type: APIs.io Search
      - url: overlays/amp-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/prometheus/
        type: Documentation
      - url: openapi/amp-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/prometheus/features/
        type: Features
      - url: https://aws.amazon.com/prometheus/pricing/
        type: Pricing
      - url: https://aws.amazon.com/prometheus/faqs/
        type: FAQ
      - url: https://aws.amazon.com/prometheus/customers/
        type: Customers
      - url: https://aws.amazon.com/prometheus/partners/
        type: Partners
      - url: https://aws.amazon.com/prometheus/resources/
        type: Resources
      - url: https://aws.amazon.com/prometheus/videos/
        type: Videos
    description: |-

      The Amazon Managed Service for Prometheus API is a serverless monitoring
      service designed for container metrics. It allows users to securely
      monitor container environments at scale using the familiar open-source
      Prometheus data model and query language. This service provides improved
      scalability, availability, and security without the need to manage
      underlying infrastructure. The API includes both an Amazon Web Services
      API for managing resources such as workspaces, rule groups, and alert
      managers, as well as a Prometheus-compatible API for working within the
      Prometheus workspace.
  - aid: amazon-web-services:amazon-api-gateway
    name: Amazon API Gateway
    tags:
      - ARN
      - Accounts
      - Authorizers
      - Base Paths
      - Cache
      - Certificates
      - Clients
      - Data
      - Default
      - Deployments
      - Documentation
      - Domain Names
      - Domains
      - Exports
      - Flush
      - Gateways
      - Import
      - Integrations
      - Keys
      - Links
      - Mapping
      - Methods
      - Model Name
      - Models
      - Names
      - Parts
      - Paths
      - Plans
      - REST
      - Request Validators
      - Resources
      - Response Types
      - Responses
      - Stage Name
      - Stages
      - Status Codes
      - Tags
      - Templates
      - Types
      - Untag
      - Usage
      - Usage Plans
      - VPC
      - VPC Links
      - Validators
      - Versions
      - Vpclink
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/api-gateway/
    overlays:
      - url: overlays/apigateway-openapi-search.yml
        type: APIs.io Search
      - url: overlays/apigateway-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/api-gateway/
        type: Documentation
      - url: openapi/apigateway-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/api-gateway/features/
        type: Features
      - url: https://aws.amazon.com/api-gateway/pricing/
        type: Pricing
      - url: https://aws.amazon.com/api-gateway/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/api-gateway/resources/
        type: Resources
      - url: https://aws.amazon.com/api-gateway/faqs/
        type: FAQ
      - url: https://console.aws.amazon.com/apigateway/
        type: Documentation
      - url: >-

          https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html
        type: Websockets
    description: |-

      Amazon API Gateway is a powerful tool that enables developers to create
      and manage secure and scalable back ends for mobile and web applications.
      With API Gateway, developers can easily connect their applications to APIs
      running on Lambda, Amazon EC2, or other external web services. This
      ensures robust and reliable communication between applications and APIs,
      all within a secure environment.
  - aid: amazon-web-services:amazon-web-services-private-certificate-authority
    name: Amazon Web Services Private Certificate Authority
    tags:
      - Authorization
      - Certificates
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/private-ca/
    overlays:
      - url: overlays/acm-pca-openapi-search.yml
        type: APIs.io Search
      - url: overlays/acm-pca-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/private-ca/
        type: Documentation
      - url: openapi/acm-pca-openapi-original.yml
        type: OpenAPI
    description: |-

      The API Reference for Amazon Web Services Private Certificate Authority
      offers a detailed overview on setting up and controlling a private
      certificate authority (CA) for your organization. It provides in-depth
      explanations on each action and data type, including syntax and usage
      examples. The documentation for each action includes information on API
      request parameters and JSON responses. Additionally, users have the option
      to utilize Amazon Web Services SDKs for accessing APIs that are customized
      for their preferred programming language or platform.
  - aid: amazon-web-services:aws-application-fabric
    name: AWS Application Fabric
    tags:
      - ARN
      - Access
      - Application  Authorizations
      - Application  Bundles
      - Applications
      - Authorization
      - Batches
      - Bundles
      - Connect
      - Destinations
      - Ingestion  Destinations
      - Ingestions
      - Resources
      - Stop
      - Tasks
      - Untag
      - User  Access
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/appfabric/
    overlays:
      - url: overlays/appfabric-openapi-search.yml
        type: APIs.io Search
      - url: overlays/appfabric-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/appfabric/
        type: Documentation
      - url: openapi/appfabric-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Web Services AppFabric API offers effortless incorporation of
      SaaS applications into your company's infrastructure, facilitating
      streamlined oversight and protection by IT and security professionals
      using a standardized data structure. Leveraging the capabilities of
      generative AI, employees can simplify their daily workflows.
  - aid: amazon-web-services:amazon-appflow
    name: Amazon AppFlow
    tags:
      - ARN
      - Cache
      - Cancel
      - Connectors
      - Describe
      - Entities
      - Execution
      - Executions
      - Flows
      - Metadata
      - Profiles
      - Records
      - Register
      - Registrations
      - Reset
      - Resources
      - Stop
      - Unregister
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/appflow/
    overlays:
      - url: overlays/appflow-openapi-search.yml
        type: APIs.io Search
      - url: overlays/appflow-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/appflow/
        type: Documentation
      - url: openapi/appflow-openapi-original.yml
        type: OpenAPI
    description: |-

      This API, Amazon AppFlow, allows for seamless automation of data flows
      between SaaS applications and AWS services with just a few clicks. You can
      run these data flows at your preferred frequency, whether on a schedule,
      in response to a business event, or on demand. Simplify data preparation
      through transformations, partitioning, and aggregation. Additionally,
      automate the preparation and registration of your schema with the AWS Glue
      Data Catalog for easy discovery and sharing of data with AWS analytics and
      machine learning services.
  - aid: amazon-web-services:aws-auto-scaling
    name: AWS Auto Scaling
    tags:
      - Resources
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/autoscaling/
    overlays:
      - url: overlays/application-autoscaling-openapi-search.yml
        type: APIs.io Search
      - url: overlays/application-autoscaling-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/autoscaling/
        type: Documentation
      - url: openapi/application-autoscaling-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/autoscaling/features/
        type: Features
      - url: https://aws.amazon.com/autoscaling/pricing/
        type: Pricing
      - url: https://aws.amazon.com/autoscaling/resources/
        type: Resources
      - url: https://aws.amazon.com/autoscaling/faqs/
        type: FAQ
    description: |-

      AWS Auto Scaling is a service that automatically adjusts the capacity of
      your applications to maintain consistent performance at the most
      cost-effective rate. It allows you to easily set up scaling for multiple
      resources across various services in just minutes. With a user-friendly
      interface, you can create scaling plans for resources such as Amazon EC2
      instances, Amazon ECS tasks, Amazon DynamoDB tables, Amazon Aurora
      Replicas, and Spot Fleets.
  - aid: amazon-web-services:aws-application-cost-profiler
    name: AWS Application Cost Profiler
    tags:
      - Applications
      - Definitions
      - Import
      - Reports
      - Usage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/
    overlays:
      - url: overlays/applicationcostprofiler-openapi-search.yml
        type: APIs.io Search
      - url: overlays/applicationcostprofiler-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/
        type: Documentation
      - url: openapi/applicationcostprofiler-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS Application Cost Profiler API enables users to manage application
      cost report definitions, including viewing, creating, updating, and
      deleting them. It also allows users to import usage data into the
      Application Cost Profiler service. For more information on using this API,
      please consult the AWS Application Cost Profiler User Guide.
  - aid: amazon-web-services:aws-app-mesh
    name: AWS App Mesh
    tags:
      - Gateways
      - Mesh
      - Meshes
      - Names
      - Nodes
      - Resources
      - Router
      - Routers
      - Routes
      - Services
      - Tags
      - Untag
      - Virtual
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/app-mesh/
    overlays:
      - url: overlays/appmesh-openapi-search.yml
        type: APIs.io Search
      - url: overlays/appmesh-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/app-mesh/
        type: Documentation
      - url: openapi/appmesh-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/app-mesh/features/
        type: Features
      - url: https://aws.amazon.com/app-mesh/pricing/
        type: Pricing
      - url: https://aws.amazon.com/app-mesh/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/app-mesh/faqs/
        type: FAQ
      - url: https://aws.amazon.com/app-mesh/resources/
        type: Resources
    description: |-

      The AWS App Mesh is a service mesh powered by the Envoy proxy that
      streamlines the monitoring and management of containerized microservices.
      It simplifies communication between microservices, providing in-depth
      visibility and ensuring reliable availability for applications. 
  - aid: amazon-web-services:aws-appsync
    name: AWS AppSync
    tags:
      - ARN
      - Associate
      - Associations
      - Cache
      - Caches
      - Code
      - Creation
      - Data
      - Data Planes
      - Data Source
      - Disassociate
      - Domain Names
      - Domains
      - Environments
      - Evaluate
      - Evaluate Code
      - Evaluate Template
      - Fields
      - Flush
      - Functions
      - Graph QL
      - Introspections
      - Keys
      - Mapping
      - Merge
      - Merged
      - Names
      - Resolvers
      - Resources
      - Schemas
      - Sources
      - Tags
      - Templates
      - Types
      - Untag
      - Variables
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/appsync/
    overlays:
      - url: overlays/appsync-openapi-search.yml
        type: APIs.io Search
      - url: overlays/appsync-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/appsync/
        type: Documentation
      - url: openapi/appsync-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/appsync/pricing/
        type: Pricing
      - url: https://aws.amazon.com/appsync/faqs/
        type: FAQ
      - url: https://aws.amazon.com/appsync/customers/
        type: Customers
      - url: https://aws.amazon.com/appsync/resources/
        type: Resources
      - url: https://aws.amazon.com/appsync/blog/
        type: Blog
      - url: >-

          https://docs.aws.amazon.com/appsync/latest/devguide/rds-introspection.html
        type: Introspection
    description: |-

      With AWS AppSync, easily create serverless GraphQL and Pub/Sub APIs that
      streamline application development by providing a secure endpoint for
      querying, updating, and publishing data.
  - aid: amazon-web-services:amazon-appstream
    name: Amazon AppStream
    tags:
      - Stack
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/appstream2/
    overlays:
      - url: overlays/appstream-openapi-search.yml
        type: APIs.io Search
      - url: overlays/appstream-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/appstream2/
        type: Documentation
      - url: openapi/appstream-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/appstream2/features/
        type: Features
      - url: https://aws.amazon.com/appstream2/pricing/
        type: Pricing
      - url: https://aws.amazon.com/appstream2/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/appstream2/resources/
        type: Resources
      - url: https://aws.amazon.com/appstream2/faqs/
        type: FAQ
      - url: https://aws.amazon.com/appstream2/customers/
        type: Customers
      - url: https://aws.amazon.com/appstream2/software-vendors/
        type: Vendors
      - url: https://aws.amazon.com/appstream2/enterprises/
        type: Enterprise
      - url: https://aws.amazon.com/appstream2/education/
        type: Education
    description: |-

      Explore the Amazon AppStream 2.0 API Reference to access detailed
      descriptions and syntax for actions and data types within the service.
      Amazon AppStream 2.0 is a secure, fully managed application streaming
      service that allows you to effortlessly stream desktop applications to
      users without the need for application rewriting. 
  - aid: amazon-web-services:amplify
    name: Amplify
    tags:
      - ARN
      - Access
      - Access Logs
      - Applications
      - Artifacts
      - Associations
      - Backend Environments
      - Backends
      - Branch
      - Branches
      - Deployments
      - Domains
      - Environments
      - Generate
      - Jobs
      - Logs
      - Names
      - Resources
      - Stop
      - Tags
      - URL
      - Untag
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/amplify/
    overlays:
      - url: overlays/amplify-openapi-search.yml
        type: APIs.io Search
      - url: overlays/amplify-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/amplify/
        type: Documentation
      - url: openapi/amplify-openapi-original.yml
        type: OpenAPI
    description: |-

      Amplify is an API designed to facilitate the development and deployment of
      cloud-powered mobile and web applications. Amplify Hosting offers a
      continuous delivery and hosting service specifically tailored for web
      applications. To learn more about Amplify Hosting, refer to the user
      guide. 
  - aid: amazon-web-services:aws-app-runner
    name: AWS App Runner
    tags:
      - Connections
      - Ingress
      - VPC
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/apprunner/
    overlays:
      - url: overlays/apprunner-openapi-search.yml
        type: APIs.io Search
      - url: overlays/apprunner-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/apprunner/
        type: Documentation
      - url: openapi/apprunner-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/apprunner/features/
        type: Features
      - url: https://aws.amazon.com/apprunner/pricing/
        type: Pricing
      - url: https://aws.amazon.com/apprunner/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/apprunner/resources/
        type: Resources
      - url: https://aws.amazon.com/apprunner/faqs/
        type: FAQ
      - url: https://aws.amazon.com/apprunner/customers/
        type: Customers
      - url: https://aws.amazon.com/apprunner/partners/
        type: Partners
    description: |-

      App Runner is an application service on Amazon Web Services that allows
      you to quickly and easily deploy container images or source code to the
      cloud. It eliminates the need to learn new technologies or manually
      provision resources. App Runner seamlessly connects to your container
      registry or source code repository, providing a fully managed delivery
      pipeline with high performance, scalability, and security. For more
      information, refer to the App Runner Developer Guide and Release Notes. 
  - aid: amazon-web-services:amazon-athena
    name: Amazon Athena
    tags:
      - Group
      - Work
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/athena/
    overlays:
      - url: overlays/athena-openapi-search.yml
        type: APIs.io Search
      - url: overlays/athena-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/athena/
        type: Documentation
      - url: openapi/athena-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/athena/pricing/
        type: Pricing
      - url: https://aws.amazon.com/athena/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/athena/resources/
        type: Resources
      - url: https://aws.amazon.com/athena/faqs/
        type: FAQ
      - url: https://aws.amazon.com/athena/features/
        type: Features
      - url: https://aws.amazon.com/athena/spark/
        type: Spark
      - url: https://docs.aws.amazon.com/athena/latest/ug/connectors-prebuilt.html
        type: Connectors
    description: |-

      Amazon Athena is a user-friendly query service that allows you to analyze
      data stored in Amazon S3 using standard SQL. By pointing Athena to your
      data in S3, you can easily run ad-hoc queries and receive results within
      seconds. This serverless tool eliminates the need for infrastructure setup
      and management, as you only pay for the queries you execute. Athena is
      designed to scale automatically, executing queries in parallel to deliver
      fast results even with large datasets and complex queries. 
  - aid: amazon-web-services:amazon-ec2-auto-scaling
    name: Amazon EC2 Auto Scaling
    tags:
      - Auto
      - Group
      - Scaling
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ec2/autoscaling/
    overlays:
      - url: overlays/autoscaling-openapi-search.yml
        type: APIs.io Search
      - url: overlays/autoscaling-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ec2/autoscaling/
        type: Documentation
      - url: openapi/autoscaling-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ec2/autoscaling/features/
        type: Features
      - url: https://aws.amazon.com/ec2/autoscaling/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ec2/autoscaling/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/ec2/autoscaling/resources/
        type: Resources
      - url: https://aws.amazon.com/ec2/autoscaling/faqs/
        type: FAQ
      - url: >-

          https://docs.aws.amazon.com/autoscaling/latest/userguide/GettingStartedTutorial.html
        type: Tutorial
    description: |-

      The Amazon EC2 Auto Scaling API allows users to automate the launching and
      terminating of EC2 instances based on predefined scaling policies,
      scheduled actions, and health checks. Refer to the Amazon EC2 Auto Scaling
      User Guide and API Reference for further details.
  - aid: amazon-web-services:aws-b2b-data-interchange
    name: AWS B2B Data Interchange
    tags:
      - Transformers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/b2b-data-interchange/
    overlays:
      - url: overlays/b2bi-openapi-search.yml
        type: APIs.io Search
      - url: overlays/b2bi-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/b2b-data-interchange/
        type: Documentation
      - url: openapi/b2bi-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/b2b-data-interchange/features/
        type: Features
      - url: https://aws.amazon.com/b2b-data-interchange/features/
        type: Pricing
      - url: https://aws.amazon.com/b2b-data-interchange/faqs/
        type: FAQ
    description: |-

      The Amazon Web Services B2B Data Interchange API Reference is a
      comprehensive guide that includes detailed descriptions, API request
      parameters, and XML responses for each of the B2BI API actions. B2BI
      facilitates the seamless exchange of EDI-based business transactions at
      cloud scale, offering elasticity and pay-as-you-go pricing. 
  - aid: amazon-web-services:aws-audit-manager
    name: AWS Audit Manager
    tags:
      - ARN
      - Accounts
      - Administrative
      - Assessments
      - Associate
      - Attributes
      - Batches
      - Change
      - Change Logs
      - Controls
      - Data
      - Delegation
      - Delegations
      - Deregister
      - Disassociate
      - Domains
      - Evidence
      - File
      - Folders
      - Frameworks
      - Import
      - Insights
      - Integrity
      - Keywords
      - Logs
      - Notifications
      - Organizations
      - Register
      - Reports
      - Resources
      - Scopes
      - Services
      - Sets
      - Settings
      - Share
      - Sources
      - Status
      - Tags
      - URL
      - Untag
      - Uploads
      - Validate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/audit-manager/
    overlays:
      - url: overlays/auditmanager-openapi-search.yml
        type: APIs.io Search
      - url: overlays/auditmanager-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/audit-manager/
        type: Documentation
      - url: openapi/auditmanager-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/audit-manager/features/
        type: Features
      - url: https://aws.amazon.com/audit-manager/pricing/
        type: Pricing
      - url: https://aws.amazon.com/audit-manager/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/audit-manager/faqs/
        type: FAQ
      - url: >-

          https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-overviews.html
        type: User Guide
      - url: >-

          https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html
        type: Examples
      - url: >-

          https://docs.aws.amazon.com/audit-manager/latest/userguide/dashboard.html
        type: Dashboard
    description: |-

      Introducing the Audit Manager API reference, a comprehensive resource for
      developers looking for in-depth insights into Audit Manager API
      functionalities, data structures, and error handling. Audit Manager is a
      robust service designed to automate the collection of evidence to support
      ongoing auditing of your Amazon Web Services usage. With this tool, users
      can evaluate the effectiveness of controls, mitigate risks, and simplify
      compliance procedures.
  - aid: amazon-web-services:aws-auto-scaling
    name: AWS Auto Scaling
    tags:
      - Plan
      - Scaling
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/autoscaling/
    overlays:
      - url: overlays/autoscaling-plans-openapi-search.yml
        type: APIs.io Search
      - url: overlays/autoscaling-plans-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/autoscaling/
        type: Documentation
      - url: openapi/autoscaling-plans-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/autoscaling/features/
        type: Features
      - url: https://aws.amazon.com/autoscaling/pricing/
        type: Pricing
      - url: https://aws.amazon.com/autoscaling/resources/
        type: Resources
      - url: https://aws.amazon.com/autoscaling/faqs/
        type: FAQ
    description: |-

      This API allows you to easily create and manage scaling plans for your
      applications using AWS Auto Scaling. With this service, you can define
      target tracking scaling policies to automatically scale your AWS resources
      based on utilization, as well as scale Amazon EC2 Auto Scaling groups
      using predictive scaling and dynamic scaling to quickly adjust your
      capacity. You can also set minimum and maximum capacity limits, retrieve
      information on existing scaling plans, and access forecast data for up to
      56 days previous.
  - aid: amazon-web-services:aws-backup
    name: AWS Backup
    tags:
      - ARN
      - Access
      - Accounts
      - Air
      - Associations
      - Audit
      - Backup
      - Cancel
      - Configurations
      - Copy
      - Describe
      - Disassociate
      - Exports
      - Frameworks
      - Gapped
      - Global
      - Hold
      - Holds
      - Inferred
      - JSON
      - Jobs
      - Legal
      - Lifecycle
      - Locks
      - Logically
      - Metadata
      - Names
      - Notifications
      - Parents
      - Plan
      - Plans
      - Points
      - Policies
      - Protected
      - Recovery
      - Regions
      - Reports
      - Resources
      - Restore
      - Results
      - Selections
      - Settings
      - Stop
      - Summaries
      - Supported
      - Tags
      - Templates
      - Testing
      - Types
      - Untag
      - Val
      - Validations
      - Vault
      - Vaults
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/backup/
    overlays:
      - url: overlays/backup-openapi-search.yml
        type: APIs.io Search
      - url: overlays/backup-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/backup/
        type: Documentation
      - url: openapi/backup-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/backup/#
        type: Features
      - url: https://aws.amazon.com/backup/pricing/?nc=sn&loc=3
        type: Pricing
      - url: https://aws.amazon.com/backup/getting-started/?nc=sn&loc=4
        type: Getting Started
      - url: https://aws.amazon.com/backup/resources/
        type: Resources
      - url: https://aws.amazon.com/backup/faqs/?nc=sn&loc=6
        type: FAQ
      - url: https://aws.amazon.com/backup/customers/?nc=sn&loc=7
        type: Customers
    description: |-

      This API, Backup Backup, offers a comprehensive backup solution
      specifically tailored for Amazon Web Services (AWS) and its related data.
      With features such as simplified backup creation, migration, restoration,
      and deletion, as well as robust reporting and auditing capabilities,
      Backup Backup ensures the protection of your AWS services and data.
  - aid: amazon-web-services:aws-batch
    name: AWS Batch
    tags:
      - ARN
      - Cancel
      - Cancel Jobs
      - Compute
      - Computer Environments
      - Definitions
      - Deregister
      - Deregister Job Definitions
      - Describe
      - Environments
      - Job Definitions
      - Job Queues
      - Jobs
      - Policies
      - Queues
      - Register
      - Register Job Definitions
      - Resources
      - Scheduling
      - Scheduling Policies
      - Scheduling Policy
      - Submit
      - Submit Jobs
      - Tags
      - Terminate
      - Terminate Jobs
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/batch/
    overlays:
      - url: overlays/batch-openapi-search.yml
        type: APIs.io Search
      - url: overlays/batch-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/batch/
        type: Documentation
      - url: openapi/batch-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/batch/features/?nc=sn&loc=2
        type: Features
      - url: https://aws.amazon.com/batch/pricing/?nc=sn&loc=3
        type: Pricing
      - url: https://aws.amazon.com/batch/faqs/
        type: FAQ
    description: |-

      Batch Using Batch, you can run batch computing workloads on the Amazon Web
      Services Cloud. Batch computing is a common means for developers,
      scientists, and engineers to access large amounts of compute resources.
      Batch uses the advantages of the batch computing to remove the
      undifferentiated heavy lifting of configuring and managing required
      infrastructure. 
  - aid: amazon-web-services:amazon-bedrock-agent
    name: Amazon Bedrock Agent
    tags:
      - Agent
      - Agents
      - Alias
      - Aliases
      - Base
      - Generate
      - Invoke
      - Knowledge
      - Knowledgebases
      - Retrieve
      - Sessions
      - Text
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/bedrock/agents/
    overlays:
      - url: overlays/bedrock-agent-runtime-openapi-search.yml
        type: APIs.io Search
      - url: overlays/bedrock-agent-runtime-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/bedrock/agents/
        type: Documentation
      - url: openapi/bedrock-agent-runtime-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/bedrock/agents/#
        type: Features
      - url: >-

          https://aws.amazon.com/bedrock/pricing/?refid=0eaabb80-ee46-4e73-94ae-368ffb759b62
        type: Pricing
      - url: https://aws.amazon.com/bedrock/agents/
        type: Models
      - url: >-

          https://aws.amazon.com/bedrock/faqs/?refid=0eaabb80-ee46-4e73-94ae-368ffb759b62
        type: FAQ
      - url: https://aws.amazon.com/bedrock/testimonials/
        type: Testimonials
      - url: >-

          https://aws.amazon.com/bedrock/resources/?refid=0eaabb80-ee46-4e73-94ae-368ffb759b62
        type: Resources
    description: |-

      Enhance the capabilities of generative AI applications by allowing them to
      seamlessly perform complex multi-step tasks across various company systems
      and data sources. Amazon Bedrock agents improve operational efficiency,
      customer service, and decision-making processes whilst simultaneously
      driving down costs and fostering innovation within the organization.
  - aid: amazon-web-services:aws-billing-conductor
    name: AWS Billing Conductor
    tags:
      - ARN
      - Accounts
      - Associate
      - Associated
      - Associations
      - Batches
      - Billing
      - Cost
      - Custom
      - Disassociate
      - Groups
      - Items
      - Line
      - Plan
      - Plans
      - Pricing
      - Reports
      - Resources
      - Rules
      - Tags
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/aws-cost-management/aws-billing-conductor/
    overlays:
      - url: overlays/billingconductor-openapi-search.yml
        type: APIs.io Search
      - url: overlays/billingconductor-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/aws-cost-management/aws-billing-conductor/
        type: Documentation
      - url: openapi/billingconductor-openapi-original.yml
        type: OpenAPI
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-billing-conductor/features/
        type: Features
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-billing-conductor/pricing/
        type: Pricing
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-billing-conductor/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/aws-cost-management/aws-billing-conductor/faqs/
        type: FAQ
    description: |-

      The Amazon Web Services Billing Conductor API is a fully managed service
      that allows you to customize your billing data each month for accurate
      showback or chargeback to your end customers. It does not alter the way
      you are billed by AWS, but rather enables you to configure, generate, and
      display rates for specific customers during a billing period. You can also
      compare the rates you set to your actual AWS rates. With the API, payer
      accounts can view custom rates on the billing details page or set up cost
      and usage reports per billing group. 
  - aid: amazon-web-services:aws-budgets
    name: AWS Budgets
    tags:
      - Subscribers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/aws-cost-management/aws-budgets/
    overlays:
      - url: overlays/budgets-openapi-search.yml
        type: APIs.io Search
      - url: overlays/budgets-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/aws-cost-management/aws-budgets/
        type: Documentation
      - url: openapi/budgets-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/
        type: Pricing
      - url: https://aws.amazon.com/aws-cost-management/aws-budgets/faqs/
        type: FAQ
      - url: >-

          https://aws.amazon.com/blogs/aws-cloud-financial-management/launch-aws-budgets-reports/
        type: Reports
    description: |-

      Manage your expenses and usage with ease using the AWS Budgets API. Create
      personalized budgets to monitor your costs and usage, and receive instant
      notifications via email or SNS alerts if you surpass your set threshold.
      Stay on top of your spending and act swiftly to prevent overages.
  - aid: amazon-web-services:aws-cost-explorer
    name: AWS  Cost Explorer
    tags:
      - Categories
      - Cost
      - Definitions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://ce.us-east-1.amazonaws.com
    humanURL: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/
    overlays:
      - url: overlays/ce-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ce-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/
        type: Documentation
      - url: openapi/ce-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/features/
        type: Features
      - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/
        type: Pricing
      - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/faqs/
        type: FAQ
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-cost-explorer/getting-started/
        type: Getting Started
    description: |-

      The Cost Explorer API allows you to access your cost and usage data
      programmatically. You can retrieve aggregated information like total
      monthly costs or daily usage, as well as more detailed data such as
      specific operations for services like Amazon DynamoDB. The service
      endpoint for the Cost Explorer API is https://ce.us-east-1.amazonaws.com.
      For pricing details, refer to Amazon Web Services Cost Management Pricing.
  - aid: amazon-web-services:aws-chime
    name: AWS Chime
    tags:
      - ARN
      - Accounts
      - Addresses
      - Administrative
      - Administrator
      - Applications
      - Arn?scope=app
      - Associate
      - Attendees
      - Available
      - Batches
      - Bots
      - Call
      - Calling
      - Calls
      - Capture
      - Channels
      - Configurations
      - Connectors
      - Conversations
      - Countries
      - Credentials
      - Delegate
      - Describe
      - Dial
      - Disassociate
      - Emergency
      - Endpoints
      - Events
      - Global
      - Groups
      - Health
      - Id?operation=disassociate
      - Id?operation=logout
      - Instances
      - Invite
      - Logging
      - Logout
      - Marker
      - Media
      - Meetings
      - Members
      - Memberships
      - Messages
      - Messaging
      - Moderated
      - Moderators
      - Numbers
      - Orders
      - Origination
      - Out
      - PIN
      - Personal
      - Phone
      - Pin
      - Pipelines
      - Programmable
      - Proxy
      - Read
      - Redact
      - Regenerate
      - Reset
      - Resources
      - Restore
      - Retention
      - Rooms
      - Rules
      - SIP
      - Search
      - Security
      - Send
      - Sessions
      - Settings
      - Sign In
      - Stop
      - Streaming
      - Supported
      - Suspend
      - Tags
      - Termination
      - Tokens
      - Transactions
      - Transcriptions
      - Unsuspend
      - Untag
      - Users
      - Validate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/chime/
    overlays:
      - url: overlays/chime-openapi-search.yml
        type: APIs.io Search
      - url: overlays/chime-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/chime/
        type: Documentation
      - url: openapi/chime-openapi-original.yml
        type: OpenAPI
      - url: https://pages.awscloud.com/chime-contact-us
        type: Contact
      - url: https://aws.amazon.com/chime/chime-sdk/
        type: SDK
      - url: https://aws.amazon.com/chime/download/
        type: Downloads
      - url: http://answers.chime.aws
        type: Answers
      - url: https://aws.amazon.com/chime/pricing/
        type: Pricing
      - url: https://aws.amazon.com/chime/customers/
        type: Customers
      - url: https://aws.amazon.com/chime/faq/
        type: FAQ
      - url: https://aws.amazon.com/chime/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/chime/features/
        type: Features
    description: |-

      The Amazon Chime API is a comprehensive communications solution that
      allows users to host online meetings, chat, and make business calls from a
      single platform. Key features include hosting high-quality video meetings,
      audio calls, screen sharing, meeting chat, dial-in numbers, and in-room
      video conferencing. The API also includes chat and chat room functionality
      for ongoing communications, as well as user management and advanced
      features like single sign-on (SSO) via the Amazon Chime management
      console. The user-friendly app is compatible with Windows, Mac, web, iOS,
      and Android devices. Developers can further enhance their applications
      with messaging, audio, video, and screen sharing capabilities using the
      Amazon Chime SDK.
  - aid: amazon-web-services:aws-clean-rooms
    name: AWS Clean Rooms
    tags:
      - ARN
      - Accounts
      - Analysis
      - Analysis Templates
      - Associations
      - Audience
      - Batches
      - Budgets
      - Collaboration
      - Collaborations
      - Configuration Audience Model Associations
      - Configured
      - Impact
      - Members
      - Memberships
      - Models
      - Names
      - Previews
      - Privacy
      - Privacy Budget Templates
      - Privacy Budgets
      - Protected
      - Queries
      - Resources
      - Rules
      - Schemas
      - Tables
      - Tags
      - Templates
      - Types
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/clean-rooms/
    overlays:
      - url: overlays/cleanrooms-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cleanrooms-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/clean-rooms/
        type: Documentation
      - url: openapi/cleanrooms-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/clean-rooms/#
        type: Features
      - url: https://aws.amazon.com/clean-rooms/faqs/
        type: FAQ
      - url: https://aws.amazon.com/clean-rooms/customers/
        type: Customers
      - url: https://aws.amazon.com/clean-rooms/partners/
        type: Partners
      - url: https://aws.amazon.com/clean-rooms/pricing/
        type: Pricing
      - url: https://aws.amazon.com/clean-rooms/resources/
        type: Resources
    description: |-

      Introducing the Clean Rooms API, designed for use with Amazon Web
      Services. This API allows multiple parties to securely collaborate and
      combine their data in a shared workspace. This collaborative environment
      enables members to query and receive insights from aggregated datasets
      without exposing raw data to other parties. 
  - aid: amazon-web-services:amazon-braket
    name: ' Amazon Braket'
    tags:
      - ARN
      - Cancel
      - Device
      - Devices
      - Jobs
      - Quantum
      - Resources
      - Search
      - Tags
      - Tasks
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/braket/
    overlays:
      - url: overlays/braket-openapi-search.yml
        type: APIs.io Search
      - url: overlays/braket-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/braket/
        type: Documentation
      - url: openapi/braket-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/braket/#
        type: Getting Started
      - url: https://aws.amazon.com/braket/#
        type: Quantum Computers
      - url: https://aws.amazon.com/braket/customers/
        type: Customers
      - url: https://aws.amazon.com/braket/features/
        type: Features
      - url: https://aws.amazon.com/braket/pricing/
        type: Pricing
      - url: https://aws.amazon.com/braket/faqs/
        type: FAQ
    description: |-

      Amazon Braket is a comprehensive and user-friendly quantum computing
      service designed to support researchers and developers in leveraging the
      power of quantum technology to enhance their research and speed up
      discovery processes. With Amazon Braket, users have access to an
      integrated development environment that enables them to experiment with
      and create quantum algorithms, validate them using quantum circuit
      simulators, and execute them on a variety of quantum hardware platforms.
  - aid: amazon-web-services:aws-cloud-control
    name: AWS Cloud Control
    tags:
      - Resources
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloudcontrolapi/
    overlays:
      - url: overlays/cloudcontrol-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloudcontrol-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloudcontrolapi/
        type: Documentation
      - url: openapi/cloudcontrol-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloudcontrolapi/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloudcontrolapi/resources/
        type: Resources
      - url: https://aws.amazon.com/cloudcontrolapi/faqs/
        type: FAQ
      - url: >-

          https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html
        type: User Guide
    description: |-

      The AWS Cloud Control API simplifies the management of AWS and third-party
      services by providing a standardized set of APIs for developers and
      partners. With five key operations (CRUDL), users can easily create, read,
      update, delete, and list their cloud infrastructure.
  - aid: amazon-web-services:amazon-cloud-directory
    name: Amazon Cloud Directory
    tags:
      - ARN
      - Applied Schema
      - Attach
      - Attached
      - Attachments
      - Attributes
      - Batches
      - Children
      - Detach
      - Development
      - Directories
      - Directory
      - Disable
      - Enable
      - Facets
      - Incoming
      - Index
      - Indices
      - Information
      - JSON
      - Link
      - Links
      - Lookups
      - Managed
      - Names
      - Objects
      - Outgoing
      - Parent Paths
      - Parents
      - Paths
      - Policies
      - Publish
      - Published
      - Read
      - Removes
      - Resources
      - Schemas
      - Tags
      - Targets
      - Typed
      - Typed Links
      - Untag
      - Upgrade
      - Upgrade Applied
      - Upgradepublished
      - Versions
      - Write
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloud-directory/
    overlays:
      - url: overlays/clouddirectory-openapi-search.yml
        type: APIs.io Search
      - url: overlays/clouddirectory-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloud-directory/
        type: Documentation
      - url: openapi/clouddirectory-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloud-directory/features/
        type: Features
      - url: https://aws.amazon.com/cloud-directory/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloud-directory/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/cloud-directory/faqs/
        type: FAQ
    description: |-

      The Amazon Cloud Directory is a feature within the AWS Directory Service
      designed to streamline the creation and organization of large-scale cloud
      applications for web, mobile, and IoT platforms. This documentation
      provides a comprehensive overview of Cloud Directory operations that can
      be accessed programmatically, offering detailed insights into data types
      and potential errors. 
  - aid: amazon-web-services:aws-cloudformation
    name: AWS CloudFormation
    tags:
      - Templates
      - Validate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloudformation/
    overlays:
      - url: overlays/cloudformation-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloudformation-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloudformation/
        type: Documentation
      - url: openapi/cloudformation-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloudformation/features/
        type: Features
      - url: https://aws.amazon.com/cloudformation/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloudformation/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/cloudformation/resources/
        type: Resources
      - url: https://aws.amazon.com/cloudformation/partners/
        type: Partners
      - url: https://aws.amazon.com/cloudformation/faqs/
        type: FAQ
    description: |-

      CloudFormation is an Amazon Web Services tool that allows users to easily
      create and manage infrastructure deployments in a predictable and
      repeatable manner. With CloudFormation, you can utilize various AWS
      products like EC2, EBS, SNS, ELB, and Auto Scaling to build reliable and
      scalable applications without needing to manually configure the underlying
      infrastructure. By declaring resources and their dependencies in a
      template file, CloudFormation organizes them into a stack, enabling
      seamless creation and deletion of all resources within the stack while
      managing dependencies between them.
  - aid: amazon-web-services:aws-cloud9
    name: AWS Cloud9
    tags:
      - Environments
      - Memberships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloud9/
    overlays:
      - url: overlays/cloud9-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloud9-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloud9/
        type: Documentation
      - url: openapi/cloud9-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloud9/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloud9/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/cloud9/faqs/
        type: FAQ
      - url: >-

          https://aws.amazon.com/blogs/aws/aws-cloud9-cloud-developer-environments/
        type: Environments
    description: |-

      The Cloud9 API provides a wide range of tools for coding, building,
      running, testing, debugging, and releasing software in the cloud. Users
      can access these features through operations such as creating a
      development environment on Amazon EC2, managing environment memberships,
      deleting environments and members, getting information about environments
      and members, listing environments, managing tags, and updating environment
      settings. 
  - aid: amazon-web-services:amazon-cloudfront
    name: Amazon CloudFront
    tags:
      - Access
      - Alias
      - Aliases
      - Associate
      - Cache
      - Cloud
      - Cloudfront
      - Configurations
      - Conflicting
      - Continuous
      - Controls
      - Copy
      - Deployments
      - Describe
      - Distributions
      - Encryption
      - Entities
      - Fields
      - Front
      - Functions
      - Groups
      - Headers
      - Identities
      - Identity
      - Invalidations
      - Keys
      - Levels
      - Logs
      - Monitoring
      - Names
      - Operations
      - Origin
      - Policies
      - Primary
      - Profiles
      - Promote
      - Public
      - Publish
      - Real Time
      - Resources
      - Responses
      - Staging
      - Store
      - Stores
      - Streaming
      - Subscriptions
      - Tagging
      - Tags
      - Targets
      - Tests
      - Untag
      - Value
      - Web
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloudfront/
    overlays:
      - url: overlays/cloudfront-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloudfront-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloudfront/
        type: Documentation
      - url: openapi/cloudfront-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloudfront/features/
        type: Features
      - url: https://aws.amazon.com/cloudfront/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloudfront/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/cloudfront/media/
        type: Media
      - url: https://aws.amazon.com/cloudfront/customers/
        type: Custoners
      - url: https://aws.amazon.com/cloudfront/partners/
        type: Partners
      - url: https://aws.amazon.com/cloudfront/resources/
        type: Resources
      - url: https://aws.amazon.com/cloudfront/faqs/
        type: FAQ
    description: |-

      Amazon CloudFront is a reliable global content delivery network (CDN)
      service that speeds up the delivery of websites, APIs, video content, and
      other web assets. By seamlessly integrating with various Amazon Web
      Services products, developers and businesses can effortlessly optimize
      content delivery to end users without any mandatory usage requirements.
  - aid: amazon-web-services:aws-clean-rooms-ml
    name: AWS Clean Rooms ML
    tags:
      - ARN
      - Audience
      - Configured
      - Datasets
      - Exports
      - Generation
      - Jobs
      - Models
      - Policies
      - Resources
      - Tags
      - Training
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/clean-rooms/ml/
    overlays:
      - url: overlays/cleanroomsml-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cleanroomsml-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/clean-rooms/ml/
        type: Documentation
      - url: openapi/cleanroomsml-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/clean-rooms/ml/
        type: Features
      - url: https://aws.amazon.com/clean-rooms/faqs/
        type: FAQ
      - url: https://aws.amazon.com/clean-rooms/customers/
        type: Customers
      - url: https://aws.amazon.com/clean-rooms/partners/
        type: Partners
      - url: https://aws.amazon.com/clean-rooms/pricing/
        type: Pricing
      - url: https://aws.amazon.com/clean-rooms/resources/
        type: Resources
    description: |-

      Introducing the Amazon Web Services Clean Rooms ML API Reference, a
      solution that offers a secure way for two parties to identify similar
      users in their datasets without sharing their data. First, one party
      provides training data to create and configure an audience model, which is
      associated with a collaboration. Then, the second party brings their seed
      data to generate an audience that closely resembles the training data.
  - aid: amazon-web-services:aws-cloudhsm
    name: AWS CloudHSM
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloudhsm/
    overlays:
      - url: overlays/cloudhsmv2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloudhsmv2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloudhsm/
        type: Documentation
      - url: openapi/cloudhsmv2-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloudhsm/features/
        type: Features
      - url: https://aws.amazon.com/cloudhsm/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloudhsm/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/cloudhsm/resources/
        type: Resources
      - url: https://aws.amazon.com/cloudhsm/customers/
        type: Customers
      - url: https://aws.amazon.com/cloudhsm/faqs/
        type: FAQ
    description: |-

      The AWS CloudHSM API provides a secure and compliant solution for managing
      and accessing keys on FIPS-validated hardware. With customer-owned,
      single-tenant HSM instances running in your Virtual Private Cloud (VPC),
      you can easily meet corporate, contractual, and regulatory data security
      requirements.
  - aid: amazon-web-services:amazon-cloudsearch
    name: Amazon CloudSearch
    tags:
      - Access
      - Policies
      - Services
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/cloudsearch/
    overlays:
      - url: overlays/cloudsearch-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloudsearch-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/cloudsearch/
        type: Documentation
      - url: openapi/cloudsearch-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon CloudSearch, is a cloud-based service that simplifies the process
      of setting up, managing, and expanding a search solution for your website.
      It allows you to easily search through extensive datasets, including web
      pages, documents, forum posts, and product information. With Amazon
      CloudSearch, you can enhance your website with search functionality
      without the need for extensive expertise or concerns about hardware
      management. 
  - aid: amazon-web-services:aws-cloudtrail-data
    name: AWS CloudTrail Data
    tags:
      - Audit
      - Events
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/cloudtrail/
    overlays:
      - url: overlays/cloudtrail-data-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloudtrail-data-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/cloudtrail/
        type: Documentation
      - url: openapi/cloudtrail-data-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/index.html
        type: User Guide
      - url: >-

          https://docs.aws.amazon.com/awscloudtrail/latest/partner-onboarding/cloudtrail-lake-partner-onboarding.html
        type: Partners
    description: |-

      With AWS CloudTrail, you can monitor your AWS deployments in the cloud by
      getting a history of AWS API calls for your account, including API calls
      made by using the AWS Management Console, the AWS SDKs, the command line
      tools, and higher-level AWS services. You can also identify which users
      and accounts called AWS APIs for services that support CloudTrail, the
      source IP address from which the calls were made, and when the calls
      occurred. 
  - aid: amazon-web-services:amazon-codecatalyst
    name: Amazon CodeCatalyst
    tags:
      - Access
      - Branch
      - Branches
      - Clone
      - Details
      - Environments
      - Events
      - Logs
      - Names
      - Projects
      - Repositories
      - Runs
      - Sessions
      - Sources
      - Space
      - Spaces
      - Stop
      - Subscriptions
      - Tokens
      - URL
      - Users
      - Verify
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/codecatalyst/
    overlays:
      - url: overlays/codecatalyst-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codecatalyst-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/codecatalyst/
        type: Documentation
      - url: openapi/codecatalyst-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon CodeCatalyst is a unified software development service for
      development teams to quickly build, deliver and scale applications on AWS
      while adhering to organization-specific best practices. Developers can
      automate development tasks and innovate faster with generative AI
      capabilities, and spend less time setting up project tools, managing CI/CD
      pipelines, provisioning and configuring various development environments
      or coordinating with team members.
  - aid: amazon-web-services:aws-codebuild
    name: AWS CodeBuild
    tags:
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/codebuild/
    overlays:
      - url: overlays/codebuild-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codebuild-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/codebuild/
        type: Documentation
      - url: openapi/codebuild-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/codebuild/customer-testimonials/
        type: Testimonials
      - url: https://aws.amazon.com/codebuild/product-integrations/
        type: Integrations
      - url: https://aws.amazon.com/codebuild/faqs/
        type: FAQ
      - url: https://aws.amazon.com/codebuild/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/codebuild/pricing/
        type: Pricing
      - url: https://aws.amazon.com/codebuild/features/
        type: Features
    description: |+

      AWS CodeBuild is a fully managed continuous integration service that
      compiles source code, runs tests, and produces ready-to-deploy software
      packages. With CodeBuild, you don't need to provision, manage, and scale
      your own build servers. You just specify the location of your source code
      and choose your build settings, and CodeBuild will run your build scripts
      for compiling, testing, and packaging your code.



  - aid: amazon-web-services:amazon-codeguru-reviewer
    name: Amazon CodeGuru Reviewer
    tags:
      - ARN
      - Associations
      - Code
      - Code Reviews
      - Describe
      - Disassociate
      - Feedback
      - Recommendations
      - Repositories
      - Resources
      - Reviews
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/index.html
    overlays:
      - url: overlays/codeguru-reviewer-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codeguru-reviewer-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/index.html
        type: Documentation
      - url: openapi/codeguru-reviewer-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/index.html
        type: User Guide
      - url: >-

          https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html
        type: CLI
    description: |-

      Amazon CodeGuru Reviewer is a service that uses program analysis and
      machine learning to detect potential defects that are difficult for
      developers to find and offers suggestions for improving your Java and
      Python code. This service has been released for general availability in
      several Regions.
  - aid: amazon-web-services:aws-codeartifact
    name: AWS CodeArtifact
    tags:
      - Assets
      - Authorization
      - Configurations
      - Connections
      - Copy
      - Dependencies
      - Describe
      - Disassociate
      - Dispose
      - Domains
      - Endpoints
      - External
      - Origin
      - Packages
      - Permissions
      - Policies
      - Publish
      - Readme
      - Repositories
      - Resources
      - Status
      - Tags
      - Tokens
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/codeartifact/
    overlays:
      - url: overlays/codeartifact-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codeartifact-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/codeartifact/
        type: Documentation
      - url: openapi/codeartifact-openapi-original.yml
        type: OpenAPI
    description: |-

      CodeArtifact is a managed artifact repository that supports various
      language-native package managers and build tools like npm, Apache Maven,
      pip, and dotnet. It allows teams to share and pull packages from both
      public and CodeArtifact repositories. Additionally, CodeArtifact enables
      the creation of upstream relationships between repositories, effectively
      combining their contents for package manager clients.
  - aid: amazon-web-services:aws-cloudtrail
    name: AWS CloudTrail
    tags:
      - Trails
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloudtrail/
    overlays:
      - url: overlays/cloudtrail-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cloudtrail-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloudtrail/
        type: Documentation
      - url: openapi/cloudtrail-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloudtrail/features/
        type: Features
      - url: https://aws.amazon.com/cloudtrail/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloudtrail/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/cloudtrail/resources/
        type: Resources
      - url: https://aws.amazon.com/cloudtrail/faqs/
        type: FAQ
      - url: https://aws.amazon.com/cloudtrail/partners/
        type: Partners
    description: |-

      The CloudTrail API Reference provides detailed information on actions,
      data types, parameters, and errors for CloudTrail, a web service that
      records Amazon Web Services API calls and stores log files in an Amazon S3
      bucket. The recorded information includes user identity, API call start
      time, source IP address, request parameters, and response elements. 
  - aid: amazon-web-services:aws-codedeploy
    name: AWS CodeDeploy
    tags:
      - Deployments
      - Group
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/codedeploy/
    overlays:
      - url: overlays/codedeploy-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codedeploy-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/codedeploy/
        type: Documentation
      - url: openapi/codedeploy-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/codedeploy/features/
        type: Features
      - url: https://aws.amazon.com/codedeploy/pricing/
        type: Pricing
      - url: https://aws.amazon.com/codedeploy/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/codedeploy/resources/
        type: Resources
      - url: https://aws.amazon.com/codedeploy/faqs/
        type: FAQ
      - url: https://aws.amazon.com/codedeploy/product-integrations/
        type: Integrations
    description: |-

      AWS CodeDeploy is a deployment service that effortlessly automates
      software deployments to a range of compute services including Amazon EC2,
      ECS, AWS Lambda, and on-premises servers. By utilizing CodeDeploy, you can
      streamline software deployments, reducing the risk of errors associated
      with manual operations.
  - aid: amazon-web-services:amazon-codeguru-security
    name: Amazon CodeGuru Security
    tags:
      - ARN
      - Accounts
      - Batches
      - Configurations
      - Findings
      - Metrics
      - Names
      - Resources
      - Scans
      - Summaries
      - Tags
      - URL
      - Untag
      - Uploads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/codeguru/latest/security-api/index.html
    overlays:
      - url: overlays/codeguru-security-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codeguru-security-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/codeguru/latest/security-api/index.html
        type: Documentation
      - url: openapi/codeguru-security-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/codeguru/latest/security-ug/index.html
        type: User Guide
      - url: >-

          https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-security/index.html
        type: CLI
    description: |-

      Amazon CodeGuru Security is a static application security tool that uses
      machine learning to detect security policy violations and vulnerabilities.
      It provides suggestions for addressing security risks and generates
      metrics so you can track the security posture of your applications.
      CodeGuru Security's policies, which are informed by years of Amazon.com
      and AWS security best practices, help you to create and deploy secure,
      high-quality applications.
  - aid: amazon-web-services:aws-codecommit
    name: AWS CodeCommit
    tags:
      - Names
      - Repositories
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/codecommit/
    overlays:
      - url: overlays/codecommit-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codecommit-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/codecommit/
        type: Documentation
      - url: openapi/codecommit-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/codecommit/features/
        type: Features
      - url: https://aws.amazon.com/codecommit/pricing/
        type: Pricing
      - url: https://aws.amazon.com/codecommit/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/codecommit/resources/
        type: Resources
      - url: https://aws.amazon.com/codecommit/faqs/
        type: FAQ
      - url: https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html
        type: User Guide
    description: |-

      Securely host highly scalable private Git repositories and collaborate on
      code. AWS CodeCommit is a secure, highly scalable, fully managed source
      control service that hosts private Git repositories.
  - aid: amazon-web-services:amazon-codeguru-profiler
    name: Amazon CodeGuru Profiler
    tags:
      - ARN
      - Accounts
      - Actions
      - Agent
      - Anomalies
      - Anomaly
      - Batches
      - Channels
      - Configurations
      - Configure
      - Data
      - Feedback
      - Findings
      - Frames
      - Groups
      - Instances
      - Internal
      - Metrics
      - Names
      - Notifications
      - Permission
      - Policies
      - Posts
      - Profiles
      - Profiling
      - Recommendations
      - Removes
      - Reports
      - Resources
      - Submit
      - Summaries
      - Tags
      - Times
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/codeguru/latest/profiler-api/index.html
    overlays:
      - url: overlays/codeguruprofiler-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codeguruprofiler-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/index.html
        type: Documentation
      - url: openapi/codeguruprofiler-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/index.html
        type: User Guide
      - url: >-

          https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/index.html
        type: CLI
    description: |-

      The Amazon CodeGuru Profiler API gathers real-time performance data from
      your applications and offers tailored suggestions to optimize their
      performance. By leveraging machine learning techniques, CodeGuru Profiler
      assists in pinpointing the most resource-intensive lines of code and
      suggests enhancements to increase efficiency and overcome CPU bottlenecks.
      With various visualization tools, the API allows you to track CPU usage,
      identify time-consuming code segments, and offers actionable insights to
      minimize CPU consumption.
  - aid: amazon-web-services:aws-codepipeline
    name: AWS CodePipeline
    tags:
      - Pipelines
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/codepipeline/
    overlays:
      - url: overlays/codepipeline-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codepipeline-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/codepipeline/
        type: Documentation
      - url: openapi/codepipeline-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/codepipeline/features/
        type: Features
      - url: https://aws.amazon.com/codepipeline/pricing/
        type: Pricing
      - url: https://aws.amazon.com/codepipeline/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/codepipeline/faqs/
        type: FAQ
      - url: https://aws.amazon.com/codepipeline/product-integrations/
        type: Integrations
    description: |-

      The API provided by AWS CodePipeline is a comprehensive continuous
      delivery service that simplifies the automation of release pipelines,
      facilitating swift and dependable updates to both applications and
      infrastructure.
  - aid: amazon-web-services:aws-codestar-notifications
    name: AWS CodeStar Notifications
    tags:
      - ARN
      - Describe
      - Events
      - Notifications
      - Resources
      - Rules
      - Subscribe
      - Tags
      - Targets
      - Targets
      - Types
      - Unsubscribe
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/Welcome.html
    overlays:
      - url: overlays/codestar-notifications-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codestar-notifications-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/Welcome.html
        type: Documentation
      - url: openapi/codestar-notifications-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS CodeStar Notifications API Reference offers detailed explanations
      and practical examples on using the various operations and data types
      within the AWS CodeStar Notifications API.
  - aid: amazon-web-services:aws-codestar-connections
    name: AWS CodeStar Connections
    tags:
      - Configurations
      - Sync
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html
    overlays:
      - url: overlays/codestar-connections-openapi-search.yml
        type: APIs.io Search
      - url: overlays/codestar-connections-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html
        type: Documentation
      - url: openapi/codestar-connections-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS CodeStar Connections is an API provided by Amazon Web Services that
      allows you to work with connections and installations. Connections are
      configurations used to connect AWS resources to external code
      repositories, allowing services like CodePipeline to trigger actions based
      on changes in third-party code repositories.
  - aid: amazon-web-services:amazon-cognito-user-pools
    name: Amazon Cognito User Pools
    tags:
      - Attributes
      - Users
      - Verify
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
    overlays:
      - url: overlays/cognito-idp-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cognito-idp-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
        type: Documentation
      - url: openapi/cognito-idp-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Cognito user pool, serves as a user directory for authenticating
      and authorizing users in web and mobile applications. When integrated into
      your app, the user pool functions as an OpenID Connect (OIDC) identity
      provider, offering enhanced security features, identity federation
      capabilities, seamless app integration, and customizable user experiences.
  - aid: amazon-web-services:amazon-cognito-sync
    name: Amazon Cognito Sync
    tags:
      - Bulk
      - Bulk Publish
      - Cognito
      - Configurations
      - Datasets
      - Describe
      - Details
      - Device
      - Entities
      - Entity Pools
      - Events
      - Identity
      - Names
      - Pools
      - Publish
      - Records
      - Register
      - Sets
      - Subscriptions
      - Unsubscribe
      - Usage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync.html
    overlays:
      - url: overlays/cognito-sync-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cognito-sync-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync.html
        type: Documentation
      - url: openapi/cognito-sync-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Cognito Sync is an AWS service and client library that allows for
      seamless syncing of user data across multiple devices. With high-level
      client libraries available for iOS and Android, developers can easily
      persist data locally for offline access without the need to store
      credentials on the device. 
  - aid: amazon-web-services:amazon-comprehend-medical
    name: Amazon Comprehend Medical
    tags:
      - Inference
      - Jobs
      - Stop
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/comprehend/medical/
    overlays:
      - url: overlays/comprehendmedical-openapi-search.yml
        type: APIs.io Search
      - url: overlays/comprehendmedical-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/comprehend/medical/
        type: Documentation
      - url: openapi/comprehendmedical-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/comprehend/medical/features/
        type: Features
      - url: https://aws.amazon.com/comprehend/medical/pricing/
        type: Pricing
      - url: https://aws.amazon.com/comprehend/medical/faqs/
        type: FAQ
      - url: https://aws.amazon.com/comprehend/medical/resources/
        type: Resources
      - url: https://aws.amazon.com/comprehend/medical/customers/
        type: Customers
    description: |-

      The Amazon Comprehend Medical API is designed to extract structured
      information from unstructured clinical text, allowing users to gain
      valuable insights from their documents. It should be noted, however, that
      this API only detects entities in English language texts and imposes size
      limits on files for various API operations.
  - aid: amazon-web-services:amazon-cognito-federated-identities
    name: Amazon Cognito Federated Identities
    tags:
      - Identity
      - Pools
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html
    overlays:
      - url: overlays/cognito-identity-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cognito-identity-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html
        type: Documentation
      - url: openapi/cognito-identity-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Cognito Federated Identities is a web service that provides scoped
      temporary credentials for mobile devices and other untrusted environments.
      It offers consistent identity management for users throughout the lifespan
      of an application. 
  - aid: amazon-web-services:amazon-connect
    name: Amazon Connect
    tags:
      - ARN
      - Activate
      - Agent
      - Analysis
      - Analytics
      - Applications
      - Approved
      - Associate
      - Associations
      - Attributes
      - Availability
      - Available
      - Batches
      - Bots
      - Caller
      - Case
      - Cases
      - Chat
      - Claim
      - Code
      - Concurrency
      - Configurations
      - Connect
      - Connects
      - Contacts
      - Content
      - Current
      - Data
      - Deactivate
      - Default
      - Describe
      - Disassociate
      - Dismiss
      - Distributions
      - Entities
      - Evaluations
      - Events
      - Federate
      - Federation
      - File
      - Flows
      - Forms
      - Functions
      - Groups
      - Hierarchy
      - Historical
      - Hours
      - Identity
      - Import
      - Info
      - Initial
      - Instances
      - Integrations
      - Keys
      - Lambda
      - Languages
      - Maximum
      - Metadata
      - Metrics
      - Modules
      - Monitors
      - Names
      - Numbers
      - Operation
      - Operations
      - Origin
      - Origins
      - Outbound
      - Participants
      - Pause
      - Permissions
      - Persistent
      - Phone
      - Predefined
      - Proficiencies
      - Profiles
      - Prompts
      - Queues
      - RTC
      - Real Time
      - Recording
      - References
      - Removes
      - Replicate
      - Resources
      - Resume
      - Roles
      - Routing
      - Rules
      - Schedules
      - Search
      - Security
      - Segments
      - Send
      - Sets
      - Status
      - Statuses
      - Stop
      - Storage
      - Streaming
      - Structures
      - Submit
      - Summaries
      - Suspend
      - Tags
      - Tasks
      - Templates
      - Time
      - Timer
      - Tokens
      - Traffic
      - Transfers
      - Types
      - Untag
      - Userdata
      - Users
      - Versions
      - View
      - Views
      - Vocabularies
      - Web
      - Web RTC
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/connect/
    overlays:
      - url: overlays/connect-openapi-search.yml
        type: APIs.io Search
      - url: overlays/connect-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/connect/
        type: Documentation
      - url: openapi/connect-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/connect/
        type: Use Cases
      - url: https://aws.amazon.com/connect/
        type: Featured
      - url: https://aws.amazon.com/connect/pricing/
        type: Pricing
      - url: https://aws.amazon.com/connect/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/connect/resources/
        type: Resources
      - url: https://aws.amazon.com/connect/customers/
        type: Customers
      - url: https://aws.amazon.com/connect/partners/
        type: Partners
    description: |-

      The API for Amazon Connect is a cloud-based solution for setting up and
      managing customer contact centers, offering reliable customer engagement
      at any scale. It provides metrics and real-time reporting for optimizing
      contact routing and efficiently resolving customer issues by connecting
      them with the appropriate agents. 
  - aid: amazon-web-services:aws-config
    name: AWS Config
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/config/
    overlays:
      - url: overlays/config-openapi-search.yml
        type: APIs.io Search
      - url: overlays/config-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/config/
        type: Documentation
      - url: openapi/config-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/config/features/
        type: Features
      - url: https://aws.amazon.com/config/pricing/
        type: Pricing
      - url: https://aws.amazon.com/config/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/config/resources/
        type: Resources
      - url: https://aws.amazon.com/config/faq/
        type: FAQ
      - url: https://aws.amazon.com/config/customers/
        type: Customers
      - url: https://aws.amazon.com/config/partners/
        type: Partners
    description: |-

      Config provides a comprehensive solution for monitoring and managing the
      configurations of Amazon Web Services resources within your AWS account.
      With Config, you can easily access current and historical configurations
      for resources such as Amazon EC2 instances, EBS volumes, ENIs, and
      security groups.
  - aid: amazon-web-services:contact-lens-for-amazon-connect
    name: Contact Lens for Amazon Connect
    tags:
      - Analysis
      - Contacts
      - Real Time
      - Segments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/connect/contact-lens/
    overlays:
      - url: overlays/connect-contact-lens-openapi-search.yml
        type: APIs.io Search
      - url: overlays/connect-contact-lens-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/connect/contact-lens/
        type: Documentation
      - url: openapi/connect-contact-lens-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/connect/contact-lens/
        type: Use Cases
      - url: https://aws.amazon.com/connect/contact-lens/
        type: Features
      - url: https://aws.amazon.com/connect/pricing/
        type: Pricing
      - url: https://aws.amazon.com/connect/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/connect/resources/
        type: Resources
      - url: https://aws.amazon.com/connect/customers/
        type: Customers
      - url: https://aws.amazon.com/connect/partners/
        type: Partners
    description: |-

      The Contact Lens API for Amazon Connect allows users to analyze
      conversations between customers and agents through features such as speech
      transcription, natural language processing, and intelligent search. It
      includes sentiment analysis, issue detection, and automatic contact
      categorization. This tool provides real-time and post-call analytics for
      customer-agent interactions.
  - aid: amazon-web-services:aws-compute-optimizer
    name: AWS Compute Optimizer
    tags:
      - Enrollment
      - Status
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/compute-optimizer/
    overlays:
      - url: overlays/compute-optimizer-openapi-search.yml
        type: APIs.io Search
      - url: overlays/compute-optimizer-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/compute-optimizer/
        type: Documentation
      - url: openapi/compute-optimizer-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html
        type: Metrics
      - url: https://aws.amazon.com/compute-optimizer/faqs/
        type: FAQ
      - url: https://aws.amazon.com/compute-optimizer/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/compute-optimizer/pricing/
        type: Pricing
    description: |-

      Compute Optimizer is an API that evaluates the configuration and usage
      metrics of your AWS compute resources, including EC2 instances, Auto
      Scaling groups, Lambda functions, EBS volumes, and ECS services on
      Fargate. It provides optimization recommendations to enhance performance
      and reduce costs, based on current and projected utilization data.
  - aid: amazon-web-services:amazon-comprehend
    name: Amazon Comprehend
    tags:
      - Flywheel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/comprehend/
    overlays:
      - url: overlays/comprehend-openapi-search.yml
        type: APIs.io Search
      - url: overlays/comprehend-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/comprehend/
        type: Documentation
      - url: openapi/comprehend-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/comprehend/pricing/
        type: Pricing
      - url: https://aws.amazon.com/comprehend/faqs/
        type: FAQ
      - url: https://aws.amazon.com/comprehend/customers/
        type: Customers
      - url: https://aws.amazon.com/comprehend/resources/
        type: Resources
      - url: https://aws.amazon.com/comprehend/features/
        type: Features
      - url: https://aws.amazon.com/comprehend/idp/
        type: Intelligent Document Processing
      - url: https://aws.amazon.com/comprehend/trust-and-safety/
        type: Trust and Safety
    description: |-

      Amazon Comprehend is an AI-powered service from Amazon Web Services that
      provides deep analysis of document content. It allows users to extract
      topics, sentiment, language, and other insights from their documents.
  - aid: amazon-web-services:aws-cost-optimization-hub
    name: AWS Cost Optimization Hub
    tags:
      - Preferences
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/aws-cost-management/cost-optimization-hub/
    overlays:
      - url: overlays/cost-optimization-hub-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cost-optimization-hub-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/aws-cost-management/cost-optimization-hub/
        type: Documentation
      - url: openapi/cost-optimization-hub-openapi-original.yml
        type: OpenAPI
      - url: >-

          https://aws.amazon.com/aws-cost-management/cost-optimization-hub/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/aws-cost-management/cost-optimization-hub/faqs/
        type: FAQ
    description: |-

      The Cost Optimization Hub API allows you to automate the identification,
      filtering, aggregation, and quantification of cost savings for your
      optimization recommendations across various Amazon Web Services Regions
      and accounts within your organization. 
  - aid: amazon-web-services:aws-control-tower
    name: AWS Control Tower
    tags:
      - ARN
      - Baselines
      - Controls
      - Disable
      - Enable
      - Enabled
      - Landing
      - Landing Zones
      - Operation
      - Reset
      - Resources
      - Tags
      - Untag
      - Zones
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/controltower/
    overlays:
      - url: overlays/controltower-openapi-search.yml
        type: APIs.io Search
      - url: overlays/controltower-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/controltower/
        type: Documentation
      - url: openapi/controltower-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/controltower/features/
        type: Features
      - url: https://aws.amazon.com/controltower/pricing/
        type: Pricing
      - url: https://aws.amazon.com/controltower/faqs/
        type: FAQ
      - url: https://aws.amazon.com/controltower/customers/
        type: Customers
      - url: https://aws.amazon.com/controltower/partners/
        type: Partners
    description: |-

      Use AWS Control Tower to set up and operate your multi-account AWS
      environment with prescriptive controls designed to accelerate your cloud
      journey.  AWS Control Tower orchestrates multiple AWS services on your
      behalf while maintaining the security and compliance needs of your new or
      existing organization.
  - aid: amazon-web-services:aws-glue-databrew
    name: AWS Glue DataBrew
    tags:
      - ARN
      - Actions
      - Batches
      - Datasets
      - Describe
      - Jobs
      - Names
      - Profiles
      - Projects
      - Publish
      - Recipes
      - Resources
      - Rulesets
      - Runs
      - Schedules
      - Send
      - Sessions
      - Stop
      - Tags
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/glue/features/databrew/
    overlays:
      - url: overlays/databrew-openapi-search.yml
        type: APIs.io Search
      - url: overlays/databrew-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/glue/features/databrew/
        type: Documentation
      - url: openapi/databrew-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/databrew/latest/dg/what-is.html
        type: About
    description: |-

      DataBrew is a user-friendly API designed to simplify the data preparation
      process by allowing users of all technical levels to visualize and
      transform data with just one click. This visual, cloud-scale service
      targets and resolves data issues that are difficult to identify and
      time-consuming to address, making data preparation more efficient and
      accessible. 
  - aid: amazon-web-services:amazon-connect-customer-profiles
    name: Amazon Connect Customer Profiles
    tags:
      - ARN
      - Accounts
      - Attributes
      - Auto
      - Based
      - Calculated
      - Definitions
      - Detect
      - Domains
      - Entities
      - Events
      - Identity
      - Integrations
      - Jobs
      - Keys
      - Matches
      - Merge
      - Merging
      - Names
      - Objects
      - Previews
      - Profiles
      - Resolutions
      - Resources
      - Rules
      - Search
      - Similar
      - Steps
      - Stream
      - Streams
      - Tags
      - Templates
      - Types
      - Untag
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/connect/customer-profiles/
    overlays:
      - url: overlays/customer-profiles-openapi-search.yml
        type: APIs.io Search
      - url: overlays/customer-profiles-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/connect/customer-profiles/
        type: Documentation
      - url: openapi/customer-profiles-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/connect/customer-profiles/
        type: Use Cases
    description: |-

      The Amazon Connect Customer Profiles API offers a centralized customer
      profile solution for contact centers, featuring pre-built connectors
      utilizing AppFlow technology. These connectors seamlessly integrate
      customer data from third-party applications like Salesforce, ServiceNow,
      and ERP systems with contact history from your Amazon Connect contact
      center. If you are a new user, the Amazon Connect Administrator Guide can
      assist you in familiarizing yourself with the platform.
  - aid: amazon-web-services:aws-cost-and-usage-report
    name: AWS Cost and Usage Report
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/
    overlays:
      - url: overlays/cur-openapi-search.yml
        type: APIs.io Search
      - url: overlays/cur-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/
        type: Documentation
      - url: openapi/cur-openapi-original.yml
        type: OpenAPI
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/features/
        type: Features
      - url: >-

          https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/faqs/
        type: FAQ
    description: |-

      With the Amazon Web Services Cost and Usage Report API, you can manage
      Cost and Usage Report definitions programmatically. This API allows you to
      create, query, and delete Cost and Usage Report definitions, which track
      monthly costs and usage associated with your Amazon Web Services account.
  - aid: amazon-web-services:aws-datasync
    name: AWS DataSync
    tags:
      - Data
      - Execution
      - Tasks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/datasync/
    overlays:
      - url: overlays/datasync-openapi-search.yml
        type: APIs.io Search
      - url: overlays/datasync-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/datasync/
        type: Documentation
      - url: openapi/datasync-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/datasync/discovery/
        type: Discovery
      - url: https://aws.amazon.com/datasync/customers/
        type: Customers
      - url: https://aws.amazon.com/datasync/faqs/
        type: FAQ
      - url: https://aws.amazon.com/datasync/resources/
        type: Resources
      - url: https://aws.amazon.com/datasync/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/datasync/pricing/
        type: Pricing
    description: |

      AWS DataSync is a secure, online service that automates and accelerates
      moving data between on premises and AWS Storage services.
  - aid: amazon-web-services:amazon-datazone
    name: Amazon DataZone
    tags:
      - ARN
      - Accept
      - Activities
      - Assets
      - Blueprints
      - Cancel
      - Change
      - Configurations
      - Data
      - Domains
      - Environments
      - Forms
      - Glossaries
      - Glossary
      - Grants""
      - Grants
      - Groups
      - Groups
      - IAM
      - Listings
      - Listings
      - Login
      - Memberships
      - Notifications
      - Portals
      - Predictions
      - Profiles
      - Projects
      - Reject
      - Resources
      - Revisions
      - Revoke
      - Runs
      - Search
      - Sets
      - Sources
      - Sources
      - Status
      - Subscriptions
      - Tags
      - Targets
      - Targets
      - Term
      - Terms
      - Types
      - URL
      - Untag
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/datazone/
    overlays:
      - url: overlays/datazone-openapi-search.yml
        type: APIs.io Search
      - url: overlays/datazone-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/datazone/
        type: Documentation
      - url: openapi/datazone-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/datazone/features/
        type: Features
      - url: https://aws.amazon.com/datazone/faqs/
        type: FAQ
      - url: https://aws.amazon.com/datazone/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/datazone/pricing/
        type: Pricing
      - url: https://aws.amazon.com/datazone/resources/
        type: Resources
    description: |-

      Amazon DataZone is a comprehensive data management service designed to
      streamline the organization, governance, and analysis of your data. This
      API allows you to easily catalog, discover, and share your data across
      accounts and regions. With Amazon DataZone, you can seamlessly integrate
      with various Amazon Web Services offerings such as Redshift, Athena, Glue,
      and Lake Formation to enhance your data management capabilities.
  - aid: amazon-web-services:aws-data-exchange
    name: AWS Data Exchange
    tags:
      - ARN
      - Actions
      - Assets
      - Data
      - Events
      - Jobs
      - Notifications
      - Resources
      - Revisions
      - Revoke
      - Send
      - Sets
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/data-exchange/
    overlays:
      - url: overlays/dataexchange-openapi-search.yml
        type: APIs.io Search
      - url: overlays/dataexchange-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/data-exchange/
        type: Documentation
      - url: openapi/dataexchange-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/data-exchange/latest-updates/
        type: Updates
      - url: https://aws.amazon.com/data-exchange/latest-updates/
        type: Updates
      - url: https://aws.amazon.com/data-exchange/providers/
        type: Providers
    description: |-

      AWS Data Exchange is a service that makes it easy for AWS customers to
      exchange data in the cloud. You can use the AWS Data Exchange APIs to
      create, update, manage, and access file-based data set in the AWS Cloud. 
  - aid: amazon-web-services:aws-data-pipeline
    name: AWS Data Pipeline
    tags:
      - Definitions
      - Pipelines
      - Validate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/data-pipeline/
    overlays:
      - url: overlays/datapipeline-openapi-search.yml
        type: APIs.io Search
      - url: overlays/datapipeline-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/data-pipeline/
        type: Documentation
      - url: openapi/datapipeline-openapi-original.yml
        type: OpenAPI
      - url: >-

          https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/index.html
        type: Guide
    description: |-

      AWS Data Pipeline configures and manages a data-driven workflow called a
      pipeline. AWS Data Pipeline handles the details of scheduling and ensuring
      that data dependencies are met so that your application can focus on
      processing the data. 
  - aid: amazon-web-services:aws-device-farm
    name: AWS Device Farm
    tags:
      - Configurations
      - VPCE
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/device-farm/
    overlays:
      - url: overlays/devicefarm-openapi-search.yml
        type: APIs.io Search
      - url: overlays/devicefarm-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/device-farm/
        type: Documentation
      - url: openapi/devicefarm-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/device-farm/device-list/
        type: Device List
      - url: https://aws.amazon.com/device-farm/pricing/
        type: Pricing
      - url: https://aws.amazon.com/device-farm/resources/
        type: Resources
      - url: https://aws.amazon.com/device-farm/faqs/
        type: FAQ
    description: |-

      Explore the AWS Device Farm API documentation, offering APIs for two main
      testing services: desktop browser testing and real mobile device testing.
      Use Device Farm to test your web applications on desktop browsers with
      Selenium through the TestGrid-named APIs. 
  - aid: amazon-web-services:aws-direct-connect
    name: AWS Direct Connect
    tags:
      - Attributes
      - Interfaces
      - Virtual
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/directconnect/
    overlays:
      - url: overlays/directconnect-openapi-search.yml
        type: APIs.io Search
      - url: overlays/directconnect-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/directconnect/
        type: Documentation
      - url: openapi/directconnect-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/directconnect/features/
        type: Features
      - url: https://aws.amazon.com/directconnect/pricing/
        type: Pricing
      - url: https://aws.amazon.com/directconnect/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/directconnect/faqs/
        type: FAQ
      - url: https://aws.amazon.com/directconnect/partners/
        type: Partners
    description: |-

      Direct Connect allows you to establish a high-speed, private connection
      between your internal network and an Direct Connect location using a
      standard Ethernet fiber-optic cable. 
  - aid: amazon-web-services:aws-detective
    name: AWS Detective
    tags:
      - ARN
      - Accept
      - Accounts
      - Accounts List
      - Administrative
      - Batches
      - Configurations
      - Data Source
      - Describe
      - Disable
      - Disassociate
      - Enable
      - Graphs
      - Indicators
      - Investigations
      - Invitation
      - Invitations
      - Members
      - Memberships
      - Monitoring
      - Monitoring State
      - Organizations
      - Packages
      - Reject
      - Removal
      - Resources
      - States
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/detective/
    overlays:
      - url: overlays/detective-openapi-search.yml
        type: APIs.io Search
      - url: overlays/detective-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/detective/
        type: Documentation
      - url: openapi/detective-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/detective/features/
        type: Features
      - url: https://aws.amazon.com/detective/pricing/
        type: Pricing
      - url: https://aws.amazon.com/detective/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/detective/faqs/
        type: FAQ
      - url: https://aws.amazon.com/detective/faqs/
        type: FAQ
    description: |-

      The Amazon Detective API streamlines the investigation process for
      security teams, enabling faster and more efficient analysis. By leveraging
      prebuilt data aggregations, summaries, and context provided by Amazon
      Detective, users can quickly assess and understand potential security
      threats.
  - aid: amazon-web-services:amazon-data-lifecycle-manager
    name: Amazon Data Lifecycle Manager
    tags:
      - ARN
      - Lifecycle
      - Policies
      - Resources
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html
    overlays:
      - url: overlays/dlm-openapi-search.yml
        type: APIs.io Search
      - url: overlays/dlm-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html
        type: Documentation
      - url: openapi/dlm-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Data Lifecycle Manager With Amazon Data Lifecycle Manager, you can
      manage the lifecycle of your Amazon Web Services resources. You create
      lifecycle policies, which are used to automate operations on the specified
      resources. Amazon Data Lifecycle Manager supports Amazon EBS volumes and
      snapshots.
  - aid: amazon-web-services:amazon-devops-guru
    name: Amazon DevOps Guru
    tags:
      - Accounts
      - Anomalies
      - Anomalous
      - Anomaly
      - Channels
      - Collections
      - Configurations
      - Cost
      - Describe
      - Estimation
      - Events
      - Feedback
      - Groups
      - Health
      - Insights
      - Integrations
      - Logs
      - Monitored
      - Notifications
      - Organizations
      - Overview
      - Recommendations
      - Removes
      - Resources
      - Search
      - Services
      - Sources
      - Types
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/devops-guru/
    overlays:
      - url: overlays/devops-guru-openapi-search.yml
        type: APIs.io Search
      - url: overlays/devops-guru-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/devops-guru/
        type: Documentation
      - url: openapi/devops-guru-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/devops-guru/pricing/
        type: Pricing
      - url: https://aws.amazon.com/devops-guru/resources/
        type: Resources
      - url: https://aws.amazon.com/devops-guru/faqs/
        type: FAQ
      - url: https://aws.amazon.com/devops-guru/customers/
        type: Customers
      - url: https://aws.amazon.com/devops-guru/partners/
        type: Partners
      - url: https://aws.amazon.com/devops-guru/features/
        type: Features
    description: |-

      Amazon DevOps Guru is a managed service designed to detect abnormal
      behavior in critical operational applications. Users can select the Amazon
      Web Services resources they want DevOps Guru to monitor, allowing the
      service to analyze CloudWatch metrics and CloudTrail events related to
      those resources. 
  - aid: amazon-web-services:amazon-dynamodb-accelerator-dax
    name: Amazon DynamoDB Accelerator (DAX)
    tags:
      - Subnets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/dynamodbaccelerator/
    overlays:
      - url: overlays/dax-openapi-search.yml
        type: APIs.io Search
      - url: overlays/dax-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/dynamodbaccelerator/
        type: Documentation
      - url: openapi/dax-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/dynamodbaccelerator/customers/
        type: Customers
    description: |-

      DAX is a managed caching service designed specifically for Amazon
      DynamoDB. It significantly boosts database read speeds by storing
      frequently accessed data from DynamoDB, allowing applications to retrieve
      that data with extremely low latency. Setting up a DAX cluster is a
      straightforward process through the AWS Management Console. 
  - aid: amazon-web-services:aws-application-discovery-service
    name: AWS Application Discovery Service
    tags:
      - Applications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/application-discovery/
    overlays:
      - url: overlays/discovery-openapi-search.yml
        type: APIs.io Search
      - url: overlays/discovery-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/application-discovery/
        type: Documentation
      - url: openapi/discovery-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/application-discovery/features/
        type: Feature
      - url: https://aws.amazon.com/application-discovery/pricing/
        type: Pricing
      - url: https://aws.amazon.com/application-discovery/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/application-discovery/resources/
        type: Resources
      - url: https://aws.amazon.com/application-discovery/faqs/
        type: FAQ
      - url: https://aws.amazon.com/application-discovery/partners/
        type: Partners
    description: |-

      The Amazon Web Services Application Discovery Service helps users plan
      application migration projects by automatically identifying servers,
      virtual machines, and network dependencies in on-premises data centers. 
  - aid: amazon-web-services:aws-directory-service
    name: AWS Directory Service
    tags:
      - Trust
      - Verify
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/directoryservice/
    overlays:
      - url: overlays/ds-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ds-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/directoryservice/
        type: Documentation
      - url: openapi/ds-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/directoryservice/features/
        type: Features
      - url: https://aws.amazon.com/directoryservice/pricing/
        type: Pricing
      - url: https://aws.amazon.com/directoryservice/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/directoryservice/faqs/
        type: FAQ
    description: |-

      API for Directory Service is a convenient web service designed to help
      users easily establish and manage directories in the Amazon Web Services
      cloud. It also allows users to connect their Amazon Web Services resources
      to an existing Microsoft Active Directory that they manage themselves. 
  - aid: amazon-web-services:aws-elastic-disaster-recovery-service
    name: AWS Elastic Disaster Recovery Service
    tags:
      - ARN
      - Accounts
      - Actions
      - Associate
      - Configurations
      - Data
      - Describe
      - Disconnect
      - Exports
      - Extended
      - Extensible
      - Failback
      - Initialize
      - Instances
      - Items
      - Jobs
      - Launch
      - Logs
      - Networks
      - Recovery
      - Replication
      - Resources
      - Retry
      - Reverse
      - Servers
      - Services
      - Snapshots
      - Sources
      - Stack
      - Staging
      - Stop
      - Tags
      - Templates
      - Terminate
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/disaster-recovery/
    overlays:
      - url: overlays/drs-openapi-search.yml
        type: APIs.io Search
      - url: overlays/drs-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/disaster-recovery/
        type: Documentation
      - url: openapi/drs-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/disaster-recovery/features/
        type: Features
      - url: https://aws.amazon.com/disaster-recovery/pricing/
        type: Pricing
      - url: https://aws.amazon.com/disaster-recovery/resources/
        type: Resources
      - url: https://aws.amazon.com/disaster-recovery/faqs/
        type: FAQ
    description: |-

      AWS Elastic Disaster Recovery (AWS DRS), helps to reduce downtime and
      prevent data loss by quickly and reliably recovering on-premises and
      cloud-based applications. It utilizes cost-effective storage, minimal
      computing resources, and offers point-in-time recovery for optimal
      efficiency.
  - aid: amazon-web-services:aws-database-migration-service
    name: AWS Database Migration Service
    tags:
      - Database
      - Migrations
      - Subscriptions
      - Events
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/dms/
    overlays:
      - url: overlays/dms-openapi-search.yml
        type: APIs.io Search
      - url: overlays/dms-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/dms/
        type: Documentation
      - url: openapi/dms-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/dms/features/
        type: Features
      - url: https://aws.amazon.com/dms/schema-conversion-tool/
        type: Schema Conversion Tool
      - url: https://aws.amazon.com/dms/pricing/
        type: Pricing
      - url: https://docs.aws.amazon.com/dms/
        type: Resources
      - url: https://aws.amazon.com/dms/partners/
        type: Partners
      - url: https://aws.amazon.com/dms/testimonials/
        type: Customers
    description: |-

      Our Database Migration Service (DMS) is a flexible tool that can
      seamlessly move data between a variety of commercial and open-source
      databases, including Oracle, PostgreSQL, Microsoft SQL Server, Amazon
      Redshift, MariaDB, Amazon Aurora, MySQL, and SAP Adaptive Server
      Enterprise (ASE). 
  - aid: amazon-web-services:amazon-elastic-block-store
    name: Amazon Elastic Block Store
    tags:
      - Blocks
      - Changed
      - Changed Blocks
      - Complete
      - Completions
      - Index
      - Second
      - Snapshots
      - Storage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ebs/
    overlays:
      - url: overlays/ebs-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ebs-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ebs/
        type: Documentation
      - url: openapi/ebs-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ebs/features/
        type: Features
      - url: https://aws.amazon.com/ebs/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ebs/volume-types/
        type: Volume Types
      - url: https://aws.amazon.com/ebs/resources/
        type: Resources
      - url: https://aws.amazon.com/ebs/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/ebs/faqs/
        type: FAQ
      - url: https://aws.amazon.com/ebs/customers/
        type: Customers
    description: |-

      Use the Amazon Elastic Block Store (Amazon EBS) direct APIs to easily
      create Amazon EBS snapshots, write data directly to your snapshots, read
      data on your snapshots, and identify differences or changes between two
      snapshots. 
  - aid: amazon-web-services:amazon-documentdb
    name: Amazon DocumentDB
    tags:
      - Stop
      - Database Cluster
      - Database
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/documentdb/
    overlays:
      - url: overlays/docdb-openapi-search.yml
        type: APIs.io Search
      - url: overlays/docdb-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/documentdb/
        type: Documentation
      - url: openapi/docdb-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/documentdb/features/
        type: Features
      - url: https://aws.amazon.com/documentdb/pricing/
        type: Pricing
      - url: https://aws.amazon.com/documentdb/resources/
        type: Resources
      - url: https://aws.amazon.com/documentdb/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/documentdb/faqs/
        type: FAQ
      - url: https://aws.amazon.com/documentdb/customers/
        type: Customers
    description: |-

      Amazon DocumentDB is a cloud-based database service that offers fast and
      reliable performance. It is fully managed and compatible with MongoDB,
      making it easy to set up, operate, and scale databases. With Amazon
      DocumentDB, you can seamlessly run your existing application code and
      access the same drivers and tools you currently use with MongoDB.
  - aid: amazon-web-services:amazon-elastic-documentdb
    name: Amazon Elastic DocumentDB
    tags:
      - ARN
      - Cluster
      - Clusters
      - Resources
      - Restore
      - Snapshots
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html
    overlays:
      - url: overlays/docdb-elastic-openapi-search.yml
        type: APIs.io Search
      - url: overlays/docdb-elastic-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html
        type: Documentation
      - url: openapi/docdb-elastic-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon DocumentDB API offers elastic clusters that can handle high
      volumes of reads/writes per second and store petabytes of data. These
      clusters make it easier for developers to work with Amazon DocumentDB by
      removing the need to select, oversee, or update instances.
  - aid: amazon-web-services:amazon-ec2-instance-connect
    name: Amazon EC2 Instance Connect
    tags:
      - Console
      - Keys
      - SSHPublic
      - Send
      - Serial
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html
    overlays:
      - url: overlays/ec2-instance-connect-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ec2-instance-connect-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html
        type: Documentation
      - url: openapi/ec2-instance-connect-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon EC2 Instance Connect allows system administrators to generate and
      share one-time use SSH public keys on EC2, offering users a convenient and
      reliable method to access their instances securely.
  - aid: amazon-web-services:amazon-dynamodb
    name: Amazon DynamoDB
    tags:
      - Database
      - ' NoSQL'
      - ' Live'
      - Time
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/dynamodb/
    overlays:
      - url: overlays/dynamodb-openapi-search.yml
        type: APIs.io Search
      - url: overlays/dynamodb-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/dynamodb/
        type: Documentation
      - url: openapi/dynamodb-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/dynamodb/features/
        type: Features
      - url: https://aws.amazon.com/dynamodb/pricing/
        type: Pricing
      - url: https://aws.amazon.com/dynamodb/resources/
        type: Resources
      - url: https://aws.amazon.com/dynamodb/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/dynamodb/migrations/
        type: Migrations
      - url: https://aws.amazon.com/dynamodb/partners/
        type: Partners
      - url: https://aws.amazon.com/dynamodb/solutions-by-industry/
        type: Solutions
      - url: https://aws.amazon.com/dynamodb/faqs/
        type: FAQ
      - url: https://aws.amazon.com/dynamodb/customers/
        type: Customers
    description: |-

      Amazon DynamoDB, is a NoSQL database service that operates in a serverless
      environment, allowing you to build modern applications of any size. With
      DynamoDB, you only pay for the resources you use, and the database can
      scale down to zero, eliminating cold starts, version upgrades, maintenance
      windows, patching, and downtime. 
  - aid: amazon-web-services:amazon-elastic-compute-cloud
    name: Amazon Elastic Compute Cloud
    tags:
      - Withdraw
      - CIDR
      - Storage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ec2/
    overlays:
      - url: overlays/ec2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ec2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ec2/
        type: Documentation
      - url: openapi/ec2-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ec2/features/
        type: Features
      - url: https://aws.amazon.com/ec2/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ec2/instance-types/
        type: Instance Types
      - url: https://aws.amazon.com/ec2/faqs/
        type: FAQ
      - url: https://aws.amazon.com/ec2/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/ec2/resources/
        type: Resources
      - url: https://aws.amazon.com/ec2/videos/
        type: Videos
      - url: https://aws.amazon.com/ec2/customers/
        type: Customers
      - url: https://aws.amazon.com/ec2/cost-and-capacity/
        type: Cost Optimizations
    description: |-

      The Amazon Elastic Compute Cloud (Amazon EC2) API provides a comprehensive
      compute platform with a wide range of instance options and the latest
      technology choices in processors, storage, networking, operating systems,
      and purchase models to suit your workload requirements. We are the leading
      cloud provider to support Intel, AMD, and Arm processors, offer on-demand
      EC2 Mac instances, and feature 400 Gbps Ethernet networking. This API
      delivers exceptional price performance for machine learning training and
      the most cost-effective inference instances in the cloud. AWS has the
      largest number of SAP, high performance computing (HPC), ML, and Windows
      workloads compared to any other cloud provider.
  - aid: amazon-web-services:amazon-elastic-kubernetes-service
    name: Amazon Elastic Kubernetes Service
    tags:
      - ARN
      - Access
      - Addons
      - Anywhere
      - Associate
      - Associated
      - Associations
      - Clusters
      - Configurations
      - Deregister
      - Describe
      - Disassociate
      - EKS
      - Encryption
      - Entities
      - Entries
      - Entry
      - Er
      - Fargate
      - Groups
      - Identity
      - Insights
      - Names
      - Node Groups
      - Nodes
      - Pods
      - Policies
      - Principals
      - Profiles
      - Prov
      - Providers
      - Register
      - Registrations
      - Resources
      - Schemas
      - Subscriptions
      - Supported
      - Tags
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/eks/
    overlays:
      - url: overlays/eks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/eks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/eks/
        type: Documentation
      - url: openapi/eks-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/eks/features/
        type: Features
      - url: https://aws.amazon.com/eks/pricing/
        type: Pricing
      - url: https://aws.amazon.com/eks/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/eks/faqs/
        type: FAQ
      - url: https://aws.amazon.com/eks/customers/
        type: Customers
      - url: https://aws.amazon.com/eks/partners/
        type: Partners
    description: |-

      Amazon Elastic Kubernetes Service (Amazon EKS) is a fully managed service
      designed to simplify the process of running Kubernetes on Amazon Web
      Services. With Amazon EKS, users can easily deploy, scale, and manage
      containerized applications without the need to set up or maintain their
      own Kubernetes control plane. 
  - aid: amazon-web-services:amazon-elastic-container-registry
    name: Amazon Elastic Container Registry
    tags:
      - Cache
      - Pull
      - Rules
      - Validate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ecr/
    overlays:
      - url: overlays/ecr-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ecr-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ecr/
        type: Documentation
      - url: openapi/ecr-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ecr/features/
        type: Features
      - url: https://aws.amazon.com/ecr/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ecr/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/ecr/resources/
        type: Resources
      - url: https://aws.amazon.com/ecr/faqs/
        type: FAQ
      - url: https://aws.amazon.com/ecr/customers/
        type: Customers
    description: |-

      The Amazon Elastic Container Registry (Amazon ECR) is a managed service
      that allows customers to store and manage container images securely. Users
      can easily push, pull, and manage images using the Docker CLI or their
      preferred client. Amazon ECR supports private repositories with
      resource-based permissions using IAM, allowing specific users or Amazon
      EC2 instances to access repositories and images. 
  - aid: amazon-web-services:amazon-elastic-container-service
    name: Amazon Elastic Container Service
    tags:
      - Tasks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ecs/
    overlays:
      - url: overlays/ecs-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ecs-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ecs/
        type: Documentation
      - url: openapi/ecs-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ecs/features/
        type: Features
      - url: https://aws.amazon.com/ecs/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ecs/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/ecs/resources/
        type: Resources
      - url: https://aws.amazon.com/ecs/faqs/
        type: FAQ
      - url: https://aws.amazon.com/ecs/customers/
        type: Customers
      - url: https://aws.amazon.com/ecs/partners/
        type: Partners
    description: |-

      Amazon Elastic Container Service (Amazon ECS) is a robust container
      management service provided by Amazon. It enables easy running, stopping,
      and management of Docker containers with high scalability and speed.
      Amazon ECS allows you to host your container clusters on a serverless
      infrastructure using Fargate or on Amazon EC2 instances that you manage.
      With Amazon ECS, you can effortlessly launch and stop container-based
      applications through simple API calls and benefit from centralized
      monitoring capabilities and familiar Amazon EC2 features. Additionally,
      Amazon ECS offers advanced scheduling capabilities for placing containers
      based on resource requirements, isolation policies, and availability
      needs. By using Amazon ECS, you can simplify cluster management,
      configuration, and scalability, eliminating the need for your own cluster
      and configuration management systems.
  - aid: amazon-web-services:amazon-elasticache
    name: Amazon ElastiCache
    tags:
      - Migrations
      - Tests
      - Cache
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/elasticache/
    overlays:
      - url: overlays/elasticache-openapi-search.yml
        type: APIs.io Search
      - url: overlays/elasticache-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/elasticache/
        type: Documentation
      - url: openapi/elasticache-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/elasticache/features/
        type: Features
      - url: https://aws.amazon.com/elasticache/pricing/
        type: Pricing
      - url: https://aws.amazon.com/elasticache/resources/
        type: Resources
      - url: https://aws.amazon.com/elasticache/migrations/
        type: Migrations
      - url: https://aws.amazon.com/elasticache/faqs/
        type: FAQ
      - url: https://aws.amazon.com/elasticache/customers/
        type: Customers
    description: |-

      Amazon ElastiCache is a convenient web service that simplifies the process
      of setting up, operating, and expanding a distributed cache in the cloud.
      By utilizing ElastiCache, users can enjoy the advantages of a
      high-performance, in-memory cache without the extensive administrative
      tasks typically associated with launching and maintaining a distributed
      cache. The service streamlines setup, scaling, and cluster failure
      management compared to a self-managed cache deployment. Additionally,
      Amazon ElastiCache offers integration with Amazon CloudWatch, providing
      users with increased visibility into the important performance metrics of
      their cache and the ability to receive alerts if any parts of their cache
      become overloaded.
  - aid: amazon-web-services:amazon-elastic-container-registry-public
    name: Amazon Elastic Container Registry Public
    tags:
      - Layers
      - Uploads
      - Containers
      - Registry
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/AmazonECR/latest/public/what-is-ecr.html
    overlays:
      - url: overlays/ecr-public-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ecr-public-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/AmazonECR/latest/public/what-is-ecr.html
        type: Documentation
      - url: openapi/ecr-public-openapi-original.yml
        type: OpenAPI
      - url: https://gallery.ecr.aws/
        type: Gallery
    description: |-

      The Amazon Elastic Container Registry Public (Amazon ECR Public) is a
      managed service that allows you to host and manage container images in
      both public and private registries. You can utilize popular tools like the
      Docker CLI to push, pull, and manage images within a secure, scalable, and
      reliable registry for Docker or OCI images. This API specifically supports
      public repositories within Amazon ECR, while private repository
      functionality can be found in the Amazon Elastic Container Registry API
      Reference.
  - aid: amazon-web-services:amazon-elastic-file-system
    name: Amazon Elastic File System
    tags:
      - Access
      - Accounts
      - Backup
      - Configurations
      - Describe
      - File
      - Groups
      - Lifecycle
      - Modify
      - Mount
      - Points
      - Policies
      - Preferences
      - Protection
      - Replication
      - Resources
      - Security
      - Sources
      - Systems
      - Tags
      - Targets
      - Targets
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/efs/
    overlays:
      - url: overlays/elasticfilesystem-openapi-search.yml
        type: APIs.io Search
      - url: overlays/elasticfilesystem-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/efs/
        type: Documentation
      - url: openapi/elasticfilesystem-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/efs/features/
        type: Features
      - url: https://aws.amazon.com/efs/pricing/
        type: Pricing
      - url: https://aws.amazon.com/efs/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/efs/resources/
        type: Resources
      - url: https://aws.amazon.com/efs/faq/
        type: FAQ
      - url: https://aws.amazon.com/efs/customers/
        type: Customers
    description: |-

      Introducing Amazon Elastic File System (Amazon EFS), a user-friendly,
      scalable file storage solution designed for seamless integration with
      Amazon EC2 Linux and Mac instances within the AWS Cloud. With Amazon EFS,
      storage capacity dynamically adjusts to accommodate your changing file
      needs, ensuring your applications always have the necessary storage
      resources available. 
  - aid: amazon-web-services:aws-elastic-load-balancing
    name: AWS Elastic Load Balancing
    tags:
      - Balancer
      - Listeners
      - Load
      - Policies
      - Sets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/elasticloadbalancing/
    overlays:
      - url: overlays/elasticloadbalancing-openapi-search.yml
        type: APIs.io Search
      - url: overlays/elasticloadbalancing-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/elasticloadbalancing/
        type: Documentation
      - url: openapi/elasticloadbalancing-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/elasticloadbalancing/pricing/
        type: Pricing
      - url: https://aws.amazon.com/elasticloadbalancing/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/elasticloadbalancing/faqs/
        type: FAQ
      - url: https://aws.amazon.com/elasticloadbalancing/partners/
        type: Partners
      - url: https://aws.amazon.com/elasticloadbalancing/customers/
        type: Customers
      - url: https://aws.amazon.com/elasticloadbalancing/features/
        type: Features
      - url: https://aws.amazon.com/elasticloadbalancing/application-load-balancer/
        type: Application Load Balancers
      - url: https://aws.amazon.com/elasticloadbalancing/network-load-balancer/
        type: Network Load Balancers
      - url: https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/
        type: Gateway Load Balancers
      - url: https://aws.amazon.com/elasticloadbalancing/classic-load-balancer/
        type: Classic Load Balancers
    description: |-

      Elastic Load Balancing is a feature that allows you to distribute incoming
      traffic across your EC2 instances, increasing the availability of your
      application. The load balancer monitors the health of registered instances
      and ensures that traffic is only routed to healthy instances. 
  - aid: amazon-web-services:aws-elastic-beanstalk
    name: AWS Elastic Beanstalk
    tags:
      - Configurations
      - Settings
      - Validate
      - Applications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/elasticbeanstalk/
    overlays:
      - url: overlays/elasticbeanstalk-openapi-search.yml
        type: APIs.io Search
      - url: overlays/elasticbeanstalk-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/elasticbeanstalk/
        type: Documentation
      - url: openapi/elasticbeanstalk-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/elasticbeanstalk/pricing/
        type: Pricing
      - url: https://aws.amazon.com/elasticbeanstalk/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/elasticbeanstalk/developer-resources/
        type: Resources
      - url: https://aws.amazon.com/elasticbeanstalk/faqs/
        type: FAQ
      - url: https://aws.amazon.com/elasticbeanstalk/partners/
        type: Partners
    description: |-

      AWS Elastic Beanstalk makes it easy to develop, deploy, and maintain
      resilient and scalable applications in the Amazon Web Services cloud.
  - aid: amazon-web-services:amazon-emr
    name: Amazon EMR
    tags:
      - Mapping
      - Sessions
      - Studios
      - Datasets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/emr/
    overlays:
      - url: overlays/elasticmapreduce-openapi-search.yml
        type: APIs.io Search
      - url: overlays/elasticmapreduce-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/emr/
        type: Documentation
      - url: openapi/elasticmapreduce-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/emr/pricing/
        type: Pricing
      - url: https://aws.amazon.com/emr/faqs/
        type: FAQ
      - url: https://aws.amazon.com/emr/partners/
        type: Partners
      - url: https://aws.amazon.com/emr/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/emr/features/
        type: Features
      - url: https://aws.amazon.com/emr/features/studio/
        type: Studio
      - url: https://aws.amazon.com/emr/features/notebooks/
        type: Notebooks
      - url: https://aws.amazon.com/emr/serverless/
        type: Serverless
    description: |-

      The API provided by Amazon EMR is a powerful web service designed to
      streamline the processing of large datasets with efficiency. By leveraging
      Hadoop processing and integrating various Amazon Web Services, this tool
      allows for seamless execution of tasks like web indexing, data mining, log
      file analysis, machine learning, scientific simulation, and data warehouse
      management.
  - aid: amazon-web-services:amazon-emr-on-eks
    name: Amazon EMR on EKS
    tags:
      - ARN
      - Clusters
      - Credentials
      - Describe
      - Endpoints
      - Job RUns
      - Job Templates
      - Jobs
      - Managed
      - Resources
      - Runs
      - Sessions
      - Tags
      - Templates
      - Untag
      - Virtual
      - Virtual Clusters
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html
    overlays:
      - url: overlays/emr-containers-openapi-search.yml
        type: APIs.io Search
      - url: overlays/emr-containers-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html
        type: Documentation
      - url: openapi/emr-containers-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon EMR on EKS is a deployment option that allows you to run big data
      frameworks on Amazon EKS. This option allows you to focus on analytics
      workloads while Amazon EMR on EKS manages containers for open-source
      applications. The API name for this service is Amazon EMR containers, and
      it is used for CLI commands, IAM policy actions, and service endpoints
      related to Amazon EMR on EKS. For more information about Amazon EMR on EKS
      concepts and tasks, please refer to the documentation.
  - aid: amazon-web-services:aws-elastic-transcoder-service
    name: AWS Elastic Transcoder Service
    tags:
      - Jobs
      - Notifications
      - Pipelines
      - Presets
      - Read
      - Roles
      - Status
      - Tests
      - Transcoder
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/elastictranscoder/
    overlays:
      - url: overlays/elastictranscoder-openapi-search.yml
        type: APIs.io Search
      - url: overlays/elastictranscoder-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/elastictranscoder/
        type: Documentation
      - url: openapi/elastictranscoder-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Elastic Transcoder is media transcoding in the cloud. It is
      designed to be a highly scalable, easy to use and a cost effective way for
      developers and businesses to convert (or "transcode") media files from
      their source format into versions that will playback on devices like
      smartphones, tablets and PCs.
  - aid: amazon-web-services:amazon-simple-email-service
    name: Amazon Simple Email Service
    tags:
      - Emails
      - Identity
      - Verify
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ses/
    overlays:
      - url: overlays/email-openapi-search.yml
        type: APIs.io Search
      - url: overlays/email-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ses/
        type: Documentation
      - url: openapi/email-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ses/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ses/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/ses/faqs/
        type: FAQ
      - url: https://aws.amazon.com/ses/developer-resources/
        type: Resources
      - url: https://aws.amazon.com/ses/customers/
        type: Customers
      - url: https://aws.amazon.com/ses/partners/
        type: Partners
    description: |-

      This document provides detailed information about the Amazon Simple Email
      Service (Amazon SES) API version 2010-12-01. It is recommended to refer to
      the Amazon SES Developer Guide in conjunction with this document. The
      Amazon SES Developer Guide also includes a list of Amazon SES endpoints
      for service requests. 
  - aid: amazon-web-services:amazon-emr-serverless
    name: Amazon EMR Serverless
    tags:
      - ARN
      - Applications
      - Dashboard
      - Job RUns
      - Jobs
      - Resources
      - Runs
      - Stop
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://emr-serverless.[region].amazonaws.com
    humanURL: >-

      https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html
    overlays:
      - url: overlays/emr-serverless-openapi-search.yml
        type: APIs.io Search
      - url: overlays/emr-serverless-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html
        type: Documentation
      - url: openapi/emr-serverless-openapi-original.yml
        type: OpenAPI
    description: |-

      Introducing Amazon EMR Serverless, a new deployment option for Amazon EMR
      that offers a serverless runtime environment for running analytics
      applications with popular open source frameworks like Apache Spark and
      Apache Hive. 
  - aid: amazon-web-services:amazon-elasticsearch-configuration-service
    name: Amazon Elasticsearch Configuration Service
    tags:
      - Accept
      - Access
      - Associate
      - Authorize
      - Auto
      - Cancel
      - Change
      - Clusters
      - Compatible
      - Configurations
      - Connections
      - Describe
      - Dissociate
      - Domains
      - Elasticsearch
      - Endpoints
      - History
      - Inbound
      - Info
      - Instances
      - Limits
      - Names
      - Offerings
      - Outbound
      - Packages
      - Progress
      - Purchase
      - Reject
      - Removal
      - Removes
      - Reserved
      - Revoke
      - Roles
      - Search
      - Services
      - Software
      - Status
      - Tags
      - Tunes
      - Types
      - Upgrade
      - VPC
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://es.[region].amazonaws.com
    humanURL: >-

      https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html
    overlays:
      - url: overlays/es-openapi-search.yml
        type: APIs.io Search
      - url: overlays/es-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html
        type: Documentation
      - url: openapi/es-openapi-original.yml
        type: OpenAPI
    description: |-

      Utilize the Amazon Elasticsearch Configuration Service API for creating,
      customizing, and overseeing Elasticsearch domains. Developers can refer to
      the Amazon Elasticsearch Service Developer Guide for sample code
      showcasing the Configuration API in action, as well as instructions for
      sending signed HTTP requests to Elasticsearch APIs.
  - aid: amazon-web-services:aws-marketplace-entitlement-service
    name: AWS Marketplace Entitlement Service
    tags:
      - Entitlements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/marketplace/latest/userguide/checking-entitlements.html
    overlays:
      - url: overlays/entitlementmarketplace-openapi-search.yml
        type: APIs.io Search
      - url: overlays/entitlementmarketplace-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/marketplace/latest/userguide/checking-entitlements.html
        type: Documentation
      - url: openapi/entitlementmarketplace-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS Marketplace Entitlement Service API documentation provides an
      overview of how to use the service to determine a customer's entitlement
      to a specific product. Entitlements represent the capacity or access a
      customer has to a particular product, such as user seats in an SaaS
      application or data capacity in a database. The GetEntitlements function
      retrieves entitlement records for a Marketplace product.
  - aid: amazon-web-services:aws-entity-resolution
    name: AWS Entity Resolution
    tags:
      - ARN
      - Er
      - Erservices
      - Jobs
      - Mapping
      - Mappingworkflows
      - Match
      - Matches
      - Matching
      - Matching Workflows
      - Names
      - Prov
      - Providers
      - Resources
      - Schemas
      - Services
      - Tags
      - Untag
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/entity-resolution/
    overlays:
      - url: overlays/entityresolution-openapi-search.yml
        type: APIs.io Search
      - url: overlays/entityresolution-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/entity-resolution/
        type: Documentation
      - url: openapi/entityresolution-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/entity-resolution/features/
        type: Features
      - url: https://aws.amazon.com/entity-resolution/faqs/
        type: FAQ
      - url: https://aws.amazon.com/entity-resolution/pricing/
        type: Pricing
      - url: https://aws.amazon.com/entity-resolution/resources/
        type: Resources
      - url: https://aws.amazon.com/entity-resolution/customers/
        type: Customers
      - url: https://aws.amazon.com/entity-resolution/partners/
        type: Partners
    description: |-

      Discover the capabilities of the Entity Resolution API, a part of Amazon
      Web Services that simplifies the process of matching consumer identifiers
      within source records. By utilizing Entity Resolution, developers and
      analysts in the advertising and marketing industries can effortlessly
      create a comprehensive and accurate view of their customers.
  - aid: amazon-web-services:amazon-eventbridge
    name: Amazon EventBridge
    tags:
      - Endpoints
      - ' Events'
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/eventbridge/
    overlays:
      - url: overlays/eventbridge-openapi-search.yml
        type: APIs.io Search
      - url: overlays/eventbridge-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/eventbridge/
        type: Documentation
      - url: openapi/eventbridge-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/eventbridge/pricing/
        type: Pricing
      - url: https://aws.amazon.com/eventbridge/resources/
        type: Resources
      - url: https://aws.amazon.com/eventbridge/faqs/
        type: FAQ
      - url: https://aws.amazon.com/eventbridge/integrations/
        type: Integrations
      - url: https://aws.amazon.com/eventbridge/features/
        type: Features
      - url: https://aws.amazon.com/eventbridge/event-bus/
        type: Event Bus
      - url: https://aws.amazon.com/eventbridge/pipes/
        type: Pipes
      - url: https://aws.amazon.com/eventbridge/scheduler/
        type: Scheduler
    description: |-

      With Amazon EventBridge, you can easily monitor and respond to changes in
      your AWS resources by setting up rules that trigger actions based on
      specific events. Events generated by your resources are sent to an event
      stream, allowing you to create customized rules that match certain events
      and direct them to designated targets for further processing. You can also
      schedule actions to be performed at specific intervals. For example, you
      can automate tasks such as updating DNS entries, analyzing API records for
      security risks, or creating snapshots of EBS volumes. 
  - aid: amazon-web-services:amazon-kinesis-data-firehose
    name: Amazon Kinesis Data Firehose
    tags:
      - Destinations
      - Data
      - Delivery
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/firehose/
    overlays:
      - url: overlays/firehose-openapi-search.yml
        type: APIs.io Search
      - url: overlays/firehose-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/firehose/
        type: Documentation
      - url: openapi/firehose-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/firehose/faqs/
        type: FAQ
      - url: https://aws.amazon.com/firehose/resources/
        type: Resources
      - url: https://aws.amazon.com/firehose/customers/
        type: Customers
      - url: https://aws.amazon.com/firehose/partners/
        type: Partners
      - url: https://aws.amazon.com/firehose/pricing/
        type: Pricing
      - url: https://aws.amazon.com/firehose/features/
        type: Features
    description: |-

      The Amazon Kinesis Data Firehose API is a comprehensive tool for managing
      real-time streaming data delivery to a variety of destinations, including
      Amazon S3, Amazon OpenSearch Service, Amazon Redshift, Splunk, and more.
      This fully managed service streamlines the process of transmitting data
      effectively and efficiently.
  - aid: amazon-web-services:amazon-cloudwatch-evidently
    name: Amazon CloudWatch Evidently
    tags:
      - ARN
      - Batches
      - Cancel
      - Data
      - Deliveries
      - Evaluate
      - Evaluations
      - Events
      - Experiment
      - Experiments
      - Feature
      - Features
      - Launch
      - Launches
      - Patterns
      - Projects
      - References
      - Resources
      - Results
      - Segments
      - Stop
      - Tags
      - Tests
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html
    overlays:
      - url: overlays/evidently-openapi-search.yml
        type: APIs.io Search
      - url: overlays/evidently-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html
        type: Documentation
      - url: openapi/evidently-openapi-original.yml
        type: OpenAPI
    description: |-

      Utilize Amazon CloudWatch Evidently API to securely introduce and test new
      features to a percentage of your user base before full deployment.
      Monitoring the performance of these new features allows you to make
      informed decisions on when to increase user traffic. 
  - aid: amazon-web-services:amazon-forecast
    name: Amazon Forecast
    tags:
      - Datasets
      - Groups
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/forecast/
    overlays:
      - url: overlays/forecast-openapi-search.yml
        type: APIs.io Search
      - url: overlays/forecast-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/forecast/
        type: Documentation
      - url: openapi/forecast-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/forecast/partners/
        type: Partners
      - url: https://aws.amazon.com/forecast/customers/
        type: Customers
      - url: https://aws.amazon.com/forecast/resources/
        type: Resources
      - url: https://aws.amazon.com/forecast/embedded-solutions/
        type: Embedded Solutions
      - url: https://aws.amazon.com/forecast/pricing/
        type: Pricing
      - url: https://aws.amazon.com/forecast/features/
        type: Features
    description: |-

      Amazon Forecast, is a powerful tool designed for businesses looking to
      analyze and predict time-series data using machine learning.
  - aid: amazon-web-services:aws-fault-injection-simulator
    name: AWS Fault Injection Simulator
    tags:
      - ARN
      - Accounts
      - Actions
      - Configurations
      - Experiment
      - Experiments
      - Resolved
      - Resources
      - Stop
      - Tags
      - Targets
      - Targets
      - Templates
      - Types
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/fis/
    overlays:
      - url: overlays/fis-openapi-search.yml
        type: APIs.io Search
      - url: overlays/fis-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/fis/
        type: Documentation
      - url: openapi/fis-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/fis/features/
        type: Features
      - url: https://aws.amazon.com/fis/pricing/
        type: Pricing
      - url: https://aws.amazon.com/fis/faqs/
        type: FAQ
      - url: https://aws.amazon.com/fis/pricing/
        type: Pricing
    description: |-

      AWS Fault Injection Service (FIS), a component of the AWS Resilience Hub,
      is a comprehensive service designed to enhance an application's
      performance, observability, and resilience through the implementation of
      fault injection experiments. By streamlining the setup and execution of
      controlled fault injection tests across various AWS services, FIS empowers
      teams to increase their confidence in the reliability of their
      applications.
  - aid: amazon-web-services:amazon-fraud-detector
    name: Amazon Fraud Detector
    tags:
      - Variables
      - Fraud
      - ' Detection'
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/fraud-detector/
    overlays:
      - url: overlays/frauddetector-openapi-search.yml
        type: APIs.io Search
      - url: overlays/frauddetector-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/fraud-detector/
        type: Documentation
      - url: openapi/frauddetector-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/fraud-detector/features/
        type: Features
      - url: https://aws.amazon.com/fraud-detector/pricing/
        type: Pricing
      - url: https://aws.amazon.com/fraud-detector/faqs/
        type: FAQ
      - url: https://aws.amazon.com/fraud-detector/resources/
        type: Resources
      - url: https://aws.amazon.com/fraud-detector/customers/
        type: Customers
    description: |-

      Build, deploy, and manage fraud detection models without previous machine
      learning (ML) experience. Gain insights from your historical data, plus
      20+ years of Amazon experience, to construct an accurate, customized fraud
      detection model. Start detecting fraud immediately, easily enhance models
      with customized business rules, and deploy results to generate critical
      predictions.
  - aid: amazon-web-services:aws-firewall-manager
    name: AWS Firewall Manager
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/firewall-manager/
    overlays:
      - url: overlays/fms-openapi-search.yml
        type: APIs.io Search
      - url: overlays/fms-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/firewall-manager/
        type: Documentation
      - url: openapi/fms-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/firewall-manager/features/
        type: Features
      - url: https://aws.amazon.com/firewall-manager/pricing/
        type: Pricing
      - url: https://aws.amazon.com/firewall-manager/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/firewall-manager/resources/
        type: Resources
      - url: https://aws.amazon.com/firewall-manager/faqs/
        type: FAQ
    description: |-

      Welcome to the Firewall Manager API Reference. This comprehensive guide is
      designed for developers seeking in-depth information on the various
      actions, data types, and errors associated with the Firewall Manager API.
      For a more detailed overview of Firewall Manager features, please refer to
      the Firewall Manager Developer Guide. 
  - aid: amazon-web-services:amazon-gamelift
    name: Amazon GameLift
    tags:
      - Matchmaking
      - Rules
      - Sets
      - Validate
      - Games
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/gamelift/
    overlays:
      - url: overlays/gamelift-openapi-search.yml
        type: APIs.io Search
      - url: overlays/gamelift-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/gamelift/
        type: Documentation
      - url: openapi/gamelift-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/gamelift/pricing/
        type: Pricing
      - url: https://aws.amazon.com/gamelift/features/
        type: Features
      - url: https://aws.amazon.com/gamelift/resources/
        type: Resources
      - url: https://aws.amazon.com/gamelift/faq/
        type: FAQ
      - url: https://aws.amazon.com/gamelift/getting-started/
        type: Getting-started
    description: |-

      The Amazon GameLift API offers comprehensive cloud hosting solutions for
      session-based multiplayer game servers. It includes features for
      deploying, managing, and expanding game servers seamlessly. Leveraging
      Amazon Web Services' robust global computing network, GameLift ensures
      top-tier performance, reliability, and cost-efficiency for your game
      servers.
  - aid: amazon-web-services:global-accelerator
    name: Global Accelerator
    tags:
      - CIDR
      - Withdraw
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/global-accelerator/
    overlays:
      - url: overlays/globalaccelerator-openapi-search.yml
        type: APIs.io Search
      - url: overlays/globalaccelerator-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/global-accelerator/
        type: Documentation
      - url: openapi/globalaccelerator-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/global-accelerator/features/
        type: Features
      - url: https://aws.amazon.com/global-accelerator/pricing/
        type: Pricing
      - url: https://aws.amazon.com/global-accelerator/faqs/
        type: FAQ
      - url: https://aws.amazon.com/global-accelerator/customers/
        type: Customers
    description: |-

      Global Accelerator is a powerful API service that allows developers to
      create accelerators to enhance the performance of their applications for
      both local and global users. This API Reference provides detailed
      information on Global Accelerator API actions, data types, and errors,
      catering to developers looking to leverage Global Accelerator features.
  - aid: amazon-web-services:amazon-s3-glacier
    name: Amazon S3 Glacier
    tags:
      - Access
      - Accounts
      - Archive
      - Archives
      - Capacity
      - Complete
      - Configurations
      - Data
      - Describe
      - Initiate
      - Jobs
      - Locks
      - Multipart
      - Names
      - Notifications
      - Output
      - Policies
      - Provisioned
      - Purchase
      - Removes
      - Retrieval
      - Sets
      - Tags
      - Uploads
      - Vault
      - Vaults
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/s3/storage-classes/glacier/
    overlays:
      - url: overlays/glacier-openapi-search.yml
        type: APIs.io Search
      - url: overlays/glacier-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/s3/storage-classes/glacier/
        type: Documentation
      - url: openapi/glacier-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/s3/storage-classes/glacier/instant-retrieval/
        type: Instant-retrieval
    description: |-

      Amazon S3 Glacier (Glacier) is a cost-effective storage solution designed
      for long-term storage of infrequently accessed data. It provides secure,
      durable, and easy-to-use storage for data backup and archival purposes.
      With Glacier, users can store data for extended periods without worrying
      about capacity planning or hardware management. Glacier is ideal for when
      low storage costs are a priority and data retrieval is rare. For
      applications requiring fast or frequent access to data, Amazon S3 is
      recommended. Users can store data in any format without limits on the
      total amount of data stored in Glacier. 
  - aid: amazon-web-services:aws-finspace
    name: AWS FinSpace
    tags:
      - Access
      - Change Sets
      - Credentials
      - Data
      - Data Views
      - Datasets
      - Details
      - Disable
      - Disassociate
      - Enable
      - External
      - Groups
      - Locations
      - Password
      - Permission
      - Programmatic
      - Reset
      - Users
      - View
      - Views
      - Working
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/finspace/
    overlays:
      - url: overlays/finspace-data-openapi-search.yml
        type: APIs.io Search
      - url: overlays/finspace-data-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/finspace/
        type: Documentation
      - url: openapi/finspace-data-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/finspace/pricing/
        type: Pricing
      - url: https://aws.amazon.com/finspace/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/finspace/partners/
        type: Partners
      - url: https://aws.amazon.com/finspace/faqs/
        type: FAQ
      - url: https://aws.amazon.com/finspace/getting-started/
        type: Getting-started
    description: |-

      Experience seamless data processing and analytics tailored for Capital
      Markets with our API, which offers Managed kdb Insights. Take advantage of
      our free AWS training to enhance your skills and advance your career with
      AWS Cloud Practitioner Essentials. 
  - aid: amazon-web-services:amazon-fsx
    name: Amazon FSx
    tags:
      - Volumes
      - File Systems
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/fsx/
    overlays:
      - url: overlays/fsx-openapi-search.yml
        type: APIs.io Search
      - url: overlays/fsx-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/fsx/
        type: Documentation
      - url: openapi/fsx-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/fsx/pricing/
        type: Pricing
      - url: https://aws.amazon.com/fsx/netapp-ontap/
        type: Netapp-ontap
      - url: https://aws.amazon.com/fsx/openzfs/
        type: Openzfs
      - url: https://aws.amazon.com/fsx/windows/
        type: Windows
      - url: https://aws.amazon.com/fsx/lustre/
        type: Lustre
    description: |-

      The Amazon FSx API simplifies the process of launching, managing, and
      expanding feature-rich, high-performance file systems in the cloud. With
      its reliability, security, scalability, and numerous capabilities, Amazon
      FSx supports a variety of workloads. Leveraging the latest AWS
      technologies in compute, networking, and disk storage, Amazon FSx delivers
      high performance at a lower total cost of ownership.
  - aid: amazon-web-services:aws-iot-greengrass
    name: AWS IoT Greengrass
    tags:
      - ARN
      - Accounts
      - Artifacts
      - Associate
      - Associated
      - Ates
      - Batches
      - Cancel
      - Cand
      - Candidates
      - Clients
      - Components
      - Connectivity
      - Core
      - Deployments
      - Describe
      - Device
      - Devices
      - Disassociate
      - Effective
      - Green Grass
      - Info
      - Installed
      - Metadata
      - Names
      - Resolve
      - Resources
      - Roles
      - Service Roles
      - Services
      - Tags
      - Things
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/greengrass/
    overlays:
      - url: overlays/greengrassv2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/greengrassv2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/greengrass/
        type: Documentation
      - url: openapi/greengrassv2-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/greengrass/features/
        type: Features
      - url: https://aws.amazon.com/greengrass/ml/
        type: Ml
      - url: https://aws.amazon.com/greengrass/pricing/
        type: Pricing
      - url: https://aws.amazon.com/greengrass/partners/
        type: Partners
      - url: https://aws.amazon.com/greengrass/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/greengrass/faqs/
        type: FAQ
    description: |-

      IoT Greengrass brings local compute, messaging, data management, sync, and
      ML inference capabilities to edge devices. This enables devices to collect
      and analyze data closer to the source of information, react autonomously
      to local events, and communicate securely with each other on local
      networks. 
  - aid: amazon-web-services:aws-glue
    name: AWS Glue
    tags:
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/glue/
    overlays:
      - url: overlays/glue-openapi-search.yml
        type: APIs.io Search
      - url: overlays/glue-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/glue/
        type: Documentation
      - url: openapi/glue-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/glue/features/
        type: Features
      - url: https://aws.amazon.com/glue/pricing/
        type: Pricing
      - url: https://aws.amazon.com/glue/partners/
        type: Partners
      - url: https://aws.amazon.com/glue/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/glue/resources/
        type: Resources
      - url: https://aws.amazon.com/glue/faqs/
        type: FAQ
      - url: https://aws.amazon.com/glue/customers/
        type: Customers
    description: |-

      The first step in any analytics or machine learning project is ensuring
      your data is prepared for quality results. AWS Glue is a serverless data
      integration service that streamlines and simplifies the data preparation
      process, making it faster and more cost-effective. 
  - aid: amazon-web-services:amazon-managed-grafana
    name: Amazon Managed Grafana
    tags:
      - ARN
      - Authentication
      - Configurations
      - Disassociate
      - Keys
      - Licenses
      - Names
      - Permissions
      - Resources
      - Tags
      - Types
      - Untag
      - Versions
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/grafana/
    overlays:
      - url: overlays/grafana-openapi-search.yml
        type: APIs.io Search
      - url: overlays/grafana-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/grafana/
        type: Documentation
      - url: openapi/grafana-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/grafana/features/
        type: Features
      - url: https://aws.amazon.com/grafana/pricing/
        type: Pricing
      - url: https://aws.amazon.com/grafana/resources/
        type: Resources
      - url: https://aws.amazon.com/grafana/faqs/
        type: FAQ
      - url: https://aws.amazon.com/grafana/customers/
        type: Customers
      - url: https://aws.amazon.com/grafana/partners/
        type: Partners
    description: |-

      Amazon Managed Grafana is a managed and secure data visualization service
      that allows you to easily query, correlate, and visualize operational
      metrics, logs, and traces from various sources. It simplifies the
      deployment, operation, and scalability of Grafana, a popular data
      visualization tool known for its flexible data support. Users can create
      isolated Grafana servers, called workspaces, where they can design
      dashboards and visualizations to analyze their data without the need for
      hardware deployment.
  - aid: amazon-web-services:amazon-guardduty
    name: Amazon GuardDuty
    tags:
      - ARN
      - Accounts
      - Administrative
      - Administrator
      - Archive
      - Configurations
      - Count
      - Coverage
      - Days
      - Decline
      - Describe
      - Destinations
      - Detectors
      - Disable
      - Disassociate
      - Enable
      - Feedback
      - Filter
      - Filters
      - Findings
      - Free
      - IP
      - IPSet
      - IPSets
      - Intelligence
      - Invitation
      - Invitations
      - Invite
      - Malware
      - Master
      - Members
      - Monitoring
      - Names
      - Organizations
      - Publishing
      - Remaining
      - Resources
      - Samples
      - Scans
      - Sets
      - Settings
      - Statistics
      - Stop
      - Tags
      - Threat
      - Trials
      - Unarchive
      - Untag
      - Usage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/guardduty/
    overlays:
      - url: overlays/guardduty-openapi-search.yml
        type: APIs.io Search
      - url: overlays/guardduty-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/guardduty/
        type: Documentation
      - url: openapi/guardduty-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/guardduty/features/
        type: Features
      - url: https://aws.amazon.com/guardduty/pricing/
        type: Pricing
      - url: https://aws.amazon.com/guardduty/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/guardduty/resources/
        type: Resources
      - url: https://aws.amazon.com/guardduty/faqs/
        type: FAQ
      - url: https://aws.amazon.com/guardduty/resources/partners/
        type: Partners
      - url: https://aws.amazon.com/guardduty/customers/
        type: Customers
    description: |-

      Amazon GuardDuty is a security monitoring service that continuously
      analyzes various data sources within your Amazon Web Services environment,
      such as VPC flow logs, CloudTrail event logs, EKS audit logs, DNS logs,
      and more. 
  - aid: amazon-web-services:aws-iot-greengrass
    name: AWS IoT Greengrass
    tags:
      - $Reset
      - $Stop
      - ARN
      - Accounts
      - Associated
      - Authorities
      - Authority
      - Bulk
      - Certificate Authorities
      - Certificates
      - Configurations
      - Connectivity
      - Connectors
      - Core
      - Cores
      - Definitions
      - Deployments
      - Detailed
      - Device
      - Devices
      - Expiry
      - Functions
      - Green Grass
      - Groups
      - Info
      - Jobs
      - Loggers
      - Names
      - Reports
      - Reset
      - Resources
      - Roles
      - Runtime
      - Runtime Configurations
      - Service Roles
      - Services
      - Software
      - Status
      - Stop
      - Subscriptions
      - Tags
      - Things
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/greengrass/
    overlays:
      - url: overlays/greengrass-openapi-search.yml
        type: APIs.io Search
      - url: overlays/greengrass-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/greengrass/
        type: Documentation
      - url: openapi/greengrass-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/greengrass/features/
        type: Features
      - url: https://aws.amazon.com/greengrass/ml/
        type: Ml
      - url: https://aws.amazon.com/greengrass/pricing/
        type: Pricing
      - url: https://aws.amazon.com/greengrass/partners/
        type: Partners
      - url: https://aws.amazon.com/greengrass/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/greengrass/faqs/
        type: FAQ
      - url: https://aws.amazon.com/greengrass/device-tester/
        type: Device-tester
    description: |-

      This API, AWS IoT Greengrass, extends the capabilities of AWS to physical
      devices, enabling them to process data locally while still utilizing the
      cloud for management, analytics, and storage. This allows devices to
      respond quickly to local events even with intermittent connectivity,
      minimizing the cost of transmitting data to the cloud by enabling the
      execution of AWS Lambda functions locally.
  - aid: amazon-web-services:aws-healthlake
    name: AWS HealthLake
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/healthlake/
    overlays:
      - url: overlays/healthlake-openapi-search.yml
        type: APIs.io Search
      - url: overlays/healthlake-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/healthlake/
        type: Documentation
      - url: openapi/healthlake-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/healthlake/features/
        type: Features
      - url: https://aws.amazon.com/healthlake/pricing/
        type: Pricing
      - url: https://aws.amazon.com/healthlake/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/healthlake/resources/
        type: Resources
      - url: https://aws.amazon.com/healthlake/faqs/
        type: Customers
      - url: https://aws.amazon.com/healthlake/customers/
        type: Customers
      - url: https://aws.amazon.com/healthlake/partners/
        type: Partners
    description: |-

      AWS HealthLake is a service designed for healthcare companies that need a
      comprehensive view of individual and patient population health data. This
      HIPAA-eligible service utilizes FHIR API transactions to securely store
      and transform data into a queryable format at a large scale.
  - aid: amazon-web-services:aws-identity-and-access-management
    name: AWS Identity and Access Management
    tags:
      - Certificates
      - Signing
      - Uploads
      - ' Identity'
      - ' IAM'
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iam/
    overlays:
      - url: overlays/iam-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iam-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iam/
        type: Documentation
      - url: openapi/iam-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iam/features/
        type: Features
      - url: https://aws.amazon.com/iam/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/iam/resources/
        type: Resources
      - url: https://aws.amazon.com/iam/faqs/
        type: FAQ
    description: |-

      IAM is a trusted web service that enables secure access control for Amazon
      Web Services. It offers centralized management of users, access keys, and
      permissions to regulate access to AWS resources. 
  - aid: amazon-web-services:aws-ground-station
    name: AWS Ground Station
    tags:
      - ARN
      - Agent
      - Configurations
      - Contacts
      - Dataflow
      - Describe
      - Endpoints
      - Ephemer
      - Ground
      - Groundstation
      - Groups
      - Minute
      - Mission
      - Mission Profile
      - Profiles
      - Register
      - Reserve
      - Resources
      - Satellites
      - Stations
      - Status
      - Tags
      - Types
      - Untag
      - Usage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ground-station/
    overlays:
      - url: overlays/groundstation-openapi-search.yml
        type: APIs.io Search
      - url: overlays/groundstation-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ground-station/
        type: Documentation
      - url: openapi/groundstation-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ground-station/features/
        type: Features
      - url: https://aws.amazon.com/ground-station/locations/
        type: Locations
      - url: https://aws.amazon.com/ground-station/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ground-station/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/ground-station/faqs/
        type: FAQ
      - url: https://aws.amazon.com/ground-station/features/
        type: Features
    description: |-

      Welcome to the AWS Ground Station API Reference. AWS Ground Station is a
      fully managed service that enables you to control satellite
      communications, downlink and process satellite data, and scale your
      satellite operations efficiently and cost-effectively without having to
      build or manage your own ground station infrastructure.
  - aid: amazon-web-services:aws-identity-store
    name: AWS  Identity Store
    tags:
      - Users
      - Identity
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html
    overlays:
      - url: overlays/identitystore-openapi-search.yml
        type: APIs.io Search
      - url: overlays/identitystore-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html
        type: Documentation
      - url: openapi/identitystore-openapi-original.yml
        type: OpenAPI
    description: |-

      The API for the Identity Store service within IAM Identity Center is a
      central hub for accessing all user and group identities. You can find
      detailed information on how to use this service in the IAM Identity Center
      User Guide, which outlines the available identity store operations that
      can be accessed programmatically. The API utilizes the sso and
      identitystore namespaces for seamless integration with your systems.
  - aid: amazon-web-services:aws-ec2-image-builder
    name: AWS EC2 Image Builder
    tags:
      - ARN
      - Actions
      - Aggregations
      - Build
      - Cancel
      - Components
      - Configurations
      - Container
      - Creation
      - Distributions
      - Execution
      - Executions
      - Findings
      - Images
      - Import
      - Infrastructure
      - Lifecycle
      - Packages
      - Pipelines
      - Policies
      - Recipes
      - Resources
      - Scans
      - Send
      - States
      - Steps
      - Tags
      - Untag
      - Versions
      - Waiting
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/image-builder/
    overlays:
      - url: overlays/imagebuilder-openapi-search.yml
        type: APIs.io Search
      - url: overlays/imagebuilder-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/image-builder/
        type: Documentation
      - url: openapi/imagebuilder-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/image-builder/features/
        type: Features
      - url: https://aws.amazon.com/image-builder/faqs/
        type: FAQ
    description: |-

      The API for EC2 Image Builder is a comprehensive AWS service designed to
      streamline the process of automating the creation, control, and
      distribution of personalized, secure, and current server images which are
      pre-loaded and pre-configured with software and settings according to
      required IT guidelines.
  - aid: amazon-web-services:amazon-inspector-scan
    name: Amazon Inspector Scan
    tags:
      - Inspector
      - Scans
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/inspector/
    overlays:
      - url: overlays/inspector-scan-openapi-search.yml
        type: APIs.io Search
      - url: overlays/inspector-scan-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/inspector/
        type: Documentation
      - url: openapi/inspector-scan-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/inspector/features/
        type: Features
      - url: https://aws.amazon.com/inspector/pricing/
        type: Pricing
      - url: https://aws.amazon.com/inspector/resources/
        type: Resources
      - url: https://aws.amazon.com/inspector/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/inspector/faqs/
        type: FAQ
      - url: https://aws.amazon.com/inspector/customers/
        type: Customers
      - url: https://aws.amazon.com/inspector/partners/
        type: Partners
    description: |-

      The Amazon Inspector API effortlessly identifies workloads, such as Amazon
      EC2 instances, containers, and Lambda functions, and conducts thorough
      scans to detect software vulnerabilities and unintentional network risks.
  - aid: amazon-web-services:aws-health
    name: AWS Health
    tags:
      - Access
      - Enable
      - Health
      - Organizations
      - Services
      - Healthcare
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/health/
    overlays:
      - url: overlays/health-openapi-search.yml
        type: APIs.io Search
      - url: overlays/health-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/health/
        type: Documentation
      - url: openapi/health-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/health/case-studies/
        type: Case-studies
      - url: https://aws.amazon.com/health/life-sciences/solutions/
        type: Life Science Solutions
      - url: https://aws.amazon.com/health/genomics/solutions/
        type: Genomics Solutions
      - url: https://aws.amazon.com/health/healthcare/solutions/
        type: Healthcare Solutions
      - url: https://aws.amazon.com/health/providers/
        type: Providers
      - url: https://aws.amazon.com/health/payors/
        type: Payors
      - url: https://aws.amazon.com/health/healthtech/
        type: Healthtech
    description: |-

      The Health API grants access to Health information displayed in the Health
      Dashboard. Users can utilize API operations to retrieve data on events
      that may impact their Amazon Web Services and resources. 
  - aid: amazon-web-services:aws-iot
    name: AWS IoT
    tags:
      - ARN
      - Accept
      - Accounts
      - Actions
      - Active
      - Aggregation
      - Alias
      - Aliases
      - Associate
      - Ate
      - Attached
      - Audit
      - Audits
      - Authorization
      - Authorizers
      - Behavior
      - Behaviors
      - Billing
      - Buckets
      - CA
      - CACertificate
      - CACertificates
      - Cancel
      - Cardinality
      - Certificates
      - Claim
      - Code
      - Configurations
      - Confirm
      - Confirmation
      - Confirmdestination
      - Custom
      - Default
      - Demand
      - Deprecate
      - Describe
      - Destinations
      - Detach
      - Detect
      - Dimensions
      - Disable
      - Documents
      - Domains
      - Dynamic
      - Effective
      - Enable
      - Endpoints
      - Er
      - Ers
      - Events
      - Execution
      - Executions
      - Findings
      - Fleets
      - Groups
      - Index
      - Indexing
      - Indices
      - Invoke
      - Jobs
      - Keys
      - Levels
      - Logging
      - Managed
      - Metrics
      - Mitigation
      - Mitigation Actions
      - Models
      - Names
      - Numbers
      - OTAUpdate
      - OTAUpdates
      - 'On'
      - Options
      - Out
      - Outgoing
      - Packages
      - Percentiles
      - Policies
      - Principals
      - Profiles
      - Prov
      - Providers
      - Provisioning
      - Register
      - Registration Codes
      - Registrations
      - Reject
      - Related
      - Removes
      - Replace
      - Reports
      - Resources
      - Roles
      - Rules
      - Scheduled
      - Scheduled Audits
      - Search
      - Security
      - Sets
      - States
      - Statistics
      - Stop
      - Stream
      - Streams
      - Summaries
      - Suppressions
      - Tags
      - Targets
      - Tasks
      - Templates
      - Tests
      - Things
      - Tokens
      - Topics
      - Training
      - Transfers
      - Types
      - Untag
      - Validate
      - Values
      - Verification
      - Versions
      - Violations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot/
    overlays:
      - url: overlays/iot-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iot-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot/
        type: Documentation
      - url: openapi/iot-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot/customers/
        type: Customers
      - url: https://aws.amazon.com/iot/iot-events-partner-news/
        type: News
      - url: https://aws.amazon.com/iot/partner-solutions/
        type: Partners
      - url: https://aws.amazon.com/iot/solutions/
        type: Solutions
      - url: https://aws.amazon.com/iot/resources/
        type: Resources
      - url: https://aws.amazon.com/iot/blog/
        type: Blog
      - url: https://aws.amazon.com/iot/customers/
        type: Customers
      - url: https://aws.amazon.com/iot/edukit/
        type: Edukit
    description: |-

      The IoT API enables secure communication between Internet-connected
      devices and the Amazon Web Services cloud. Users can access custom
      IoT-Data endpoints, set up data processing rules, integrate with other
      services, manage device resources, configure logging, and create
      authentication policies and credentials. 
  - aid: amazon-web-services:aws-iot-jobs
    name: AWS IoT Jobs
    tags:
      - Executions
      - Jobs
      - Names
      - Next
      - Pending
      - Things
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html
    overlays:
      - url: overlays/iot-jobs-data-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iot-jobs-data-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://example.com
        type: Documentation
      - url: openapi/iot-jobs-data-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS IoT Jobs is a service that allows you to create and manage a set of
      remote operations to be executed on devices connected to AWS IoT. These
      operations can include tasks such as downloading updates, installing
      firmware, rebooting devices, rotating certificates, and troubleshooting. 
  - aid: amazon-web-services:amazon-cloudwatch-internet-monitor
    name: Amazon CloudWatch Internet Monitor
    tags:
      - ARN
      - Events
      - Health
      - Monitors
      - Names
      - Queries
      - Resources
      - Results
      - Status
      - Stop
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html
    overlays:
      - url: overlays/internetmonitor-openapi-search.yml
        type: APIs.io Search
      - url: overlays/internetmonitor-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html
        type: Documentation
      - url: openapi/internetmonitor-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon CloudWatch Internet Monitor provides visibility into how internet
      issues impact the performance and availability between your applications
      hosted on Amazon Web Services and your end users. It can reduce the time
      it takes for you to diagnose internet issues from days to minutes. 
  - aid: amazon-web-services:aws-iot-analytics
    name: AWS IoT Analytics
    tags:
      - Activity
      - Batches
      - Cancel
      - Channels
      - Content
      - Contents
      - Data
      - Data Store
      - Datasets
      - Logging
      - Messages
      - Names
      - Options
      - Pipeline Activities
      - Pipelines
      - Reprocessing
      - Resources
      - Runs
      - Samples
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-analytics/
    overlays:
      - url: overlays/iotanalytics-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotanalytics-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-analytics/
        type: Documentation
      - url: openapi/iotanalytics-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-analytics/features/
        type: Features
      - url: https://aws.amazon.com/iot-analytics/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-analytics/faq/
        type: FAQ
      - url: https://aws.amazon.com/iot-analytics/resources/
        type: Resources
      - url: https://aws.amazon.com/iot-analytics/partners/
        type: Partners
    description: |-

      IoT Analytics is a powerful tool designed to streamline the collection,
      processing, storage, and analysis of large amounts of device data. This
      API allows users to easily query and run sophisticated analytics on IoT
      data, enabling advanced exploration and visualization through integration
      with Jupyter Notebooks and Amazon QuickSight. 
  - aid: amazon-web-services:aws-iot-core-device-advisor
    name: AWS IoT Core Device Advisor
    tags:
      - ARN
      - Definitions
      - Endpoints
      - Reports
      - Resources
      - Runs
      - Stop
      - Suites
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-core/device-advisor/
    overlays:
      - url: overlays/iotdeviceadvisor-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotdeviceadvisor-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-core/device-advisor/
        type: Documentation
      - url: openapi/iotdeviceadvisor-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-core/features/
        type: Features
      - url: https://aws.amazon.com/iot-core/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-core/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/iot-core/faqs/
        type: Features
      - url: https://aws.amazon.com/iot/customers/
        type: Customers
    description: |-

      Amazon Web Services IoT Core Device Advisor is a cloud-based testing
      service designed to verify the functionality and security of IoT devices
      before deployment. It offers a range of pre-built tests to ensure reliable
      connectivity with Amazon Web Services IoT Core. 
  - aid: amazon-web-services:aws-iot-1-click-projects
    name: ' AWS IoT 1-Click Projects'
    tags:
      - ARN
      - Device
      - Devices
      - Disassociate
      - Names
      - Placements
      - Projects
      - Resources
      - Tags
      - Templates
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-1-click/
    overlays:
      - url: overlays/iot1click-projects-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iot1click-projects-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-1-click/
        type: Documentation
      - url: openapi/iot1click-projects-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-1-click/features/
        type: Features
      - url: https://aws.amazon.com/iot-1-click/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-1-click/devices/
        type: Devices
      - url: https://aws.amazon.com/iot-1-click/faq/
        type: FAQ
      - url: https://aws.amazon.com/iot-1-click/features/
        type: Features
    description: |-

      This API allows AWS IoT 1-Click devices to easily and securely connect to
      AWS IoT Core upon deployment, eliminating the need for manual certificate
      management.
  - aid: amazon-web-services:aws-iot-events
    name: AWS IoT Events
    tags:
      - Acknowledge
      - Alarm
      - Alarms
      - Batches
      - Describe
      - Detectors
      - Disable
      - Enable
      - Inputs
      - Keys
      - Messages
      - Models
      - Names
      - Reset
      - Snooze
      - Values
      - Events
      - IoT
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-events/
    overlays:
      - url: overlays/iotevents-data-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotevents-data-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-events/
        type: Documentation
      - url: openapi/iotevents-data-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-events/features/
        type: Features
      - url: https://aws.amazon.com/iot-events/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-events/faqs/
        type: FAQ
      - url: https://aws.amazon.com/iot-events/features/
        type: Features
    description: |-

      The IoT Events API allows you to track the status and performance of your
      equipment or device fleets, enabling you to detect failures or changes in
      operation and take appropriate actions. With IoT Events Data API, you can
      interact with detectors by sending inputs, listing detectors, and
      accessing or modifying their status. 
  - aid: amazon-web-services:aws-iot-device-management
    name: AWS IoT Device Management
    tags:
      - Applications
      - ARN
      - Resources
      - Tags
      - Untag
      - Devices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-device-management/
    overlays:
      - url: overlays/iotfleethub-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotfleethub-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-device-management/
        type: Documentation
      - url: openapi/iotfleethub-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-device-management/features/
        type: Features
      - url: https://aws.amazon.com/iot-device-management/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-device-management/resources/
        type: Resources
      - url: https://aws.amazon.com/iot-device-management/faq/
        type: FAQ
    description: |-

      AWS IoT Device Management simplifies the process of registering,
      organizing, monitoring, and remotely managing IoT devices on a large
      scale. Seamlessly integrate with AWS IoT Core for cloud device
      connectivity and management, as well as with AWS IoT Device Defender for
      auditing and monitoring the security posture of your fleet.
  - aid: amazon-web-services:aws-iot-data
    name: AWS IoT Data
    tags:
      - Messages
      - Named
      - Names
      - Publish
      - Retained
      - Shadow
      - Shadows
      - Things
      - Topics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Data_Plane.html
    overlays:
      - url: overlays/iot-data-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iot-data-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Data_Plane.html
        type: Documentation
      - url: openapi/iot-data-openapi-original.yml
        type: OpenAPI
    description: |-

      This API, IoT data, facilitates secure communication between
      Internet-connected devices and the Amazon Web Services cloud. It acts as a
      broker for devices to publish messages via HTTP and manage shadows,
      persistent representations of the device state in the AWS cloud. 
  - aid: amazon-web-services:aws-iot-1-click-devices
    name: AWS IoT 1-Click devices
    tags:
      - ARN
      - Claim
      - Claims
      - Code
      - Describe
      - Device
      - Devices
      - Events
      - Finalize
      - Initiate
      - Invoke
      - Methods
      - Resources
      - States
      - Tags
      - Unclaim
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-1-click/devices/
    overlays:
      - url: overlays/iot1click-devices-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iot1click-devices-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-1-click/devices/
        type: Documentation
      - url: openapi/iot1click-devices-openapi-original.yml
        type: OpenAPI
    description: |-

      Manufacturing partners of AWS IoT 1-Click develop devices that
      effortlessly connect to the AWS Cloud upon unboxing. These supported
      devices come pre-provisioned with certificates during manufacturing,
      eliminating the need for writing firmware or device-specific code to
      utilize them.
  - aid: amazon-web-services:aws-ot-secure-tunneling
    name: AWS oT Secure Tunneling
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html
    overlays:
      - url: overlays/iotsecuretunneling-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotsecuretunneling-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html
        type: Documentation
      - url: openapi/iotsecuretunneling-openapi-original.yml
        type: OpenAPI
    description: |-

      This API, IoT Secure Tunneling, allows users to establish secure remote
      connections to devices deployed in the field. This is particularly useful
      for devices situated behind restricted firewalls at remote sites. With IoT
      Secure Tunneling, users can troubleshoot, perform configuration updates,
      and execute other operational tasks on these devices. 
  - aid: amazon-web-services:aws-iot-fleetwise
    name: AWS IoT FleetWise
    tags:
      - Vehicles
      - ' Fleets'
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-fleetwise/
    overlays:
      - url: overlays/iotfleetwise-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotfleetwise-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-fleetwise/
        type: Documentation
      - url: openapi/iotfleetwise-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-fleetwise/features/
        type: Features
      - url: https://aws.amazon.com/iot-fleetwise/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-fleetwise/faqs/
        type: FAQ
      - url: https://aws.amazon.com/iot-fleetwise/customers/
        type: Customers
      - url: https://aws.amazon.com/iot-fleetwise/partners/
        type: Partners
    description: |-

      The Amazon Web Services IoT FleetWise API is a comprehensive solution for
      efficiently gathering and transmitting vehicle data to the AWS cloud. This
      fully managed service allows users to standardize data models, regardless
      of communication systems in use, and set up rules for transferring only
      essential data to the cloud.
  - aid: amazon-web-services:amazon-interactive-video-service-ivs
    name: Amazon Interactive Video Service (IVS)
    tags:
      - ARN
      - Batches
      - Channels
      - Configurations
      - Import
      - Keys
      - Metadata
      - Pairs
      - Playback
      - Policies
      - Recording
      - Resources
      - Restrictions
      - Revocations
      - Sessions
      - Stop
      - Stream
      - Streams
      - Tags
      - Untag
      - Videos
      - Viewers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ivs/
    overlays:
      - url: overlays/ivs-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ivs-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ivs/
        type: Documentation
      - url: openapi/ivs-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ivs/pricing/
        type: Pricing
      - url: https://aws.amazon.com/ivs/faqs/
        type: FAQ
      - url: https://aws.amazon.com/ivs/features/
        type: Features
      - url: https://aws.amazon.com/ivs/resources/
        type: Resources
      - url: https://aws.amazon.com/ivs/blogs/
        type: Blogs
    description: |-

      The Amazon IVS API is a REST-compatible interface utilizing standard HTTP
      requests and an EventBridge event stream for responses. JSON format is
      used for both requests and responses, including error messages. This
      regional service is compatible with various Amazon IVS HTTPS endpoints
      across supported regions as detailed in the Amazon Web Services General
      Reference. API Request Parameters and URLs are case-sensitive. For a
      detailed account of documentation changes in each release, please refer to
      the Document History section.
  - aid: amazon-web-services:aws-iot-events
    name: AWS IoT Events
    tags:
      - Alarm
      - Analysis
      - Describe
      - Detectors
      - Events
      - Inputs
      - Logging
      - Models
      - Names
      - Options
      - Resources
      - Results
      - Routings
      - Tags
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-events/
    overlays:
      - url: overlays/iotevents-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotevents-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-events/
        type: Documentation
      - url: openapi/iotevents-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-events/features/
        type: Features
      - url: https://aws.amazon.com/iot-events/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-events/faqs/
        type: FAQ
      - url: https://aws.amazon.com/iot-events/features/
        type: Features
    description: |-

      With AWS IoT Events, you can effortlessly monitor your equipment or device
      fleets for any failures or operational changes, and automatically trigger
      actions in response to these events. The API provides operations to manage
      inputs and detector models, including creating, reading, updating, and
      deleting them, as well as listing their versions.
  - aid: amazon-web-services:aws-iot-sitewise
    name: AWS IoT SiteWise
    tags:
      - Access
      - Accounts
      - Actions
      - Aggregates
      - Assets
      - Associate
      - Associated
      - Batches
      - Bulk
      - Capabilities
      - Composite
      - Compositions
      - Configurations
      - Dashboard
      - Dashboards
      - Default
      - Describe
      - Disassociate
      - Encryption
      - Execute
      - Execution
      - Gateways
      - Hierarchy
      - History
      - Import
      - Interpolated
      - Jobs
      - Latest
      - Logging
      - Models
      - Namespaces
      - Options
      - Policies
      - Portals
      - Projects
      - Properties
      - Queries
      - Relationships
      - Resources
      - Series
      - Storage
      - Tags
      - Time
      - Time Series
      - Untag
      - Value
      - Values
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-sitewise/
    overlays:
      - url: overlays/iotsitewise-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotsitewise-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-sitewise/
        type: Documentation
      - url: openapi/iotsitewise-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-sitewise/features/
        type: Features
      - url: https://aws.amazon.com/iot-sitewise/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-sitewise/resources/
        type: Resources
      - url: https://aws.amazon.com/iot-sitewise/faqs/
        type: FAQ
      - url: https://aws.amazon.com/iot-sitewise/customers/
        type: Customers
    description: |-

      Introducing the IoT SiteWise API, a powerful tool for connecting
      Industrial Internet of Things (IIoT) devices to the Amazon Web Services
      Cloud. Dive into the IoT SiteWise User Guide for further details and
      resources.
  - aid: amazon-web-services:iot-twinmaker
    name: IoT TwinMaker
    tags:
      - Batches
      - Cancel
      - Components
      - Entities
      - Execute
      - Execution
      - History
      - Jobs
      - Metadata
      - Plan
      - Pricing
      - Pricing Plans
      - Properties
      - Queries
      - Resources
      - Scenes
      - Sources
      - Sync
      - Tags
      - Transfers
      - Types
      - Untag
      - Value
      - Values
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iot-twinmaker/
    overlays:
      - url: overlays/iottwinmaker-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iottwinmaker-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iot-twinmaker/
        type: Documentation
      - url: openapi/iottwinmaker-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iot-twinmaker/features/
        type: Features
      - url: https://aws.amazon.com/iot-twinmaker/pricing/
        type: Pricing
      - url: https://aws.amazon.com/iot-twinmaker/resources/
        type: Resources
      - url: https://aws.amazon.com/iot-twinmaker/faqs/
        type: FAQ
      - url: https://aws.amazon.com/iot-twinmaker/customers/
        type: Customers
      - url: https://aws.amazon.com/iot-twinmaker/partners/
        type: Partners
    description: |-

      IoT TwinMaker is a cutting-edge service that allows users to create
      accurate digital replicas, also known as digital twins, of physical
      systems. By integrating data from a variety of sources including sensors,
      cameras, and enterprise applications, users can generate detailed
      visualizations to effectively monitor the performance of their factories,
      buildings, or industrial plants. This real-time data can be utilized for
      operational monitoring, error detection, and troubleshooting purposes.
  - aid: amazon-web-services:amazon-ivs-chat
    name: Amazon IVS Chat
    tags:
      - ARN
      - Chat
      - Configurations
      - Disconnect
      - Events
      - Logging
      - Messages
      - Resources
      - Rooms
      - Send
      - Tags
      - Tokens
      - Untag
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ivs/features/chat/
    overlays:
      - url: overlays/ivschat-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ivschat-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ivs/features/chat/
        type: Documentation
      - url: openapi/ivschat-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon IVS Chat control-plane API allows you to create and manage
      resources for Amazon IVS Chat, and integrate with the Amazon IVS Chat
      Messaging API for real-time chat room interactions. This regional AWS
      service includes resources such as LoggingConfiguration and Room, which
      can be tagged for organization and access management.
  - aid: amazon-web-services:amazon-msk
    name: Amazon MSK
    tags:
      - ARN
      - Bootstrap
      - Brokers
      - Clients
      - Clusters
      - Compatible
      - Configurations
      - Connections
      - Connectivity
      - Count
      - Describe
      - Info
      - Kafka
      - Monitoring
      - Nodes
      - Operation
      - Operations
      - Policies
      - Reboot
      - Replication
      - Replicators
      - Resources
      - Revisions
      - Secrets
      - Security
      - Storage
      - Tags
      - Types
      - Untag
      - VPC
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/msk/
    overlays:
      - url: overlays/kafka-openapi-search.yml
        type: APIs.io Search
      - url: overlays/kafka-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/msk/
        type: Documentation
      - url: openapi/kafka-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/msk/pricing/
        type: Pricing
      - url: https://aws.amazon.com/msk/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/msk/partners/
        type: Partners
      - url: https://aws.amazon.com/msk/customer-success/
        type: Customer-success
      - url: https://aws.amazon.com/msk/resources/
        type: Resources
      - url: https://aws.amazon.com/msk/faqs/
        type: FAQ
      - url: https://aws.amazon.com/msk/features/
        type: Features
    description: |-

      Amazon Managed Streaming for Apache Kafka (Amazon MSK) simplifies the
      process of ingesting and processing real-time streaming data by offering a
      fully managed Apache Kafka service.
  - aid: amazon-web-services:amazon-kendra
    name: Amazon Kendra
    tags:
      - Thesaurus
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/kendra/
    overlays:
      - url: overlays/kendra-openapi-search.yml
        type: APIs.io Search
      - url: overlays/kendra-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/kendra/
        type: Documentation
      - url: openapi/kendra-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/kendra/features/
        type: Features
      - url: https://aws.amazon.com/kendra/connectors/
        type: Connectors
      - url: https://aws.amazon.com/kendra/pricing/
        type: Pricing
      - url: https://aws.amazon.com/kendra/resources/
        type: Resources
      - url: https://aws.amazon.com/kendra/faqs/
        type: FAQ
      - url: https://aws.amazon.com/kendra/customers/
        type: Customers
    description: |-

      Amazon Kendra is a sophisticated enterprise search tool that simplifies
      the process of searching through multiple content repositories by
      providing pre-installed connectors.
  - aid: amazon-web-services:amazon-keyspaces
    name: Amazon Keyspaces
    tags:
      - Tables
      - KeySpaces
      - Cassandra
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/keyspaces/
    overlays:
      - url: overlays/keyspaces-openapi-search.yml
        type: APIs.io Search
      - url: overlays/keyspaces-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/keyspaces/
        type: Documentation
      - url: openapi/keyspaces-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/keyspaces/pricing/
        type: Pricing
      - url: https://aws.amazon.com/keyspaces/faqs/
        type: FAQ
      - url: https://aws.amazon.com/keyspaces/customers/
        type: Customers
      - url: https://aws.amazon.com/keyspaces/resources/
        type: Resources
      - url: https://aws.amazon.com/keyspaces/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/keyspaces/scaling-data/
        type: Scaling-data
      - url: https://aws.amazon.com/keyspaces/features/
        type: Features
      - url: https://aws.amazon.com/keyspaces/multi-region-replication/
        type: Regions
    description: |-

      Amazon Keyspaces (for Apache Cassandra) is a managed, highly scalable, and
      reliable database service that is compatible with Apache Cassandra. This
      service makes it simple to migrate, operate, and expand Cassandra
      workloads within the Amazon Web Services Cloud environment. Users can
      easily create keyspaces and tables in Amazon Keyspaces with just a few
      clicks on the Amazon Web Services Management Console or through a few
      lines of code, without the need to set up any infrastructure or install
      software. 
  - aid: amazon-web-services:aws-iot-wireless
    name: AWS IoT Wireless
    tags:
      - Accounts
      - Analyzer
      - Associate
      - Bulk
      - Certificates
      - Configurations
      - Data
      - Definitions
      - Deregister
      - Destinations
      - Device
      - Devices
      - Disassociate
      - Endpoints
      - Estimates
      - Events
      - Firmware
      - Gateways
      - Groups
      - Import
      - Information
      - Levels
      - Logs
      - Multicast
      - Names
      - Networks
      - Partners
      - Positions
      - Profiles
      - Reset
      - Resources
      - Send
      - Services
      - Sessions
      - Single
      - Statistics
      - Tags
      - Tasks
      - Tests
      - Things
      - Types
      - Untag
      - Wireless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/iot-wireless/
    overlays:
      - url: overlays/iotwireless-openapi-search.yml
        type: APIs.io Search
      - url: overlays/iotwireless-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/iot-wireless/
        type: Documentation
      - url: openapi/iotwireless-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS IoT Wireless API allows for bi-directional communication between
      internet-connected wireless devices and the AWS Cloud. It supports
      onboarding of LoRaWAN and Sidewalk devices, which use the Low Power Wide
      Area Networking (LPWAN) protocol to communicate with AWS IoT. 
  - aid: amazon-web-services:amazon-kendra-intelligent-ranking
    name: Amazon Kendra Intelligent Ranking
    tags:
      - Execution
      - Plan
      - Rescore
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/kendra/latest/dg/intelligent-rerank.html
    overlays:
      - url: overlays/kendra-ranking-openapi-search.yml
        type: APIs.io Search
      - url: overlays/kendra-ranking-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/kendra/latest/dg/intelligent-rerank.html
        type: Documentation
      - url: openapi/kendra-ranking-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/kendra/intelligent-ranking-pricing/
        type: Pricing
    description: |-

      Amazon Kendra Intelligent Ranking leverages the advanced semantic search
      capabilities of Amazon Kendra to intelligently re-prioritize the search
      results provided by a search service.
  - aid: amazon-web-services:aws-lambda
    name: AWS Lambda
    tags:
      - ARN
      - Accounts
      - Alias
      - Aliases
      - Async
      - Code
      - Concurrency
      - Configurations
      - Events
      - Functions
      - Invocations
      - Invoke
      - Layers
      - Management
      - Mapping
      - Names
      - Numbers
      - Permission
      - Policies
      - Provisioned
      - Publish
      - Removes
      - Resources
      - Responses
      - Runtime
      - Settings
      - Signing
      - Sources
      - Statements
      - Stream
      - Streaming
      - Tags
      - URL
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/lambda/
    overlays:
      - url: overlays/lambda-openapi-search.yml
        type: APIs.io Search
      - url: overlays/lambda-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/lambda/
        type: Documentation
      - url: openapi/lambda-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/lambda/features/
        type: Features
      - url: https://aws.amazon.com/lambda/pricing/
        type: Pricing
      - url: https://aws.amazon.com/lambda/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/lambda/resources/
        type: Resources
      - url: https://aws.amazon.com/lambda/faqs/
        type: FAQ
      - url: https://aws.amazon.com/lambda/partners/
        type: Partners
    description: |-

      This is the API Reference for AWS Lambda, a serverless computing service
      provided by Amazon Web Services. For a more in-depth understanding of AWS
      Lambda, please refer to the AWS Lambda Developer Guide. You can also visit
      "What is AWS Lambda" for a service overview and "AWS Lambda How it Works"
      in the AWS Lambda Developer Guide for detailed information on how the
      service functions.
  - aid: amazon-web-services:amazon-kinesis-data-streams
    name: Amazon Kinesis Data Streams
    tags:
      - Mode
      - Stream
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/kinesis/data-streams/
    overlays:
      - url: overlays/kinesis-openapi-search.yml
        type: APIs.io Search
      - url: overlays/kinesis-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/kinesis/data-streams/
        type: Documentation
      - url: openapi/kinesis-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/kinesis/data-streams/features/
        type: Features
      - url: https://aws.amazon.com/kinesis/data-streams/pricing/
        type: Pricing
      - url: https://aws.amazon.com/kinesis/data-streams/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/kinesis/data-streams/customers/
        type: Customers
      - url: https://aws.amazon.com/kinesis/data-streams/integrations/
        type: Integrations
      - url: https://aws.amazon.com/kinesis/data-streams/resources/
        type: Resources
      - url: https://aws.amazon.com/kinesis/data-streams/faqs/
        type: FAQ
    description: |-

      The Amazon Kinesis Data Streams Service API Reference provides developers
      with access to a managed service that can dynamically scale for processing
      streaming big data in real-time.
  - aid: amazon-web-services:aws-key-management-service
    name: AWS Key Management Service
    tags:
      - Verify
      - Keys
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/kms/
    properties:
      - url: https://aws.amazon.com/kms/
        type: Documentation
      - url: openapi/kms-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/kms/features/
        type: Features
      - url: https://aws.amazon.com/kms/pricing/
        type: Pricing
      - url: https://aws.amazon.com/kms/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/kms/resources/
        type: Resources
      - url: https://aws.amazon.com/kms/faqs/
        type: FAQ
    description: |-

      The Key Management Service (KMS) API is an encryption and key management
      web service that allows you to programmatically call various operations.
      KMS has replaced the term customer master key (CMK) with KMS key, but the
      concept remains the same. Amazon Web Services provides SDKs for various
      programming languages and platforms to create programmatic access to KMS. 
  - aid: amazon-web-services:aws-launch-wizard
    name: AWS Launch Wizard
    tags:
      - Deployments
      - Events
      - Patterns
      - Workloads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/launchwizard/
    overlays:
      - url: overlays/launch-wizard-openapi-search.yml
        type: APIs.io Search
      - url: overlays/launch-wizard-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/launchwizard/
        type: Documentation
      - url: openapi/launch-wizard-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/launchwizard/faq/
        type: FAQ
    description: |-

      Launch Wizard is a tool that simplifies the process of sizing,
      configuring, and deploying Amazon Web Services resources for third party
      applications, including Microsoft SQL Server Always On and HANA based SAP
      systems. This streamlined approach eliminates the need for manual
      identification and provisioning of individual AWS resources.
  - aid: amazon-web-services:amazon-lex-build-time-actions
    name: Amazon Lex Build-Time Actions
    tags:
      - ARN
      - Alias
      - Aliases
      - Associations
      - Bot Name
      - Bots
      - Built In
      - Channels
      - Exports
      - Import
      - Imports
      - Intent
      - Intents
      - Migrations
      - Names
      - Resources
      - Signatures
      - Slot Types
      - Slots
      - Tags
      - Types
      - Untag
      - Users
      - Utterances
      - Versions
      - View
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/lex/latest/dg/API_Operations.html
    overlays:
      - url: overlays/lex-models-openapi-search.yml
        type: APIs.io Search
      - url: overlays/lex-models-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/lex/latest/dg/API_Operations.html
        type: Documentation
      - url: openapi/lex-models-openapi-original.yml
        type: OpenAPI
    description: |-

      Build voice and text conversational interfaces with Amazon Lex API for
      AWS. These actions will allow you to easily create, update, and delete
      chatbots for both new and existing client applications.
  - aid: amazon-web-services:aws-license-manager
    name: AWS License Manager
    tags:
      - Services
      - Settings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/license-manager/
    overlays:
      - url: overlays/license-manager-openapi-search.yml
        type: APIs.io Search
      - url: overlays/license-manager-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/license-manager/
        type: Documentation
      - url: openapi/license-manager-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/license-manager/features/
        type: Features
      - url: https://aws.amazon.com/license-manager/pricing/
        type: Pricing
      - url: https://aws.amazon.com/license-manager/customers/
        type: Customers
      - url: https://aws.amazon.com/license-manager/resources/
        type: Resources
      - url: https://aws.amazon.com/license-manager/faqs/
        type: FAQ
    description: |-

      The License Manager API simplifies the management of software licenses for
      various vendors across numerous Amazon Web Services accounts and physical
      servers located on-premises.
  - aid: amazon-web-services:amazon-lightsail
    name: Amazon Lightsail
    tags:
      - Databases
      - Parameters
      - Relational
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/lightsail/
    overlays:
      - url: overlays/lightsail-openapi-search.yml
        type: APIs.io Search
      - url: overlays/lightsail-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/lightsail/
        type: Documentation
      - url: openapi/lightsail-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/lightsail/pricing/
        type: Pricing
      - url: https://aws.amazon.com/lightsail/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/lightsail/resources/
        type: Resources
      - url: https://aws.amazon.com/lightsail/faq/
        type: FAQ
      - url: https://aws.amazon.com/lightsail/customers/
        type: Customers
      - url: https://aws.amazon.com/lightsail/features/
        type: Features
      - url: https://aws.amazon.com/lightsail/research/
        type: Research
    description: |-

      The Amazon Lightsail API is a user-friendly platform that offers
      developers a simple way to leverage Amazon Web Services for building
      websites and web applications. It provides a wide range of essential
      features, including virtual private servers, container services, storage
      options, managed databases, and more, all at a cost-effective monthly
      rate. With the ability to manage resources through the Lightsail console,
      API, CLI, and SDKs, developers can easily launch and maintain their
      projects.
  - aid: amazon-web-services:amazon-lookout-for-equipment
    name: Amazon Lookout for Equipment
    tags:
      - Retraining
      - Scheduler
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/lookout-for-equipment/
    overlays:
      - url: overlays/lookoutequipment-openapi-search.yml
        type: APIs.io Search
      - url: overlays/lookoutequipment-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/lookout-for-equipment/
        type: Documentation
      - url: openapi/lookoutequipment-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/lookout-for-equipment/features/
        type: Features
      - url: https://aws.amazon.com/lookout-for-equipment/pricing/
        type: Pricing
      - url: https://aws.amazon.com/lookout-for-equipment/faqs/
        type: FAQ
      - url: https://aws.amazon.com/lookout-for-equipment/resources/
        type: Resources
      - url: https://aws.amazon.com/lookout-for-equipment/customers/
        type: Customers
      - url: https://aws.amazon.com/lookout-for-equipment/partners/
        type: Partners
    description: |-

      Amazon Lookout for Equipment is a machine learning service that uses
      advanced analytics to identify anomalies in machines from sensor data for
      use in predictive maintenance.
  - aid: amazon-web-services:aws-lake-formation
    name: AWS Lake Formation
    tags:
      - Assume
      - Batches
      - Cancel
      - Cells
      - Center
      - Commit
      - Configurations
      - Credentials
      - Data
      - Databases
      - Decorated
      - Deregister
      - Describe
      - Effective
      - Extend
      - Filter
      - Formation
      - Glue
      - Grants
      - Identity
      - LFTag
      - LFTags
      - Lakes
      - Lftag
      - Objects
      - 'On'
      - Opt
      - Optimizers
      - Partition
      - Paths
      - Permissions
      - Planning
      - Queries
      - Register
      - Removes
      - Resources
      - Results
      - Revoke
      - Roles
      - SAML
      - Saml
      - Search
      - Settings
      - States
      - Statistics
      - Storage
      - Tables
      - Temporary
      - Transactions
      - Units
      - Work
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/lake-formation/
    overlays:
      - url: overlays/lakeformation-openapi-search.yml
        type: APIs.io Search
      - url: overlays/lakeformation-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/lake-formation/
        type: Documentation
      - url: openapi/lakeformation-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/lake-formation/features/
        type: Features
      - url: https://aws.amazon.com/lake-formation/pricing/
        type: Pricing
      - url: https://aws.amazon.com/lake-formation/resources/
        type: Resources
      - url: https://aws.amazon.com/lake-formation/faqs/
        type: FAQ
    description: |-

      The AWS Lake Formation API streamlines data permissions management and
      facilitates seamless sharing within and outside your organization.
  - aid: amazon-web-services:amazon-cloudwatch-logs
    name: Amazon CloudWatch Logs
    tags:
      - Anomaly
      - Detectors
      - Logs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html
    overlays:
      - url: overlays/logs-openapi-search.yml
        type: APIs.io Search
      - url: overlays/logs-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html
        type: Documentation
      - url: openapi/logs-openapi-original.yml
        type: OpenAPI
    description: |-

      This API allows you to monitor, store, and access log files from EC2
      instances, CloudTrail, and other sources using Amazon CloudWatch Logs. You
      can retrieve log data through the CloudWatch console, AWS CLI, API, or
      SDK. 
  - aid: amazon-web-services:amazon-lookout-for-metrics
    name: Amazon Lookout for Metrics
    tags:
      - ARN
      - Activate
      - Alerts
      - Anomaly
      - Configurations
      - Data
      - Deactivate
      - Describe
      - Detect
      - Detections
      - Detectors
      - Executions
      - Feedback
      - Groups
      - Metrics
      - Quality
      - Related
      - Resources
      - Samples
      - Series
      - Sets
      - Summaries
      - Tags
      - Tests
      - Time
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/lookout-for-metrics/
    overlays:
      - url: overlays/lookoutmetrics-openapi-search.yml
        type: APIs.io Search
      - url: overlays/lookoutmetrics-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/lookout-for-metrics/
        type: Documentation
      - url: openapi/lookoutmetrics-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/lookout-for-metrics/features/
        type: Features
      - url: https://aws.amazon.com/lookout-for-metrics/pricing/
        type: Pricing
      - url: https://aws.amazon.com/lookout-for-metrics/resources/
        type: Resources
      - url: https://aws.amazon.com/lookout-for-metrics/faqs/
        type: FAQ
      - url: https://aws.amazon.com/lookout-for-metrics/customers/
        type: Customers
    description: |-

      Amazon Lookout for Metrics, leverages machine learning technology to
      identify and explain abnormal patterns in business and operational
      datasets.
  - aid: amazon-web-services:amazon-lookout-for-vision
    name: Amazon Lookout for Vision
    tags:
      - ARN
      - Anomalies
      - Datasets
      - Describe
      - Detect
      - Entries
      - Jobs
      - Model Packaging Jobs
      - Models
      - Names
      - Packaging
      - Projects
      - Resources
      - Stop
      - Tags
      - Types
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/lookout-for-vision/
    overlays:
      - url: overlays/lookoutvision-openapi-search.yml
        type: APIs.io Search
      - url: overlays/lookoutvision-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/lookout-for-vision/
        type: Documentation
      - url: openapi/lookoutvision-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/lookout-for-vision/features/
        type: Features
      - url: https://aws.amazon.com/lookout-for-vision/pricing/
        type: Pricing
      - url: https://aws.amazon.com/lookout-for-vision/faqs/
        type: FAQ
      - url: https://aws.amazon.com/lookout-for-vision/resources/
        type: Resources
      - url: https://aws.amazon.com/lookout-for-vision/partners/
        type: Partners
      - url: https://aws.amazon.com/lookout-for-vision/customers/
        type: Customers
    description: |-

      The Amazon Lookout for Vision API offers details on actions, data types,
      parameters, and errors. This API allows users to detect visual defects in
      various industrial products with precision and efficiency. By utilizing
      computer vision technology, it can identify missing parts in products,
      damages in vehicles or structures, inconsistencies in manufacturing lines,
      and even tiny imperfections in items like silicon wafers or printed
      circuit boards. Lookout for Vision is a powerful tool for ensuring quality
      in production processes.
  - aid: amazon-web-services:amazon-machine-learning
    name: Amazon Machine Learning
    tags:
      - Machine Learning
      - Model
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ai/machine-learning/
    overlays:
      - url: overlays/machinelearning-openapi-search.yml
        type: APIs.io Search
      - url: overlays/machinelearning-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ai/machine-learning/
        type: Documentation
      - url: openapi/machinelearning-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ai/infrastructure/
        type: Infrastructure
      - url: https://aws.amazon.com/machine-learning/learn/
        type: Learn
      - url: https://aws.amazon.com/ai/resources/
        type: Resources
      - url: https://aws.amazon.com/machine-learning/ai-use-cases/
        type: Use Cases
      - url: https://aws.amazon.com/machine-learning/partner-solutions/
        type: Partners
    description: |-

      Amazon Machine Learning allows users to leverage machine learning
      capabilities at scale, offering a wide range of services, infrastructure,
      and deployment resources. Trusted by over 100,000 customers, from major
      corporations to new businesses, AWS machine learning services are used to
      tackle business challenges and foster innovation. 
  - aid: amazon-web-services:amazon-macie
    name: Amazon Macie
    tags:
      - ARN
      - Accept
      - Accounts
      - Administrative
      - Administrator
      - Allow
      - Artifacts
      - Automated
      - Availability
      - Batches
      - Buckets
      - Buckets
      - Classifications
      - Configurations
      - Count
      - Custom
      - Data
      - Data Source
      - Decline
      - Describe
      - Detections
      - Disassociate
      - Discovery
      - Entifiers
      - Exports
      - Filter
      - Filters
      - Findings
      - Findings Filter
      - Inspections
      - Invitation
      - Invitations
      - Jobs
      - Managed
      - Master
      - Members
      - Occurrences
      - Organizations
      - Profiles
      - Publication
      - Resources
      - Reveal
      - Samples
      - Scopes
      - Search
      - Sensitive
      - Sensitivity
      - Sessions
      - Statistics
      - Tags
      - Templates
      - Tests
      - Totals
      - Untag
      - Usage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/macie/
    overlays:
      - url: overlays/macie2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/macie2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/macie/
        type: Documentation
      - url: openapi/macie2-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/macie/features/
        type: Features
      - url: https://aws.amazon.com/macie/pricing/
        type: Pricing
      - url: https://aws.amazon.com/macie/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/macie/faq/
        type: FAQ
      - url: https://aws.amazon.com/macie/resources/
        type: Resources
    description: |-

      Amazon Macie is a fully managed data security and data privacy service
      that uses machine learning and pattern matching to help you discover and
      protect your sensitive data in AWS. Macie automates the discovery of
      sensitive data, such as PII and intellectual property, to provide you with
      insight into the data that your organization stores in AWS. 
  - aid: amazon-web-services:aws-mainframe-modernization
    name: AWS Mainframe Modernization
    tags:
      - ARN
      - Applications
      - Batches
      - Cancel
      - Data
      - Datasets
      - Definitions
      - Deployments
      - Details
      - Engines
      - Environments
      - Execution
      - Executions
      - History
      - Import
      - Jobs
      - Names
      - Resources
      - Sets
      - Signed
      - Stop
      - Tags
      - Tasks
      - URL
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/mainframe-modernization/
    overlays:
      - url: overlays/m2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/m2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/mainframe-modernization/
        type: Documentation
      - url: openapi/m2-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/mainframe-modernization/features/
        type: Features
      - url: https://aws.amazon.com/mainframe-modernization/pricing/
        type: Pricing
      - url: https://aws.amazon.com/mainframe-modernization/resources/
        type: Resources
      - url: https://aws.amazon.com/mainframe-modernization/faqs/
        type: FAQ
    description: |-

      The Amazon Web Services Mainframe Modernization API offers a comprehensive
      suite of tools and support for seamlessly transitioning from mainframes to
      AWS managed runtime environments. It includes features for examining
      current mainframe applications, creating or enhancing applications with
      COBOL or PL/I, and setting up a streamlined automated process for
      continuous integration and delivery of the applications.
  - aid: amazon-web-services:aws-location
    name: AWS Location
    tags:
      - ARN
      - Associate
      - Batches
      - Calculate
      - Calculators
      - Collections
      - Consumer
      - Consumers
      - Descriptions
      - Device
      - Devices
      - Disassociate
      - Evaluate
      - File
      - Fonts
      - Geofences
      - Geofencing
      - Glyphs
      - History
      - Index
      - Indexes
      - Keys
      - Latest
      - Maps
      - Matrix
      - Metadata
      - Names
      - Places
      - Positions
      - Ranges
      - Resources
      - Routes
      - Search
      - Sprites
      - Stack
      - Styles
      - Suggestions
      - Tags
      - Text
      - Tiles
      - Trackers
      - Tracking
      - Unicode
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/location/
    overlays:
      - url: overlays/location-openapi-search.yml
        type: APIs.io Search
      - url: overlays/location-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/location/
        type: Documentation
      - url: openapi/location-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/location/features/
        type: Features
      - url: https://aws.amazon.com/location/pricing/
        type: Pricing
      - url: https://aws.amazon.com/location/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/location/faqs/
        type: FAQ
      - url: https://aws.amazon.com/location/customers/
        type: Customers
      - url: https://aws.amazon.com/location/data-providers/
        type: Data-providers
    description: |-

      Amazon Location Service makes it easy for developers to add location
      functionality, such as maps, points of interest, geocoding, routing,
      tracking, and geofencing, to their applications without sacrificing data
      security and user privacy.
  - aid: amazon-web-services:aws-marketplace-catalog
    name: AWS Marketplace Catalog
    tags:
      - Batches
      - Cancel
      - Change
      - Describe
      - Entities
      - Policies
      - Resources
      - Sets
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html
    overlays:
      - url: overlays/marketplace-catalog-openapi-search.yml
        type: APIs.io Search
      - url: overlays/marketplace-catalog-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html
        type: Documentation
      - url: openapi/marketplace-catalog-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS Marketplace Catalog API enables users to interact with their
      entities, such as products or offers on AWS Marketplace, by providing
      functionality for listing, describing, and updating them. By integrating
      the AWS Marketplace Catalog API with product build or deployment
      pipelines, users can streamline the process of updating entities. 
  - aid: amazon-web-services:amazon-managed-blockchain-amb
    name: Amazon Managed Blockchain (AMB)
    tags:
      - Assets
      - Balance
      - Balances
      - Batches
      - Blockchain
      - Contracts
      - Events
      - Tokens
      - Transactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/managed-blockchain/
    overlays:
      - url: overlays/managedblockchain-query-openapi-search.yml
        type: APIs.io Search
      - url: overlays/managedblockchain-query-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/managed-blockchain/
        type: Documentation
      - url: openapi/managedblockchain-query-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/managed-blockchain/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/managed-blockchain/pricing/
        type: Pricing
      - url: https://aws.amazon.com/managed-blockchain/resources/
        type: Resources
      - url: https://aws.amazon.com/managed-blockchain/faqs/
        type: FAQ
    description: |-

      The Amazon Managed Blockchain (AMB) Query API allows users to easily
      access multi-blockchain network data, enabling them to extract relevant
      information regarding blockchain activity. This API allows users to read
      data from public blockchain networks like Bitcoin Mainnet and Ethereum
      Mainnet, providing details such as current and historical balances of
      addresses, as well as a list of blockchain transactions within a specified
      time frame. Users can also retrieve specific transaction details,
      including transaction events, which can be further analyzed or
      incorporated into business logic for various applications.
  - aid: amazon-web-services:aws-marketplace-deployment
    name: AWS Marketplace Deployment
    tags:
      - ARN
      - Resources
      - Tags
      - Untag
      - Catalog
      - Catalogs
      - Deployments
      - Parameters
      - Products
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/welcome.html
    overlays:
      - url: overlays/marketplace-deployment-openapi-search.yml
        type: APIs.io Search
      - url: overlays/marketplace-deployment-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/welcome.html
        type: Documentation
      - url: openapi/marketplace-deployment-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS Marketplace Deployment Service supports the Quick Launch
      experience, which is a deployment option for software as a service (SaaS)
      products. Quick Launch simplifies and reduces the time, resources, and
      steps required to configure, deploy, and launch a products. The AWS
      Marketplace Deployment Service provides sellers with a secure method for
      passing deployment parameters (for example, API keys and external IDs) to
      buyers during the Quick Launch experience.
  - aid: amazon-web-services:aws-elemental-mediaconnect
    name: AWS Elemental MediaConnect
    tags:
      - ARN
      - Bridges
      - Describe
      - Entitlements
      - Flows
      - Gateways
      - Grants
      - Instances
      - Interfaces
      - Media
      - Metadata
      - Names
      - Offerings
      - Output
      - Outputs
      - Purchase
      - Removes
      - Reservations
      - Resources
      - Sources
      - States
      - Stop
      - Stream
      - Streams
      - Tags
      - Untag
      - VPC
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/mediaconnect/
    overlays:
      - url: overlays/mediaconnect-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mediaconnect-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/mediaconnect/
        type: Documentation
      - url: openapi/mediaconnect-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/mediaconnect/pricing/
        type: Pricing
      - url: https://aws.amazon.com/mediaconnect/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/mediaconnect/faqs/
        type: FAQ
      - url: https://aws.amazon.com/mediaconnect/ready/
        type: Ready
      - url: https://aws.amazon.com/mediaconnect/features/
        type: Features
    description: |-

      AWS Elemental MediaConnect is an advanced live video transport service
      that combines the reliability and security of satellite and fiber-optic
      technology with the flexibility, agility, and cost-effectiveness of
      IP-based networks.
  - aid: amazon-web-services:aws-elemental-mediaconvert
    name: AWS Elemental MediaConvert
    tags:
      - ARN
      - Associate
      - Certificates
      - Describe
      - Disassociate
      - Endpoints
      - Jobs
      - Names
      - Policies
      - Presets
      - Queues
      - Resources
      - Tags
      - Templates
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/mediaconvert/
    overlays:
      - url: overlays/mediaconvert-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mediaconvert-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/mediaconvert/
        type: Documentation
      - url: openapi/mediaconvert-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/mediaconvert/features/
        type: Features
      - url: https://aws.amazon.com/mediaconvert/pricing/
        type: Pricing
      - url: https://aws.amazon.com/mediaconvert/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/mediaconvert/resources/
        type: Resources
      - url: https://aws.amazon.com/mediaconvert/faqs/
        type: FAQ
    description: |-

      AWS Elemental MediaConvert is a high-quality video transcoding service
      designed for creating live stream content for broadcast and multi-screen
      delivery on a large scale.
  - aid: amazon-web-services:aws-elemental-medialive
    name: AWS Elemental MediaLive
    tags:
      - ARN
      - Accept
      - Accounts
      - Batches
      - Cancel
      - Channels
      - Claim
      - Classes
      - Configurations
      - Data
      - Describe
      - Device
      - Devices
      - Groups
      - Inputs
      - Maintenance
      - Multiplex
      - Multiplexes
      - Names
      - Offerings
      - Partners
      - Program
      - Programs
      - Purchase
      - Reboot
      - Reject
      - Reservations
      - Resources
      - Schedules
      - Security
      - Stop
      - Tags
      - Thumbnails
      - Transfers
      - Window
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/medialive/
    overlays:
      - url: overlays/medialive-openapi-search.yml
        type: APIs.io Search
      - url: overlays/medialive-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/medialive/
        type: Documentation
      - url: openapi/medialive-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/medialive/pricing/
        type: Pricing
      - url: https://aws.amazon.com/medialive/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/medialive/resources/
        type: Resources
      - url: https://aws.amazon.com/medialive/faqs/
        type: FAQ
      - url: https://aws.amazon.com/medialive/features/
        type: Features
    description: |-

      AWS Elemental MediaLive is a professional live video processing service
      designed to produce high-quality streams for distribution to both
      broadcast televisions and internet-connected devices.
  - aid: amazon-web-services:aws-marketplace-agreement
    name: AWS Marketplace Agreement
    tags:
      - Agreements
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/marketplace-agreements/latest/api-reference/welcome.html
    overlays:
      - url: overlays/marketplace-agreement-openapi-search.yml
        type: APIs.io Search
      - url: overlays/marketplace-agreement-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/marketplace-agreements/latest/api-reference/welcome.html
        type: Documentation
      - url: openapi/marketplace-agreement-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS Marketplace API enables sellers to manage product-related
      agreements, including listing, searching, and filtering agreements. To use
      this API, sellers must ensure that their AWS IAM policies and roles are
      properly configured. Users must have the necessary permissions to carry
      out actions such as describing agreements, getting agreement terms, and
      searching through all agreements.
  - aid: amazon-web-services:aws-marketplace
    name: AWS Marketplace
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/mediastore/
    overlays:
      - url: overlays/mediastore-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mediastore-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/mediastore/
        type: Documentation
      - url: openapi/mediastore-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/mediastore/features/
        type: Features
      - url: https://aws.amazon.com/mediastore/pricing/
        type: Pricing
      - url: https://aws.amazon.com/mediastore/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/mediastore/resources/
        type: Resources
      - url: https://aws.amazon.com/mediastore/faqs/
        type: FAQ
    description: |-

      The AWS Elemental MediaStore API is designed to provide high-performance
      storage specifically tailored for media content, offering reliable
      consistency and minimal latency to support the seamless delivery of live
      streaming video content.
  - aid: amazon-web-services:aws-marketplace-commerce-analytics-service
    name: AWS Marketplace Commerce Analytics Service
    tags:
      - Data
      - Exports
      - Support
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/marketplace/latest/userguide/commerce-analytics-service.html
    overlays:
      - url: overlays/marketplacecommerceanalytics-openapi-search.yml
        type: APIs.io Search
      - url: >-

          overlays/marketplacecommerceanalytics-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/marketplace/latest/userguide/commerce-analytics-service.html
        type: Documentation
      - url: openapi/marketplacecommerceanalytics-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS Marketplace Commerce Analytics Service allows you to access
      product and customer data from AWS Marketplace through a programmable
      interface. Upon signing up for the service, you can retrieve usage,
      subscription, and billing reports using the AWS SDK.
  - aid: amazon-web-services:aws-marketplace-metering-service
    name: AWS Marketplace Metering Service
    tags:
      - Customers
      - Resolve
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/marketplace/
    overlays:
      - url: overlays/meteringmarketplace-openapi-search.yml
        type: APIs.io Search
      - url: overlays/meteringmarketplace-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/marketplace/
        type: Documentation
      - url: openapi/meteringmarketplace-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/marketplace/latest/userguide/index.html
        type: Seller Guide
      - url: https://docs.aws.amazon.com/marketplace/latest/buyerguide/index.html
        type: Buyer Guide
    description: |-

      The AWS Marketplace Metering Service API allows AWS Marketplace sellers to
      submit usage data for custom usage dimensions. This reference provides
      detailed descriptions of the low-level API functions available for use.
  - aid: amazon-web-services:aws-application-migration-service
    name: AWS Application Migration Service
    tags:
      - ARN
      - Accounts
      - Actions
      - Applications
      - Archive
      - Archived
      - Associate
      - Change
      - Clients
      - Configurations
      - Connectors
      - Cycle
      - Data
      - Describe
      - Disassociate
      - Disconnect
      - Errors
      - Exports
      - Finalize
      - Import
      - Imports
      - Initialize
      - Instances
      - Items
      - Jobs
      - Launch
      - Life
      - Logs
      - Managed
      - Mark
      - Pause
      - Removes
      - Replication
      - Resources
      - Resume
      - Retry
      - Servers
      - Services
      - Sources
      - States
      - Stop
      - Tags
      - Targets
      - Templates
      - Terminate
      - Tests
      - Types
      - Unarchive
      - Untag
      - Waves
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/application-migration-service/
    overlays:
      - url: overlays/mgn-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mgn-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/application-migration-service/
        type: Documentation
      - url: openapi/mgn-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/application-migration-service/pricing/
        type: Pricing
      - url: https://aws.amazon.com/application-migration-service/faqs/
        type: FAQ
      - url: https://aws.amazon.com/application-migration-service/resources/
        type: Resources
      - url: https://aws.amazon.com/application-migration-service/windows/
        type: Windows
    description: |-

      The AWS Application Migration Service streamlines the migration of your
      source servers to run directly on AWS, reducing the need for manual
      processes that are time-consuming and prone to errors. It also offers
      convenient optimization options for modernizing your applications, both
      through pre-built configurations and custom settings.
  - aid: amazon-web-services:aws-healthimaging
    name: AWS Health Imaging
    tags:
      - ARN
      - Copy
      - Data Store
      - Frames
      - Images
      - Jobs
      - Metadata
      - Resources
      - Search
      - Sets
      - Sources
      - Tags
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/healthimaging/
    properties:
      - url: https://example.com
        type: Documentation
      - url: openapi/medical-imaging-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/healthimaging/features/
        type: Features
      - url: https://aws.amazon.com/healthimaging/pricing/
        type: Pricing
      - url: https://aws.amazon.com/healthimaging/faqs/
        type: FAQ
      - url: https://aws.amazon.com/healthimaging/customers/
        type: Customers
      - url: https://aws.amazon.com/healthimaging/resources/
        type: Resources
    description: |-

      The AWS HealthImaging API is a secure service that meets HIPAA compliance
      standards. It is specifically built to help healthcare providers and their
      medical imaging ISV partners effectively store, manipulate, and utilize
      machine learning techniques on medical images.
  - aid: amazon-web-services:amazon-web-services-migration-hub-refactor-spaces
    name: Amazon Web Services Migration Hub Refactor Spaces
    tags:
      - ARN
      - Applications
      - Environments
      - Policies
      - Resource Policies
      - Resources
      - Routes
      - Services
      - Tags
      - Untag
      - VPC
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/what-is-mhub-refactor-spaces.html
    overlays:
      - url: overlays/migration-hub-refactor-spaces-openapi-search.yml
        type: APIs.io Search
      - url: >-

          overlays/migration-hub-refactor-spaces-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/what-is-mhub-refactor-spaces.html
        type: Documentation
      - url: openapi/migration-hub-refactor-spaces-openapi-original.yml
        type: OpenAPI
    description: |-

      Refactor Spaces within AWS Migration Hub serves as a comprehensive
      solution for gradually refactoring applications into microservices within
      the AWS ecosystem. By leveraging Refactor Spaces, users can seamlessly
      transition from monolithic to microservices architecture, minimizing the
      manual effort involved in setting up and managing AWS infrastructure. 
  - aid: amazon-web-services:aws-memorydb
    name: AWS MemoryDB
    tags:
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/memorydb/
    overlays:
      - url: overlays/memorydb-openapi-search.yml
        type: APIs.io Search
      - url: overlays/memorydb-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/memorydb/
        type: Documentation
      - url: openapi/memorydb-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/memorydb/features/
        type: Features
      - url: https://aws.amazon.com/memorydb/pricing/
        type: Pricing
      - url: https://aws.amazon.com/memorydb/resources/
        type: Resources
      - url: https://aws.amazon.com/memorydb/faqs/
        type: FAQ
      - url: https://aws.amazon.com/memorydb/sla/
        type: Sla
    description: |-

      MemoryDB for Redis is a managed in-memory database that offers fast
      performance and Multi-AZ durability for microservices applications. It
      stores the entire database in-memory for low latency and high throughput
      access. Compatible with Redis, it supports Redis' data structures, APIs,
      and commands.
  - aid: amazon-web-services:migration-hub-strategy-recommendations
    name: Migration Hub Strategy Recommendations
    tags:
      - Analyzable
      - Application Components
      - Applications
      - Assessments
      - Collectors
      - Components
      - Configurations
      - Details
      - File
      - Generation
      - Import
      - Latest
      - Portfolio
      - Preferences
      - Recommendations
      - Reports
      - Servers
      - Stop
      - Strategies
      - Summaries
      - Tasks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/migrationhub/
    overlays:
      - url: overlays/migrationhubstrategy-openapi-search.yml
        type: APIs.io Search
      - url: overlays/migrationhubstrategy-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/migrationhub/
        type: Documentation
      - url: openapi/migrationhubstrategy-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS Migration Hub offers a centralized platform for monitoring migration
      tasks from various AWS tools and partner solutions. Through Migration Hub,
      users can select the migration tools that align with their requirements
      and gain insight into the progress of their migration projects.
      Additionally, Migration Hub delivers essential metrics and progress
      updates for specific applications, regardless of the tools employed for
      their migration.
  - aid: amazon-web-services:aws-migration-hub-orchestrator
    name: AWS Migration Hub Orchestrator.
    tags:
      - ARN
      - Groups
      - Migration Workflow Templates
      - Migration Workflows
      - Plugins
      - Resources
      - Retry
      - Retry Workflow Steps
      - Step Groups
      - Steps
      - Stop
      - Tags
      - Template Steps
      - Templates
      - Templatestepgroups
      - Untag
      - Workflow Step
      - Workflow Step Group
      - Workflow Step Groups
      - Workflow Steps
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.html
    overlays:
      - url: overlays/migrationhuborchestrator-openapi-search.yml
        type: APIs.io Search
      - url: overlays/migrationhuborchestrator-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.html
        type: Documentation
      - url: openapi/migrationhuborchestrator-openapi-original.yml
        type: OpenAPI
    description: |-

      This API reference provides descriptions, syntax, and other details about
      each of the actions and data types for AWS Migration Hub Orchestrator. he
      topic for each action shows the API request parameters and the response.
      Alternatively, you can use one of the AWS SDKs to access an API that is
      tailored to the programming language or platform that you're using.
  - aid: amazon-web-services:aws-elemental-mediatailor
    name: AWS Elemental MediaTailor
    tags:
      - ARN
      - Alerts
      - Channels
      - Configurations
      - Configure
      - Live
      - Locations
      - Logs
      - Names
      - Playback
      - Policies
      - Prefetch
      - Program
      - Resources
      - Schedules
      - Sources
      - Stop
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/mediatailor/
    overlays:
      - url: overlays/mediatailor-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mediatailor-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/mediatailor/
        type: Documentation
      - url: openapi/mediatailor-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/mediatailor/features/
        type: Features
      - url: https://aws.amazon.com/mediatailor/pricing/
        type: Pricing
      - url: https://aws.amazon.com/mediatailor/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/mediatailor/faqs/
        type: FAQ
      - url: https://aws.amazon.com/mediatailor/resources/
        type: Resources
      - url: https://aws.amazon.com/mediatailor/integrations/
        type: Integrations
    description: |-

      AWS Elemental MediaTailor is a versatile platform designed for video
      providers to easily create customized linear over-the-top (OTT) channels
      by leveraging their existing video content. With this service, users can
      seamlessly monetize their channels and live streams through personalized
      ad insertion, enhancing the overall viewing experience for audiences.
  - aid: amazon-web-services:amazon-mechanical-turk
    name: Amazon Mechanical Turk
    tags:
      - Qualification
      - Types
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://www.mturk.com/
    overlays:
      - url: overlays/mturk-requester-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mturk-requester-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://www.mturk.com/
        type: Documentation
      - url: openapi/mturk-requester-openapi-original.yml
        type: OpenAPI
      - url: https://www.mturk.com/worker
        type: Worker
      - url: https://www.mturk.com/product-details
        type: Product
      - url: https://www.mturk.com/pricing
        type: Pricing
      - url: https://www.mturk.com/help
        type: Help
      - url: https://www.mturk.com/resources
        type: Resources
      - url: https://www.mturk.com/customers
        type: Customers
    description: |-

      This API, Amazon Mechanical Turk (MTurk), offers a platform for
      individuals and businesses to easily outsource tasks to a distributed
      workforce. These tasks can range from data validation and research to more
      subjective tasks like survey participation and content moderation. MTurk
      allows companies to leverage a global workforce to streamline processes,
      improve data collection and analysis, and enhance machine learning
      projects.
  - aid: amazon-web-services:amazon-cloudwatch
    name: Amazon CloudWatch
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloudwatch/
    overlays:
      - url: overlays/monitoring-openapi-search.yml
        type: APIs.io Search
      - url: overlays/monitoring-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloudwatch/
        type: Documentation
      - url: openapi/monitoring-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloudwatch/features/
        type: Features
      - url: https://aws.amazon.com/cloudwatch/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloudwatch/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/cloudwatch/faqs/
        type: FAQ
      - url: https://aws.amazon.com/cloudwatch/customers/
        type: Customers
    description: |+

      Amazon CloudWatch is a service that monitors applications, responds to
      performance changes, optimizes resource use, and provides insights into
      operational health. By collecting data across AWS resources, CloudWatch
      gives visibility into system-wide performance and allows users to set
      alarms, automatically react to changes, and gain a unified view of
      operational health.



  - aid: amazon-web-services:amazon-managed-workflows-for-apache-airflow
    name: Amazon Managed Workflows for Apache Airflow
    tags:
      - ARN
      - CLI
      - Environments
      - Login
      - Metrics
      - Names
      - Publish
      - Resources
      - Tags
      - Tokens
      - Untag
      - Web
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/managed-workflows-for-apache-airflow/
    overlays:
      - url: overlays/mwaa-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mwaa-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/managed-workflows-for-apache-airflow/
        type: Documentation
      - url: openapi/mwaa-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/managed-workflows-for-apache-airflow/features/
        type: Features
      - url: https://aws.amazon.com/managed-workflows-for-apache-airflow/pricing/
        type: Pricing
      - url: >-

          https://aws.amazon.com/managed-workflows-for-apache-airflow/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/managed-workflows-for-apache-airflow/resources/
        type: Resources
      - url: https://aws.amazon.com/managed-workflows-for-apache-airflow/faqs/
        type: FAQ
    description: |-

      Amazon Managed Workflows for Apache Airflow (Amazon MWAA) is a service
      that helps you organize and automate your tasks by utilizing Directed
      Acyclic Graphs (DAGs) written in Python. Your DAGs, plugins, and Python
      requirements are stored in an Amazon Simple Storage Service (S3) bucket
      provided by you. 
  - aid: amazon-web-services:amazon-neptune
    name: Amazon Neptune
    tags:
      - DBCluster
      - Stop
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/neptune/
    overlays:
      - url: overlays/neptune-openapi-search.yml
        type: APIs.io Search
      - url: overlays/neptune-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/neptune/
        type: Documentation
      - url: openapi/neptune-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/neptune/pricing/
        type: Pricing
      - url: https://aws.amazon.com/neptune/faqs/
        type: FAQ
      - url: https://aws.amazon.com/neptune/features/
        type: Features
      - url: https://aws.amazon.com/neptune/global-database/
        type: Global-database
      - url: https://aws.amazon.com/neptune/machine-learning/
        type: Machine-learning
      - url: https://aws.amazon.com/neptune/serverless/
        type: Serverless
      - url: https://aws.amazon.com/neptune/getting-started/
        type: Getting-started
    description: |-

      Amazon Neptune Amazon Neptune is a fast, reliable, fully-managed graph
      database service that makes it easy to build and run applications that
      work with highly connected datasets. The core of Amazon Neptune is a
      purpose-built, high-performance graph database engine optimized for
      storing billions of relationships and querying the graph with milliseconds
      latency.
  - aid: amazon-web-services:amazon-mq
    name: Amazon MQ
    tags:
      - Brokers
      - ActiveMQ
      - RabbitMQ
      - Real-Time
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/amazon-mq/
    overlays:
      - url: overlays/mq-openapi-search.yml
        type: APIs.io Search
      - url: overlays/mq-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/amazon-mq/
        type: Documentation
      - url: openapi/mq-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/amazon-mq/features/
        type: Features
      - url: https://aws.amazon.com/amazon-mq/pricing/
        type: Pricing
      - url: https://aws.amazon.com/amazon-mq/resources/
        type: Resources
      - url: https://aws.amazon.com/amazon-mq/faqs/
        type: FAQ
      - url: https://aws.amazon.com/amazon-mq/customers/
        type: Customers
    description: |-

      Amazon MQ is an API service that manages message brokers for Apache
      ActiveMQ and RabbitMQ, simplifying the setup and operation of message
      brokers in the cloud. Message brokers enable communication between
      software applications and components, supporting multiple programming
      languages, operating systems, and messaging protocols.
  - aid: amazon-web-services:neptune-analytics
    name: Neptune Analytics
    tags:
      - ARN
      - Endpoints
      - Graphs
      - Import
      - Import Tasks
      - Private
      - Queries
      - Resources
      - Restore
      - Snapshots
      - Summaries
      - Tags
      - Tasks
      - Untag
      - VPC
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html
    overlays:
      - url: overlays/neptune-graph-openapi-search.yml
        type: APIs.io Search
      - url: overlays/neptune-graph-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html
        type: Documentation
      - url: openapi/neptune-graph-openapi-original.yml
        type: OpenAPI
    description: |-

      Neptune Analytics is a cutting-edge analytics database engine designed for
      Amazon Neptune, enabling users to efficiently analyze vast amounts of
      graph data. By leveraging high-speed processing capabilities and executing
      popular graph analytic algorithms through rapid queries, Neptune Analytics
      greatly accelerates the insights generation process, delivering analytics
      results within seconds.
  - aid: amazon-web-services:amazon-nimble-studio
    name: Amazon Nimble Studio
    tags:
      - ARN
      - Acceptances
      - Backup
      - Backups
      - Components
      - Configurations
      - Details
      - EULA
      - Eulas
      - Images
      - Initialization
      - Initialize
      - Launch
      - Members
      - Memberships
      - Principals
      - Profiles
      - Repair
      - Resources
      - SSO
      - SSOConfiguration
      - Sessions
      - Stop
      - Stream
      - Streaming
      - Streams
      - Studios
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/nimble-studio/
    overlays:
      - url: overlays/nimble-openapi-search.yml
        type: APIs.io Search
      - url: overlays/nimble-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/nimble-studio/
        type: Documentation
      - url: openapi/nimble-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/nimble-studio/features/
        type: Features
      - url: https://aws.amazon.com/nimble-studio/pricing/
        type: Pricing
      - url: https://aws.amazon.com/nimble-studio/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/nimble-studio/faqs/
        type: FAQ
    description: |-

      Thank you for visiting the Amazon Nimble Studio API documentation. This
      comprehensive reference guide offers detailed information on methods,
      schema, resources, and parameters to maximize your utilization of Nimble
      Studio. Nimble Studio is a cutting-edge virtual studio designed to support
      visual effects, animation, and interactive content teams, enabling them to
      create securely within a flexible, private cloud environment.
  - aid: amazon-web-services:amazon-cloudwatch-network-monitor
    name: Amazon CloudWatch Network Monitor
    tags:
      - ARN
      - Monitors
      - Names
      - Probes
      - Resources
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-
      https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html
    properties:
      - url: >-
          https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html
        type: Documentation
      - url: openapi/networkmonitor-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon CloudWatch Network Monitor is an active network monitoring service
      provided by Amazon Web Services. It is designed to identify network issues
      within either the AWS network or your own company's network. With Network
      Monitor, users can select source VPCs and subnets from AWS and specify
      destination IP addresses from their own on-premises network. 
  - aid: amazon-web-services:aws-healthomics
    name: AWS HealthOmics
    tags:
      - ARN
      - Abort
      - Activation
      - Activation Jobs
      - Annotations
      - Batches
      - Cancel
      - Complete
      - Export Jobs
      - Exports
      - Groups
      - Import
      - Import JObs
      - Import Jobs
      - Jobs
      - Metadata
      - Multipart
      - Names
      - Parts
      - Read
      - Readsets
      - Reference Store
      - References
      - Resources
      - Runs
      - Sequence
      - Sequence Stores
      - Sets
      - Share
      - Shares
      - Store
      - Stores
      - Tags
      - Tasks
      - Untag
      - Uploads
      - Variants
      - Versions
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/healthomics/
    overlays:
      - url: overlays/omics-openapi-search.yml
        type: APIs.io Search
      - url: overlays/omics-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/healthomics/
        type: Documentation
      - url: openapi/omics-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/healthomics/features/
        type: Features
      - url: https://aws.amazon.com/healthomics/pricing/
        type: Pricing
      - url: https://aws.amazon.com/healthomics/resources/
        type: Resources
      - url: https://aws.amazon.com/healthomics/faqs/
        type: FAQ
      - url: https://aws.amazon.com/healthomics/customers/
        type: Customers
    description: |-

      AWS HealthOmics is a specialized platform designed to assist healthcare
      and life science organizations, as well as their software partners, in
      storing, retrieving, and analyzing various omics data including genomic
      and transcriptomic data. By leveraging this service, users can extract
      valuable insights from the data to enhance health outcomes. The platform
      also enables large-scale analysis and facilitates collaborative research
      efforts.
  - aid: amazon-web-services:amazon-cloudwatch-observability-access-manager
    name: Amazon CloudWatch Observability Access Manager
    tags:
      - ARN
      - Attached
      - Link
      - Links
      - Policies
      - Resources
      - Sink
      - Sinks
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/OAM/latest/APIReference/Welcome.html
    overlays:
      - url: overlays/oam-openapi-search.yml
        type: APIs.io Search
      - url: overlays/oam-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://example.com
        type: Documentation
      - url: openapi/oam-openapi-original.yml
        type: OpenAPI
    description: |-

      Use Amazon CloudWatch Observability Access Manager to establish and manage
      connections between source accounts and monitoring accounts for CloudWatch
      cross-account observability. This feature allows you to effectively
      monitor and troubleshoot applications that span across multiple accounts
      within a specific region. With CloudWatch cross-account observability, you
      can seamlessly search, visualize, and analyze metrics, logs, traces, and
      Application Insights applications from linked accounts without any account
      limitations. 
  - aid: amazon-web-services:aws-network-firewall
    name: AWS Network Firewall
    tags:
      - Configurations
      - TLSInspection
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/network-firewall/
    properties:
      - url: https://aws.amazon.com/network-firewall/
        type: Documentation
      - url: openapi/network-firewall-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/network-firewall/features/
        type: Features
      - url: https://aws.amazon.com/network-firewall/pricing/
        type: Pricing
      - url: https://aws.amazon.com/network-firewall/resources/
        type: Resources
      - url: https://aws.amazon.com/network-firewall/faqs/
        type: FAQ
      - url: https://aws.amazon.com/network-firewall/partners/
        type: Partners
      - url: https://aws.amazon.com/network-firewall/customers/
        type: Customers
    description: |-

      Utilize AWS Network Firewall to establish customized firewall rules that
      offer precise management of network traffic and seamlessly implement
      firewall security measures across your VPCs.
  - aid: amazon-web-services:amazon-opensearch-serverless
    name: Amazon OpenSearch Serverless
    tags:
      - Endpoints
      - VPC
      - Search
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/opensearch-service/features/serverless/
    overlays:
      - url: overlays/opensearchserverless-openapi-search.yml
        type: APIs.io Search
      - url: overlays/opensearchserverless-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/opensearch-service/features/serverless/
        type: Documentation
      - url: openapi/opensearchserverless-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/opensearch-service/features/
        type: Features
      - url: https://aws.amazon.com/opensearch-service/pricing/
        type: Pricing
      - url: https://aws.amazon.com/opensearch-service/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/opensearch-service/resources/
        type: Resources
      - url: https://aws.amazon.com/opensearch-service/customers/
        type: Customers
      - url: https://aws.amazon.com/big-data/datalakes-and-analytics/migrations/
        type: Migrations
      - url: >-

          https://aws.amazon.com/big-data/datalakes-and-analytics/partner-solutions/
        type: Partners
      - url: https://aws.amazon.com/big-data/datalakes-and-analytics/customers/
        type: Customers
    description: |-

      Use the Amazon OpenSearch Serverless API to create, configure, and manage
      OpenSearch Serverless collections and security policies. OpenSearch
      Serverless is an on-demand, pre-provisioned serverless configuration for
      Amazon OpenSearch Service. OpenSearch Serverless removes the operational
      complexities of provisioning, configuring, and tuning your OpenSearch
      clusters. 
  - aid: amazon-web-services:amazon-opensearch-service
    name: Amazon OpenSearch Service
    tags:
      - Accept
      - Access
      - Actions
      - Associate
      - Authorize
      - Auto
      - Cancel
      - Change
      - Compatible
      - Configurations
      - Connections
      - Data
      - Describe
      - Details
      - Dissociate
      - Domains
      - Dry
      - Endpoints
      - Engines
      - Health
      - History
      - Inbound
      - Info
      - Instances
      - Limits
      - Maintenance
      - Maintenances
      - Names
      - Nodes
      - Offerings
      - Open Search
      - Outbound
      - Packages
      - Progress
      - Purchase
      - Reject
      - Removal
      - Removes
      - Reserved
      - Revoke
      - Runs
      - Scheduled
      - Search
      - Services
      - Software
      - Sources
      - Status
      - Tags
      - Tunes
      - Types
      - Upgrade
      - VPC
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/opensearch-service/
    overlays:
      - url: overlays/opensearch-openapi-search.yml
        type: APIs.io Search
      - url: overlays/opensearch-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/opensearch-service/
        type: Documentation
      - url: openapi/opensearch-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/opensearch-service/pricing/
        type: Pricing
      - url: https://aws.amazon.com/opensearch-service/partners/
        type: Partners
      - url: https://aws.amazon.com/opensearch-service/faqs/
        type: FAQ
      - url: https://aws.amazon.com/opensearch-service/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/opensearch-service/resources/
        type: Resources
      - url: https://aws.amazon.com/opensearch-service/customers/
        type: Customers
      - url: https://aws.amazon.com/opensearch-service/features/
        type: Features
      - url: https://aws.amazon.com/opensearch-service/migrations/
        type: Migrations
    description: |-

      Amazon OpenSearch Service makes it easy for you to perform interactive log
      analytics, real-time application monitoring, website search, and more.
      OpenSearch is an open source, distributed search and analytics suite
      derived from Elasticsearch. 
  - aid: amazon-web-services:aws-organizations
    name: AWS Organizations
    tags:
      - Policies
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/organizations/
    overlays:
      - url: overlays/organizations-openapi-search.yml
        type: APIs.io Search
      - url: overlays/organizations-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/organizations/
        type: Documentation
      - url: openapi/organizations-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/organizations/features/
        type: Features
      - url: https://aws.amazon.com/organizations/resources/
        type: Resources
      - url: https://aws.amazon.com/organizations/getting-started/best-practices/
        type: Best Practices
      - url: https://aws.amazon.com/organizations/resources/
        type: Resources
      - url: https://aws.amazon.com/organizations/faqs/
        type: FAQ
      - url: https://aws.amazon.com/organizations/customers/
        type: Customers
    description: |-

      AWS Organizations simplifies the management of policies across multiple
      AWS accounts by providing a policy-based management system. This feature
      enables users to efficiently manage policies for groups of accounts and
      streamline the process of creating new accounts through automation.
  - aid: amazon-web-services:aws-opsworks
    name: AWS OpsWorks
    tags:
      - Attributes
      - Engines
      - Servers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/opsworks/
    overlays:
      - url: overlays/opsworkscm-openapi-search.yml
        type: APIs.io Search
      - url: overlays/opsworkscm-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/opsworks/
        type: Documentation
      - url: openapi/opsworkscm-openapi-original.yml
        type: OpenAPI
    description: |-

      The API offered by AWS OpsWorks allows for seamless configuration
      management through the utilization of Chef and Puppet, powerful automation
      platforms that enable code-based automation of server configurations. With
      OpsWorks, users can leverage Chef and Puppet to automate the setup,
      deployment, and maintenance of servers within Amazon EC2 instances or
      on-premises compute environments. 
  - aid: amazon-web-services:amazon-opensearch-ingestion
    name: Amazon OpenSearch Ingestion
    tags:
      - Blueprints
      - Change
      - Names
      - Pipelines
      - Progress
      - Resources
      - Stop
      - Tags
      - Untag
      - Validate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html
    overlays:
      - url: overlays/osis-openapi-search.yml
        type: APIs.io Search
      - url: overlays/osis-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html
        type: Documentation
      - url: openapi/osis-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon OpenSearch Ingestion API is a fully managed, serverless data
      collection tool designed to deliver real-time log, metric, and trace data
      to Amazon OpenSearch Service domains and OpenSearch Serverless
      collections. With OpenSearch Ingestion, there is no longer a need for
      third-party solutions like Logstash or Jaeger to ingest data into your
      OpenSearch Service domains and OpenSearch Serverless collections. 
  - aid: amazon-web-services:aws-panorama
    name: AWS Panorama
    tags:
      - ARN
      - Applications
      - Dependencies
      - Describe
      - Details
      - Device
      - Devices
      - Import
      - Instances
      - Jobs
      - Metadata
      - Nodes
      - Packages
      - Patch
      - Provision
      - Register
      - Removes
      - Resources
      - Signals
      - Tags
      - Templates
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/panorama/
    overlays:
      - url: overlays/panorama-openapi-search.yml
        type: APIs.io Search
      - url: overlays/panorama-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/panorama/
        type: Documentation
      - url: openapi/panorama-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/panorama/pricing/
        type: Pricing
      - url: https://aws.amazon.com/panorama/resources/
        type: Resources
      - url: https://aws.amazon.com/panorama/faqs/
        type: FAQ
      - url: https://aws.amazon.com/panorama/customers/
        type: Customers
      - url: https://aws.amazon.com/panorama/partners/
        type: Partners
      - url: https://aws.amazon.com/panorama/partners/
        type: Partners
      - url: https://aws.amazon.com/panorama/use-cases/
        type: Use-cases
      - url: https://aws.amazon.com/panorama/developers/
        type: Developers
      - url: https://aws.amazon.com/panorama/appliance/
        type: Appliance
    description: |-

      AWS Panorama is a set of machine learning (ML) tools and software
      development kit (SDK) that enables the integration of computer vision (CV)
      capabilities into on-site internet protocol (IP) cameras.
  - aid: amazon-web-services:aws-payment-cryptography-control-plane
    name: AWS Payment Cryptography Control Plane
    tags:
      - Alias
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/payment-cryptography/
    overlays:
      - url: overlays/payment-cryptography-openapi-search.yml
        type: APIs.io Search
      - url: overlays/payment-cryptography-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/payment-cryptography/
        type: Documentation
      - url: openapi/payment-cryptography-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Web Services Payment Cryptography Control Plane APIs are used
      to manage encryption keys for payment-related cryptographic operations.
      With these APIs, you can create, import, export, share, manage, and delete
      keys, as well as manage Identity and Access Management (IAM) policies. 
  - aid: amazon-web-services:aws-private-ca-connector-for-active-directory
    name: AWS Private CA Connector for Active Directory
    tags:
      - ARN
      - Access
      - Connectors
      - Controls
      - Directory
      - Entries
      - Entry
      - Groups
      - Names
      - Principals
      - Registrations
      - Resources
      - Security
      - Services
      - Tags
      - Templates
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad.html
    overlays:
      - url: overlays/pca-connector-ad-openapi-search.yml
        type: APIs.io Search
      - url: overlays/pca-connector-ad-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad.html
        type: Documentation
      - url: openapi/pca-connector-ad-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Web Services Private CA Connector for Active Directory
      establishes a connection between Amazon Web Services Private CA and Active
      Directory, allowing you to generate security certificates for Active
      Directory that are signed by your own private CA. For further details,
      visit the Amazon Web Services Private CA Connector for Active Directory
      documentation.
  - aid: amazon-web-services:amazon-personalize
    name: Amazon Personalize
    tags:
      - Actions
      - Interactions
      - Events
      - Items
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/personalize/latest/dg/API_Types_Amazon_Personalize_Events.html
    overlays:
      - url: overlays/personalize-events-openapi-search.yml
        type: APIs.io Search
      - url: overlays/personalize-events-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/personalize/latest/dg/API_Types_Amazon_Personalize_Events.html
        type: Documentation
      - url: openapi/personalize-events-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Personalize API enables the consumption of real-time user event
      data, such as streaming or click data, for model training purposes. This
      data can be used on its own or in combination with historical data. For
      further details, refer to the documentation on Recording item interaction
      events.
  - aid: amazon-web-services:aws-cloud-wan-core-network
    name: 'AWS Cloud WAN Core Network '
    tags:
      - Accept
      - Attachments
      - Associations
      - Connect
      - Global
      - Networks
      - Peer
      - Customers
      - Gateways
      - Link
      - Transit
      - Peers
      - Connections
      - Core
      - Devices
      - Describe
      - Links
      - Sites
      - VPN
      - Peerings
      - Routes
      - Tables
      - VPC
      - Policies
      - Versions
      - Device
      - ARN
      - Resources
      - Deregister
      - Registrations
      - Disassociate
      - Change
      - Execute
      - Sets
      - Events
      - Count
      - Counts
      - Relationships
      - Telemetry
      - Analysis
      - Register
      - Access
      - Organizations
      - Services
      - Tags
      - Untag
      - Reject
      - Restore
      - Metadata
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html
    overlays:
      - url: overlays/networkmanager-openapi-search.yml
        type: APIs.io Search
      - url: overlays/networkmanager-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html
        type: Documentation
      - url: openapi/networkmanager-openapi-original.yml
        type: OpenAPI
    description: |-

      This API allows you to efficiently manage your Amazon Web Services Cloud
      WAN core network and Transit Gateway network across multiple AWS accounts,
      Regions, and on-premises locations.
  - aid: amazon-web-services:aws-outposts
    name: AWS Outposts
    tags:
      - ARN
      - Addresses
      - Assets
      - Cancel
      - Catalog
      - Connections
      - Instances
      - Items
      - Orders
      - Outposts
      - Physical
      - Properties
      - Rack
      - Resources
      - Sites
      - Tags
      - Types
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/outposts/
    overlays:
      - url: overlays/outposts-openapi-search.yml
        type: APIs.io Search
      - url: overlays/outposts-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/outposts/
        type: Documentation
      - url: openapi/outposts-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Web Services Outposts is a service that brings Amazon Web Services
      infrastructure, APIs, and tools to customer premises in a fully managed
      capacity. With Outposts, customers can access AWS managed infrastructure
      locally, allowing for the development and operation of applications on
      premises with the same programming interfaces as in AWS Regions.
  - aid: amazon-web-services:amazon-personalize
    name: Amazon Personalize
    tags:
      - Recommenders
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/personalize/
    overlays:
      - url: overlays/personalize-openapi-search.yml
        type: APIs.io Search
      - url: overlays/personalize-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/personalize/
        type: Documentation
      - url: openapi/personalize-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/personalize/features/
        type: Featurs
      - url: https://aws.amazon.com/personalize/pricing/
        type: Pricing
      - url: https://aws.amazon.com/personalize/resources/
        type: Resources
      - url: https://aws.amazon.com/personalize/faqs/
        type: FAQ
      - url: https://aws.amazon.com/personalize/customers/
        type: Customers
      - url: https://aws.amazon.com/personalize/partners/
        type: Partners
    description: |-

      Amazon Personalize simplifies the process of integrating personalized
      recommendations powered by machine learning into various platforms,
      including websites, applications, and email marketing systems, thereby
      facilitating your digital transformation.
  - aid: amazon-web-services:amazon-pinpoint-email
    name: Amazon Pinpoint Email
    tags:
      - Accounts
      - Attributes
      - Blacklist
      - Campaigns
      - Configurations
      - DKIM
      - Dashboard
      - Dedicated
      - Deliverability
      - Deliveries
      - Destinations
      - Domains
      - Emails
      - Entities
      - Events
      - Feedback
      - IP
      - IP Addresses
      - Identities
      - Identity
      - Mail
      - Names
      - Options
      - Outbound
      - Pools
      - Reports
      - Reputation
      - Resources
      - Send
      - Sending
      - Sets
      - Statistics
      - Subscribed
      - Tags
      - Tests
      - Tracking
      - Untag
      - Warmup
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/Welcome.html
    overlays:
      - url: overlays/pinpoint-email-openapi-search.yml
        type: APIs.io Search
      - url: overlays/pinpoint-email-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/Welcome.html
        type: Documentation
      - url: openapi/pinpoint-email-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Pinpoint Email API is a specialized feature within the AWS
      service that allows businesses to connect with customers through email
      messaging. This API enhances the functionality of the Amazon Pinpoint
      platform, enabling users to send personalized email campaigns and track
      performance metrics.
  - aid: amazon-web-services:amazon-pinpoint-sms-and-voice
    name: Amazon Pinpoint SMS and Voice
    tags:
      - Destinations
      - Numbers
      - Verify
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/welcome.html
    overlays:
      - url: overlays/pinpoint-sms-voice-v2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/pinpoint-sms-voice-v2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/welcome.html
        type: Documentation
      - url: openapi/pinpoint-sms-voice-v2-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Pinpoint SMS and Voice, version 2 API allows developers to
      access specialized features for sending SMS messages and making voice
      calls, expanding upon the functionalities available in the Amazon Pinpoint
      API.
  - aid: amazon-web-services:amazon-eventbridge-pipes
    name: Amazon EventBridge Pipes
    tags:
      - ARN
      - Names
      - Pipe
      - Pipes
      - Resources
      - Stop
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html
    overlays:
      - url: overlays/pipes-openapi-search.yml
        type: APIs.io Search
      - url: overlays/pipes-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html
        type: Documentation
      - url: openapi/pipes-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon EventBridge Pipes API seamlessly connects event sources to
      targets, simplifying the development of event-driven architectures by
      eliminating the need for specialized knowledge and integration code. This
      tool ensures consistency across a company's applications by allowing any
      available EventBridge target to be used. 
  - aid: amazon-web-services:aws-proton
    name: AWS Proton
    tags:
      - Configurations
      - Sync
      - Templates
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/proton/
    overlays:
      - url: overlays/proton-openapi-search.yml
        type: APIs.io Search
      - url: overlays/proton-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/proton/
        type: Documentation
      - url: openapi/proton-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/proton/features/
        type: Features
      - url: https://aws.amazon.com/proton/pricing/
        type: Pricing
      - url: https://aws.amazon.com/proton/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/proton/faqs/
        type: FAQ
      - url: https://aws.amazon.com/proton/partners/
        type: Partners
      - url: https://aws.amazon.com/proton/features/
        type: Features
    description: |-

      The Proton Service API Reference provides detailed descriptions, syntax,
      and usage examples for the various actions and data types available within
      the Proton service. The API documentation includes Query API request
      parameters and XML responses for each action. 
  - aid: amazon-web-services:aws-private-5g
    name: AWS Private 5G
    tags:
      - ARN
      - Access
      - Acknowledge
      - Activate
      - Configure
      - Deactivate
      - Device
      - Entifiers
      - Networks
      - Orders
      - Ping
      - Plan
      - Points
      - Receipts
      - Resources
      - Sites
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/private5g/
    overlays:
      - url: overlays/privatenetworks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/privatenetworks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/private5g/
        type: Documentation
      - url: openapi/privatenetworks-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/private5g/features/
        type: Features
      - url: https://aws.amazon.com/private5g/pricing/
        type: Pricing
      - url: https://aws.amazon.com/private5g/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/private5g/faqs/
        type: FAQ
    description: |-

      The Amazon Web Services Private 5G API offers a managed solution for
      setting up and expanding your private mobile network on-site. It includes
      pre-configured hardware and software, simplifies setup with automation,
      and allows for seamless scalability to accommodate more devices when
      necessary.
  - aid: amazon-web-services:amazon-polly
    name: Amazon Polly
    tags:
      - Describe
      - Lexicons
      - Names
      - Speech
      - Synthesis
      - Synthesize
      - Tasks
      - Voices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/polly/
    overlays:
      - url: overlays/polly-openapi-search.yml
        type: APIs.io Search
      - url: overlays/polly-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/polly/
        type: Documentation
      - url: openapi/polly-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/polly/features/
        type: Features
      - url: https://aws.amazon.com/polly/pricing/
        type: Pricing
      - url: https://aws.amazon.com/polly/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/polly/resources/
        type: Resources
      - url: https://aws.amazon.com/polly/customers/
        type: Customers
    description: |-

      Amazon Polly is a web service that makes it easy to synthesize speech from
      text. The Amazon Polly service provides API operations for synthesizing
      high-quality speech from plain text and Speech Synthesis Markup Language
      (SSML), along with managing pronunciations lexicons that enable you to get
      the best results for your application domain.
  - aid: amazon-web-services:amazon-q-in-connect
    name: Amazon Q in Connect
    tags:
      - ARN
      - Assistants
      - Associations
      - Base
      - Bases
      - Content
      - Contents
      - Feedback
      - Import
      - Jobs
      - Knowledge
      - Notify
      - Queries
      - Received
      - Recommendations
      - Resources
      - Responses
      - Search
      - Sessions
      - Summaries
      - Tags
      - Templates
      - URI
      - Untag
      - Uploads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/connect/q/
    overlays:
      - url: overlays/qconnect-openapi-search.yml
        type: APIs.io Search
      - url: overlays/qconnect-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/connect/q/
        type: Documentation
      - url: openapi/qconnect-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/connect/pricing/
        type: Pricing
      - url: https://aws.amazon.com/connect/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/connect/resources/
        type: Resources
      - url: https://aws.amazon.com/connect/customers/
        type: Customers
      - url: https://aws.amazon.com/connect/partners/
        type: Partners
    description: |-

      The Amazon Q in Connect API is an upgraded version of Amazon Connect
      Wisdom that utilizes generative AI to provide agents with suggested
      responses and actions to resolve customer inquiries quickly and enhance
      customer satisfaction. Instead of having knowledge articles, wikis, and
      FAQs scattered across various repositories, Amazon Q in Connect integrates
      them into one platform. 
  - aid: amazon-web-services:amazon-q
    name: Amazon Q
    tags:
      - ARN
      - Applications
      - Batches
      - Chat
      - Chat Controls
      - Configurations
      - Controls
      - Conversations
      - Data
      - Data Source
      - Documents
      - Experience
      - Experiences
      - Feedback
      - Groups
      - Index
      - Indices
      - Jobs
      - Messages
      - Names
      - Plugins
      - Resources
      - Sources
      - Start Sync
      - Stop
      - Stopsync
      - Sync
      - Sync Jobs
      - Tags
      - Untag
      - Users
      - Web
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/q/
    overlays:
      - url: overlays/qbusiness-openapi-search.yml
        type: APIs.io Search
      - url: overlays/qbusiness-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/q/
        type: Documentation
      - url: openapi/qbusiness-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/q/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/q/customers/
        type: Customers
    description: |-

      Amazon Q generates code, tests, debugs, and has multistep planning and
      reasoning capabilities that can transform and implement new code generated
      from developer requests. Amazon Q also makes it easier for employees to
      get answers to questions across business data-such as company policies,
      product information, business results, code base, employees, and many
      other topics-by connecting to enterprise data repositories to summarize
      the data logically, analyze trends, and engage in dialogue about the data.
  - aid: amazon-web-services:amazon-rds-performance-insights
    name: Amazon RDS Performance Insights
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/rds/performance-insights/
    overlays:
      - url: overlays/pi-openapi-search.yml
        type: APIs.io Search
      - url: overlays/pi-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/rds/performance-insights/
        type: Documentation
      - url: openapi/pi-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/rds/performance-insights/pricing/
        type: Pricing
      - url: https://aws.amazon.com/rds/performance-insights/faqs/
        type: FAQ
      - url: https://aws.amazon.com/rds/performance-insights/customers/
        type: Customers
    description: |-

      The Amazon RDS Performance Insights API allows you to monitor and analyze
      various aspects of database load by capturing data from a running DB
      instance. This guide provides detailed information on Performance Insights
      data types, parameters, and errors. With Performance Insights enabled, the
      API offers visibility into the performance of your DB instance. Amazon
      CloudWatch serves as the source for monitoring metrics, while Performance
      Insights provides a specialized view of DB load, measured in average
      active sessions. 
  - aid: amazon-web-services:aws-price-list
    name: AWS Price List
    tags:
      - Prices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/pricing/
    overlays:
      - url: overlays/pricing-openapi-search.yml
        type: APIs.io Search
      - url: overlays/pricing-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/pricing/
        type: Documentation
      - url: openapi/pricing-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/pricing/cost-optimization/
        type: Cost-optimization
    description: |-

      The Amazon Web Services Price List API is a user-friendly tool that allows
      you to access Amazon Web Services' services, products, and pricing
      information through programmatic queries. The API utilizes standardized
      product attributes like Location, Storage Class, and Operating System, and
      provides pricing at the SKU level. 
  - aid: amazon-web-services:amazon-qldb
    name: Amazon QLDB
    tags:
      - Command
      - Send
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/qldb/
    overlays:
      - url: overlays/qldb-session-openapi-search.yml
        type: APIs.io Search
      - url: overlays/qldb-session-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/qldb/
        type: Documentation
      - url: openapi/qldb-session-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/qldb/features/
        type: Features
      - url: https://aws.amazon.com/qldb/pricing/
        type: Pricing
      - url: https://aws.amazon.com/qldb/resources/
        type: Resources
      - url: https://aws.amazon.com/qldb/faqs/
        type: FAQ
      - url: https://aws.amazon.com/qldb/customers/
        type: Customers
    description: |-

      The recommended way to interact with the transactional data APIs for
      Amazon QLDB is to use the QLDB driver or the QLDB shell for executing data
      transactions on a ledger. When working with an AWS SDK, it is advised to
      use the QLDB driver, which abstracts the data plane and manages
      SendCommand API calls.
  - aid: amazon-web-services:resource-access-manager
    name: Resource Access Manager
    tags:
      - Accept
      - Accept Resource Share Invitation
      - Associate
      - Associate Resource Share
      - Associate Resource Share Permission
      - Associations
      - Default
      - Disassociate
      - Disassociate Resource Share
      - Disassociate Resource Share Permissions
      - Enable
      - Enable Sharing
      - Invitation
      - Invitations
      - Organizations
      - Pending
      - Pending Invitation Resources
      - Permission
      - Permission Associations
      - Permission Verions
      - Permission Version
      - Permission Versions
      - Permissions
      - Policies
      - Principals
      - Promote
      - Promote Permission From Policy
      - Promote Resource Share From Policy
      - Reject
      - Reject Resource Share Invitations
      - Replace
      - Replace Permission Associations
      - Resource Policies
      - Resource Share
      - Resource Share Associations
      - Resource Share Invitations
      - Resource Share Permissions
      - Resource Shares
      - Resource Types
      - Resources
      - Set Default Permission Versions
      - Sets
      - Share
      - Shares
      - Sharing
      - Tag Resources
      - Tags
      - Types
      - Untag
      - Updateresourceshare
      - Versions
      - Work
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/ram/
    overlays:
      - url: overlays/ram-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ram-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/ram/
        type: Documentation
      - url: openapi/ram-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/ram/faqs/
        type: FAQ
    description: |-

      The Resource Access Manager API Reference is a comprehensive guide that
      details all actions and data types available in RAM. RAM is a service
      designed to facilitate secure resource sharing between different Amazon
      Web Services accounts. This documentation provides users with the
      necessary information to effectively utilize RAM's features, including the
      ability to share resources with entire Organizations or specific
      organizational units. Additionally, supported resource types can be shared
      with individual IAM roles and users. 
  - aid: amazon-web-services:aws-rds
    name: AWS RDS
    tags:
      - Batches
      - Execute
      - Statements
      - Begins
      - Transactions
      - Commit
      - SQL
      - Rollback
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/rds/
    overlays:
      - url: overlays/rds-data-openapi-search.yml
        type: APIs.io Search
      - url: overlays/rds-data-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/rds/
        type: Documentation
      - url: openapi/rds-data-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/rds/features/
        type: Features
      - url: https://aws.amazon.com/rds/pricing/
        type: Pricing
      - url: https://aws.amazon.com/rds/resources/
        type: Resources
      - url: https://aws.amazon.com/rds/faqs/
        type: FAQ
      - url: https://aws.amazon.com/rds/customers/
        type: Customers
      - url: https://aws.amazon.com/rds/partners/
        type: Partners
    description: |-

      The RDS Data API from Amazon RDS allows users to execute SQL statements on
      an Amazon Aurora DB cluster via an HTTP endpoint. This API is compatible
      with various types of Aurora databases, including Aurora PostgreSQL
      (Serverless v2, Serverless v1, and provisioned) and Aurora MySQL
      (Serverless v1). Detailed instructions on utilizing the Data API can be
      found in the Amazon Aurora User Guide.
  - aid: amazon-web-services:amazon-quicksight
    name: Amazon QuickSight
    tags:
      - ARN
      - Accounts
      - Alias
      - Aliases
      - Analysis
      - Anonymous
      - Assets
      - Assignment
      - Assignments
      - Bundles
      - Configurations
      - Connections
      - Custom
      - Customizations
      - Dashboard
      - Dashboards
      - Data
      - Datasets
      - Definitions
      - Describe
      - Embed
      - Entities
      - Exports
      - Folders
      - Generate
      - Groups
      - IAM
      - IAMPolicy
      - IP
      - Identity
      - Import
      - Ingestions
      - Jobs
      - Linked
      - Links
      - Members
      - Memberships
      - Names
      - Namespaces
      - Numbers
      - Permission
      - Permissions
      - Policies
      - Principals
      - Propagation
      - Properties
      - Public
      - Published
      - Refresh
      - Register
      - Registered
      - Resolved
      - Resources
      - Restore
      - Restrictions
      - Results
      - Roles
      - Schedules
      - Search
      - Services
      - Sessions
      - Sets
      - Settings
      - Sharing
      - Snapshots
      - Sources
      - Subscriptions
      - Tags
      - Templates
      - Theme
      - Themes
      - Topics
      - Types
      - URL
      - Untag
      - Users
      - VPC
      - VPCConnection
      - VPCConnections
      - Versions
      - Vpcconnection
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/quicksight/
    overlays:
      - url: overlays/quicksight-openapi-search.yml
        type: APIs.io Search
      - url: overlays/quicksight-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/quicksight/
        type: Documentation
      - url: openapi/quicksight-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/quicksight/features/
        type: Features
      - url: https://aws.amazon.com/quicksight/gallery/
        type: Gallery
      - url: https://aws.amazon.com/quicksight/pricing/
        type: Pricing
      - url: https://aws.amazon.com/quicksight/customers/
        type: Customers
      - url: https://aws.amazon.com/quicksight/partners/
        type: Partners
      - url: https://aws.amazon.com/quicksight/resources/blog/
        type: Blogs
      - url: https://aws.amazon.com/quicksight/resources/case_studies/
        type: Case Studies
      - url: https://aws.amazon.com/quicksight/resources/
        type: Learning Resources
      - url: https://aws.amazon.com/quicksight/resources/faqs/
        type: FAQ
    description: |-

      Amazon QuickSight provides businesses with expansive and unified business
      intelligence solutions. Through modern interactive dashboards, paginated
      reports, natural language queries, and embedded analytics, all users can
      access reliable data to meet their analytical needs. With Amazon Q
      integration, business analysts and users can quickly build, discover, and
      share valuable insights using natural language, ultimately making informed
      decisions faster.
  - aid: amazon-web-services:amazon-redshift
    name: Amazon Redshift
    tags:
      - Partners
      - Status
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/redshift/
    overlays:
      - url: overlays/redshift-openapi-search.yml
        type: APIs.io Search
      - url: overlays/redshift-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/redshift/
        type: Documentation
      - url: openapi/redshift-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/redshift/features/
        type: Features
      - url: https://aws.amazon.com/redshift/pricing/
        type: Pricing
      - url: https://aws.amazon.com/redshift/customer-success/
        type: Customer Success
      - url: https://aws.amazon.com/redshift/solutions/
        type: Solutions
      - url: https://aws.amazon.com/redshift/resources/
        type: Resources
      - url: https://aws.amazon.com/redshift/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/redshift/faqs/
        type: FAQ
      - url: https://aws.amazon.com/big-data/datalakes-and-analytics/migrations/
        type: Migrations
      - url: https://aws.amazon.com/redshift/partners/
        type: Partners
    description: |-

      Amazon Redshift is a comprehensive data warehouse solution offered by
      Amazon Web Services. This API reference provides documentation for the
      various programming and command line interfaces available for managing
      Amazon Redshift clusters. It is important to note that Amazon Redshift
      operates asynchronously, requiring techniques such as polling or
      asynchronous callback handlers to track the status of commands. The
      parameter descriptions in this reference specify whether a change takes
      effect immediately, upon the next instance reboot, or during the next
      maintenance window. Amazon Redshift handles tasks such as provisioning
      capacity, monitoring, backup, and applying patches and upgrades to the
      engine, allowing users to focus on leveraging their data for business
      insights.
  - aid: amazon-web-services:aws-recycle-bin
    name: AWS Recycle Bin
    tags:
      - ARN
      - Locks
      - Resources
      - Rules
      - Tags
      - Unlock
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/recyclebin/latest/APIReference/Welcome.html
    overlays:
      - url: overlays/rbin-openapi-search.yml
        type: APIs.io Search
      - url: overlays/rbin-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/recyclebin/latest/APIReference/Welcome.html
        type: Documentation
      - url: openapi/rbin-openapi-original.yml
        type: OpenAPI
      - url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin.html
        type: User Guide
      - url: https://docs.aws.amazon.com/cli/latest/reference/rbin/index.html
        type: Command Line Interface
    description: |-

      This is the API Reference for Recycle Bin, a feature that allows you to
      recover accidentally deleted snapshots and EBS-backed AMIs. The
      documentation provides detailed descriptions and syntax for each action
      and data type within Recycle Bin. When you use Recycle Bin, any deleted
      resources are stored in the bin for a specified time period. 
  - aid: amazon-web-services:amazon-redshift
    name: Amazon Redshift
    tags:
      - Tables
      - Data
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/redshift/
    overlays:
      - url: overlays/redshift-data-openapi-search.yml
        type: APIs.io Search
      - url: overlays/redshift-data-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/redshift/
        type: Documentation
      - url: openapi/redshift-data-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/redshift/features/
        type: Features
      - url: https://aws.amazon.com/redshift/pricing/
        type: Pricing
      - url: https://aws.amazon.com/redshift/customer-success/
        type: Customer Success
      - url: https://aws.amazon.com/redshift/solutions/
        type: Solutions
    description: |-

      Utilize the Amazon Redshift Data API to execute queries on Amazon Redshift
      tables by running SQL statements. Successful statements will be committed.
      Refer to the Amazon Redshift Management Guide for further details on the
      Amazon Redshift Data API and CLI usage examples.
  - aid: amazon-web-services:amazon-rekognition
    name: Amazon Rekognition
    tags:
      - Processor
      - Stream
      - Machine Learning
      - Videos
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/rekognition/
    overlays:
      - url: overlays/rekognition-openapi-search.yml
        type: APIs.io Search
      - url: overlays/rekognition-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/rekognition/
        type: Documentation
      - url: openapi/rekognition-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/rekognition/pricing/
        type: Pricing
      - url: https://aws.amazon.com/rekognition/resources/
        type: Resources
      - url: https://aws.amazon.com/rekognition/faqs/
        type: FAQ
      - url: https://aws.amazon.com/rekognition/customers/
        type: Customers
    description: |-

      The Amazon Rekognition API provides endpoints for Amazon Rekognition
      Image, Amazon Rekognition Custom Labels, Amazon Rekognition Stored Video,
      and Amazon Rekognition Streaming Video. The API includes actions such as
      detecting faces, labels, text, and celebrities, as well as functionalities
      for creating collections, comparing faces, analyzing video content, and
      managing datasets and projects. Common parameters and errors are also
      documented to assist developers in integrating this API into their
      applications.
  - aid: amazon-web-services:amazon-redshift-serverless
    name: Amazon Redshift Serverless
    tags:
      - Workgroup
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/redshift/redshift-serverless/
    overlays:
      - url: overlays/redshift-serverless-openapi-search.yml
        type: APIs.io Search
      - url: overlays/redshift-serverless-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/redshift/redshift-serverless/
        type: Documentation
      - url: openapi/redshift-serverless-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/redshift/features/
        type: Features
      - url: https://aws.amazon.com/redshift/pricing/
        type: Pricing
      - url: https://aws.amazon.com/redshift/customer-success/
        type: Customer Success
      - url: https://aws.amazon.com/redshift/solutions/
        type: Solutions
    description: |-

      This API reference provides documentation for an interface for managing
      Amazon Redshift Serverless. This service automatically adjusts data
      warehouse capacity and scales resources based on workload demands,
      delivering high performance and simplified operations. With Amazon
      Redshift Serverless, users can focus on utilizing their data to gain new
      insights for their business and customers.
  - aid: amazon-web-services:aws-resource-explorer
    name: AWS Resource Explorer
    tags:
      - ARN
      - Accounts
      - Associate
      - Batches
      - Configurations
      - Default
      - Disassociate
      - Index
      - Indexes
      - Levels
      - Members
      - Resources
      - Search
      - Services
      - Supported
      - Tags
      - Types
      - Untag
      - View
      - Views
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/resourceexplorer/
    overlays:
      - url: overlays/resource-explorer-2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/resource-explorer-2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/resourceexplorer/
        type: Documentation
      - url: openapi/resource-explorer-2-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/resourceexplorer/features/
        type: Features
      - url: https://aws.amazon.com/resourceexplorer/pricing/
        type: Pricing
      - url: https://aws.amazon.com/resourceexplorer/faqs/
        type: FAQ
    description: |-

      Amazon Web Services Resource Explorer is a search and discovery service
      that allows users to explore their resources using an internet search
      engine-like experience. Examples of resources that can be searched for
      include Amazon RDS instances, Amazon S3 buckets, and Amazon DynamoDB
      tables. Users can search for resources using metadata such as names, tags,
      and IDs. Resource Explorer can search across all AWS Regions in the user's
      account to simplify cross-Region workloads. By turning on Resource
      Explorer, users can scan and index resources in each Region, with the
      option to designate one Region as the aggregator index for the account.
      This aggregator index contains a copy of all resource information from all
      Regions where Resource Explorer is enabled. Users can access a
      comprehensive view of their resources across all indexed Regions in their
      account. For more information on enabling and configuring Resource
      Explorer, refer to the user guide provided by Amazon Web Services.
  - aid: amazon-web-services:aws-resource-groups-tagging
    name: AWS Resource Groups Tagging
    tags:
      - Resources
      - Untag
      - Tags
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html
    overlays:
      - url: overlays/resourcegroupstaggingapi-openapi-search.yml
        type: APIs.io Search
      - url: overlays/resourcegroupstaggingapi-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html
        type: Documentation
      - url: openapi/resourcegroupstaggingapi-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS supports tagging on all core infrastructure resources that incur
      charges. Most other AWS resources also support tagging. Some resources
      support tagging only through that service's native tagging operations, and
      don't yet support this API. See the documentation for an individual
      service for information about that service's native tagging operations.
  - aid: amazon-web-services:aws-robomaker
    name: AWS RoboMaker
    tags:
      - ARN
      - Applications
      - Batches
      - Body
      - Cancel
      - Deployments
      - Deregister
      - Describe
      - Exports
      - Fleets
      - Generation
      - Jobs
      - Register
      - Resources
      - Restart
      - Robots
      - Simulations
      - Sync
      - Tags
      - Templates
      - Untag
      - Versions
      - Worlds
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/robomaker/
    overlays:
      - url: overlays/robomaker-openapi-search.yml
        type: APIs.io Search
      - url: overlays/robomaker-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/robomaker/
        type: Documentation
      - url: openapi/robomaker-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/robomaker/pricing/
        type: Pricing
      - url: https://aws.amazon.com/robomaker/resources/
        type: Resources
      - url: https://aws.amazon.com/robomaker/faqs/
        type: FAQ
      - url: https://aws.amazon.com/robomaker/customers/
        type: Customers
    description: |-

      AWS RoboMaker is a cloud-based simulation service that enables robotics
      developers to run, scale, and automate simulation without managing any
      infrastructure.
  - aid: amazon-web-services:aws-repost-private
    name: AWS re:Post Private
    tags:
      - ARN
      - Administrative
      - Administrator
      - Invite
      - Invites
      - Register
      - Resources
      - Send
      - Space
      - Spaces
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/repost-private/
    overlays:
      - url: overlays/repostspace-openapi-search.yml
        type: APIs.io Search
      - url: overlays/repostspace-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/repost-private/
        type: Documentation
      - url: openapi/repostspace-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/repost-private/features/
        type: Features
      - url: https://aws.amazon.com/repost-private/pricing/
        type: Pricing
      - url: https://aws.amazon.com/repost-private/faqs/
        type: FAQ
    description: |-

      re:Post Private is a tailored version of AWS re:Post designed exclusively
      for enterprise customers with Enterprise Support or Enterprise On-Ramp
      Support plans. This platform grants access to a wealth of knowledge and
      expert guidance, enabling organizations to expedite their transition to
      the cloud and enhance developer productivity.
  - aid: amazon-web-services:aws-identity-and-access-management-roles-anywhere
    name: AWS Identity and Access Management Roles Anywhere
    tags:
      - Anchor
      - Anchors
      - Disable
      - Enable
      - Notifications
      - Profiles
      - Reset
      - Resources
      - Settings
      - Subjects
      - Tags
      - Trust
      - Trust Anchors
      - Trustanchor
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iam/roles-anywhere/
    overlays:
      - url: overlays/rolesanywhere-openapi-search.yml
        type: APIs.io Search
      - url: overlays/rolesanywhere-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iam/roles-anywhere/
        type: Documentation
      - url: openapi/rolesanywhere-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iam/roles-anywhere/resources/
        type: Resources
    description: |-

      The API for Identity and Access Management Roles Anywhere enables secure
      access for workloads running outside of Amazon Web Services to obtain
      temporary AWS credentials. By leveraging IAM policies and roles, workloads
      can access AWS resources without the need for long-term credentials
      management. 
  - aid: amazon-web-services:aws-resource-groups
    name: AWS Resource Groups
    tags:
      - ARN
      - Accounts
      - Configurations
      - Groups
      - Queries
      - Resources
      - Search
      - Settings
      - Tags
      - Ungroup
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html
    overlays:
      - url: overlays/resource-groups-openapi-search.yml
        type: APIs.io Search
      - url: overlays/resource-groups-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html
        type: Documentation
      - url: openapi/resource-groups-openapi-original.yml
        type: OpenAPI
    description: |-

      The Resource Groups API allows users to effectively organize various
      Amazon Web Services resources, including instances from Amazon Elastic
      Compute Cloud, databases from Amazon Relational Database Service, and
      buckets from Amazon Simple Storage Service. 
  - aid: amazon-web-services:aws-routing-control
    name: AWS Routing Control
    tags:
      - Controls
      - Routing
      - States
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html
    overlays:
      - url: overlays/route53-recovery-cluster-openapi-search.yml
        type: APIs.io Search
      - url: overlays/route53-recovery-cluster-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html
        type: Documentation
      - url: openapi/route53-recovery-cluster-openapi-original.yml
        type: OpenAPI
    description: |-

      Welcome to the API Reference Guide for the Routing Control (Recovery
      Cluster) feature in Amazon Route 53 Application Recovery Controller (ARC).
      With Route 53 ARC, you can utilize routing control to recover applications
      by redirecting traffic across different Availability Zones or Amazon Web
      Services Regions with high reliability. Routing controls act as simple
      on/off switches hosted on a highly available cluster within Route 53 ARC. 
  - aid: amazon-web-services:amazon-route-53
    name: "Amazon Route\_53"
    tags:
      - Accounts
      - Activate
      - Associate
      - Associate VPC
      - Authorization
      - Authorizers VPC Association
      - Blocks
      - CIDR
      - Change
      - Checker
      - Checker IP Ranges
      - Checks
      - Collections
      - Comments
      - Configurations
      - Count
      - DNS Security
      - DNSAnswer
      - DNSSEC
      - Deactivate
      - Deauthorize VPC Association
      - Delegation
      - Delegation Sets
      - Disable
      - Disassociate
      - Disassociate VPC
      - Enable
      - Failure
      - Geo
      - Geolocation
      - Health
      - Health Check
      - Hosted
      - Hosted Zone Count
      - Hosted Zones
      - Hostedzonelimit
      - IP
      - Instances
      - Key Signing
      - Keys
      - Last
      - Last Failure Reasons
      - Limits
      - Locations
      - Logging
      - Names
      - Policies
      - Queries
      - Query Logging Configurations
      - Ranges
      - Rblocks
      - Rcollection
      - Reasons
      - Record
      - Resources
      - Reusable
      - Sets
      - Signing
      - Status
      - Tags
      - Tests
      - Traffic
      - Traffic Policies
      - Traffic Policy Instance Count
      - Traffic Policy Instances
      - Types
      - VPC
      - VPCAssociation
      - VPCFrom
      - VPCWith
      - Versions
      - Zones
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/route53/
    overlays:
      - url: overlays/route53-openapi-search.yml
        type: APIs.io Search
      - url: overlays/route53-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/route53/
        type: Documentation
      - url: openapi/route53-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/route53/features/
        type: Features
      - url: https://aws.amazon.com/route53/pricing/
        type: Pricing
      - url: https://aws.amazon.com/route53/resources/
        type: Resources
      - url: https://aws.amazon.com/route53/faqs/
        type: FAQ
    description: |-

      Amazon Route 53, is a robust and reliable Domain Name System (DNS) web
      service that ensures high availability and scalability for connecting user
      requests to internet applications hosted on AWS or on-premises
      environments.
  - aid: amazon-web-services:amazon-route-53-application-recovery-controller
    name: Amazon Route 53 Application Recovery Controller
    tags:
      - ARN
      - Accounts
      - Architecture
      - Authorization
      - Cell
      - Cellreadiness
      - Cells
      - Checks
      - Cross Account Authorizations
      - Groups
      - Names
      - Readiness
      - Readiness Checks
      - Recommendations
      - Recovery
      - Recovery Groups
      - Recoverygroupreadiness
      - Resource Sets
      - Resources
      - Rules
      - Sets
      - Status
      - Summaries
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/amazonarc/
    overlays:
      - url: overlays/route53-recovery-readiness-openapi-search.yml
        type: APIs.io Search
      - url: overlays/route53-recovery-readiness-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/amazonarc/
        type: Documentation
      - url: openapi/route53-recovery-readiness-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Route 53 Application Recovery Controller (Route 53 ARC) allows
      you to monitor the readiness of your applications and resources for
      recovery and facilitates traffic redirection between AWS Regions or away
      from Availability Zones to support application disaster recovery efforts.
  - aid: amazon-web-services:aws-resilience-hub
    name: AWS Resilience Hub
    tags:
      - ARN
      - Alarm
      - Applications
      - Assessments
      - Batches
      - Compliance
      - Components
      - Describe
      - Draft
      - Drifts
      - Import
      - Inputs
      - Mapping
      - Policies
      - Publish
      - Recommendations
      - Removes
      - Resiliency
      - Resolutions
      - Resolve
      - Resources
      - Sources
      - Status
      - Suggested
      - Tags
      - Templates
      - Tests
      - Unsupported
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/resilience-hub/
    overlays:
      - url: overlays/resiliencehub-openapi-search.yml
        type: APIs.io Search
      - url: overlays/resiliencehub-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/resilience-hub/
        type: Documentation
      - url: openapi/resiliencehub-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/resilience-hub/pricing/
        type: Pricing
      - url: https://aws.amazon.com/resilience-hub/resources/
        type: Resources
    description: |-

      Resilience Hub is an API designed to help you protect your Amazon Web
      Services applications by conducting continuous resiliency assessments and
      validations. Integrated into your software development pipeline, it
      proactively identifies and mitigates weaknesses in your applications,
      ensures RTO and RPO targets are met, and resolves potential issues before
      deployment to production.
  - aid: amazon-web-services:amazon-route-53-domains
    name: Amazon Route 53 Domains
    tags:
      - Billing
      - View
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html
    overlays:
      - url: overlays/route53domains-openapi-search.yml
        type: APIs.io Search
      - url: overlays/route53domains-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html
        type: Documentation
      - url: openapi/route53domains-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Route 53 API allows users to easily register domain names and
      carry out various related functions.
  - aid: amazon-web-services:aws-route53-resolver
    name: AWS route53 resolver
    tags:
      - Resolvers
      - Rules
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/route53/resolver/
    overlays:
      - url: overlays/route53resolver-openapi-search.yml
        type: APIs.io Search
      - url: overlays/route53resolver-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/route53/resolver/
        type: Documentation
      - url: openapi/route53resolver-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/route53/features/
        type: Features
      - url: https://aws.amazon.com/route53/pricing/
        type: Pricing
      - url: https://aws.amazon.com/route53/resources/
        type: Resources
      - url: https://aws.amazon.com/route53/faqs/
        type: FAQ
    description: |-

      Amazon Route 53 Resolver offers comprehensive functionalities for
      efficiently resolving DNS queries across AWS, the internet, and
      on-premises networks. It also enables secure management of DNS within your
      Amazon Virtual Private Cloud (VPC).
  - aid: amazon-web-services:amazon-lex
    name: Amazon Lex
    tags:
      - Alias
      - Bots
      - Content
      - Conversational
      - Names
      - Posts
      - Sessions
      - Text
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/lex/
    overlays:
      - url: overlays/runtimelex-openapi-search.yml
        type: APIs.io Search
      - url: overlays/runtimelex-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/lex/
        type: Documentation
      - url: openapi/runtimelex-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/lex/features/
        type: Features
      - url: https://aws.amazon.com/lex/pricing/
        type: Pricing
      - url: https://aws.amazon.com/lex/faqs/
        type: FAQ
      - url: https://aws.amazon.com/lex/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/lex/resources/
        type: Resources
      - url: https://aws.amazon.com/lex/customers/
        type: Customers
    description: |-

      Amazon Lex offers build and runtime endpoints, each with a specific set of
      operations. Your conversational bot utilizes the runtime API to interpret
      user input text or voice. For instance, if a user says "I want pizza," the
      bot sends this input to Amazon Lex via the runtime API. 
  - aid: amazon-web-services:amazon-cloudwatch-rum
    name: Amazon CloudWatch RUM
    tags:
      - ARN
      - Application Monitors
      - Applications
      - Data
      - Definitions
      - Destinations
      - Events
      - Metric Destination
      - Metrics
      - Monitors
      - Names
      - Resources
      - Rummetrics
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html
    overlays:
      - url: overlays/rum-openapi-search.yml
        type: APIs.io Search
      - url: overlays/rum-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html
        type: Documentation
      - url: openapi/rum-openapi-original.yml
        type: OpenAPI
    description: |-

      With Amazon CloudWatch RUM, you can monitor real user activities to gather
      client-side information on your web application's performance from live
      user sessions. This data includes load times, errors, and user actions.
      View this data in aggregated form or broken down by browsers and devices
      used by customers. Use this data to quickly pinpoint and resolve
      client-side performance issues.
  - aid: amazon-web-services:amazon-route-53-application-recovery-controller
    name: Amazon Route 53 Application Recovery Controller
    tags:
      - ARN
      - Associated
      - Checks
      - Clusters
      - Control Panels
      - Controls
      - Describe
      - Panels
      - Policies
      - Resources
      - Routing
      - Routing Controls
      - Rules
      - Safety
      - Safety Rules
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/route53/application-recovery-controller/
    overlays:
      - url: overlays/route53-recovery-control-config-openapi-search.yml
        type: APIs.io Search
      - url: >-

          overlays/route53-recovery-control-config-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/route53/application-recovery-controller/
        type: Documentation
      - url: openapi/route53-recovery-control-config-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon Route 53 Application Recovery Controller provides monitoring
      and coordination for application recovery across AWS Regions and
      Availability Zones. By streamlining the recovery process and reducing
      manual steps, this tool helps ensure that applications and resources are
      prepared for recovery. 
  - aid: amazon-web-services:aws-s3-control
    name: 'AWS S3 Control '
    tags:
      - ARN
      - Access
      - Access Grants Instances
      - Access Point
      - Async
      - Blocks
      - Buckets
      - Center
      - Configurations
      - Data
      - Data Access
      - Describe
      - Dissociate
      - Entitycenter
      - Grants
      - Grants""
      - Groups
      - Identity
      - Instances
      - Jobs
      - Lambda
      - Lens
      - Lifecycle
      - Lifecycle Configuration
      - Locations
      - Multi
      - Names
      - Objects
      - Operation
      - Points
      - Policies
      - Policy Status
      - Prefix
      - Priorities
      - Public
      - Regional
      - Regions
      - Replication
      - Resource Policies
      - Resources
      - Routes
      - Status
      - Storage
      - Storage Lens
      - Storage Lens Groups
      - Submit
      - Tagging
      - Tags
      - Tokens
      - Untag
      - Versioning
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html
    overlays:
      - url: overlays/s3control-openapi-search.yml
        type: APIs.io Search
      - url: overlays/s3control-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/AmazonS3/latest/API/API_Types_AWS_S3_Control.html
        type: Documentation
      - url: openapi/s3control-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Web Services S3 Control, allows users to perform control plane
      actions on Amazon S3.
  - aid: amazon-web-services:amazon-augmented-ai
    name: Amazon Augmented AI
    tags:
      - Describe
      - Human
      - Loops
      - Names
      - Stop
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/augmented-ai/
    overlays:
      - url: overlays/sagemaker-a2i-runtime-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sagemaker-a2i-runtime-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/augmented-ai/
        type: Documentation
      - url: openapi/sagemaker-a2i-runtime-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/augmented-ai/features/
        type: Features
      - url: https://aws.amazon.com/augmented-ai/pricing/
        type: Pricing
      - url: https://aws.amazon.com/augmented-ai/resources/
        type: Resources
      - url: https://aws.amazon.com/augmented-ai/faqs/
        type: FAQ
      - url: https://aws.amazon.com/augmented-ai/customers/
        type: Customers
    description: |-

      Amazon Augmented AI (Amazon A2I) enhances machine learning applications by
      incorporating human judgment when necessary. Human reviewers can step in
      when an AI application is unable to assess data confidently, through a
      process known as a human review workflow. 
  - aid: amazon-web-services:aws-sagemaker
    name: AWS SageMaker
    tags:
      - Workteam
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/sagemaker/
    overlays:
      - url: overlays/sagemaker-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sagemaker-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/sagemaker/
        type: Documentation
      - url: openapi/sagemaker-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/sagemaker/features/
        type: Features
      - url: https://aws.amazon.com/sagemaker/pricing/
        type: Pricing
      - url: https://aws.amazon.com/sagemaker/faqs/
        type: FAQ
      - url: https://aws.amazon.com/sagemaker/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/sagemaker/resources/
        type: Resources
      - url: https://aws.amazon.com/sagemaker/partners/
        type: Partners
      - url: https://aws.amazon.com/sagemaker/customers/
        type: Customers
    description: |-

      Amazon SageMaker is a fully managed service that provides a comprehensive
      set of tools for high-performance, cost-effective machine learning (ML)
      for any scenario. With SageMaker, you can create, train, and deploy ML
      models at scale using various tools like notebooks, debuggers, profilers,
      pipelines, MLOps, and more within a single integrated development
      environment (IDE).
  - aid: amazon-web-services:aws-s3
    name: AWS S3
    tags:
      - ACL
      - Accelerate
      - Access
      - Analytics
      - Attributes
      - Blocks
      - Buckets
      - Buckets
      - CORS
      - Configurations
      - Content
      - Controls
      - Copy
      - Directory
      - Encryption
      - Hold
      - Intelligent
      - Inventory
      - Key&select
      - Key+?acl
      - Key+?attributes
      - Key+?legal
      - Key+?restore
      - Key+?retention
      - Key+?tagging
      - Key+?torrent
      - Keys
      - Legal
      - Lifecycle
      - Locations
      - Locks
      - Logging
      - Metrics
      - Multipart
      - Notifications
      - Objects
      - Ownership
      - Payments
      - Policies
      - Public
      - Replication
      - Responses
      - Restore
      - Retention
      - Sessions
      - Status
      - Tagging
      - Tiering
      - Torrent
      - Types
      - Uploads
      - Versioning
      - Versions
      - Websites
      - Write
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/s3/
    overlays:
      - url: overlays/s3-openapi-search.yml
        type: APIs.io Search
      - url: overlays/s3-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/s3/
        type: Documentation
      - url: openapi/s3-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/s3/pricing/
        type: Pricing
      - url: https://aws.amazon.com/s3/security/
        type: Security
      - url: https://aws.amazon.com/s3/faqs/
        type: FAQ
      - url: https://aws.amazon.com/s3/features/
        type: Features
      - url: https://aws.amazon.com/s3/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/s3/videos/
        type: Videos
      - url: https://aws.amazon.com/s3/customers/
        type: Customers
      - url: https://aws.amazon.com/s3/resources/
        type: Resources
    description: |-

      The API for Amazon Simple Storage Service (Amazon S3) provides an object
      storage solution with top-notch scalability, data availability, security,
      and performance. It caters to customers of varying sizes and industries,
      offering the ability to store and secure any volume of data for a wide
      range of purposes, including data lakes, cloud-native applications, and
      mobile apps. 
  - aid: amazon-web-services:aws-sagemaker-edge
    name: AWS SageMaker Edge
    tags:
      - Deployments
      - Device
      - Registrations
      - Heart Beats
      - Send
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/greengrass/v2/developerguide/sagemaker-edge-manager-component.html
    overlays:
      - url: overlays/sagemaker-edge-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sagemaker-edge-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/greengrass/v2/developerguide/sagemaker-edge-manager-component.html
        type: Documentation
      - url: openapi/sagemaker-edge-openapi-original.yml
        type: OpenAPI
    description: |-

      The API for Amazon SageMaker Edge Manager
      (aws.greengrass.SageMakerEdgeManager) facilitates the installation of the
      SageMaker Edge Manager agent binary. This component enables edge device
      model management, allowing users to optimize, secure, monitor, and
      maintain machine learning models across fleets of edge devices. The
      SageMaker Edge Manager component takes care of installing and managing the
      SageMaker Edge Manager agent lifecycle on the core device. 
  - aid: amazon-web-services:amazon-sagemaker-feature-store
    name: Amazon SageMaker Feature Store
    tags:
      - Batches
      - Record
      - Feature
      - Groups
      - Names
      - Machine Learning
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/sagemaker/feature-store/
    overlays:
      - url: overlays/sagemaker-featurestore-runtime-openapi-search.yml
        type: APIs.io Search
      - url: >-

          overlays/sagemaker-featurestore-runtime-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/sagemaker/feature-store/
        type: Documentation
      - url: openapi/sagemaker-featurestore-runtime-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon SageMaker Feature Store is a fully managed repository
      specifically designed for storing, sharing, and managing features for
      machine learning (ML) models. Features are the inputs necessary for ML
      models during both training and inference. 
  - aid: amazon-web-services:amazon-s3-on-outposts
    name: Amazon S3 on Outposts
    tags:
      - Endpoints
      - Outposts
      - Shared
      - Storage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/s3/outposts/
    overlays:
      - url: overlays/s3outposts-openapi-search.yml
        type: APIs.io Search
      - url: overlays/s3outposts-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/s3/outposts/
        type: Documentation
      - url: openapi/s3outposts-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/outposts/rack/pricing/
        type: Pricing
      - url: https://aws.amazon.com/outposts/rack/resources/
        type: Resources
      - url: https://aws.amazon.com/outposts/rack/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/outposts/rack/faqs/
        type: FAQ
      - url: https://aws.amazon.com/outposts/partners/
        type: Partners
    description: |-

      Amazon S3 on Outposts delivers object storage to your on-premises AWS
      Outposts environment to meet local data processing and data residency
      needs. Using the S3 APIs and features, S3 on Outposts makes it easy to
      store, secure, tag, retrieve, report on, and control access to the data on
      your Outpost. AWS Outposts is a fully managed service that extends AWS
      infrastructure, services, and tools to virtually any data center,
      co-location space, or on-premises facility for a truly consistent hybrid
      experience
  - aid: amazon-web-services:amazon-sagemaker-metrics
    name: Amazon SageMaker Metrics
    tags:
      - Batches
      - Metrics
      - Data
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html
    overlays:
      - url: overlays/sagemaker-metrics-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sagemaker-metrics-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html
        type: Documentation
      - url: openapi/sagemaker-metrics-openapi-original.yml
        type: OpenAPI
    description: |-

      Contains all data plane API operations and data types for Amazon SageMaker
      Metrics. Use these APIs to put and retrieve (get) features related to your
      training run.    BatchPutMetrics
  - aid: amazon-web-services:geospatial-ml-with-amazon-sagemaker
    name: Geospatial ML with Amazon SageMaker
    tags:
      - ARN
      - Collections
      - Data
      - Earth
      - Enrichment
      - Exports
      - Jobs
      - Machine Learning
      - Models
      - Observation
      - Raster
      - Resources
      - Search
      - Stop
      - Tags
      - Tiles
      - Untag
      - Vectors
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/sagemaker/geospatial/
    overlays:
      - url: overlays/sagemaker-geospatial-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sagemaker-geospatial-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/sagemaker/geospatial/
        type: Documentation
      - url: openapi/sagemaker-geospatial-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/sagemaker/geospatial/features/
        type: Features
      - url: https://aws.amazon.com/sagemaker/geospatial/pricing/
        type: Pricing
      - url: https://aws.amazon.com/sagemaker/geospatial/resources/
        type: Resources
      - url: https://aws.amazon.com/sagemaker/geospatial/faqs/
        type: FAQ
      - url: https://aws.amazon.com/sagemaker/geospatial/customers/
        type: Customers
    description: |-

      Amazon SageMaker offers specialized machine learning features tailored for
      geospatial data analysis. With this API, users can easily create, train,
      and deploy ML models using geospatial data sources. Additionally, the API
      provides access to pre-built processing operations, pretrained ML models,
      and visualization tools, enabling users to run geospatial ML efficiently
      and on a large scale.
  - aid: amazon-web-services:aws-savings-plans
    name: AWS Savings Plans
    tags:
      - Describe
      - Offerings
      - Plan
      - Plans
      - Queued
      - Rates
      - Resources
      - Savings
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/savingsplans/
    overlays:
      - url: overlays/savingsplans-openapi-search.yml
        type: APIs.io Search
      - url: overlays/savingsplans-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/savingsplans/
        type: Documentation
      - url: openapi/savingsplans-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/savingsplans/faq/
        type: FAQ
      - url: https://aws.amazon.com/savingsplans/compute-pricing/
        type: Compute-pricing
      - url: https://aws.amazon.com/savingsplans/ml-pricing/
        type: Ml-pricing
      - url: https://aws.amazon.com/savingsplans/faq/
        type: FAQ
    description: |-

      Savings Plans is a flexible pricing model that can help you reduce your
      bill by up to 72% compared to On-Demand prices, in exchange for a one- or
      three-year hourly spend commitment. AWS offers three types of Savings
      Plans: Compute Savings Plans, EC2 Instance Savings Plans, and Amazon
      SageMaker.
  - aid: amazon-web-services:amazon-eventbridge-schema-registry
    name: Amazon EventBridge Schema Registry
    tags:
      - ARN
      - Binding
      - Code
      - Discover
      - Discovered
      - Discoverers
      - Events
      - Exports
      - Languages
      - Names
      - Policies
      - Registries
      - Resources
      - Schemas
      - Search
      - Sources
      - Stop
      - Tags
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html
    overlays:
      - url: overlays/schemas-openapi-search.yml
        type: APIs.io Search
      - url: overlays/schemas-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://example.com
        type: Documentation
      - url: openapi/schemas-openapi-original.yml
        type: OpenAPI
    description: |-

      EventBridge offers pre-defined schemas for events generated by AWS
      services, but you can also create custom schemas or infer them from events
      on an event bus. Once you have a schema, you can download code bindings
      for popular programming languages to accelerate development. You can
      manage schemas and work with code bindings from the EventBridge console,
      API, or directly in your IDE using AWS toolkits.
  - aid: amazon-web-services:amazon-eventbridge-scheduler
    name: Amazon EventBridge Scheduler
    tags:
      - ARN
      - Events
      - Groups
      - Names
      - Resources
      - Schedules
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/eventbridge/
    overlays:
      - url: overlays/scheduler-openapi-search.yml
        type: APIs.io Search
      - url: overlays/scheduler-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/eventbridge/
        type: Documentation
      - url: openapi/scheduler-openapi-original.yml
        type: OpenAPI
    description: |-

      The Amazon EventBridge Scheduler API is a serverless tool for scheduling
      and managing tasks in one centralized service. It reliably delivers tasks
      and adjusts schedules based on downstream target availability. This
      reference provides a list of available API actions and data types for
      EventBridge Scheduler.
  - aid: amazon-web-services:amazon-simpledb
    name: Amazon SimpleDB
    tags:
      - Databases
      - SQL
      - Selects
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/simpledb/
    overlays:
      - url: overlays/sdb-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sdb-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/simpledb/
        type: Documentation
      - url: openapi/sdb-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/simpledb/pricing/
        type: Pricing
      - url: https://aws.amazon.com/simpledb/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/simpledb/developer-resources/
        type: Developer-resources
      - url: https://aws.amazon.com/simpledb/faqs/
        type: FAQ
    description: |-

      This API, Amazon SimpleDB, is a cloud-based web service that offers
      essential database functionalities such as data indexing and querying. By
      handling the complex tasks of managing a web-scale database, SimpleDB
      empowers developers to concentrate on developing applications without
      worrying about database operations. 
  - aid: amazon-web-services:amazon-web-services-secrets-manager
    name: Amazon Web Services Secrets Manager
    tags:
      - Policies
      - Resources
      - Validate
      - Secrets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/secrets-manager/
    overlays:
      - url: overlays/secretsmanager-openapi-search.yml
        type: APIs.io Search
      - url: overlays/secretsmanager-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/secrets-manager/
        type: Documentation
      - url: openapi/secretsmanager-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/secrets-manager/features/
        type: Features
      - url: https://aws.amazon.com/secrets-manager/pricing/
        type: Pricing
      - url: https://aws.amazon.com/secrets-manager/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/secrets-manager/resources/
        type: Resources
      - url: https://aws.amazon.com/secrets-manager/faqs/
        type: FAQ
      - url: https://aws.amazon.com/secrets-manager/customers/
        type: Customers
    description: |-

      The AWS Secrets Manager API allows users to securely manage, fetch, and
      update database credentials, API keys, and other sensitive information at
      various stages of their existence.
  - aid: amazon-web-services:aws-serverless-application-repository
    name: AWS Serverless Application Repository
    tags:
      - Applications
      - Change
      - Change Sets
      - Cloud
      - Dependencies
      - Formation
      - Policies
      - Semantic
      - Sets
      - Templates
      - Unshare
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/serverless/serverlessrepo/
    overlays:
      - url: overlays/serverlessrepo-openapi-search.yml
        type: APIs.io Search
      - url: overlays/serverlessrepo-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/serverless/serverlessrepo/
        type: Documentation
      - url: openapi/serverlessrepo-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/serverless/serverlessrepo/publishing/
        type: Publishing
      - url: https://aws.amazon.com/serverless/serverlessrepo/resources/
        type: Resources
      - url: https://aws.amazon.com/serverless/serverlessrepo/faqs/
        type: FAQ
    description: |-

      The AWS Serverless Application Repository simplifies the process for
      developers and businesses to discover and deploy serverless applications
      in the AWS Cloud. This integration with the AWS Lambda console allows
      developers of all skill levels to easily start with serverless computing. 
  - aid: amazon-web-services:amazon-security-lake
    name: Amazon Security Lake
    tags:
      - ARN
      - Administrator
      - Configurations
      - Custom
      - Data
      - Data Lakes
      - Delegate
      - Delegated
      - Exceptions
      - Lakes
      - Log Sources
      - Logs
      - Names
      - Notifications
      - Organizations
      - Register
      - Resources
      - Sources
      - Subscribers
      - Subscriptions
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/security-lake/
    overlays:
      - url: overlays/securitylake-openapi-search.yml
        type: APIs.io Search
      - url: overlays/securitylake-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/security-lake/
        type: Documentation
      - url: openapi/securitylake-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/security-lake/features/
        type: Features
      - url: https://aws.amazon.com/security-lake/pricing/
        type: Pricing
      - url: https://aws.amazon.com/security-lake/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/security-lake/faqs/
        type: FAQ
      - url: https://aws.amazon.com/security-lake/customers/
        type: Customers
      - url: https://aws.amazon.com/security-lake/resources/
        type: Resources
      - url: https://aws.amazon.com/security-lake/partners/
        type: Partners
    description: |-

      Amazon Security Lake is a fully managed security data lake service. You
      can use Security Lake to automatically centralize security data from
      cloud, on-premises, and custom sources into a data lake that's stored in
      your Amazon Web Services account. Amazon Web Services Organizations is an
      account management service that lets you consolidate multiple Amazon Web
      Services accounts into an organization that you create and centrally
      manage. 
  - aid: amazon-web-services:aws-service-quotas
    name: AWS Service Quotas
    tags:
      - Resources
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html
    overlays:
      - url: overlays/service-quotas-openapi-search.yml
        type: APIs.io Search
      - url: overlays/service-quotas-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html
        type: Documentation
      - url: openapi/service-quotas-openapi-original.yml
        type: OpenAPI
    description: |-

      Easily monitor and control your quotas as your Amazon Web Services
      projects expand with Service Quotas. Limits, also known as quotas, define
      the maximum number of resources you can generate within your AWS account. 
  - aid: amazon-web-services:aws-cloud-map
    name: AWS Cloud Map
    tags:
      - Services
      - Clouds
      - Maps
      - DNS
      - Namespaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/cloud-map/
    overlays:
      - url: overlays/servicediscovery-openapi-search.yml
        type: APIs.io Search
      - url: overlays/servicediscovery-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/cloud-map/
        type: Documentation
      - url: openapi/servicediscovery-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/cloud-map/features/
        type: Features
      - url: https://aws.amazon.com/cloud-map/pricing/
        type: Pricing
      - url: https://aws.amazon.com/cloud-map/faqs/
        type: FAQ
    description: |-

      Our Cloud Map API allows you to easily set up and manage public DNS,
      private DNS, or HTTP namespaces for your microservice applications. By
      registering instances with Cloud Map via the API, you can ensure seamless
      integration and availability. Cloud Map automatically creates DNS records
      and optional health checks for public or private DNS namespaces, providing
      clients with up to eight healthy records in response to queries or
      requests.
  - aid: amazon-web-services:aws-service-catalog
    name: AWS Service Catalog
    tags:
      - ARN
      - Applications
      - Associated
      - Attributes
      - Configurations
      - Details
      - Disassociate
      - Groups
      - Resources
      - Sync
      - Tags
      - Types
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/servicecatalog/
    overlays:
      - url: overlays/servicecatalog-appregistry-openapi-search.yml
        type: APIs.io Search
      - url: overlays/servicecatalog-appregistry-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/servicecatalog/
        type: Documentation
      - url: openapi/servicecatalog-appregistry-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS Service Catalog enables IT administrators to create, manage, and
      distribute portfolios of approved products to end users, who can then
      access the products they need in a personalized portal. Typical products
      include servers, databases, websites, or applications that are deployed
      using AWS resources (for example, an Amazon EC2 instance or an Amazon RDS
      database). 
  - aid: amazon-web-services:aws-shield-advanced
    name: AWS Shield Advanced
    tags:
      - Subscriptions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/shield/
    overlays:
      - url: overlays/shield-openapi-search.yml
        type: APIs.io Search
      - url: overlays/shield-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/shield/
        type: Documentation
      - url: openapi/shield-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/shield/features/
        type: Features
      - url: https://aws.amazon.com/shield/pricing/
        type: Pricing
      - url: https://aws.amazon.com/shield/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/shield/resources/
        type: Resources
    description: |-

      The Shield Advanced API Reference is a comprehensive guide for developers
      seeking detailed information on the Shield Advanced API actions, data
      types, and errors. To learn more about the WAF and Shield Advanced
      features and how to effectively utilize the APIs, refer to the WAF and
      Shield Developer Guide.
  - aid: amazon-web-services:aws-simspace-weaver
    name: 'AWS SimSpace Weaver '
    tags:
      - ARN
      - Applications
      - Clock
      - Describe
      - Resources
      - Simulations
      - Snapshots
      - Start Application
      - Start Clock
      - Start Simulation
      - Stop
      - Stop APplication
      - Stop Clock
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/simspaceweaver/
    overlays:
      - url: overlays/simspaceweaver-openapi-search.yml
        type: APIs.io Search
      - url: overlays/simspaceweaver-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/simspaceweaver/
        type: Documentation
      - url: openapi/simspaceweaver-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/simspaceweaver/features/
        type: Features
      - url: https://aws.amazon.com/simspaceweaver/pricing/
        type: Pricing
      - url: https://aws.amazon.com/simspaceweaver/resources/
        type: Resources
    description: |-

      SimSpace Weaver is a cloud-based service on Amazon Web Services that
      enables users to construct and deploy large spatial simulations. These
      simulations can include crowd scenarios, real-world environments, and
      immersive experiences. The SimSpace Weaver API allows direct interaction
      with the service, providing detailed descriptions of available operations
      and data structures. 
  - aid: amazon-web-services:aws-application-migration-service
    name: AWS Application Migration Service
    tags:
      - Jobs
      - Replication
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/application-migration-service/
    overlays:
      - url: overlays/sms-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sms-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/application-migration-service/
        type: Documentation
      - url: openapi/sms-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/application-migration-service/pricing/
        type: Pricing
      - url: https://aws.amazon.com/application-migration-service/faqs/
        type: FAQ
      - url: https://aws.amazon.com/application-migration-service/resources/
        type: Resources
    description: |-

      The AWS Application Migration Service streamlines the migration process by
      automating the conversion of source servers to run on AWS, reducing manual
      errors and saving time. It also offers a range of built-in and custom
      optimization options to simplify application modernization.
  - aid: amazon-web-services:aws-snow-family
    name: AWS Snow Family
    tags:
      - ARN
      - Cancel
      - Describe
      - Device
      - Devices
      - EC2
      - Ec2Instances
      - Execution
      - Executions
      - Managed
      - Resources
      - Tags
      - Tasks
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/snow/
    overlays:
      - url: overlays/snow-device-management-openapi-search.yml
        type: APIs.io Search
      - url: overlays/snow-device-management-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/snow/
        type: Documentation
      - url: openapi/snow-device-management-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/snow/faqs/
        type: FAQ
    description: |-

      The AWS Snow Family helps customers who need to run operations in austere,
      non-data center environments, and in locations which lack consistent
      network connectivity. The Snow Family (comprised of AWS Snowcone,
      Snowball, and AWS Snowmobile) offers a number of physical devices and
      capacity profiles, most with built-in computing capabilities.
  - aid: amazon-web-services:aws-security-hub
    name: AWS Security Hub
    tags:
      - ARN
      - Accounts
      - Actions
      - Administrative
      - Administrator
      - Aggregator
      - Aggregators
      - Associate
      - Associations
      - Automation
      - Automation Rules
      - Batches
      - Configurations
      - Controls
      - Count
      - Decline
      - Definitions
      - Deregister
      - Describe
      - Disable
      - Disassociate
      - Disassociation
      - Enable
      - Enabled
      - Findings
      - History
      - Hub
      - Import
      - Insights
      - Invitations
      - Invite
      - Master
      - Members
      - Organizations
      - Policies
      - Products
      - Register
      - Resources
      - Results
      - Rules
      - Security
      - Standards
      - Subscriptions
      - Tags
      - Targets
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/security-hub/
    overlays:
      - url: overlays/securityhub-openapi-search.yml
        type: APIs.io Search
      - url: overlays/securityhub-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/security-hub/
        type: Documentation
      - url: openapi/securityhub-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/security-hub/features/
        type: Features
      - url: https://aws.amazon.com/security-hub/pricing/
        type: Pricing
      - url: https://aws.amazon.com/security-hub/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/security-hub/resources/
        type: Resources
      - url: https://aws.amazon.com/security-hub/faqs/
        type: FAQ
      - url: https://aws.amazon.com/security-hub/customers/
        type: Customers
      - url: https://aws.amazon.com/security-hub/partners/
        type: Partners
    description: |-

      The Security Hub API offers a comprehensive view of your security state
      within Amazon Web Services, allowing you to assess your environment
      against industry standards and best practices. By collecting security data
      across AWS accounts and third-party products, Security Hub enables
      analysis of security trends and identification of high-priority issues.
  - aid: amazon-web-services:amazon-simple-notification-service
    name: Amazon Simple Notification Service
    tags:
      - Numbers
      - Phone
      - SMSSandbox
      - Verify
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/sns/
    overlays:
      - url: overlays/sns-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sns-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/sns/
        type: Documentation
      - url: openapi/sns-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/sns/features/
        type: Features
      - url: https://aws.amazon.com/sns/pricing/
        type: Pricing
      - url: https://aws.amazon.com/sns/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/sns/resources/
        type: Resources
    description: |-

      The Amazon Simple Notification Service (Amazon SNS) is a web service that
      allows developers to create distributed web-enabled applications. With
      Amazon SNS, applications can easily send real-time notification messages
      to subscribers using multiple delivery protocols. 
  - aid: amazon-web-services:amazon-simple-queue-service
    name: Amazon Simple Queue Service
    tags:
      - Queues
      - Untag
      - Tags
      - Microservices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/sqs/
    overlays:
      - url: overlays/sqs-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sqs-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/sqs/
        type: Documentation
      - url: openapi/sqs-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/sqs/features/
        type: Features
      - url: https://aws.amazon.com/sqs/pricing/
        type: Pricing
      - url: https://aws.amazon.com/sqs/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/sqs/resources/
        type: Resources
      - url: https://aws.amazon.com/sqs/faqs/
        type: FAQ
    description: |-

      Introducing the Amazon SQS API Reference, a reliable and highly-scalable
      hosted queue that facilitates the storage and transmission of messages
      between applications and microservices. Amazon SQS effectively moves data
      between distributed components, promoting decoupling. 
  - aid: amazon-web-services:aws-service-catalog
    name: AWS Service Catalog
    tags:
      - Options
      - Tags
      - Catalogs
      - Services
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/servicecatalog/
    overlays:
      - url: overlays/servicecatalog-openapi-search.yml
        type: APIs.io Search
      - url: overlays/servicecatalog-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/servicecatalog/
        type: Documentation
      - url: openapi/servicecatalog-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/servicecatalog/features/
        type: Features
      - url: https://aws.amazon.com/servicecatalog/pricing/
        type: Pricing
      - url: https://aws.amazon.com/servicecatalog/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/servicecatalog/resources/
        type: Resources
      - url: https://aws.amazon.com/servicecatalog/faqs/
        type: FAQ
      - url: https://aws.amazon.com/servicecatalog/customers/
        type: Customers
      - url: https://aws.amazon.com/servicecatalog/partners/
        type: Partners
    description: |-

      AWS Service Catalog is a tool that allows you to efficiently handle your
      cloud resources by overseeing your infrastructure as code (IaC) templates,
      which can be written in either CloudFormation or Terraform configurations.
      This service helps you maintain compliance standards while enabling your
      customers to easily deploy the necessary cloud resources.
  - aid: amazon-web-services:aws-systems-manager
    name: AWS Systems Manager
    tags:
      - Services
      - Settings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/systems-manager/
    overlays:
      - url: overlays/ssm-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ssm-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/systems-manager/
        type: Documentation
      - url: openapi/ssm-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/systems-manager/features/
        type: Features
      - url: https://aws.amazon.com/systems-manager/pricing/
        type: Pricing
      - url: https://aws.amazon.com/systems-manager/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/systems-manager/faq/
        type: FAQ
      - url: https://aws.amazon.com/systems-manager/customers/
        type: Customers
      - url: https://aws.amazon.com/systems-manager/partners/
        type: Partners
    description: |-

      AWS Systems Manager provides a comprehensive and secure management
      solution for resources across AWS and in both multicloud and hybrid
      environments.
  - aid: amazon-web-services:aws-signer
    name: AWS Signer
    tags:
      - ARN
      - Describe
      - Jobs
      - Names
      - Payload
      - Permission
      - Permissions
      - Platforms
      - Profiles
      - Removes
      - Resources
      - Revocations
      - Revoke
      - Sign
      - Signatures
      - Signing
      - Statements
      - Status
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/signer/
    overlays:
      - url: overlays/signer-openapi-search.yml
        type: APIs.io Search
      - url: overlays/signer-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/signer/
        type: Documentation
      - url: openapi/signer-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS Signer is a managed code-signing service designed to ensure the trust
      and integrity of your code. This service supports code signing for various
      applications such as AWS Lambda, IoT devices supported by AWS, and
      container images stored in registries like Amazon Elastic Container
      Registry (ECR). With AWS Signer, you can create signing profiles and use
      them to sign Lambda deployment packages, IoT device code updates, and
      container images. Integrated support is provided for services like Amazon
      S3, Amazon CloudWatch, and AWS CloudTrail. For more details on how to use
      AWS Signer, refer to the AWS Signer Developer Guide.
  - aid: amazon-web-services:aws-systems-manager-incident-manager
    name: AWS Systems Manager Incident Manager
    tags:
      - ARN
      - Batches
      - Deletion
      - Events
      - Findings
      - Incident
      - Items
      - Plan
      - Plans
      - Policies
      - Protection
      - Record
      - Records
      - Related
      - Replication
      - Resources
      - Responses
      - Sets
      - Tags
      - Timeline
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html
    overlays:
      - url: overlays/ssm-incidents-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ssm-incidents-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html
        type: Documentation
      - url: openapi/ssm-incidents-openapi-original.yml
        type: OpenAPI
    description: |-

      This API, Systems Manager Incident Manager, is a comprehensive incident
      management tool specifically designed to assist users in dealing with
      unforeseen interruptions or service disruptions in their Amazon Web
      Services-hosted applications. The platform aims to enhance incident
      resolution by promptly alerting responders of the impact, presenting key
      troubleshooting information, and offering collaborative features to
      facilitate the swift restoration of services. 
  - aid: amazon-web-services:aws-iam-identity-center
    name: AWS IAM Identity Center
    tags:
      - Credentials
      - Federation
      - Roles
      - Accounts
      - Assignment
      - Logout
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/iam/identity-center/
    overlays:
      - url: overlays/sso-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sso-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/iam/identity-center/
        type: Documentation
      - url: openapi/sso-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/iam/identity-center/features/
        type: Features
      - url: https://aws.amazon.com/iam/identity-center/faqs/
        type: FAQ
      - url: https://aws.amazon.com/iam/identity-center/resources/
        type: Resources
    description: |-

      The AWS IAM Identity Center Portal is a web service that simplifies the
      assignment of user access to IAM Identity Center resources, such as the
      AWS access portal. Users can have AWS account applications and roles
      assigned to them and be federated into the application. 
  - aid: amazon-web-services:aws-systems-manager-for-sap
    name: AWS Systems Manager for SAP
    tags:
      - ARN
      - Applications
      - Components
      - Databases
      - Deregister
      - Operation
      - Operations
      - Permission
      - Refresh
      - Register
      - Resources
      - Settings
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/ssm-sap/latest/userguide/what-is-ssm-for-sap.html
    overlays:
      - url: overlays/ssm-sap-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ssm-sap-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/ssm-sap/latest/userguide/what-is-ssm-for-sap.html
        type: Documentation
      - url: openapi/ssm-sap-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS Systems Manager for SAP is a tool designed to automate the management
      and operation of SAP applications on AWS. This integration allows for
      seamless communication between AWS services and SAP applications running
      on AWS. Users can easily access and utilize AWS Systems Manager for SAP
      through AWS APIs.
  - aid: amazon-web-services:aws-step-functions
    name: AWS Step Functions
    tags:
      - Alias
      - Machines
      - States
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/step-functions/
    overlays:
      - url: overlays/states-openapi-search.yml
        type: APIs.io Search
      - url: overlays/states-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/step-functions/
        type: Documentation
      - url: openapi/states-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/step-functions/features/
        type: Features
      - url: https://aws.amazon.com/step-functions/pricing/
        type: Pricing
      - url: https://aws.amazon.com/step-functions/use-cases/
        type: Use Cases
      - url: https://aws.amazon.com/step-functions/customers/
        type: Customers
      - url: https://aws.amazon.com/step-functions/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/step-functions/faqs/
        type: FAQ
    description: |-

      This API, AWS Step Functions, is a tool that allows developers to easily
      create visual workflows for utilizing AWS services, building distributed
      applications, automating processes, orchestrating microservices, and
      setting up data and machine learning pipelines.
  - aid: amazon-web-services:aws-storage-gateway-service
    name: AWS Storage Gateway Service
    tags:
      - Types
      - VTLDevice
      - Storage
      - Gateway
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/storagegateway/
    overlays:
      - url: overlays/storagegateway-openapi-search.yml
        type: APIs.io Search
      - url: overlays/storagegateway-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/storagegateway/
        type: Documentation
      - url: openapi/storagegateway-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/storagegateway/pricing/
        type: Pricing
      - url: https://aws.amazon.com/storagegateway/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/storagegateway/developer-resources/
        type: Developer-resources
      - url: https://aws.amazon.com/storagegateway/faqs/
        type: FAQ
      - url: https://aws.amazon.com/storagegateway/customers/
        type: Customers
      - url: https://aws.amazon.com/storagegateway/features/
        type: Features
    description: |-

      The Storage Gateway Service API allows seamless and secure integration
      between on-premises software appliances and cloud-based storage within
      Amazon Web Services infrastructure. This service enables cost-effective
      backup and rapid disaster recovery by allowing secure data uploads to the
      AWS cloud. 
  - aid: amazon-web-services:aws-supply-chain
    name: AWS Supply Chain
    tags:
      - Bill
      - Configurations
      - Import
      - Instances
      - Jobs
      - Materials
      - Supply Chain
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/aws-supply-chain/
    overlays:
      - url: overlays/supplychain-openapi-search.yml
        type: APIs.io Search
      - url: overlays/supplychain-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/aws-supply-chain/
        type: Documentation
      - url: openapi/supplychain-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/aws-supply-chain/features/
        type: Features
      - url: https://aws.amazon.com/aws-supply-chain/pricing/
        type: Pricing
      - url: https://aws.amazon.com/aws-supply-chain/partners/
        type: Partners
      - url: https://aws.amazon.com/aws-supply-chain/resources/
        type: Resources
    description: |-

      The AWS Supply Chain API is a cloud-based application designed to
      streamline supply chain management processes by connecting and extracting
      inventory, supply, and demand data from existing ERP and supply chain
      systems into a single data model. This API supports configuration data
      import for Supply Planning and all operations are authenticated and signed
      by Amazon certificates. The use of the AWS SDK is required, along with AWS
      Identity and Access Management users and roles to ensure secure access and
      permission policies.
  - aid: amazon-web-services:aws-security-token-service
    name: AWS Security Token Service
    tags:
      - Sessions
      - Tokens
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html
    overlays:
      - url: overlays/sts-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sts-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html
        type: Documentation
      - url: openapi/sts-openapi-original.yml
        type: OpenAPI
    description: |-

      Introducing the Security Token Service (STS) API, which allows you to
      conveniently request temporary, restricted-access credentials for your
      users. This documentation offers comprehensive explanations of the STS API
      functionality, with detailed instructions on how to utilize this service
      effectively. For further insights on using temporary security credentials,
      refer to the resources on Temporary Security Credentials.
  - aid: amazon-web-services:amazon-simple-workflow-service
    name: Amazon Simple Workflow Service
    tags:
      - Resources
      - Untag
      - Tags
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/swf/
    overlays:
      - url: overlays/swf-openapi-search.yml
        type: APIs.io Search
      - url: overlays/swf-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/swf/
        type: Documentation
      - url: openapi/swf-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/swf/pricing/
        type: Pricing
      - url: https://aws.amazon.com/swf/testimonials/
        type: Testimonials
      - url: https://aws.amazon.com/swf/developer-resources/
        type: Developer-resources
      - url: https://aws.amazon.com/swf/faqs/
        type: FAQ
      - url: https://aws.amazon.com/swf/getting-started/
        type: Getting-started
    description: |-

      The Amazon Simple Workflow Service (Amazon SWF) simplifies the process of
      building cloud-based applications that require coordination between
      distributed components. Tasks in Amazon SWF represent individual units of
      work within a workflow, with the service handling the management of
      intertask dependencies, scheduling, and concurrency to maintain the
      logical flow of the application.
  - aid: amazon-web-services:amazon-cloudwatch-synthetics
    name: Amazon CloudWatch Synthetics
    tags:
      - ARN
      - Associate
      - Associated
      - Canaries
      - Canary
      - Describe
      - Disassociate
      - Groups
      - Last
      - Names
      - Resources
      - Runs
      - Runtime
      - Stop
      - Tags
      - Untag
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/cloudwatch/
    overlays:
      - url: overlays/synthetics-openapi-search.yml
        type: APIs.io Search
      - url: overlays/synthetics-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://example.com
        type: Documentation
      - url: openapi/synthetics-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon CloudWatch Synthetics provides a way to continuously monitor your
      services by creating and managing canaries. These canaries are lightweight
      scripts that monitor your endpoints and APIs externally, allowing you to
      set them up to run 24/7, once per minute.
  - aid: amazon-web-services:amazon-timestream-query
    name: Amazon Timestream Query
    tags:
      - Queries
      - Scheduled
      - time Series
      - Analytics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/timestream/
    overlays:
      - url: overlays/timestream-query-openapi-search.yml
        type: APIs.io Search
      - url: overlays/timestream-query-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/timestream/
        type: Documentation
      - url: openapi/timestream-query-openapi-original.yml
        type: OpenAPI
    description: |-

      Easily store and analyze sensor data for IoT applications, metrics for
      DevOps use cases, and telemetry for application monitoring scenarios like
      clickstream data analysis with Amazon Timestream for LiveAnalytics. This
      managed time-series database engine allows developers and DevOps teams to
      run InfluxDB databases on AWS using open-source APIs for real-time
      time-series applications. 
  - aid: amazon-web-services:amazon-textract
    name: Amazon Textract
    tags:
      - Adapter
      - Content
      - OCR
      - PDF
      - Tables
      - Forms
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/textract/
    overlays:
      - url: overlays/textract-openapi-search.yml
        type: APIs.io Search
      - url: overlays/textract-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/textract/
        type: Documentation
      - url: openapi/textract-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/textract/pricing/
        type: Pricing
      - url: https://aws.amazon.com/textract/resources/
        type: Resources
      - url: https://aws.amazon.com/textract/faqs/
        type: FAQ
      - url: https://aws.amazon.com/textract/customers/
        type: Customers
      - url: https://aws.amazon.com/textract/partners/
        type: Partners
      - url: https://aws.amazon.com/textract/features/
        type: Features
    description: |-

      Amazon Textract is an advanced machine learning service that effortlessly
      extracts text, handwriting, layout elements, and data from scanned
      documents. Unlike traditional OCR tools, Textract can intelligently
      identify and extract specific data from various types of documents,
      including PDFs, images, tables, and forms. 
  - aid: amazon-web-services:amazon-timestream-write
    name: Amazon Timestream Write
    tags:
      - Records
      - Write
      - Database
      - Time-Series
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/timestream/
    overlays:
      - url: overlays/timestream-write-openapi-search.yml
        type: APIs.io Search
      - url: overlays/timestream-write-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/timestream/
        type: Documentation
      - url: openapi/timestream-write-openapi-original.yml
        type: OpenAPI
    description: |-

      Amazon Timestream is a powerful time-series database service designed for
      storing and analyzing large volumes of time-series data. It is fully
      managed and scalable, allowing you to easily store and analyze trillions
      of data points per day. Timestream is ideal for IoT sensor data analysis,
      industrial telemetry management, and log data and metric analysis for
      application performance improvement. 
  - aid: amazon-web-services:aws-transfer
    name: AWS Transfer
    tags:
      - Users
      - Transfers
      - FTP
      - FTPS
      - SFTP
      - AS2
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/aws-transfer-family/
    overlays:
      - url: overlays/transfer-openapi-search.yml
        type: APIs.io Search
      - url: overlays/transfer-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/aws-transfer-family/
        type: Documentation
      - url: openapi/transfer-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/aws-transfer-family/pricing/
        type: Pricing
      - url: https://aws.amazon.com/aws-transfer-family/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/aws-transfer-family/resources/
        type: Resources
      - url: https://aws.amazon.com/aws-transfer-family/faqs/
        type: FAQ
      - url: https://aws.amazon.com/aws-transfer-family/customers/
        type: Customers
      - url: https://aws.amazon.com/aws-transfer-family/partners/
        type: Partners
    description: |-

      Transfer Family is a managed service that allows for the transfer of files
      via FTP, FTPS, SFTP, and AS2 directly to and from Amazon S3 or Amazon EFS.
      Amazon Web Services facilitates the seamless migration of file transfer
      workflows to Transfer Family by integrating with existing authentication
      systems and providing DNS routing via Amazon Route 53. 
  - aid: amazon-web-services:amazon-transcribe
    name: Amazon Transcribe
    tags:
      - Analytics
      - Call
      - Stream
      - Transcriptions
      - Medical
      - Healthcare
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/transcribe/
    overlays:
      - url: overlays/transcribe-streaming-openapi-search.yml
        type: APIs.io Search
      - url: overlays/transcribe-streaming-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/transcribe/
        type: Documentation
      - url: openapi/transcribe-streaming-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/transcribe/features/
        type: Features
      - url: https://aws.amazon.com/transcribe/pricing/
        type: Pricing
      - url: https://aws.amazon.com/transcribe/getting-started/
        type: Getting-started
      - url: https://aws.amazon.com/transcribe/resources/
        type: Resources
      - url: https://aws.amazon.com/transcribe/faqs/
        type: FAQ
      - url: https://aws.amazon.com/transcribe/customers/
        type: Customers
    description: |-

      The Amazon Transcribe streaming API provides real-time transcription
      services in three main categories: Standard, Medical, and Call Analytics.
      Standard transcriptions are suitable for general use cases, while Medical
      transcriptions are specialized for medical professionals and incorporate
      medical terminology. The Call Analytics option is specifically designed
      for call center audio, providing insights into customer service
      interactions.
  - aid: amazon-web-services:aws-telco-network-builder
    name: AWS Telco Network Builder
    tags:
      - ARN
      - Ate
      - Cancel
      - Content
      - Descriptions
      - Descriptors
      - Functions
      - Info
      - Instances
      - Instantiate
      - Networks
      - Occs
      - Operation
      - Operations
      - Packages
      - Resources
      - Tags
      - Terminate
      - Untag
      - Validate
      - Tags
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/tnb/
    overlays:
      - url: overlays/tnb-openapi-search.yml
        type: APIs.io Search
      - url: overlays/tnb-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/tnb/
        type: Documentation
      - url: openapi/tnb-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/tnb/features/
        type: Features
      - url: https://aws.amazon.com/tnb/pricing/
        type: Pricing
      - url: https://aws.amazon.com/tnb/faqs/
        type: FAQ
    description: |-

      The Amazon Web Services Telco Network Builder (TNB) is a network
      automation service designed to assist in the deployment and management of
      telecom networks. With AWS TNB, users can efficiently manage the lifecycle
      of their telecommunication network functions, from initial planning to
      deployment and ongoing maintenance.
  - aid: amazon-web-services:aws-translate
    name: AWS Translate
    tags:
      - Data
      - Parallel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/translate/
    overlays:
      - url: overlays/translate-openapi-search.yml
        type: APIs.io Search
      - url: overlays/translate-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/translate/
        type: Documentation
      - url: openapi/translate-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/translate/details/
        type: Features
      - url: https://aws.amazon.com/translate/pricing/
        type: Pricing
      - url: https://aws.amazon.com/translate/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/translate/resources/
        type: Resources
      - url: https://aws.amazon.com/translate/faqs/
        type: FAQ
      - url: https://aws.amazon.com/translate/customers/
        type: Customers
    description: |-

      Amazon Translate enables users to adapt content for a global audience and
      efficiently translate and analyze a large amount of text to facilitate
      communication across different languages.
  - aid: amazon-web-services:amazon-verified-permissions
    name: Amazon Verified Permissions
    tags:
      - Policies
      - Templates
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/verified-permissions/
    overlays:
      - url: overlays/verifiedpermissions-openapi-search.yml
        type: APIs.io Search
      - url: overlays/verifiedpermissions-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/verified-permissions/
        type: Documentation
      - url: openapi/verifiedpermissions-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/verified-permissions/features/
        type: Features
      - url: https://aws.amazon.com/verified-permissions/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/verified-permissions/pricing/
        type: Pricing
      - url: https://aws.amazon.com/verified-permissions/resources/
        type: Resources
      - url: https://aws.amazon.com/verified-permissions/faqs/
        type: FAQ
      - url: https://aws.amazon.com/verified-permissions/partners/
        type: Partners
    description: |-

      Amazon Web Services offers Amazon Verified Permissions, a comprehensive
      permissions management service for applications. By utilizing Verified
      Permissions, developers can control user access through authorization
      based on various factors such as user information, resource attributes,
      and requested actions. This service allows for the creation and storage of
      authorization policies using the Cedar policy language, supporting both
      role-based access control (RBAC) and attribute-based access control (ABAC)
      models. 
  - aid: amazon-web-services:aws-trustedadvisor
    name: AWS TrustedAdvisor
    tags:
      - Organizations
      - Recommendations
      - Checks
      - Accounts
      - Resources
      - Lifecycle
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
    overlays:
      - url: overlays/trustedadvisor-openapi-search.yml
        type: APIs.io Search
      - url: overlays/trustedadvisor-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
        type: Documentation
      - url: openapi/trustedadvisor-openapi-original.yml
        type: OpenAPI
    description: |-

      The AWS Trusted Advisor API offers a comprehensive solution to help users
      optimize costs, enhance performance, bolster security and resilience, and
      effectively operate in the cloud at scale. By continuously assessing your
      AWS environment against industry best practices in categories like cost
      optimization, performance, resilience, security, operational excellence,
      and service limits, Trusted Advisor provides actionable recommendations to
      address any areas of concern.
  - aid: amazon-web-services:amazon-vpc-lattice
    name: Amazon VPC Lattice
    tags:
      - ARN
      - Access
      - Access Log Subscriptions
      - Associations
      - Authentication
      - Authpolicy
      - Deregister
      - Deregister Targets
      - Groups
      - Listeners
      - Logs
      - Networks
      - Policies
      - Register
      - Registertargets
      - Resource Policies
      - Resources
      - Rules
      - Service Network Service Associations
      - Service Network VPC Associations
      - Service Networks
      - Services
      - Subscriptions
      - Tags
      - Target Groups
      - Targets
      - Untag
      - VPC
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/vpc/lattice/
    overlays:
      - url: overlays/vpc-lattice-openapi-search.yml
        type: APIs.io Search
      - url: overlays/vpc-lattice-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/vpc/lattice/
        type: Documentation
      - url: openapi/vpc-lattice-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/vpc/lattice/features/
        type: Features
      - url: https://aws.amazon.com/vpc/lattice/pricing/
        type: Pricing
      - url: https://aws.amazon.com/vpc/lattice/faqs/
        type: FAQ
    description: |-

      The Amazon VPC Lattice API is a comprehensive managed application
      networking service designed to seamlessly connect, secure, and monitor all
      services within your organization's various accounts and virtual private
      clouds. By providing a logical boundary for interconnecting microservices
      and legacy services, Amazon VPC Lattice enhances the efficiency of
      discovery and management. Consult the Amazon VPC Lattice User Guide for
      further details.
  - aid: amazon-web-services:aws-waf-classic
    name: AWS WAF Classic
    tags:
      - Match
      - Sets
      - Firewalls
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html
    overlays:
      - url: overlays/waf-openapi-search.yml
        type: APIs.io Search
      - url: overlays/waf-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html
        type: Documentation
      - url: openapi/waf-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS WAF Classic is a web application firewall that allows you to monitor
      HTTP and HTTPS requests directed towards Amazon API Gateway API, Amazon
      CloudFront, or an Application Load Balancer. Additionally, AWS WAF Classic
      enables you to manage access to your content by setting conditions such as
      originating IP addresses or query string values. 
  - aid: amazon-web-services:amazon-connect-voice-id
    name: Amazon Connect Voice ID
    tags:
      - Watchlist
      - Voice
      - Machine Learning
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/connect/voice-id/
    overlays:
      - url: overlays/voice-id-openapi-search.yml
        type: APIs.io Search
      - url: overlays/voice-id-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/connect/voice-id/
        type: Documentation
      - url: openapi/voice-id-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/connect/features/
        type: Features
    description: |-

      Amazon Connect Voice ID is a cutting-edge feature within Amazon Connect
      that leverages machine learning technology to revolutionize caller
      authentication and fraud prevention in voice interactions. While
      traditional contact centers rely on time-consuming knowledge-based
      authentication methods, Voice ID uses the caller's unique voice
      characteristics to provide instant and accurate caller verification at a
      minimal cost. 
  - aid: amazon-web-services:aws-waf-classic-regional
    name: AWS WAF Classic Regional
    tags:
      - Match
      - Sets
      - Firewalls
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: >-

      https://docs.aws.amazon.com/waf/latest/APIReference/API_Operations_AWS_WAF_Regional.html
    overlays:
      - url: overlays/waf-regional-openapi-search.yml
        type: APIs.io Search
      - url: overlays/waf-regional-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: >-

          https://docs.aws.amazon.com/waf/latest/APIReference/API_Operations_AWS_WAF_Regional.html
        type: Documentation
      - url: openapi/waf-regional-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS WAF Classic Regional is intended for developers who are implementing
      AWS WAF Classic with AWS resources such as Elastic Load Balancing (ELB)
      Application Load Balancers and API Gateway APIs. For the most up-to-date
      version of AWS WAF, refer to the AWS WAFV2 API and Developer Guide, which
      now offers a unified set of endpoints for both regional and global use.
      The AWS WAF Regional Classic API Reference provides detailed information
      on AWS WAF Classic actions and data types for protecting ELB Application
      Load Balancers and API Gateway APIs. Developers can access these actions
      and data types through the listed endpoints in AWS Regions and Endpoints.
      This guide is designed to offer comprehensive information on API actions,
      data types, and errors for developers using AWS WAF Classic. Additional
      resources and detailed instructions on utilizing AWS WAF Classic can be
      found in the AWS WAF Classic developer guide.
  - aid: amazon-web-services:aws-well-architected-tool
    name: AWS Well-Architected Tool
    tags:
      - ARN
      - Alias
      - Answers
      - Associate
      - Ated
      - Checks
      - Consol
      - Consolidated
      - Details
      - Difference
      - Disassociate
      - Exports
      - Global
      - Import
      - Improvements
      - Invitation
      - Invitations
      - Lens
      - Lenses
      - Milestones
      - Notifications
      - Numbers
      - Profiles
      - Questions
      - Reports
      - Resources
      - Reviews
      - Settings
      - Share
      - Shares
      - Summaries
      - Tags
      - Templates
      - Untag
      - Upgrade
      - Versions
      - Workloads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/well-architected-tool/
    overlays:
      - url: overlays/wellarchitected-openapi-search.yml
        type: APIs.io Search
      - url: overlays/wellarchitected-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/well-architected-tool/
        type: Documentation
      - url: openapi/wellarchitected-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/well-architected-tool/features/
        type: Features
      - url: https://aws.amazon.com/well-architected-tool/pricing/
        type: Pricing
      - url: https://aws.amazon.com/well-architected-tool/partners/
        type: Partners
      - url: https://aws.amazon.com/well-architected-tool/customers/
        type: Customers
      - url: https://aws.amazon.com/well-architected-tool/faqs/
        type: FAQ
      - url: https://aws.amazon.com/well-architected-tool/resources/
        type: Resources
    description: |-

      The API offered by the AWS Well Architected Tool serves as a reliable
      framework to assess your cloud architecture, enabling you to develop
      scalable designs that can adapt and grow over time.
  - aid: amazon-web-services:aws-waf
    name: AWS WAF
    tags:
      - ACL
      - Web
      - Firewalls
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/waf/
    overlays:
      - url: overlays/wafv2-openapi-search.yml
        type: APIs.io Search
      - url: overlays/wafv2-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/waf/
        type: Documentation
      - url: openapi/wafv2-openapi-original.yml
        type: OpenAPI
    description: |-

      AWS WAF is a powerful web application firewall designed to safeguard your
      AWS resources by monitoring and managing incoming web requests. It offers
      protection for various resources like Amazon CloudFront distributions,
      Amazon API Gateway REST APIs, Application Load Balancers, and AWS AppSync
      GraphQL APIs.
  - aid: amazon-web-services:amazon-workmail
    name: Amazon WorkMail
    tags:
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/workmail/
    overlays:
      - url: overlays/workmail-openapi-search.yml
        type: APIs.io Search
      - url: overlays/workmail-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/workmail/
        type: Documentation
      - url: openapi/workmail-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/workmail/features/
        type: Features
      - url: https://aws.amazon.com/workmail/pricing/
        type: Pricing
      - url: https://aws.amazon.com/workmail/resources/
        type: Resources
      - url: https://aws.amazon.com/workmail/faqs/
        type: FAQ
      - url: https://aws.amazon.com/workmail/features/
        type: Features
    description: |-

      Amazon WorkMail is a secure and managed business email and calendar
      service that allows users to access their email, contacts, and calendars
      through various client applications such as Microsoft Outlook, native iOS
      and Android email apps, and web browsers. It supports integration with
      corporate directories, email journaling for compliance, encryption key
      control, and data storage location control. Additionally, Amazon WorkMail
      offers interoperability with Microsoft Exchange Server and programmable
      management of users, groups, and resources through the Amazon WorkMail
      SDK.
  - aid: amazon-web-services:amazon-workspaces
    name: Amazon WorkSpaces
    tags:
      - Images
      - Permission
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/workspaces/
    overlays:
      - url: overlays/workspaces-openapi-search.yml
        type: APIs.io Search
      - url: overlays/workspaces-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/workspaces/
        type: Documentation
      - url: openapi/workspaces-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/workspaces/pricing/
        type: Pricing
      - url: https://aws.amazon.com/workspaces/web/
        type: Web
      - url: https://aws.amazon.com/workspaces/thin-client/
        type: Thin-client
      - url: https://aws.amazon.com/workspaces/all-inclusive/
        type: All-inclusive
      - url: https://aws.amazon.com/workspaces/core/
        type: Core
    description: |-

      Amazon WorkSpaces Service is a cloud-based platform that allows you to
      easily provision virtual desktops for your users, eliminating the need for
      hardware procurement and complex software installation. With WorkSpaces,
      you can quickly add or remove users as needed and provide access to
      virtual desktops from various devices and web browsers. 
  - aid: amazon-web-services:amazon-workspaces-thin-client
    name: Amazon WorkSpaces Thin Client
    tags:
      - ARN
      - Deregister
      - Device
      - Devices
      - Environments
      - Resources
      - Sets
      - Software
      - Software Sets
      - Tags
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/workspaces/thin-client/
    overlays:
      - url: overlays/workspaces-thin-client-openapi-search.yml
        type: APIs.io Search
      - url: overlays/workspaces-thin-client-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/workspaces/thin-client/
        type: Documentation
      - url: openapi/workspaces-thin-client-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/workspaces/thin-client/features/
        type: Features
      - url: https://aws.amazon.com/workspaces/thin-client/pricing/
        type: Pricing
      - url: https://aws.amazon.com/workspaces/thin-client/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/workspaces/thin-client/resources/
        type: Resources
      - url: https://aws.amazon.com/workspaces/thin-client/faqs/
        type: FAQ
    description: |-

      The Amazon WorkSpaces Thin Client API is designed for use with Amazon Web
      Services End User Computing (EUC) virtual desktops, providing users with a
      cost-effective cloud desktop solution. The compact WorkSpaces Thin Client
      device supports up to two monitors and various peripherals, such as
      keyboards, mice, headsets, and webcams.
  - aid: amazon-web-services:amazon-workdocs
    name: Amazon WorkDocs
    tags:
      - Activation
      - Activities
      - Comments
      - Contents
      - Current
      - Custom
      - Deactivate
      - Describe
      - Documents
      - Folders
      - Groups
      - Initiate
      - Labels
      - Me
      - Metadata
      - Notifications
      - Organizations
      - Paths
      - Permission
      - Permissions
      - Principals
      - Removes
      - Resources
      - Restore
      - Root
      - Search
      - Subscriptions
      - Uploads
      - Users
      - Versions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/workdocs/
    overlays:
      - url: overlays/workdocs-openapi-search.yml
        type: APIs.io Search
      - url: overlays/workdocs-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/workdocs/
        type: Documentation
      - url: openapi/workdocs-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/workdocs/sdk/
        type: SDK
      - url: https://aws.amazon.com/workdocs/pricing/
        type: Pricing
      - url: https://aws.amazon.com/workdocs/resources/
        type: Resources
      - url: https://aws.amazon.com/workdocs/faq/
        type: FAQ
    description: |-

      The Amazon WorkDocs API is tailored for a variety of use cases, including
      file migration, security applications, and eDiscovery/analytics. The API
      supports file migration applications for users looking to transfer files
      from different systems, while also allowing for basic metadata changes.
      Security applications can utilize the API actions to detect changes in
      WorkDocs and take necessary actions to ensure data security. General
      administrative applications, such as eDiscovery and analytics, can record
      and replicate data from WorkDocs for backup and analysis purposes. 
  - aid: amazon-web-services:aws-workmail-message-flow
    name: AWS WorkMail Message Flow
    tags:
      - Content
      - Messages
      - Raw
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://docs.aws.amazon.com/workmail/
    overlays:
      - url: overlays/workmailmessageflow-openapi-search.yml
        type: APIs.io Search
      - url: overlays/workmailmessageflow-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://docs.aws.amazon.com/workmail/
        type: Documentation
      - url: openapi/workmailmessageflow-openapi-original.yml
        type: OpenAPI
    description: |-

      The WorkMail Message Flow API provides access to email messages as they
      are being sent and received by a WorkMail organization.
  - aid: amazon-web-services:workspaces-web
    name: WorkSpaces Web
    tags:
      - ARN
      - Access
      - Browser
      - Certificates
      - Disassociate
      - Entities
      - Er
      - Ers
      - IP
      - Identity
      - Logging
      - Metadata
      - Networks
      - Portals
      - Prov
      - Providers
      - Resources
      - Services
      - Settings
      - Store
      - Stores
      - Tags
      - Trust
      - Untag
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/workspaces/web/
    overlays:
      - url: overlays/workspaces-web-openapi-search.yml
        type: APIs.io Search
      - url: overlays/workspaces-web-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/workspaces/web/
        type: Documentation
      - url: openapi/workspaces-web-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/workspaces/web/pricing/
        type: Pricing
      - url: https://aws.amazon.com/workspaces/web/faqs/
        type: FAQ
      - url: https://aws.amazon.com/workspaces/web/resources/
        type: Resources
    description: |-

      The WorkSpaces Web API is a cost-effective, fully managed solution
      designed to support secure web-based workloads. It streamlines the process
      of granting employees access to internal websites and SaaS web
      applications without the need for complex appliances or specialized client
      software. 
  - aid: amazon-web-services:aws-x-ray
    name: AWS X-Ray
    tags:
      - Batches
      - Configurations
      - Encryption
      - Events
      - Graphs
      - Groups
      - Impact
      - Insights
      - Policies
      - Records
      - Resources
      - Rules
      - Sampling
      - Segments
      - Series
      - Services
      - Statistics
      - Summaries
      - Tags
      - Targets
      - Telemetry
      - Time
      - Traces
      - Untag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://aws.amazon.com/xray/
    overlays:
      - url: overlays/xray-openapi-search.yml
        type: APIs.io Search
      - url: overlays/xray-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://aws.amazon.com/xray/
        type: Documentation
      - url: openapi/xray-openapi-original.yml
        type: OpenAPI
      - url: https://aws.amazon.com/xray/features/
        type: Features
      - url: https://aws.amazon.com/xray/pricing/
        type: Pricing
      - url: https://aws.amazon.com/xray/getting-started/
        type: Getting Started
      - url: https://aws.amazon.com/xray/resources/
        type: Resources
      - url: https://aws.amazon.com/xray/faqs/
        type: FAQ
    description: |-

      AWS X-Ray offers comprehensive visibility into the flow of requests within
      your application, allowing you to analyze and filter visual data
      pertaining to payloads, functions, traces, services, APIs, and other
      components. Utilizing both no-code and low-code actions, AWS X-Ray
      provides a seamless way to track and manage requests throughout your
      application.
name: Amazon Web Services
tags:
  - Cloud
  - T1
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://aws.amazon.com/
    type: Portal
  - url: https://aws.amazon.com/developer/
    type: Developer
  - url: https://aws.amazon.com/about-aws/
    type: About
  - url: https://docs.aws.amazon.com/
    type: Documentation
  - url: https://aws.amazon.com/getting-started/
    type: Getting Started
  - url: https://aws.amazon.com/developer/tools/
    type: Tools
  - url: https://aws.amazon.com/developer/tools/
    type: SDKs
  - url: https://aws.amazon.com/developer/language/cpp/
    type: C++
  - url: https://aws.amazon.com/developer/language/net/
    type: .NET
  - url: https://aws.amazon.com/developer/language/go/
    type: Go
  - url: https://aws.amazon.com/developer/language/javascript/
    type: JavaScript
  - url: https://aws.amazon.com/developer/language/java/
    type: Java
  - url: https://aws.amazon.com/developer/language/kotlin/
    type: Kotlin
  - url: https://aws.amazon.com/developer/language/php/
    type: PHP
  - url: https://aws.amazon.com/developer/language/python/
    type: Python
  - url: https://aws.amazon.com/developer/language/ruby/
    type: Ruby
  - url: https://aws.amazon.com/developer/language/rust/
    type: Rust
  - url: https://aws.amazon.com/developer/language/swift/
    type: Swift
  - url: https://docs.aws.amazon.com/cli/
    type: Command Line Interface
  - url: https://aws.amazon.com/opensource/
    type: Open Source
  - url: https://aws.amazon.com/blogs/
    type: Blog
  - url: https://press.aboutamazon.com/press-release-archive
    type: Press
  - url: https://ir.aboutamazon.com/overview/default.aspx
    type: Investors
  - url: https://aws.amazon.com/resources/analyst-reports/
    type: Analysts
  - url: https://aws.amazon.com/premiumsupport/
    type: Support
  - url: https://aws.amazon.com/premiumsupport/plans/
    type: Support Plans
  - url: https://aws.amazon.com/premiumsupport/faqs/
    type: Support FAQs
  - url: https://aws.amazon.com/professional-services/
    type: Professional Services
  - url: https://aws.amazon.com/managed-services/
    type: Managed Services
  - url: https://aws.amazon.com/contact-us/
    type: Contact
  - url: https://aws.amazon.com/events/
    type: Events
  - url: https://aws.amazon.com/events/innovation-webinars/
    type: Webinars
  - url: https://repost.aws/
    type: Forum
  - url: https://aws.amazon.com/new/
    type: Whats New
  - url: https://aws.amazon.com/pricing/
    type: Pricing
  - url: https://aws.amazon.com/free/
    type: Free Tier
  - url: https://calculator.aws/
    type: Pricing Calculator
  - url: https://aws.amazon.com/aws-cost-management/
    type: Cost Management
  - url: https://aws.amazon.com/legal/
    type: Legal
  - url: https://aws.amazon.com/serviceterms/
    type: Terms of Service
  - url: https://aws.amazon.com/privacy/
    type: Privacy Policy
  - url: https://aws.amazon.com/agreement/
    type: Customer Agreement
  - url: https://aws.amazon.com/legal/service-level-agreements/
    type: Service Level Agreements
  - url: https://aws.amazon.com/aup/
    type: Acceptable Use Policy
  - url: https://aws.amazon.com/trademark-guidelines/
    type: Trademark
  - url: https://www.linkedin.com/company/amazon-web-services/
    type: LinkedIn
  - url: https://twitter.com/awscloud
    type: Twitter
  - url: https://www.facebook.com/amazonwebservices
    type: Facebook
  - url: https://www.instagram.com/amazonwebservices/
    type: Instagram
  - url: https://www.twitch.tv/aws
    type: Twitch
  - url: https://www.youtube.com/user/AmazonWebServices/Cloud/
    type: YouTube
  - url: https://repost.aws/knowledge-center
    type: Knowledge Center
  - url: https://aws.amazon.com/podcasts/
    type: Podcast
  - url: https://aws.amazon.com/solutions/case-studies/
    type: Case Studies
  - url: https://aws.amazon.com/industries/
    type: Industries
  - url: https://aws.amazon.com/solutions/
    type: Solutions
  - url: https://aws.amazon.com/whitepapers/
    type: White Papers
  - url: https://aws.amazon.com/architecture/
    type: Architecture
  - url: https://aws.amazon.com/executive-insights/
    type: Executive Insights
  - url: https://aws.amazon.com/partners/
    type: Partners
  - url: https://aws.amazon.com/marketplace
    type: Marketplace
  - url: https://aws.amazon.com/training/
    type: Training
  - url: https://aws.amazon.com/careers/
    type: Careers
  - url: https://community.aws/students
    type: Students
  - url: https://aws.amazon.com/education/
    type: Education
  - url: https://aws.amazon.com/security/
    type: Security
  - url: https://aws.amazon.com/accessibility/
    type: Accessibility
  - url: https://portal.aws.amazon.com/billing/signup
    type: SignUp
  - url: https://signin.aws.amazon.com/signin
    type: Login
  - url: https://console.aws.amazon.com
    type: Console
  - url: https://console.aws.amazon.com/billing/home
    type: Billing
  - url: https://console.aws.amazon.com/iam/home
    type: Credentials
  - url: https://phd.aws.amazon.com/
    type: Health Dashboard
created: 2023/11/06
modified: '2025-09-05'
position: Consuming
description: |-

  Amazon Web Services, Inc. is a subsidiary of Amazon that provides on-demand
  cloud computing platforms and APIs to individuals, companies, and governments,
  on a metered, pay-as-you-go basis. Clients will often use this in combination
  with autoscaling.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---