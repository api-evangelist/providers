---
aid: git
name: Git
description: Git is a distributed version control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-28'
position: Consumer
url: https://raw.githubusercontent.com/api-evangelist/git/refs/heads/main/apis.yml
specificationVersion: '0.19'
tags:
  - Distributed
  - Git
  - Open Source
  - Source Code Management
  - Version Control
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
  - aid: git:gitea
    name: Gitea API
    description: RESTful API for Gitea's self-hosted Git service.
    humanURL: https://docs.gitea.io/en-us/api-usage/
    tags:
      - Git
      - Gitea
      - Self-hosted
    properties:
      - type: Documentation
        url: https://docs.gitea.io/en-us/api-usage/
      - type: OpenAPI
        url: https://gitea.io/api/swagger
common:
  - type: Website
    url: https://git-scm.com/
  - type: Documentation
    url: https://git-scm.com/doc
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
