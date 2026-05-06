---
aid: safe-agile
name: SAFe Agile
description: 'The Scaled Agile Framework (SAFe) is an enterprise-scale agile framework developed by Scaled Agile, Inc. that provides guidance for implementing agile practices across large organizations with multiple teams. SAFe organizes around five core disciplines: Lean Portfolio Management, Team and Technical Agility, Product Development Flow, Large Solution Integration and Delivery, and Leadership and Culture. Organizations use SAFe to align stakeholders, coordinate Agile Release Trains (ARTs), track PI objectives, and accelerate delivery of value. SAFe tools integrate with CI/CD pipelines, ERP systems, and planning platforms to support enterprise agile transformation.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agile
  - Enterprise
  - Framework
  - Project Management
  - Scaled Agile
  - Lean Portfolio
  - DevOps
url: https://raw.githubusercontent.com/api-evangelist/safe-agile/refs/heads/main/apis.yml
created: '2025'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: safe-agile:scaledagile-framework
    name: Scaled Agile Framework (SAFe)
    description: The official Scaled Agile Framework by Scaled Agile, Inc. provides comprehensive guidance for enterprise agile transformation including roles, events, artifacts, and competencies for Lean Portfolio Management, Agile Release Trains, and PI Planning. Includes SAFe CoPilot AI assistant, certification programs, and the annual State of SAFe report.
    humanURL: https://framework.scaledagile.com/
    tags:
      - Agile
      - Enterprise
      - Framework
      - Scaled Agile
    properties:
      - type: Documentation
        url: https://framework.scaledagile.com/
      - type: Website
        url: https://scaledagile.com/
  - aid: safe-agile:jira-safe
    name: Jira SAFe Integration
    description: Jira by Atlassian provides SAFe-aligned project management and PI planning capabilities through the Advanced Roadmaps feature and SAFe-compatible workflows for Agile Release Trains, Epics, Features, and Stories. Jira's REST API enables programmatic management of SAFe backlogs, sprints, and program increments.
    humanURL: https://www.atlassian.com/agile/safe
    tags:
      - Agile
      - Project Management
      - SAFe
      - PI Planning
      - REST
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/software/rest/intro/
      - type: Website
        url: https://www.atlassian.com/agile/safe
  - aid: safe-agile:azure-devops-safe
    name: Azure DevOps SAFe Integration
    description: Azure DevOps provides SAFe-aligned planning and tracking through work item types aligned to SAFe hierarchy (Epics, Features, User Stories), delivery plans for Program Increment visualization, and REST APIs for programmatic access to backlogs, iterations, and boards.
    humanURL: https://learn.microsoft.com/en-us/azure/devops/
    tags:
      - Agile
      - DevOps
      - SAFe
      - REST
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/devops/integrate/
      - type: Website
        url: https://azure.microsoft.com/en-us/products/devops/
  - aid: safe-agile:planview-safe
    name: Planview SAFe Tool
    description: Planview provides enterprise agile planning supporting SAFe through its portfolio management, Lean flow, and Agile delivery capabilities. Enables organizations to connect strategy to delivery across multiple ARTs with real-time program board visualization and PI planning support.
    humanURL: https://www.planview.com/resources/articles/safe-agile/
    tags:
      - Agile
      - Portfolio Management
      - SAFe
      - Enterprise Planning
    properties:
      - type: Documentation
        url: https://success.planview.com/
      - type: Website
        url: https://www.planview.com/
  - aid: safe-agile:spiraplan-safe
    name: SpiraPlan SAFe Tool
    description: SpiraPlan by Inflectra is an enterprise agile portfolio and risk management platform that supports SAFe, Nexus, Scrum of Scrums, and LeSS frameworks. Provides REST API for programmatic access to portfolio, program, and team level planning artifacts.
    humanURL: https://www.inflectra.com/SpiraPlan/
    tags:
      - Agile
      - Portfolio Management
      - SAFe
      - REST
    properties:
      - type: Documentation
        url: https://www.inflectra.com/Support/KnowledgeBase/
      - type: Website
        url: https://www.inflectra.com/SpiraPlan/
common:
  - type: Website
    url: https://scaledagile.com/
  - type: Documentation
    url: https://framework.scaledagile.com/
  - type: Blog
    url: https://scaledagile.com/blog/
  - type: Certification
    url: https://scaledagile.com/training/find-training-provider/
  - type: JSONSchema
    url: json-schema/safe-agile-program-increment-schema.json
  - type: JSONStructure
    url: json-structure/safe-agile-art-structure.json
  - type: JSONLDContext
    url: json-ld/safe-agile-context.jsonld
  - type: Vocabulary
    url: vocabulary/safe-agile-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
