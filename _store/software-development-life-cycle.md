---
aid: software-development-life-cycle
name: Software Development Life Cycle
description: The Software Development Life Cycle (SDLC) is a structured framework that defines the process for planning, creating, testing, and deploying high-quality software systems. It encompasses distinct phases including requirements analysis, system design, implementation, testing, deployment, and ongoing maintenance. Tools and platforms that support SDLC workflows provide capabilities for project management, source control, continuous integration and delivery, testing automation, release management, and collaboration across development teams.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Development Process
  - Project Management
  - SDLC
  - Software Engineering
  - DevOps
  - CI/CD
url: https://raw.githubusercontent.com/api-evangelist/software-development-life-cycle/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: software-development-life-cycle:requirements-management
    name: Requirements Management APIs
    description: APIs and tools for capturing, tracking, and managing software requirements throughout the development life cycle, including user stories, acceptance criteria, and traceability matrices.
    humanURL: https://en.wikipedia.org/wiki/Requirements_management
    baseURL: https://en.wikipedia.org/wiki/Requirements_management
    tags:
      - Requirements
      - User Stories
      - Backlog
      - Agile
    properties:
      - type: Documentation
        url: https://en.wikipedia.org/wiki/Requirements_management
  - aid: software-development-life-cycle:source-control
    name: Source Control APIs
    description: APIs for version control systems that manage code repositories, branches, commits, pull requests, and code reviews as part of the software development life cycle.
    humanURL: https://en.wikipedia.org/wiki/Version_control
    baseURL: https://api.github.com
    tags:
      - Source Control
      - Version Control
      - Git
      - Repositories
    properties:
      - type: Documentation
        url: https://docs.github.com/en/rest
      - type: OpenAPI
        url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - aid: software-development-life-cycle:ci-cd
    name: Continuous Integration and Delivery APIs
    description: APIs for CI/CD pipelines that automate the building, testing, and deployment of software changes, enabling frequent and reliable releases throughout the development life cycle.
    humanURL: https://en.wikipedia.org/wiki/CI/CD
    baseURL: https://en.wikipedia.org/wiki/CI/CD
    tags:
      - CI/CD
      - Continuous Integration
      - Continuous Delivery
      - Pipelines
      - Automation
    properties:
      - type: Documentation
        url: https://en.wikipedia.org/wiki/CI/CD
  - aid: software-development-life-cycle:testing-automation
    name: Testing and Quality Assurance APIs
    description: APIs for automated testing frameworks and quality assurance platforms that support unit testing, integration testing, performance testing, and security testing throughout the SDLC.
    humanURL: https://en.wikipedia.org/wiki/Test_automation
    baseURL: https://en.wikipedia.org/wiki/Test_automation
    tags:
      - Testing
      - Quality Assurance
      - Test Automation
      - Security Testing
    properties:
      - type: Documentation
        url: https://en.wikipedia.org/wiki/Test_automation
  - aid: software-development-life-cycle:project-management
    name: Project Management APIs
    description: APIs for project management and collaboration tools that track work items, sprints, milestones, and team velocity throughout the software development life cycle.
    humanURL: https://en.wikipedia.org/wiki/Software_project_management
    baseURL: https://en.wikipedia.org/wiki/Software_project_management
    tags:
      - Project Management
      - Agile
      - Scrum
      - Kanban
      - Sprint Planning
    properties:
      - type: Documentation
        url: https://en.wikipedia.org/wiki/Software_project_management
  - aid: software-development-life-cycle:release-management
    name: Release Management APIs
    description: APIs for managing software releases, deployments, and change management processes, ensuring controlled and auditable rollouts to production environments.
    humanURL: https://en.wikipedia.org/wiki/Software_release_life_cycle
    baseURL: https://en.wikipedia.org/wiki/Software_release_life_cycle
    tags:
      - Release Management
      - Deployment
      - Change Management
      - Versioning
    properties:
      - type: Documentation
        url: https://en.wikipedia.org/wiki/Software_release_life_cycle
common:
  - url: https://en.wikipedia.org/wiki/Software_development_life_cycle
    name: SDLC Wikipedia Article
    type: Documentation
  - url: https://en.wikipedia.org/wiki/Agile_software_development
    name: Agile Software Development
    type: Documentation
  - url: https://en.wikipedia.org/wiki/DevOps
    name: DevOps
    type: Documentation
  - url: https://en.wikipedia.org/wiki/Scrum_(software_development)
    name: Scrum Methodology
    type: Documentation
  - url: https://en.wikipedia.org/wiki/Kanban_(development)
    name: Kanban Development
    type: Documentation
  - url: https://en.wikipedia.org/wiki/Test-driven_development
    name: Test-Driven Development
    type: Documentation
  - url: https://en.wikipedia.org/wiki/Continuous_integration
    name: Continuous Integration
    type: Documentation
  - url: https://en.wikipedia.org/wiki/Continuous_delivery
    name: Continuous Delivery
    type: Documentation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
