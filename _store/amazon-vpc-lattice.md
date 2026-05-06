---
aid: amazon-vpc-lattice
name: Amazon VPC Lattice
description: Amazon VPC Lattice is an application networking service that consistently connects, monitors, and secures communications between your services, helping you to improve productivity so that your developers can focus on building features that matter to your business. It simplifies service-to-service connectivity and security across VPCs and accounts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Microservices
  - Service Mesh
  - Service Networking
url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc-lattice/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-vpc-lattice:amazon-vpc-lattice-api
    name: Amazon VPC Lattice API
    description: The Amazon VPC Lattice API provides programmatic access to create and manage service networks, services, target groups, listeners, rules, and access log subscriptions. It enables service-to-service connectivity with built-in authentication and authorization across VPCs and AWS accounts.
    humanURL: https://aws.amazon.com/vpc/lattice/
    baseURL: https://vpc-lattice.amazonaws.com
    tags:
      - AWS
      - Microservices
      - Service Networking
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/
      - type: APIReference
        url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/vpc/lattice/pricing/
      - type: FAQ
        url: https://aws.amazon.com/vpc/lattice/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/vpc/lattice/
  - type: Documentation
    url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/
  - type: Console
    url: https://console.aws.amazon.com/vpc/home#VpcLattice
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc-lattice/refs/heads/main/rules/amazon-vpc-lattice-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc-lattice/refs/heads/main/vocabulary/amazon-vpc-lattice-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc-lattice/refs/heads/main/capabilities/amazon-vpc-lattice-capability.yaml
  - type: Features
    data:
      - name: Automation
        description: Automate operational tasks with Amazon VPC Lattice.
      - name: API Access
        description: Programmatic access to Amazon VPC Lattice resources.
  - type: UseCases
    data:
      - name: Cloud Operations
        description: Use Amazon VPC Lattice to manage and automate cloud operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
