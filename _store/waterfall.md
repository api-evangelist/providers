---
aid: waterfall
name: Waterfall
description: Waterfall is a sequential software development methodology where progress flows steadily downward through defined phases including requirements, system design, implementation, testing, deployment, and maintenance. It emphasizes thorough documentation, fixed-scope planning, and phase-gate reviews before proceeding to subsequent stages. Waterfall remains widely used in regulated industries, government contracting, and projects with well-understood, stable requirements.
type: Index
url: https://en.wikipedia.org/wiki/Waterfall_model
tags:
  - Project Management
  - SDLC
  - Software Development
  - Methodology
  - Software Engineering
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis: []
common:
  - type: Documentation
    url: https://en.wikipedia.org/wiki/Waterfall_model
    title: Wikipedia - Waterfall Model
  - type: Documentation
    url: https://www.techtarget.com/searchsoftwarequality/definition/waterfall-model
    title: TechTarget Waterfall Model Definition
  - type: Vocabulary
    url: vocabulary/waterfall-vocabulary.yml
    title: Waterfall Vocabulary
  - type: JSON-LD
    url: json-ld/waterfall-context.jsonld
    title: Waterfall JSON-LD Context
  - type: Features
    data:
      - name: Sequential Phase Execution
        description: Each phase (requirements, design, implementation, testing, deployment, maintenance) must be completed before the next begins, ensuring full documentation of outputs before proceeding.
      - name: Formal Phase-Gate Reviews
        description: Structured review checkpoints between phases allow stakeholders to approve progression, ensuring deliverable quality and scope alignment before the next stage.
      - name: Comprehensive Documentation
        description: Detailed documentation produced at each phase serves as the source of truth for subsequent phases and long-term system maintenance.
      - name: Fixed Scope and Requirements
        description: Requirements are gathered and locked upfront, minimizing scope creep and providing high predictability for cost and schedule estimates.
      - name: Clear Milestones and Deliverables
        description: Well-defined milestones at the end of each phase provide clear checkpoints for project tracking, stakeholder reporting, and regulatory compliance.
  - type: UseCases
    data:
      - name: Government and Defense Contracts
        description: Regulated government and defense projects with fixed requirements, formal procurement processes, and strict documentation mandates benefit from Waterfall's structured approach.
      - name: Infrastructure and Construction Projects
        description: Large infrastructure systems with well-understood requirements and high change-management costs suit the sequential Waterfall model.
      - name: Compliance-Driven Software
        description: Healthcare, finance, and safety-critical systems requiring audit trails, formal verification, and regulatory approval align well with Waterfall's documentation-heavy phases.
      - name: Fixed-Bid Contracts
        description: Projects delivered under fixed-price, fixed-scope contracts where up-front requirements definition is essential for accurate cost estimation.
      - name: System Integration Projects
        description: Integrations between large enterprise systems where interface contracts must be defined and agreed upon before implementation begins.
  - type: Integrations
    data:
      - name: Agile/Scrum
        description: Many teams adopt hybrid models combining Waterfall for high-level planning and Agile for iterative delivery within phases.
      - name: V-Model
        description: An extension of Waterfall that pairs each development phase with a corresponding testing phase, emphasizing verification and validation.
      - name: PRINCE2
        description: UK government project management framework that incorporates Waterfall concepts into structured stage-gate delivery.
      - name: CMMI
        description: Capability Maturity Model Integration often used alongside Waterfall in defense and aerospace software development programs.
      - name: DevOps
        description: Some organizations blend Waterfall for requirements and architecture with DevOps practices for continuous delivery in later phases.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
