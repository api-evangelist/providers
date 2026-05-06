---
aid: chaoss
name: CHAOSS
x-type: opensource
description: CHAOSS (Community Health Analytics in Open Source Software) is a Linux Foundation project that develops metrics, methodologies, software, and practitioner guides for measuring and improving open source community health and sustainability. It produces a metrics catalog organized into focus areas (Common, DEI, Risk, Value, Evolution) and metrics models, along with open source software (Augur, 8Knot, GrimoireLab) that ingests data from Git, GitHub, GitLab, mailing lists, and other community platforms to compute the metrics. CHAOSS-aligned SaaS services such as OSS Compass and Bitergia Analytics also expose the metrics for adopters who do not want to host the software themselves.
type: Index
position: Producer
access: Open Source
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Community Health
  - DEI
  - Linux Foundation
  - Metrics
  - Observability
  - Open Source
  - Risk
  - Sustainability
created: '2026-03-16'
modified: '2026-04-23'
url: https://raw.githubusercontent.com/api-evangelist/chaoss/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: chaoss:augur-api
    name: CHAOSS Augur REST API
    description: Augur is a CHAOSS reference implementation that collects data from GitHub, GitLab, mailing lists, and other community sources, and exposes a REST API for querying CHAOSS-aligned metrics on repositories, contributors, issues, pull requests, releases, and more. The API powers downstream analytics tools and dashboards including 8Knot.
    humanURL: https://oss-augur.readthedocs.io/
    baseURL: https://ai.chaoss.io/api
    tags:
      - Augur
      - Community Health
      - Metrics
      - REST
    properties:
      - type: Documentation
        url: https://oss-augur.readthedocs.io/
      - type: GitHubRepository
        url: https://github.com/chaoss/augur
      - type: API
        url: https://oss-augur.readthedocs.io/en/dev/rest-api/api.html
  - aid: chaoss:metrics-catalog
    name: CHAOSS Metrics Catalog
    description: The CHAOSS Metrics catalog is a community-maintained, structured reference of community-health metrics organized into focus areas (Common, DEI, Risk, Value, Evolution) plus metrics models that compose them. The catalog is openly licensed and published on the CHAOSS website and the chaoss/metrics GitHub repository, and is consumed by Augur, GrimoireLab, OSS Compass, Bitergia Analytics, and other implementations.
    humanURL: https://chaoss.community/metrics/
    tags:
      - Catalog
      - Documentation
      - Metrics
      - Models
    properties:
      - type: Documentation
        url: https://chaoss.community/kbtopic/all-metrics/
      - type: GitHubRepository
        url: https://github.com/chaoss/wg-metrics-models
      - type: MetricsRepository
        url: https://github.com/chaoss/community
  - aid: chaoss:grimoirelab
    name: CHAOSS GrimoireLab
    description: GrimoireLab is an open source platform for software development analytics. It pulls data from 30+ data sources (Git, GitHub, GitLab, mailing lists, IRC, Slack, Jira, Bugzilla, etc.) and provides a Python toolkit (Perceval, Sortinghat, GrimoireELK) plus a Kibana-based dashboard, exposing CHAOSS metrics for community health analysis.
    humanURL: https://chaoss.github.io/grimoirelab/
    tags:
      - Analytics
      - Data Pipeline
      - GrimoireLab
      - Kibana
      - Metrics
    properties:
      - type: Documentation
        url: https://chaoss.github.io/grimoirelab/
      - type: GitHubRepository
        url: https://github.com/chaoss/grimoirelab
  - aid: chaoss:8knot
    name: CHAOSS 8Knot Dashboard
    description: 8Knot is an open source community analytics dashboard built on top of Augur that provides ready-made visualizations of CHAOSS metrics for stakeholders evaluating open source project health.
    humanURL: https://github.com/oss-aspen/8knot
    tags:
      - Dashboard
      - Visualization
    properties:
      - type: Documentation
        url: https://github.com/oss-aspen/8knot
      - type: GitHubRepository
        url: https://github.com/oss-aspen/8knot
common:
  - type: Website
    url: https://chaoss.community/
  - type: Documentation
    name: CHAOSS Documentation
    description: Official documentation for CHAOSS metrics and software.
    url: https://chaoss.community/kbtopic/all-metrics/
  - type: GitHub
    name: CHAOSS GitHub
    description: Source code and repositories for CHAOSS.
    url: https://github.com/chaoss
  - type: WorkingGroups
    url: https://chaoss.community/working-groups/
  - type: Events
    url: https://chaoss.community/events/
  - type: Blog
    url: https://chaoss.community/news-blog/
  - type: PractitionerGuides
    url: https://chaoss.community/practitioner-guides/
  - type: ParentOrganization
    url: https://www.linuxfoundation.org/
  - type: GettingStarted
    url: https://chaoss.community/get-started/
  - type: Community
    url: https://chaoss.community/participate/
  - type: Slack
    url: https://chaoss.community/connect/
  - type: YouTube
    url: https://www.youtube.com/c/CHAOSScommunity
  - type: LinkedIn
    url: https://www.linkedin.com/company/chaoss-community/
  - type: X
    url: https://x.com/chaossproj
  - name: Features
    type: Features
    data:
      - name: Community Health Metrics
      - name: Metrics Models
      - name: DEI Metrics
      - name: Risk Metrics
      - name: Value Metrics
      - name: Evolution Metrics
      - name: Common Metrics
      - name: Open Source Software
      - name: Practitioner Guides
      - name: Working Groups
      - name: Reference Implementations
      - name: REST API (Augur)
      - name: Data Pipeline (GrimoireLab)
      - name: Dashboards (8Knot, Bitergia)
      - name: SaaS Adopter Services
  - name: UseCases
    type: UseCases
    data:
      - name: Open Source Project Health Assessment
      - name: Contributor Sustainability Analysis
      - name: DEI in Open Source Communities
      - name: Open Source Risk and Security Assessment
      - name: Open Source Investment ROI
      - name: Funding Impact Measurement
      - name: Community Onboarding Improvement
      - name: Foundation-Level Reporting
      - name: OSPO Health Reporting
      - name: Maintainer Burnout Detection
  - name: Tools
    type: Tools
    data:
      - name: Augur
      - name: GrimoireLab
      - name: 8Knot
      - name: Bitergia Analytics
      - name: OSS Compass
      - name: Cauldron
      - name: Sortinghat
      - name: Perceval
      - name: GrimoireELK
  - name: WorkingGroups
    type: WorkingGroups
    data:
      - name: Common Metrics
      - name: DEI Metrics
      - name: Risk Metrics
      - name: Value Metrics
      - name: Evolution Metrics
      - name: Software (Augur and GrimoireLab)
      - name: Education
      - name: Practitioner Guides
  - name: Integrations
    type: Integrations
    data:
      - name: GitHub
      - name: GitLab
      - name: Bitbucket
      - name: Git
      - name: Mailing Lists
      - name: Jira
      - name: Bugzilla
      - name: Discourse
      - name: Slack
      - name: IRC
      - name: Stack Exchange
      - name: Meetup
      - name: Linux Foundation
      - name: CNCF
      - name: Apache Software Foundation
      - name: OpenSSF
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
