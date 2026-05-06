---
name: Amazon DevOps Guru
description: Amazon DevOps Guru is a machine learning-powered service that makes it easy to improve an application's operational performance and availability. It detects behaviors that deviate from normal operating patterns so you can identify operational issues long before they impact your customers.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/devops-guru/
created: '2026-03-16'
modified: '2026-04-19'
apis:
  - name: Amazon DevOps Guru API
    description: The Amazon DevOps Guru API provides programmatic access to manage resource collections, insights, anomalies, and recommendations for improving application operational performance and availability. Covers 31 operations including insight management, anomaly investigation, remediation recommendations, notification configuration, and AWS Organizations integration.
    humanURL: https://aws.amazon.com/devops-guru/
    baseURL: https://devops-guru.amazonaws.com
    tags:
      - Anomaly Detection
      - DevOps
      - Machine Learning
      - Operational Intelligence
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-devops-guru-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/devops-guru/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/devops-guru/pricing/
      - type: FAQ
        url: https://aws.amazon.com/devops-guru/faqs/
      - type: JSONSchema
        url: json-schema/amazon-devops-guru-proactive-insight-schema.json
      - type: JSONSchema
        url: json-schema/amazon-devops-guru-reactive-insight-schema.json
      - type: JSONSchema
        url: json-schema/amazon-devops-guru-recommendation-schema.json
      - type: JSONSchema
        url: json-schema/amazon-devops-guru-proactive-anomaly-schema.json
      - type: JSONSchema
        url: json-schema/amazon-devops-guru-reactive-anomaly-schema.json
      - type: JSONStructure
        url: json-structure/amazon-devops-guru-proactive-insight-structure.json
      - type: JSONStructure
        url: json-structure/amazon-devops-guru-reactive-insight-structure.json
      - type: JSONStructure
        url: json-structure/amazon-devops-guru-recommendation-structure.json
      - type: JSON-LD
        url: json-ld/amazon-devops-guru-context.jsonld
      - type: Example
        url: examples/amazon-devops-guru-proactive-insight-example.json
      - type: Example
        url: examples/amazon-devops-guru-reactive-insight-example.json
      - type: Example
        url: examples/amazon-devops-guru-recommendation-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/devops-guru/
  - type: Website
    url: https://aws.amazon.com/devops-guru/
  - type: Documentation
    url: https://docs.aws.amazon.com/devops-guru/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/devops/category/artificial-intelligence/amazon-devops-guru/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/devops-guru/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-devops-guru-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-devops-guru-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/operational-intelligence.yaml
  - type: Features
    data:
      - name: ML-Powered Anomaly Detection
        description: Uses machine learning to detect behavioral deviations across hundreds of AWS metrics without manual threshold configuration.
      - name: Proactive Insights
        description: Identifies anomalies before they become operational issues, allowing teams to remediate before customer impact.
      - name: Reactive Insights
        description: Surfaces insights when active operational issues are detected to accelerate root cause analysis.
      - name: Actionable Recommendations
        description: Provides specific remediation recommendations with links to relevant documentation and AWS console pages.
      - name: CloudWatch Logs Integration
        description: Analyzes CloudWatch Logs for log-based anomalies to include log patterns in operational insights.
      - name: AWS OpsCenter Integration
        description: Automatically creates OpsCenter OpsItems for detected insights to streamline incident management.
      - name: CloudFormation-Based Coverage
        description: Define which applications to monitor by specifying CloudFormation stack names for precise application-scoped coverage.
      - name: Organizations Integration
        description: Enable DevOps Guru across an entire AWS Organization to centrally monitor all accounts and regions.
  - type: UseCases
    data:
      - name: Proactive Operational Monitoring
        description: Detect potential issues in application behavior before they impact end users using ML-powered proactive insights.
      - name: Incident Root Cause Analysis
        description: Rapidly identify the root cause of operational incidents by correlating anomalies, events, and recommendations.
      - name: Application Performance Optimization
        description: Use continuous behavioral monitoring to identify performance bottlenecks and optimization opportunities.
      - name: Multi-Account Operations
        description: Monitor operational health across all accounts in an AWS Organization from a single pane of glass.
      - name: DevOps Pipeline Integration
        description: Integrate DevOps Guru insights into CI/CD pipelines to gate deployments on operational health status.
  - type: Integrations
    data:
      - name: Amazon CloudWatch
        description: Ingests CloudWatch metrics and logs for anomaly detection and event correlation.
      - name: AWS CloudFormation
        description: Uses CloudFormation stacks to define application boundaries for targeted monitoring coverage.
      - name: AWS OpsCenter
        description: Automatically creates OpsCenter OpsItems for detected insights to enable incident management workflows.
      - name: Amazon SNS
        description: Sends insight notifications to SNS topics for routing to teams via email, Slack, PagerDuty, or other channels.
      - name: AWS Organizations
        description: Enables organization-wide monitoring by aggregating insights across multiple AWS accounts.
      - name: Amazon EventBridge
        description: Emits DevOps Guru events to EventBridge for custom automation and routing workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Anomaly Detection
  - AWS
  - DevOps
  - Machine Learning
  - Operational Intelligence
---
