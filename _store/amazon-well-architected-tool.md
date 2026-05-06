---
aid: amazon-well-architected-tool
name: Amazon Well-Architected Tool
description: 'The AWS Well-Architected Tool helps you review your workloads and compare them to the latest AWS architectural best practices. It provides a consistent process for evaluating architectures and implementing designs that scale over time across five pillars: operational excellence, security, reliability, performance efficiency, and cost optimization. The tool offers lens catalogs, custom lenses, profiles, review templates, and API-driven extensibility for integration into governance workflows.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Architecture
  - AWS
  - Best Practices
  - Cloud Governance
  - Well-Architected
  - Workloads
url: https://raw.githubusercontent.com/api-evangelist/amazon-well-architected-tool/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-well-architected-tool:aws-well-architected-tool-api
    name: AWS Well-Architected Tool API
    description: The AWS Well-Architected Tool API provides programmatic access to create and manage workloads, lenses, milestones, profiles, review templates, and review reports. It enables integration of the Well-Architected review process into DevOps workflows and automation pipelines for continuous architecture assessment. The API supports 56 operations covering workload management, lens operations, lens reviews, answers, milestones, profiles, review templates, notifications, checks, and administration.
    humanURL: https://aws.amazon.com/well-architected-tool/
    baseURL: https://wellarchitected.amazonaws.com
    tags:
      - Architecture
      - AWS
      - Best Practices
      - Cloud Governance
      - Workloads
      - Lenses
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/well-architected-tool/pricing/
      - type: FAQ
        url: https://aws.amazon.com/well-architected-tool/faqs/
      - type: OpenAPI
        url: openapi/amazon-well-architected-tool-openapi-original.yaml
      - type: JSONSchema
        url: json-schema/well-architected-tool-workload-schema.json
      - type: JSONLD
        url: json-ld/amazon-well-architected-tool-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/well-architected-tool/
  - type: Documentation
    url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/
  - type: Console
    url: https://console.aws.amazon.com/wellarchitected/
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
  - type: GitHubRepository
    url: https://github.com/aws-samples/custom-lens-wa-hub
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: SpectralRules
    url: rules/amazon-well-architected-tool-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-well-architected-tool-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/architecture-governance.yaml
  - type: Features
    data:
      - name: Lens Catalog
        description: Expert-authored review lenses from AWS covering diverse technology and industry-specific pillars, continuously refreshed with latest best practices.
      - name: Custom Lenses
        description: Create organization-specific lenses that combine internal best practices with AWS guidance, shareable with up to 300 IAM users or across AWS Organizations.
      - name: Profiles
        description: Pre-define business goals to auto-generate prioritized review questions tailored to your workload context.
      - name: Review Templates
        description: Standardize answers across multiple workloads to ensure consistent architectural reviews at scale.
      - name: Enhanced Collaboration
        description: Share workloads and custom lenses with IAM users or integrate with AWS Organizations for organization-wide access and visibility.
      - name: Service Integration
        description: Native integration with AWS Trusted Advisor and AWS Service Catalog AppRegistry to reduce manual review effort.
      - name: API-Driven Extensibility
        description: Robust APIs allow extending Well-Architected functionality into existing architecture governance processes, applications, and workflows.
      - name: Milestone Tracking
        description: Save milestones, implement improvements, and measure progress over time with point-in-time snapshots of workload review state.
      - name: Compliance and Regulatory Support
        description: Available in GovCloud (US) with FedRAMP compliance for organizations with stringent regulatory requirements.
      - name: Consolidated Reporting
        description: Generate consolidated reports across workloads for governance and executive visibility into architectural risk posture.
  - type: UseCases
    data:
      - name: Architecture Reviews and Governance
        description: Evaluate cloud workload architecture quality against AWS best practices across the five Well-Architected pillars.
      - name: Multi-Workload Standardization
        description: Use review templates to standardize architectural answers and enforce consistent governance across multiple workloads and teams.
      - name: Industry-Specific Best Practice Implementation
        description: Apply industry-specific and technology-specific lenses from the lens catalog to assess specialized workloads.
      - name: Regulatory Compliance Assessment
        description: Evaluate workloads for FedRAMP, GovCloud, and other regulatory compliance requirements through targeted lenses.
      - name: DevOps Pipeline Integration
        description: Integrate Well-Architected reviews into CI/CD workflows and automation pipelines for continuous architecture assessment.
      - name: Cross-Team Architectural Alignment
        description: Share workloads with reviewers and stakeholders to facilitate collaborative architectural decision-making across teams.
      - name: Sustainability Goal Realization
        description: Use the sustainability pillar to minimize environmental impact and meet organizational sustainability commitments.
  - type: Integrations
    data:
      - name: AWS Trusted Advisor
        description: Integration with AWS Trusted Advisor provides automated checks that complement manual Well-Architected review processes.
      - name: AWS Service Catalog AppRegistry
        description: AppRegistry integration enables linking Well-Architected workloads to application metadata for richer governance context.
      - name: AWS Organizations
        description: Organization-level sharing of workloads and custom lenses for enterprise-wide architectural governance programs.
      - name: AWS IAM
        description: Fine-grained access control via AWS IAM for workload sharing and reviewer management within the tool.
      - name: AWS CloudFormation
        description: Workloads can be associated with CloudFormation stacks for automated resource discovery and architecture documentation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
