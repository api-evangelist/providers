---
aid: authors-md
name: AUTHORS.md
description: AUTHORS.md is a file format standard used in open-source and collaborative software projects to list the original creators, primary authors, and significant contributors of a project. Often required by open-source licenses such as GPL and Apache 2.0 to provide proper attribution, the AUTHORS.md file documents who wrote what portions of a codebase, their email addresses, and the scope of their contributions. Related standards include CONTRIBUTORS.md, All Contributors specification, and REUSE/SPDX contributor attribution frameworks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Attribution
  - Documentation
  - Open Source
  - Repository
  - File Format
  - Contributor Management
  - License Compliance
  - Standard
url: https://raw.githubusercontent.com/api-evangelist/authors-md/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: authors-md-all-contributors
    name: All Contributors API
    description: The All Contributors specification provides a standardized way to recognize contributions to open-source projects beyond just code. It includes a bot API for automating contributor management, a configuration schema (.all-contributorsrc), and an emoji-based contribution type taxonomy. The bot responds to GitHub comments to add contributors to the project README.
    humanURL: https://allcontributors.org
    baseURL: https://allcontributors.org
    tags:
      - Contributors
      - Attribution
      - Open Source
      - Bot
      - GitHub
    properties:
      - type: Documentation
        url: https://allcontributors.org/docs/en/overview
      - type: GettingStarted
        url: https://allcontributors.org/docs/en/bot/installation
      - type: Specification
        url: https://allcontributors.org/docs/en/specification
      - type: GitHubRepository
        url: https://github.com/all-contributors/all-contributors
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/authors-md/refs/heads/main/json-schema/all-contributors-config-schema.json
common:
  - type: GitHubOrganization
    url: https://github.com/api-evangelist
  - type: GitHubRepository
    url: https://github.com/api-evangelist/authors-md
  - type: Features
    data:
      - name: Author Attribution
        description: Documents original creators and primary authors of a project, fulfilling attribution requirements for open-source licenses like GPL and Apache 2.0.
      - name: Contributor Types
        description: Supports recognition of diverse contribution types beyond code including documentation, design, translation, testing, and community management.
      - name: Machine-Readable Format
        description: The All Contributors .all-contributorsrc configuration file provides a machine-readable JSON format for managing contributor metadata programmatically.
      - name: Bot Automation
        description: The All Contributors bot automates contributor recognition by responding to GitHub issue and pull request comments to update contributor tables.
      - name: License Compliance
        description: Helps projects satisfy attribution requirements in open-source licenses including GPL, LGPL, Apache 2.0, and MPL that require author documentation.
  - type: UseCases
    data:
      - name: Open Source License Compliance
        description: Satisfying attribution requirements in GPL, Apache, and other licenses that require listing authors and contributors in distributed software.
      - name: Project Governance
        description: Documenting contributors for project governance purposes, recognition, and historical record-keeping of who built what portions of a codebase.
      - name: Contributor Onboarding
        description: Helping new contributors understand the project's authorship history and providing a clear path for getting recognized for their contributions.
      - name: Copyright Documentation
        description: Maintaining accurate copyright records for legal clarity around intellectual property ownership and contributor rights in collaborative projects.
      - name: Community Recognition
        description: Publicly recognizing contributors in README files and project documentation to build community engagement and acknowledge diverse contributions.
  - type: Integrations
    data:
      - name: GitHub
        description: All Contributors bot integrates directly with GitHub repositories, responding to issue and pull request comments to manage contributor attribution.
      - name: REUSE / SPDX
        description: The REUSE specification by FSFE provides structured SPDX-based attribution that complements AUTHORS.md files with machine-readable copyright headers.
      - name: GNU Coding Standards
        description: GNU project guidelines specify conventions for AUTHORS files in free software projects, requiring attribution of significant code contributions.
      - name: CONTRIBUTING.md
        description: AUTHORS.md files work alongside CONTRIBUTING.md files to document both past contributors and guidelines for future contributions.
      - name: CHANGELOG.md
        description: AUTHORS.md attribution works in conjunction with CHANGELOG.md files to provide a complete history of a project's contributors and changes.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/authors-md/refs/heads/main/vocabulary/authors-md-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
