---
aid: amazon-simspace-weaver
name: Amazon SimSpace Weaver
description: AWS SimSpace Weaver is a managed service that helps you build and run large-scale spatial simulations in the AWS Cloud. It provides tools to run custom spatial simulation logic at scale and use simulation workloads for defense, urban planning, and other real-world system simulations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Defense
  - Digital Twin
  - Simulation
  - Spatial Simulation
url: https://raw.githubusercontent.com/api-evangelist/amazon-simspace-weaver/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-simspace-weaver:aws-simspace-weaver-api
    name: AWS SimSpace Weaver API
    description: The AWS SimSpace Weaver API provides programmatic access to create and manage simulations, simulation apps, snapshots, and clocks for running large-scale spatial simulations in the cloud.
    humanURL: https://aws.amazon.com/simspace-weaver/
    baseURL: https://simspaceweaver.amazonaws.com
    tags:
      - Digital Twin
      - Simulation
      - Spatial Simulation
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is.html
      - type: OpenAPI
        url: openapi/amazon-simspace-weaver.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/simspaceweaver/
      - type: Pricing
        url: https://aws.amazon.com/simspaceweaver/pricing/
      - type: FAQ
        url: https://aws.amazon.com/simspaceweaver/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/simspaceweaver/
  - type: Documentation
    url: https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/hpc/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/simspaceweaver/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-simspace-weaver-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-simspace-weaver-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-simspace-weaver.yaml
  - type: Features
    data:
      - name: Large-scale Simulations
        description: Run spatial simulations at city or country scale with millions of agents.
      - name: Managed Infrastructure
        description: Fully managed compute infrastructure for simulation workloads.
      - name: App Framework
        description: Deploy custom simulation apps that interact with the simulation world.
      - name: Clock Control
        description: Start, pause, stop, and control simulation time.
  - type: UseCases
    data:
      - name: Urban Planning
        description: Simulate traffic, pedestrian movement, and city infrastructure at scale.
      - name: Emergency Response
        description: Model disaster scenarios and evacuation plans.
      - name: Defense Simulations
        description: Run large-scale defense and logistics simulations.
  - type: Integrations
    data:
      - name: AWS CloudFormation
        description: Deploy SimSpace Weaver simulations using CloudFormation.
      - name: Amazon S3
        description: Store simulation schemas and output data in S3.
      - name: Amazon CloudWatch
        description: Monitor simulation metrics and logs via CloudWatch.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
x-type: company
---
