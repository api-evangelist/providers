---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Augur is a CHAOSS reference implementation that collects data from GitHub, GitLab, mailing lists, and other community sources, and exposes a REST API for querying CHAOSS-aligned metrics on repositorie
  name: CHAOSS Augur REST API
  slug: augur-api
- description: The CHAOSS Metrics catalog is a community-maintained, structured reference of community-health metrics organized into focus areas (Common, DEI, Risk, Value, Evolution) plus metrics models that compose
  name: CHAOSS Metrics Catalog
  slug: metrics-catalog
- description: GrimoireLab is an open source platform for software development analytics. It pulls data from 30+ data sources (Git, GitHub, GitLab, mailing lists, IRC, Slack, Jira, Bugzilla, etc.) and provides a Pyt
  name: CHAOSS GrimoireLab
  slug: grimoirelab
- description: 8Knot is an open source community analytics dashboard built on top of Augur that provides ready-made visualizations of CHAOSS metrics for stakeholders evaluating open source project health.
  name: CHAOSS 8Knot Dashboard
  slug: 8knot
artifact_total: 49
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chaoss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chaoss.community/
- group: docs
  title: ''
  type: Documentation
  url: https://chaoss.community/kbtopic/all-metrics/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/chaoss
- group: other
  title: ''
  type: WorkingGroups
  url: https://chaoss.community/working-groups/
- group: other
  title: ''
  type: Events
  url: https://chaoss.community/events/
- group: company
  title: ''
  type: Blog
  url: https://chaoss.community/news-blog/
- group: docs
  title: ''
  type: PractitionerGuides
  url: https://chaoss.community/practitioner-guides/
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.linuxfoundation.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://chaoss.community/get-started/
- group: operate
  title: ''
  type: Community
  url: https://chaoss.community/participate/
- group: operate
  title: ''
  type: Slack
  url: https://chaoss.community/connect/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/CHAOSScommunity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chaoss-community/
- group: other
  title: ''
  type: X
  url: https://x.com/chaossproj
- group: build
  title: ''
  type: Tools
  url: ''
- group: other
  title: ''
  type: WorkingGroups
  url: ''
created: '2026-03-16'
description: CHAOSS (Community Health Analytics in Open Source Software) is a Linux Foundation project that develops metrics, methodologies, software, and practitioner guides for measuring and improving open source community health and sustainability. It produces a metrics catalog organized into focus areas (Common, DEI, Risk, Value, Evolution) and metrics models, along with open source software (Augur, 8Knot, GrimoireLab) that ingests data from Git, GitHub, GitLab, mailing lists, and other community platforms to compute the metrics. CHAOSS-aligned SaaS services such as OSS Compass and Bitergia Analytics also expose the metrics for adopters who do not want to host the software themselves.
features:
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
finops:
- name: Chaoss Finops
  service_category: API
  slug: chaoss-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chaoss.png
integrations:
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
layout: provider
modified: '2026-04-23'
name: CHAOSS
nav: Providers
network: true
overview: 'CHAOSS publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Community Health, DEI, Linux Foundation, and Metrics.


  CHAOSS''s developer surface includes documentation, GitHub presence, engineering blog, getting-started guide, YouTube channel, tooling, and 9 more developer resources.'
plans:
- name: Chaoss Plans Pricing
  plan_count: 3
  slug: chaoss-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Chaoss Rate Limits
  slug: chaoss-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chaoss/refs/heads/main/screenshots/chaoss-2026-06-20T174222.png
security:
- kind: domain-security
  name: Chaoss Domain Security
  slug: chaoss-domain-security
  summary_line: TLSv1.3 · HSTS
slug: chaoss
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
use_cases:
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
website: https://chaoss.community/
---
