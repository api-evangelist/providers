---
aid: sonar
url: https://raw.githubusercontent.com/api-evangelist/sonar/refs/heads/main/apis.yml
apis:
- name: SonarQube Web API
  description: REST API for interacting with SonarQube server, including project analysis, quality gates, issues, and metrics.
  image: https://www.sonarsource.com/assets/logo-sonar.svg
  humanURL: https://www.sonarqube.org
  baseURL: https://sonarcloud.io/api
  tags:
  - Code Quality
  - DevOps
  - Security
  - Static Analysis
  - Technical Debt
  properties:
  - type: Documentation
    url: https://docs.sonarqube.org/latest/extend/web-api/
  - type: OpenAPI
    url: https://sonarcloud.io/api/swagger.json
  - type: Authentication
    url: https://docs.sonarqube.org/latest/extend/web-api/#authentication
- name: SonarCloud API
  description: Cloud-based code quality and security service API for analyzing code repositories.
  image: https://www.sonarsource.com/assets/logo-sonar.svg
  humanURL: https://sonarcloud.io
  baseURL: https://sonarcloud.io/api
  tags:
  - Bitbucket
  - CI/CD
  - Cloud
  - Code Quality
  - GitHub
  - GitLab
  properties:
  - type: Documentation
    url: https://sonarcloud.io/web_api
  - type: Getting Started
    url: https://docs.sonarcloud.io/
  - type: Authentication
    url: https://docs.sonarcloud.io/advanced-setup/api-authentication/
name: Sonar
tags:
- Code Quality
- Continuous Integration
- DevOps
- Security
- Static Analysis
type: Contract
image: https://www.sonarsource.com/assets/logo-sonar.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Sonar provides code quality and security analysis tools for developers, offering continuous inspection of code quality through static code analysis.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

