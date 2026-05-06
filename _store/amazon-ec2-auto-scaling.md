---
name: Amazon EC2 Auto Scaling
description: Amazon EC2 Auto Scaling helps you maintain application availability and lets you automatically add or remove EC2 instances according to conditions you define. You can use fleet management features to maintain the health and availability of your fleet, and use dynamic and predictive scaling to add or remove EC2 instances to meet demand.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/ec2/autoscaling/
created: '2026-03-16'
modified: '2026-04-19'
tags:
  - Amazon Web Services
  - Auto Scaling
  - AWS
  - Compute
  - EC2
  - High Availability
  - Scaling
apis:
  - name: Amazon EC2 Auto Scaling API
    description: The Amazon EC2 Auto Scaling API provides programmatic access to create and manage Auto Scaling groups, launch configurations, scaling policies, scheduled actions, lifecycle hooks, and warm pools for automatic capacity management.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/ec2/autoscaling/
    baseURL: https://autoscaling.amazonaws.com
    tags:
      - Auto Scaling
      - Capacity Management
      - Compute
      - EC2
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-ec2-auto-scaling-openapi.yaml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/autoscaling/2011-01-01/openapi.yaml
      - type: JSONSchema
        url: json-schema/ec2-auto-scaling-auto-scaling-group-schema.json
      - type: JSONLD
        url: json-ld/amazon-ec2-auto-scaling-context.jsonld
      - type: GettingStarted
        url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html
      - type: Pricing
        url: https://aws.amazon.com/ec2/autoscaling/pricing/
      - type: FAQ
        url: https://aws.amazon.com/ec2/autoscaling/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/
      - type: Authentication
        url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/CommonParameters.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/ec2-auto-scaling-api-throttling.html
      - type: JSONSchema
        url: json-schema/ec2-auto-scaling-accelerator-count-request-schema.json
      - type: JSONStructure
        url: json-structure/ec2-auto-scaling-accelerator-count-request-structure.json
      - type: Example
        url: examples/ec2-auto-scaling-accelerator-count-request-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/developer/
  - type: Documentation
    url: https://docs.aws.amazon.com/autoscaling/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/category/compute/auto-scaling/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/ec2/autoscaling/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-ec2-auto-scaling
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Dynamic Scaling
        description: Automatically scales EC2 capacity up or down in response to real-time demand using target tracking, step, or simple scaling policies.
      - name: Predictive Scaling
        description: Uses machine learning to forecast future demand and proactively adds EC2 instances ahead of anticipated load spikes.
      - name: Scheduled Scaling
        description: Scales capacity at pre-defined times based on predictable load patterns or business cycles.
      - name: Fleet Management
        description: Automatically detects and replaces unhealthy instances to maintain application availability and fleet health.
      - name: Instance Refresh
        description: Gradually updates EC2 instances in an Auto Scaling group with new AMIs or launch template versions.
      - name: Warm Pools
        description: Pre-initializes EC2 instances to reduce latency for scale-out events by keeping a pool of instances in a stopped or running state.
      - name: Mixed Instances Policy
        description: Combines On-Demand and Spot instances with multiple instance types for cost optimization and availability.
      - name: Lifecycle Hooks
        description: Pauses instance launch or termination to perform custom actions such as installing software or draining connections.
  - type: UseCases
    data:
      - name: Web Application Scaling
        description: Automatically scale web server fleets to handle variable HTTP traffic loads without over-provisioning.
      - name: Batch Processing
        description: Scale compute capacity up when jobs arrive and down when completed to minimize costs for batch workloads.
      - name: Microservices Autoscaling
        description: Independently scale each microservice based on its own traffic patterns and resource utilization.
      - name: Cost Optimization
        description: Combine Spot and On-Demand instances to reduce EC2 costs while maintaining availability.
      - name: Blue/Green Deployments
        description: Use instance refresh to gradually replace old instances with new ones for zero-downtime deployments.
  - type: Integrations
    data:
      - name: Amazon EC2
        description: Launches and terminates EC2 instances based on scaling policies and schedules.
      - name: Amazon CloudWatch
        description: Uses CloudWatch metrics and alarms to trigger dynamic scaling policies automatically.
      - name: Elastic Load Balancing
        description: Automatically registers new instances with load balancers and deregisters terminated instances.
      - name: AWS Systems Manager
        description: Integrates with Systems Manager for instance configuration and patch management during lifecycle hooks.
      - name: Amazon SNS
        description: Sends notifications for scaling events, instance launches, and terminations via SNS topics.
      - name: AWS Cost Management
        description: Works with Cost Explorer and Budgets to monitor and optimize spend on Auto Scaling fleets.
  - type: SpectralRules
    url: rules/amazon-ec2-auto-scaling-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-ec2-auto-scaling-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ec2-auto-scaling-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
