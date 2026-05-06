---
aid: acadia
url: https://raw.githubusercontent.com/api-evangelist/acadia/refs/heads/main/apis.yml
name: Acadia
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Connected Worker
  - Knowledge Management
  - Manufacturing
  - Skills Management
  - Training
  - Workforce Development
description: Acadia is a Connected Worker Platform designed for employee productivity, acquired by Epicor. It delivers digital work instructions, knowledge management, skills matrices, quizzing, process evaluations, and team communications to frontline workers across manufacturing, transportation, healthcare, and retail banking. Acadia integrates with SSO, ERP, HRIS, LMS, IoT, and credentialing systems to enable enterprise-grade workforce development at scale.
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: acadia:acadia-api
    name: Acadia Platform API
    tags:
      - Connected Worker
      - Knowledge Management
      - Training
      - Workforce Development
    humanURL: https://www.acadia-software.com/
    baseURL: https://api.acadia-software.com/v1
    properties:
      - url: https://www.acadia-software.com/
        type: Documentation
      - url: openapi/acadia-platform.yaml
        type: OpenAPI
      - url: json-schema/acadia-work-instruction-schema.json
        type: JSONSchema
      - url: examples/acadia-work-instruction-example.json
        type: Example
    description: Acadia Platform API provides programmatic access to digital work instructions, employee skills matrices, quizzes, evaluations, and knowledge management features for workforce development integrations.
common:
  - type: Website
    url: https://www.acadia-software.com/
  - type: Portal
    url: https://www.acadia-software.com/
  - type: SignUp
    url: https://www.acadia-software.com/
  - type: Blog
    url: https://www.acadia-software.com/blog/
  - type: Documentation
    url: https://www.acadia-software.com/features/
  - type: SpectralRules
    url: rules/acadia-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/workforce-development.yaml
  - type: Vocabulary
    url: vocabulary/acadia-vocabulary.yaml
  - type: Features
    data:
      - name: Digital Work Instructions
        description: Convert procedures to interactive task lists with videos, images, and dynamic content; assign via QR code, ERP integration, or manager distribution
      - name: Knowledge Management
        description: Centralized document creation with automated translation, algorithmic search, and custom metadata filters
      - name: Skills Matrix
        description: Track training and skill attainment, quantify individual and team performance, and identify capability gaps
      - name: Quizzing and Evaluations
        description: Assess employee skill proficiency, measure comprehension, and perform objective skill evaluations during task execution
      - name: Team Communications
        description: Auditable acknowledgements for process changes, group communications, and document change tracking
      - name: SSO Integration
        description: Secure single sign-on via Active Directory and LDAP with role-based access control
      - name: ERP and HRIS Integration
        description: Integration with ERP, HRIS, LMS, IoT, and credentialing systems for enterprise workforce management
      - name: SOC 2 Type II Certified
        description: Enterprise-grade security with multi-layer encryption, intrusion prevention, and GDPR compliance
      - name: Career Path Visibility
        description: Display advancement requirements and skill gap identification for employee career development
  - type: UseCases
    data:
      - name: Manufacturing Workforce Onboarding
        description: Use digital work instructions to onboard new manufacturing employees quickly and ensure procedure compliance
      - name: Compliance Training
        description: Assign and track completion of compliance-critical training and policy acknowledgements with full auditability
      - name: Frontline Skill Gap Analysis
        description: Use the skills matrix to identify capability gaps in frontline teams and prioritize training investments
      - name: Process Improvement Feedback
        description: Capture structured employee feedback on task-specific procedures to improve standard work over time
      - name: ERP-Triggered Work Instructions
        description: Automatically assign work instructions based on ERP work orders for synchronized production operations
      - name: Multi-Language Training Deployment
        description: Deploy synchronized multi-language training content to global workforces without manual translation delays
  - type: Integrations
    data:
      - name: SAP
        description: Integration with SAP ERP for work order-triggered digital work instruction assignment
      - name: Active Directory
        description: Single sign-on via Microsoft Active Directory for enterprise identity management
      - name: LDAP
        description: LDAP-based SSO for enterprise authentication systems
      - name: Learning Management Systems
        description: Integration with third-party LMS platforms for training record synchronization
      - name: HRIS Systems
        description: Integration with HR information systems for employee data synchronization
      - name: IoT Platforms
        description: Integration with IoT systems for operational data correlation with training and task execution
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
