---
aid: todo-group
name: TODO Group
description: The TODO Group is an open community of practitioners under the Linux Foundation who collaborate on best practices, tools, and guidance for running successful Open Source Program Offices (OSPOs). It provides open source tooling including Repolinter for repository linting, the OSPO Landscape mapping OSPO adopters and tools, comprehensive OSPO guides and case studies, and OSPOlogy community programs. The TODO Group serves organizations managing enterprise open source strategies across 120+ member organizations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Community
  - Linux Foundation
  - Open Source
  - OSPO
created: '2026-03-16'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/todo-group/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: todo-group:repolinter
    name: Repolinter
    description: Repolinter is an open source linting tool for repositories that validates compliance with open source best practices. It checks repositories for standard files like LICENSE, README, CONTRIBUTING, and CODE-OF-CONDUCT, and supports configurable rulesets. Available as a CLI tool (repolinter lint) and a JavaScript API for programmatic integration. Installable via npm as the repolinter package.
    humanURL: https://github.com/todogroup/repolinter
    tags:
      - Linting
      - Open Source
      - Repository
      - Compliance
    properties:
      - type: Documentation
        url: https://github.com/todogroup/repolinter
      - type: GitHubRepository
        url: https://github.com/todogroup/repolinter
      - type: NpmPackage
        url: https://www.npmjs.com/package/repolinter
  - aid: todo-group:repolinter-action
    name: Repolinter Action
    description: A GitHub Action that runs Repolinter on repositories as part of CI/CD workflows. Validates repositories against configurable rulesets to enforce open source compliance policies. Supports outputting results as exit codes for PR status checks or creating GitHub issues for non-intrusive notifications. Originally created by New Relic, maintained by TODO Group.
    humanURL: https://github.com/todogroup/repolinter-action
    tags:
      - GitHub Actions
      - Linting
      - CI/CD
      - Compliance
    properties:
      - type: Documentation
        url: https://github.com/todogroup/repolinter-action
      - type: GitHubRepository
        url: https://github.com/todogroup/repolinter-action
      - type: GitHubMarketplace
        url: https://github.com/marketplace/actions/repolinter-action
  - aid: todo-group:ospo-landscape
    name: OSPO Landscape
    description: An interactive landscape mapping the Open Source Program Office ecosystem, including OSPO adopter organizations and tools supporting OSPO operations. Data is maintained in landscape.yml and browsable at landscape.todogroup.org. Modeled after the CNCF landscape approach, covering companies, governments, academic institutions, and supporting tooling.
    humanURL: https://landscape.todogroup.org/
    tags:
      - Landscape
      - OSPO
      - Ecosystem
      - Data
    properties:
      - type: Documentation
        url: https://landscape.todogroup.org/
      - type: GitHubRepository
        url: https://github.com/todogroup/ospolandscape
      - type: Website
        url: https://landscape.todogroup.org/
  - aid: todo-group:ospo-guides
    name: OSPO Guides
    description: A comprehensive collection of 23+ practitioner guides covering all aspects of running Open Source Program Offices. Topics include creating an OSPO, setting open source strategy, measuring program success, managing career development, recruiting open source developers, legal compliance, and community engagement. All guides are open source and community-contributed.
    humanURL: https://todogroup.org/guides/
    tags:
      - Guides
      - OSPO
      - Best Practices
      - Documentation
    properties:
      - type: Documentation
        url: https://todogroup.org/guides/
      - type: GitHubRepository
        url: https://github.com/todogroup/guides
  - aid: todo-group:ospology
    name: OSPOlogy
    description: The OSPOlogy program provides monthly community webinars, working group meetings, and collaborative sessions focused on OSPO practices and challenges. It serves as the primary community engagement platform for TODO Group members and OSPO practitioners worldwide, covering topics from OSPO maturity models to specific industry challenges.
    humanURL: https://community.linuxfoundation.org/todo-group-ospology/
    tags:
      - Community
      - Webinars
      - OSPO
      - Education
    properties:
      - type: Documentation
        url: https://github.com/todogroup/ospology
      - type: GitHubRepository
        url: https://github.com/todogroup/ospology
      - type: Website
        url: https://community.linuxfoundation.org/todo-group-ospology/
  - aid: todo-group:ospo-career-path
    name: OSPO Career Path
    description: An open source career development framework defining roles, skills, and progression paths for OSPO professionals. Covers job functions from open source program manager to legal counsel, providing organizations with a structured approach to building and growing OSPO teams with defined competencies and seniority levels.
    humanURL: https://github.com/todogroup/ospo-career-path
    tags:
      - Career Development
      - OSPO
      - Human Resources
      - Skills Framework
    properties:
      - type: Documentation
        url: https://github.com/todogroup/ospo-career-path
      - type: GitHubRepository
        url: https://github.com/todogroup/ospo-career-path
common:
  - type: Website
    url: https://todogroup.org/
  - type: Documentation
    url: https://todogroup.org/guides/
  - type: GitHubOrg
    url: https://github.com/todogroup
  - type: Slack
    url: https://slack.todogroup.org/
  - type: Newsletter
    url: https://todogroup.org/community/newsletter/
  - type: SpectralRules
    url: rules/todo-group-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/todo-group-vocabulary.yaml
  - type: Features
    data:
      - name: Repolinter CLI
        description: Command-line tool for linting open source repositories against configurable compliance rulesets.
      - name: Repolinter JavaScript API
        description: Programmatic Node.js API for integrating repository linting into custom workflows and tools.
      - name: Repolinter GitHub Action
        description: CI/CD integration for automated repository compliance checks in GitHub workflows.
      - name: OSPO Landscape
        description: Interactive ecosystem map of OSPO adopter organizations and supporting tools worldwide.
      - name: OSPO Guides
        description: Comprehensive practitioner guides covering all aspects of running an Open Source Program Office.
      - name: OSPOlogy Webinars
        description: Monthly community webinars and working group sessions for OSPO practitioners.
      - name: OSPO Career Path
        description: Structured career framework defining roles, skills, and progression paths for OSPO professionals.
      - name: Awesome OSPO
        description: Curated list of tools and resources for open source program management.
  - type: UseCases
    data:
      - name: Repository Compliance Automation
        description: Use Repolinter and Repolinter Action to automate checks that all repos have required open source files and follow organizational policies.
      - name: OSPO Program Launch
        description: Use TODO Group guides and case studies to establish and launch a new Open Source Program Office within an organization.
      - name: OSPO Ecosystem Mapping
        description: Reference the OSPO Landscape to discover tools, peer organizations, and adopters in the OSPO ecosystem.
      - name: Developer Career Development
        description: Apply the OSPO Career Path framework to define roles and progression for open source professionals.
      - name: Open Source Strategy Development
        description: Leverage TODO Group best practice guides to define and implement an enterprise open source strategy.
      - name: Community Building
        description: Participate in OSPOlogy webinars and TODO Group working groups to learn from and contribute to the OSPO community.
  - type: Integrations
    data:
      - name: GitHub Actions
        description: Repolinter Action integrates repository linting into GitHub CI/CD workflows.
      - name: Linux Foundation
        description: TODO Group operates under the Linux Foundation governance and community infrastructure.
      - name: CNCF Landscape
        description: OSPO Landscape follows the CNCF landscape pattern for ecosystem visualization.
      - name: Node.js / npm
        description: Repolinter is distributed as an npm package and supports Node.js 12+ runtime.
      - name: OpenSSF
        description: Collaboration with Open Source Security Foundation on best practices for open source security and compliance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
