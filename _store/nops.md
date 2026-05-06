---
aid: nops
url: https://raw.githubusercontent.com/api-evangelist/nops/refs/heads/main/apis.yml
apis:
  - aid: nops:nops
    name: nOps
    tags:
      - Costs
      - FinOps
    humanURL: ' https://www.nops.io/'
    baseURL: https://app.nops.io
    properties:
      - url: ' https://www.nops.io/'
        type: Documentation
      - url: https://app.nops.io/public_redoc/
        type: Documentation
      - url: openapi/nops-nops-openapi.yml
        type: OpenAPI
      - url: json-schema/map-migration-project.json
        type: JSONSchema
      - url: json-schema/map-migration-product.json
        type: JSONSchema
      - url: json-schema/map-migration-resource.json
        type: JSONSchema
      - url: json-schema/scheduler.json
        type: JSONSchema
      - url: json-ld/nops-context.jsonld
        type: JSONLD
    description: nOps is an AWS-focused cloud management platform that helps engineering and FinOps teams cut costs, improve governance, and keep environments well-architected. It ingests AWS billing and telemetry data (such as CUR, CloudTrail, and CloudWatch) to surface real-time insights, flag anomalies, and recommend actions like rightsizing, eliminating idle resources, scheduling non‑production workloads, optimizing EBS/S3, and increasing efficient use of Spot.
name: nOps
tags:
  - Costs
  - FinOps
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-18'
position: Consuming
description: nOps is an AI-powered cloud cost visibility and optimization platform that helps organizations reduce their AWS spending by 50% or more through autonomous management and automation. The platform provides 100% visibility into cloud costs across AWS, GCP, Azure, Kubernetes, GenAI, and SaaS applications, enabling teams to allocate and track spending by customer, product, cost center, or any other dimension even without complete tagging.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Technical Blogs & Tutorials | nOps
    description: 'null'
    url: https://www.nops.io/blog/
    type: Blog
  - name: Webcasts and Podcasts | Live & On-Demand | nOps
    description: 'null'
    url: https://www.nops.io/webinars-and-workshops/
    type: Webinars
  - name: nCast | nOps
    description: 'null'
    url: https://www.nops.io/ncast/
    type: Resources
  - name: Welcome to the nOps Docs | nOps docs
    description: 'null'
    url: https://help.nops.io/docs/introduction/platform-introduction
    type: Documentation
  - name: nOps Customer Service SLAs | nOps docs
    description: 'null'
    url: https://help.nops.io/docs/support/customer-service-sla
    type: Documentation
  - name: Open a support case with nOps | nOps docs
    description: 'null'
    url: https://help.nops.io/docs/support/open-support-case
    type: Support
  - name: Integrations Overview | nOps docs
    description: 'null'
    url: https://help.nops.io/docs/agents-integrations/integrations
    type: Integrations
  - type: Features
    data:
      - name: Autonomous Cost Optimization
        description: AI-powered autonomous management that identifies and implements cost savings without manual intervention.
      - name: 100% Cost Visibility
        description: Complete visibility into cloud costs across AWS, GCP, Azure, Kubernetes, GenAI, and SaaS applications.
      - name: Essentials Scheduler
        description: Automated scheduling of non-production workloads to eliminate idle resource costs.
      - name: MAP Migration Support
        description: AWS Migration Acceleration Program tracking for migration projects, products, and resources.
      - name: Spot Instance Optimization
        description: Intelligent spot instance management for maximizing cost savings on compute workloads.
  - type: UseCases
    data:
      - name: FinOps Automation
        description: Automate cloud cost allocation, tracking, and optimization across teams and business units.
      - name: Cloud Migration Tracking
        description: Track MAP migration projects and measure cost savings from AWS migration programs.
      - name: Idle Resource Elimination
        description: Identify and schedule or terminate idle resources to reduce wasted cloud spending.
      - name: Cost Anomaly Detection
        description: Real-time detection and alerting on unusual cost spikes and billing anomalies.
  - type: Integrations
    data:
      - name: AWS Services
        description: Deep integration with AWS billing, CUR, CloudTrail, CloudWatch, and resource management services.
      - name: Kubernetes
        description: Container cost visibility and optimization for EKS and self-managed Kubernetes clusters.
      - name: Slack and Teams
        description: Notification integrations for cost alerts, optimization recommendations, and scheduler events.
---
