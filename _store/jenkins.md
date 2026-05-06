---
aid: jenkins
name: Jenkins
description: Jenkins is the leading open source automation server that enables developers to reliably build, test, and deploy software. Jenkins exposes a machine-consumable Remote Access API for nearly every resource it manages, available in XML (with XPath filtering), JSON (with JSONP), and a Python-compatible variant, and supports HTTP Basic auth with API tokens for scripted clients.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Build Server
  - CI/CD
  - Continuous Delivery
  - Continuous Integration
  - DevOps
  - Open Source
  - Remote Access API
url: https://raw.githubusercontent.com/api-evangelist/jenkins/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jenkins:jenkins-remote-access-api
    name: Jenkins Remote Access API
    description: Jenkins provides a machine-consumable Remote Access API to nearly every resource it exposes. The API is reached by appending /api/ to any Jenkins resource URL (top-level, jobs, builds, queue, nodes, views, etc.), is available in XML, JSON (JSONP), and Python variants, and supports authenticated requests via HTTP Basic auth with API tokens. Common operations include triggering builds, retrieving job and build information, and inspecting build queues, with depth and tree query parameters for controlling response shape.
    humanURL: https://www.jenkins.io/doc/book/using/remote-access-api/
    tags:
      - JSON
      - Python
      - Remote Access
      - REST API
      - XML
    properties:
      - type: Documentation
        url: https://www.jenkins.io/doc/book/using/remote-access-api/
      - type: Authentication
        url: https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/
      - type: APITokens
        url: https://www.jenkins.io/doc/book/managing/system-configuration/#configuring-api-tokens
common:
  - type: Website
    url: https://www.jenkins.io/
  - type: GettingStarted
    url: https://www.jenkins.io/doc/pipeline/tour/getting-started/
  - type: Documentation
    url: https://www.jenkins.io/doc/
  - type: Installation
    url: https://www.jenkins.io/doc/book/installing/
  - type: Plugins
    url: https://plugins.jenkins.io/
  - type: Tutorials
    url: https://www.jenkins.io/doc/tutorials/
  - type: Blog
    url: https://www.jenkins.io/node/
  - type: Community
    url: https://www.jenkins.io/participate/
  - type: GitHubOrganization
    url: https://github.com/jenkinsci
  - type: SecurityAdvisories
    url: https://www.jenkins.io/security/advisories/
  - type: Governance
    url: https://www.jenkins.io/project/governance/
  - type: Roadmap
    url: https://www.jenkins.io/project/roadmap/
  - type: PrivacyPolicy
    url: https://www.jenkins.io/privacy/
  - type: TermsOfService
    url: https://www.jenkins.io/project/conduct/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
