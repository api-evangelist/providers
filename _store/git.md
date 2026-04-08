---
aid: git
url: https://raw.githubusercontent.com/api-evangelist/git/refs/heads/main/apis.yml
apis:
- aid: git:git-cli
  name: Git CLI
  description: Git command-line interface for version control operations.
  humanURL: https://git-scm.com/docs
  tags:
  - Version Control
  properties:
  - type: Documentation
    url: https://git-scm.com/doc
  - type: Reference
    url: https://git-scm.com/docs
- aid: git:github
  name: GitHub API
  description: RESTful API for GitHub's Git hosting platform.
  humanURL: https://docs.github.com/en/rest
  baseURL: https://api.github.com
  tags:
  - Git
  - GitHub
  properties:
  - type: Documentation
    url: https://docs.github.com/en/rest
  - type: OpenAPI
    url: https://github.com/github/rest-api-description
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
- aid: git:gitlab
  name: GitLab API
  description: RESTful API for GitLab's Git repository management.
  humanURL: https://docs.gitlab.com/ee/api/
  baseURL: https://gitlab.com/api/v4
  tags:
  - Git
  - GitLab
  properties:
  - type: Documentation
    url: https://docs.gitlab.com/ee/api/
  - type: OpenAPI
    url: https://docs.gitlab.com/ee/api/openapi/openapi.yaml
  - type: Authentication
    url: https://docs.gitlab.com/ee/api/rest/index.html#authentication
name: Git
tags:
- Distributed
- Git
- Open Source
- Source Code Management
- Version Control
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Git is a distributed version control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

