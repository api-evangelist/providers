---
aid: contributing-md
url: https://raw.githubusercontent.com/api-evangelist/contributing-md/refs/heads/main/apis.yml
name: CONTRIBUTING.md
x-type: standard
description: CONTRIBUTING.md is a community health convention used by open source projects on GitHub and other platforms to document how external contributors can participate. The file communicates contribution guidelines, pull request processes, issue reporting procedures, coding standards, development setup, testing expectations, and code of conduct references. GitHub recognizes CONTRIBUTING.md placed in the repository root, the .github folder, or the docs folder, and surfaces a link to it whenever a contributor opens a new issue or pull request.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Code Of Conduct
  - Collaboration
  - Community Health
  - Developer Guidelines
  - Documentation
  - GitHub
  - Markdown
  - Open Source
  - Pull Requests
  - Repository
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: contributing-md:format
    name: CONTRIBUTING.md Format
    tags:
      - Community Health
      - Convention
      - Documentation
      - Markdown
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
    properties:
      - url: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
        type: Documentation
      - url: https://contributing.md/
        type: Reference
      - url: https://opensource.guide/how-to-contribute/
        type: Guide
      - url: https://github.com/github/docs/blob/main/CONTRIBUTING.md
        type: Example
    description: 'The CONTRIBUTING.md format is an unstructured Markdown convention that documents how to contribute to a project. GitHub recognizes the file in three locations checked in priority order: the .github folder, the repository root, and the docs folder. When a contributor opens an issue or pull request, GitHub automatically links to the file. Typical sections include contribution workflow, development setup, branch and commit conventions, code style, testing, pull request review process, code of conduct reference, and licensing terms.'
    x-features:
      - Triggers contribution prompt on new issues and pull requests
      - Recognized by GitHub, GitLab, Bitbucket, and Gitea
      - Pairs with CODE_OF_CONDUCT.md, ISSUE_TEMPLATE, and PULL_REQUEST_TEMPLATE
      - Can live in repository root, .github, or docs directory
      - Often references a Developer Certificate of Origin or CLA process
    x-useCases:
      - Onboarding first-time contributors to an open source project
      - Documenting fork-and-pull workflow expectations
      - Defining branch naming, commit message, and review conventions
      - Specifying local development setup and required toolchains
      - Linking to community resources such as Discord, mailing lists, or forums
  - aid: contributing-md:related-conventions
    name: CONTRIBUTING.md Related Conventions
    tags:
      - Community Health
      - Convention
      - GitHub
      - Open Source
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions
    properties:
      - url: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories
        type: Documentation
      - url: https://www.contributor-covenant.org/
        type: Reference
      - url: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests
        type: Documentation
    description: CONTRIBUTING.md is one of several community health files GitHub looks for when scoring a repository community profile. Sibling files include README.md, LICENSE, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md, and issue and pull request templates. Together these conventions establish a well-formed, welcoming open source project that lowers the barrier for new contributors.
    x-features:
      - Recognized as part of the GitHub community profile checklist
      - Composable with CODE_OF_CONDUCT.md, SECURITY.md, and SUPPORT.md
      - Compatible with All Contributors specification for recognition
      - Often pairs with .github/ISSUE_TEMPLATE and PULL_REQUEST_TEMPLATE.md
    x-useCases:
      - Completing the GitHub community profile health checklist
      - Defining the entire community health surface for an organization
      - Standardizing contribution conventions across many repositories
common:
  - type: Documentation
    url: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
  - type: Reference
    url: https://contributing.md/
  - type: Guide
    url: https://opensource.guide/how-to-contribute/
  - type: Example
    url: https://github.com/github/docs/blob/main/CONTRIBUTING.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
