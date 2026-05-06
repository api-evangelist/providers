---
name: Amazon Elastic Beanstalk
description: AWS Elastic Beanstalk is a platform-as-a-service (PaaS) that makes it easy to deploy, manage, and scale web applications and services. You simply upload your code and Elastic Beanstalk automatically handles the deployment, capacity provisioning, load balancing, auto-scaling, and application health monitoring.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/elasticbeanstalk/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - Auto Scaling
  - Deployment
  - Elastic Beanstalk
  - PaaS
  - Platform As A Service
  - Web Applications
apis:
  - name: AWS Elastic Beanstalk API
    description: API for managing AWS Elastic Beanstalk applications, environments, and related resources including configuration templates and application versions.
    humanURL: https://aws.amazon.com/elasticbeanstalk/
    baseURL: https://elasticbeanstalk.amazonaws.com
    tags:
      - Auto Scaling
      - Deployment
      - PaaS
      - Web Applications
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/
      - type: OpenAPI
        url: openapi/amazon-elastic-beanstalk-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/
      - type: GettingStarted
        url: https://aws.amazon.com/elasticbeanstalk/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/elasticbeanstalk/pricing/
      - type: FAQ
        url: https://aws.amazon.com/elasticbeanstalk/faqs/
      - type: JSONSchema
        url: json-schema/amazon-elastic-beanstalk-application-description-message-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elastic-beanstalk-application-description-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elastic-beanstalk-application-descriptions-message-schema.json
      - type: JSONLD
        url: json-ld/amazon-elastic-beanstalk-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/elasticbeanstalk/
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticbeanstalk/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/elasticbeanstalk/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/elasticbeanstalk/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/elasticbeanstalk
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-elastic-beanstalk-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-elastic-beanstalk-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-elastic-beanstalk-vocabulary.yaml
  - type: Features
    data:
      - name: Automatic Deployment
        description: Upload code and Elastic Beanstalk handles deployment automatically
      - name: Auto Scaling
        description: Automatically scale capacity up and down based on application needs
      - name: Health Monitoring
        description: Monitor application health and performance with built-in dashboards
      - name: Multi-Language Support
        description: Support for Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker
      - name: Environment Management
        description: Manage multiple deployment environments (development, staging, production)
  - type: UseCases
    data:
      - name: Web Application Hosting
        description: Deploy and host web applications without managing infrastructure
      - name: API Backend Deployment
        description: Deploy REST API backends with automatic scaling and load balancing
      - name: Microservices Deployment
        description: Deploy containerized microservices using Docker or multi-container configurations
      - name: Blue-Green Deployments
        description: Perform zero-downtime deployments using environment URL swapping
  - type: Integrations
    data:
      - name: Amazon EC2
        description: Runs application environments on EC2 instances
      - name: Amazon RDS
        description: Provision and manage RDS databases alongside environments
      - name: Amazon S3
        description: Store application versions and deployment artifacts
      - name: AWS CloudFormation
        description: Manage environment infrastructure as code
      - name: AWS CodePipeline
        description: Integrate with CI/CD pipelines for automated deployments
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
